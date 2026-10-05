# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the major Python code for running DDLC mods on Android.
# Altering this file WILL break your mod on Android.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import renpy  # type: ignore

"""renpy
init -2 python:
"""

import errno
import os
import shutil
import threading
import zipfile
from contextlib import contextmanager

###################################
# Constants
###################################

# Request codes for Android Activity.
REQUEST_CODE_PC = 2001
REQUEST_CODE_ANDROID = 2002
_REQUEST_MODES = {REQUEST_CODE_PC: "pc", REQUEST_CODE_ANDROID: "android"}

# Assets needed for the game to run from PC and Android.
PC_RPAS = frozenset({"audio.rpa", "fonts.rpa", "images.rpa"})
ANDROID_PREFIXES = (
    "assets/game/images/",
    "assets/game/gui/",
    "assets/game/fonts/",
    "assets/game/bgm/",
    "assets/game/sfx/",
)
ANDROID_ASSET_ROOT = "assets/game/"

# Signal file written after successful extraction.
ASSET_MARKER = ".ddlc_assets_installed"

# Temporary folders for storing the assets while extracting them.
STAGING_DIR = ".ddlc_staging"
TEMP_IMPORT_NAME = "temp_import.archive"
NESTED_APK_NAME = ".ddlc_nested.apk"

COPY_CHUNK = 1024 * 1024  # 1 MiB

###################################
# States
###################################

asset_setup_status = ""
asset_setup_busy = False
asset_setup_complete = False

_state_lock = threading.Lock()
_job_running = False

# Bumped per picker launch so stale pollers exit.
_picker_token = 0

PICKER_POLL_INTERVAL = 0.25  # .25 secs


class AssetSetupError(Exception):
    """Exception thrown when the extraction process fails."""


def _set_status(msg: str, busy=None):
    """Sets the status message for the extraction process."""
    global asset_setup_status, asset_setup_busy
    asset_setup_status = msg
    if busy is not None:
        asset_setup_busy = busy


def _fail(msg: str):
    """Sets the status message to a failure state."""
    _set_status(msg, busy=False)


def _try_begin(status: str) -> bool:
    """
    Attempts to begin the extraction process.

    Args:
        status (str): The status message to set.

    Returns:
        bool: True if the extraction process was started, False otherwise.
    """
    global asset_setup_busy, asset_setup_status, asset_setup_complete
    with _state_lock:
        if asset_setup_busy:
            return False
        asset_setup_busy = True
        asset_setup_status = status
        asset_setup_complete = False
        return True


def _fmt_size(n: int) -> str:
    """Formats a size in bytes into a human-readable string."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024.0


def get_android_game_dir() -> str:
    """
    Returns the writeable game directory on Android.

    Returns:
        str: The path to the Android game's directory.
    """
    if renpy.android:
        return renpy.config.gamedir

    from game.definitions.py.core_ren import _get_android_game_dir

    data_dir = _get_android_game_dir()
    if data_dir is None:
        return renpy.config.gamedir

    game_dir = os.path.join(data_dir, "game")
    if not os.path.exists(game_dir):
        os.makedirs(game_dir, 0o777)
    return game_dir


def _marker_path() -> str:
    """Returns the path to the marker file."""
    return os.path.join(get_android_game_dir(), ASSET_MARKER)


def has_installed_ddlc_assets():
    """
    Checks if DDLC base assets are present.

    The marker file is written only after a fully successful extraction, so a
    partial install can't pass.

    Returns:
        bool: True if the assets are present, False otherwise.
    """
    if not renpy.android:
        return True
    if os.path.exists(_marker_path()):
        return True
    return all(renpy.loadable(name) for name in PC_RPAS)


def _safe_join(base: str, rel: str) -> str:
    """Joins rel onto base and rejects anything that escapes base (zip-slip)."""
    base_real = os.path.realpath(base)
    out = os.path.realpath(os.path.join(base_real, rel))
    if not out.startswith(base_real + os.sep):
        raise AssetSetupError(
            "The selected file contains an unsafe path and was rejected."
        )
    return out


def _check_free_space(path: str, needed: int):
    if not hasattr(os, "statvfs"):
        return
    try:
        st = os.statvfs(path)
    except OSError:
        return
    free = st.f_bavail * st.f_frsize
    required = int(needed * 1.05) + 32 * 1024 * 1024
    if free < required:
        raise AssetSetupError(
            f"Not enough free storage. About {_fmt_size(required)} is needed, "
            f"but only {_fmt_size(free)} is available."
        )


def _mod_provides(rel: str, target_dir: str) -> bool:
    """
    True if the mod itself supplies this path (so we shouldn't override it).
    A file already sitting in target_dir is from a previous extraction, which
    can be safely overwritten.
    """
    if os.path.exists(os.path.join(target_dir, rel)):
        return False
    try:
        return bool(renpy.loadable(rel))
    except Exception:
        return False


def _cleanup_stale():
    """Removes leftovers from interrupted runs."""
    try:
        game_dir = get_android_game_dir()
        shutil.rmtree(os.path.join(game_dir, STAGING_DIR), ignore_errors=True)
        for name in os.listdir(game_dir):
            if name.endswith(".part") or name in (TEMP_IMPORT_NAME, NESTED_APK_NAME):
                try:
                    os.remove(os.path.join(game_dir, name))
                except OSError:
                    pass
    except OSError:
        pass


def _commit(pairs):
    """
    Moves staged files into place, then writes the marker last.

    Args:
        pairs: iterable of (staged_path, final_path). Same filesystem, so
        `os.replace` is a cheap rename.
    """
    marker = _marker_path()
    if os.path.exists(marker):
        os.remove(marker)  # Not "installed" while we're mid-commit.

    for src, dest in pairs:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        os.replace(src, dest)

    with open(marker, "w") as f:
        f.write("1\n")


def extract_pc_zip(zip_source):
    """
    Extracts the PC assets from DDLC into the mod's game directory.

    Args:
        zip_source (str | file object): The official DDLC PC ZIP (path or a
            seekable binary file object).

    Raises:
        AssetSetupError: If the archive isn't a usable DDLC PC ZIP.
    """
    target_dir = get_android_game_dir()
    staged = {}

    try:
        # Fetch RPA files from the ZIP.
        with zipfile.ZipFile(zip_source, "r") as zf:
            wanted = {}
            for info in zf.infolist():
                if info.is_dir():
                    continue
                name = os.path.basename(info.filename).lower()
                if name in PC_RPAS and name not in wanted:
                    wanted[name] = info

            # Validate BEFORE writing anything.
            missing = PC_RPAS - set(wanted)
            if missing:
                raise AssetSetupError(
                    f"This ZIP is missing {', '.join(sorted(missing))}. "
                    "Make sure it is the official DDLC PC download."
                )

            _check_free_space(target_dir, sum(i.file_size for i in wanted.values()))

            for name in sorted(wanted):
                _set_status(f"Extracting {name}...")
                dest = os.path.join(target_dir, name)
                part = dest + ".part"
                with zf.open(wanted[name]) as src, open(part, "wb") as dst:
                    shutil.copyfileobj(src, dst, COPY_CHUNK)  # CRC checked at EOF
                staged[name] = (part, dest)

                with open(part, "rb") as f:
                    if f.read(4) != b"RPA-":
                        raise AssetSetupError(
                            f"{name} in this ZIP appears to be corrupt."
                        )

        _set_status("Installing assets...")
        _commit(staged.values())
    finally:
        for part, _ in staged.values():
            if os.path.exists(part):
                try:
                    os.remove(part)
                except OSError:
                    pass


def _has_game_assets(apk_path: str) -> bool:
    with zipfile.ZipFile(apk_path, "r") as z:
        return any(n.startswith(ANDROID_PREFIXES) for n in z.namelist())


def _unpack_apk(apk: zipfile.ZipFile, staging: str, target_dir: str):
    wanted = []
    for info in apk.infolist():
        name = info.filename
        if info.is_dir():
            continue
        # Skip script files to prevent duplicate label errors
        if name.endswith((".rpy", ".rpyc")):
            continue
        if name.startswith(ANDROID_PREFIXES):
            wanted.append((info, name[len(ANDROID_ASSET_ROOT) :]))

    if not wanted:
        raise AssetSetupError(
            "No DDLC assets were found in this file. "
            "Make sure it is a downloaded DDLC Android APK/XAPK."
        )

    _check_free_space(target_dir, sum(i.file_size for i, _ in wanted))

    total = len(wanted)
    for n, (info, rel) in enumerate(wanted, 1):
        if _mod_provides(rel, target_dir):
            continue
        out = _safe_join(staging, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with apk.open(info) as src, open(out, "wb") as dst:
            shutil.copyfileobj(src, dst, COPY_CHUNK)
        if n % 25 == 0 or n == total:
            _set_status(f"Extracting Android assets... ({n}/{total})")


def extract_android_xapk(apk_source):
    """
    Extracts the Android assets from DDLC into the mod's game directory.

    Args:
        apk_source (str | file object): The APK/XAPK (path or a seekable binary
            file object).

    Raises:
        AssetSetupError: If the archive isn't a usable DDLC Android package.
    """
    target_dir = get_android_game_dir()
    staging = os.path.join(target_dir, STAGING_DIR)
    nested_path = os.path.join(target_dir, NESTED_APK_NAME)

    shutil.rmtree(staging, ignore_errors=True)
    os.makedirs(staging)

    try:
        with zipfile.ZipFile(apk_source, "r") as outer:
            nested = [
                i for i in outer.infolist() if i.filename.lower().endswith(".apk")
            ]

            if nested:
                # XAPK/Split APK: find the nested APK that carries assets/game/.
                # Spooled to disk (not BytesIO) so we don't hold it in RAM.
                found = False
                for info in nested:
                    _check_free_space(target_dir, info.file_size)
                    _set_status("Scanning package...")
                    with outer.open(info) as src, open(nested_path, "wb") as dst:
                        shutil.copyfileobj(src, dst, COPY_CHUNK)
                    if _has_game_assets(nested_path):
                        found = True
                        break
                    os.remove(nested_path)

                if not found:
                    raise AssetSetupError(
                        "No DDLC assets were found in this XAPK. "
                        "Make sure it is the official DDLC Android package."
                    )
                with zipfile.ZipFile(nested_path, "r") as apk:
                    _unpack_apk(apk, staging, target_dir)
            else:
                # Standalone APK file
                _unpack_apk(outer, staging, target_dir)

        _set_status("Installing assets...")
        pairs = []
        for root, _dirs, files in os.walk(staging):
            for fname in files:
                src = os.path.join(root, fname)
                rel = os.path.relpath(src, staging)
                pairs.append((src, _safe_join(target_dir, rel)))
        _commit(pairs)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
        if os.path.exists(nested_path):
            try:
                os.remove(nested_path)
            except OSError:
                pass


###################################
# Worker Thread
###################################


def _finish_success():
    global asset_setup_complete
    _set_status("Extraction complete! Restarting...")
    asset_setup_complete = True
    renpy.invoke_in_main_thread(renpy.utter_restart)


def _run_job(mode: str, opener):
    """
    Worker body. `opener` is a callable returning a context manager that yields
    a path or seekable file object for the extractor.
    """
    global _job_running
    _job_running = True

    try:
        _set_status("Reading selected file...", busy=True)
        _cleanup_stale()

        with opener() as source:
            if mode == "pc":
                _set_status("Extracting PC assets...")
                extract_pc_zip(source)
            else:
                _set_status("Extracting Android assets...")
                extract_android_xapk(source)

        _finish_success()
    except AssetSetupError as e:
        _fail(str(e))
    except zipfile.BadZipFile:
        _fail(
            "That file isn't a valid ZIP/APK archive, or it is damaged. Try downloading it again."
        )
    except OSError as e:
        if e.errno == errno.ENOSPC:
            _fail("Not enough free storage to extract the DDLC assets.")
        else:
            _fail(f"File error during extraction: {e}")
    except Exception as e:
        _fail(f"Unexpected error during extraction: {type(e).__name__}: {e}")
    finally:
        _job_running = False
        _cleanup_stale()


def _start_job(mode: str, opener):
    threading.Thread(target=_run_job, args=(mode, opener), daemon=True).start()


def cancel_asset_setup():
    """
    Resets the UI if the picker never reported back (e.g. the activity was
    killed while it was open). No-op while an extraction is actually running.
    Returns None, so it's safe to use as a screen Function().
    """
    global _picker_token
    if _job_running:
        return
    _picker_token += 1  # Stops any pending picker poller.
    _set_status("", busy=False)


###################################
# File picker + URI access
###################################

if renpy.android:
    import time

    from jnius import autoclass  # type: ignore

    PythonSDLActivity = autoclass("org.renpy.android.PythonSDLActivity")
    Intent = autoclass("android.content.Intent")
    Activity = autoclass("android.app.Activity")
    Files = autoclass("java.nio.file.Files")
    StandardCopyOption = autoclass("java.nio.file.StandardCopyOption")
    File = autoclass("java.io.File")

    def _handle_picker_result(request_code: int, result_code: int, data):
        mode = _REQUEST_MODES.get(request_code)
        if mode is None:
            return False  # Not ours; keep waiting.

        try:
            if result_code != Activity.RESULT_OK or data is None:
                _set_status("Asset extraction canceled.", busy=False)
                return True

            uri = data.getData()
            if uri is None:
                _fail("Error: No file selected.")
                return True

            _start_job(mode, lambda: _open_picked_uri(uri))
        except Exception as e:
            _fail(f"Error handling the selected file: {e}")
        return True

    def _poll_picker(token: int):
        """
        RAPT's PythonSDLActivity has no result-listener API. Its
        onActivityResult() just stores the result in public fields, which
        are intended to be polled from Python.

        Args:
            token (int): The token to use for polling.
        """
        activity = PythonSDLActivity.mActivity

        while token == _picker_token:
            time.sleep(PICKER_POLL_INTERVAL)
            try:
                request_code = activity.mActivityResultRequestCode
                if request_code == -1:
                    continue
                result_code = activity.mActivityResultResultCode
                data = activity.mActivityResultResultData
                activity.mActivityResultRequestCode = -1  # Consume it.
                if _handle_picker_result(request_code, result_code, data):
                    return
            except Exception as e:
                _fail(f"Error reading the file picker result: {e}")
                return

    @contextmanager
    def _open_picked_uri(uri):
        """
        Yields a seekable binary file object for a SAF document URI.

        Preferred: a detached file descriptor (no copy). If the provider hands
        back a non-seekable descriptor, stream it into a temp file. Fallback to
        Files.copy if no descriptor is provided.

        Args:
            uri (urllib.parse.ParseResult): The URI to open.
        """
        resolver = PythonSDLActivity.mActivity.getContentResolver()
        temp_path = os.path.join(get_android_game_dir(), TEMP_IMPORT_NAME)
        f = None

        try:
            try:
                pfd = resolver.openFileDescriptor(uri, "r")
                f = os.fdopen(pfd.detachFd(), "rb")
            except Exception:
                f = None

            if f is not None and not f.seekable():
                _set_status("Copying selected file...")
                with open(temp_path, "wb") as out:
                    shutil.copyfileobj(f, out, COPY_CHUNK)
                f.close()
                f = open(temp_path, "rb")
            elif f is None:
                _set_status("Copying selected file...")
                stream = resolver.openInputStream(uri)
                try:
                    Files.copy(
                        stream,
                        File(temp_path).toPath(),
                        StandardCopyOption.REPLACE_EXISTING,
                    )
                finally:
                    stream.close()
                f = open(temp_path, "rb")

            yield f
        finally:
            if f is not None:
                try:
                    f.close()
                except Exception:
                    pass
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass

    def _launch_picker(request_code: int):
        global _picker_token
        activity = PythonSDLActivity.mActivity

        # Clear any stale result before launching.
        activity.mActivityResultRequestCode = -1
        activity.mActivityResultResultData = None

        intent = Intent(Intent.ACTION_OPEN_DOCUMENT)
        intent.addCategory(Intent.CATEGORY_OPENABLE)
        intent.setType("*/*")

        _picker_token += 1
        token = _picker_token
        activity.startActivityForResult(intent, request_code)
        threading.Thread(target=_poll_picker, args=(token,), daemon=True).start()


###################################
# Entry points called by the screen buttons (main thread; always return None)
###################################


def _prompt(request_code: int, status: str):
    if not renpy.android:
        return
    if not _try_begin(status):
        return  # Already busy; ignore double taps.

    try:
        _launch_picker(request_code)
    except Exception as e:
        _fail(f"Error opening file picker: {e}")


def prompt_and_extract_pc():
    """
    Opens the file manager to select a DDLC PC ZIP file for extraction.
    """
    _prompt(REQUEST_CODE_PC, "Select a DDLC PC ZIP file...")


def prompt_and_extract_android():
    """
    Opens the file manager to select a DDLC Android APK/XAPK file for extraction.
    """
    _prompt(REQUEST_CODE_ANDROID, "Select a DDLC Android APK/XAPK file...")
