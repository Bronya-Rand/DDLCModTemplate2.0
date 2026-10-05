## Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# core.rpy
# This file contains the major Python code for DDLC and the Mod Template + Features.
# Altering this file may break the game or mod functionality.

init -3 python:
    persistent = renpy.store.persistent
    store = renpy.store

    # The default splash message for the game that players will see when launching your mod.
    splash_message_default = (
        "This mod is an unofficial fan game that is unaffiliated with Team Salvato."
    )

    # Stores multiple splash messages that can be used in the game.
    splash_messages = [
        ":o",
        "Bronya... :o",
    ]


    ## DDLC Functions

    def _get_android_data_directory():
        """
        Returns the Android data directory path or None.
        """
        if not renpy.android:
            return None

        try:
            import jnius
            activity = jnius.autoclass("org.renpy.android.PythonSDLActivity")
            current_activity = jnius.cast("android.app.Activity", activity.mActivity)
            data_directory = current_activity.getFilesDir().getAbsolutePath()
            return data_directory
        except Exception:
            return os.environ.get("ANDROID_PUBLIC")


    def get_characters_folder():
        """
        Returns the path to the characters folder.
        """
        characters_folder = None
        if renpy.android:
            android_public_directory = _get_android_data_directory()
            if android_public_directory:
                characters_folder = os.path.join(android_public_directory, "characters")
        else:
            characters_folder = os.path.join(renpy.config.basedir, "characters").replace("\\", "/")

        return characters_folder


    def restore_character(characters):
        """
        Restores the specified characters to the 'characters' folder
        and removes any characters not in the list.

        :param characters: A character name (str) or a list of character names to restore.
        """
        if isinstance(characters, basestring):
            characters = [characters]

        characters_folder = get_characters_folder()
        if characters_folder is None:
            return

        if not os.path.exists(characters_folder):
            try:
                os.makedirs(characters_folder)
            except OSError:
                pass

        # Remove existing character files not in the restore list
        try:
            existing_files = os.listdir(characters_folder)
        except OSError:
            existing_files = []

        for existing_file in existing_files:
            if existing_file.endswith(".chr"):
                character_name = os.path.splitext(existing_file)[0]
                if character_name not in characters:
                    try:
                        os.remove(os.path.join(characters_folder, existing_file))
                    except OSError:
                        pass

        # Restore specified character files
        for character in characters:
            character_file_path = os.path.join(characters_folder, character + ".chr")
            if not os.path.exists(character_file_path):
                src_path = os.path.join("chrs", character + ".chr").replace("\\", "/")
                try:
                    src_file = renpy.file(src_path)
                    data = src_file.read()
                    src_file.close()
                    with open(character_file_path, "wb") as char_file:
                        char_file.write(data)
                except (IOError, OSError):
                    pass


    def restore_characters():
        """
        Restores all characters depending on the current playthrough.
        """
        if renpy.store.persistent.playthrough == 0:
            restore_character(["monika", "natsuki", "sayori", "yuri"])
        elif (
            renpy.store.persistent.playthrough == 1
            or renpy.store.persistent.playthrough == 2
        ):
            restore_character(["monika", "natsuki", "yuri"])
        elif renpy.store.persistent.playthrough == 3:
            restore_character(["monika"])
        else:
            restore_character(["natsuki", "sayori", "yuri"])


    def restore_all_characters():
        """
        Backward compatibility alias for older scripts.
        """
        restore_characters()


    def restore_relevant_characters():
        """
        Backward compatibility alias for older scripts.
        """
        restore_characters()


    def delete_character(name):
        """
        Deletes a character file from the 'characters' folder.
        """
        characters_folder = get_characters_folder()
        if characters_folder is None:
            return

        try:
            os.remove(os.path.join(characters_folder, name + ".chr"))
        except OSError:
            pass


    def initialize_characters_folder():
        """
        Initializes the characters folder by creating it if it does not exist.
        """
        characters_folder = get_characters_folder()
        if characters_folder is not None and not os.path.exists(characters_folder):
            try:
                os.makedirs(characters_folder)
            except OSError:
                pass

        restore_characters()


    def delete_all_saves():
        """
        Deletes all save files in the game.
        """
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
        try:
            renpy.loadsave.location.unlink_persistent()
        except Exception:
            pass
        renpy.persistent.should_save_persistent = False


    def get_pos(channel="music"):
        """
        Returns the current position of the specified music channel.
        """
        pos = renpy.music.get_pos(channel)
        if pos is not None:
            return pos
        return 0


    def pause(time=None):
        """
        Pauses the game for a specified amount of time or indefinitely.
        """
        global _windows_hidden

        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0:
            return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False


    ## OS Functions

    def get_process_list():
        """
        Retrieves the list of currently running processes on the system.
        """
        if renpy.android:
            return set()

        process_list = set()
        if renpy.windows:
            try:
                p = subprocess.Popen(
                    ["powershell", "-NoProfile", "-Command", "(Get-Process).ProcessName"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                )
                stdout, _ = p.communicate()
                for line in stdout.splitlines():
                    proc = line.strip().lower()
                    if proc:
                        process_list.add(proc + ".exe")
            except Exception:
                pass
        else:
            try:
                p = subprocess.Popen(
                    "ps -eo comm=",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                )
                stdout, _ = p.communicate()
                for line in stdout.splitlines():
                    parts = line.strip().split()
                    if parts:
                        proc = parts[0].strip().lower()
                        if proc:
                            process_list.add(proc)
            except Exception:
                pass

        return process_list


    def process_check(stream_list):
        """
        Checks whether the given application stream list is running on the current system.
        """
        targets = list(stream_list)
        if not renpy.windows:
            for index, process in enumerate(targets):
                targets[index] = process.replace(".exe", "")

        process_list = get_process_list()
        for process in targets:
            for running_process in process_list:
                if running_process == process or running_process.startswith(process + "/"):
                    return True
        return False


    def is_user_streaming():
        """
        Checks if any known streaming applications are currently running.
        """
        streaming_apps = [
            "obs.exe",
            "obs64.exe",
            "obs32.exe",
            "streamlabsobs.exe",
            "xsplit.core.exe",
            "xsplit.broadcaster.exe",
            "twitchstudio.exe",
            "elgato.streamdeck.exe",
            "nvidia.share.exe",
            "amd.raptr.exe",
            "zoom.exe",
            "teams.exe",
            "livehime.exe",
            "pandatool.exe",
            "yymixer.exe",
            "douyutool.exe",
            "huomaotool.exe",
        ]
        return process_check(streaming_apps)


    def get_user_account_name():
        """
        Retrieves the current user's account name.
        """
        if renpy.android:
            return None

        # Reject if streaming to protect privacy
        if is_user_streaming():
            return None

        try:
            if renpy.windows:
                p = subprocess.Popen("whoami", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                stdout, _ = p.communicate()
                name = stdout.strip().split("\\")[-1]
                return name if name else None
            else:
                p = subprocess.Popen("id -un", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                stdout, _ = p.communicate()
                name = stdout.strip()
                return name if name else None
        except Exception:
            return None


    def get_windows_version():
        """
        Retrieves the current Windows version tuple (major, minor, build).
        """
        if not renpy.windows:
            return None

        try:
            version = sys.getwindowsversion()
            return (version.major, version.minor, version.build)
        except Exception:
            return None


    def get_macos_version():
        """
        Retrieves the current macOS version tuple (major, minor, patch).
        """
        if not renpy.macintosh:
            return None

        try:
            release, _, _ = platform.mac_ver()
            if release != "":
                version_parts = release.split(".")
                if len(version_parts) >= 2:
                    major = int(version_parts[0])
                    minor = int(version_parts[1])
                    patch = int(version_parts[2]) if len(version_parts) > 2 else 0
                    return (major, minor, patch)
        except Exception:
            pass

        return None


    def ddlc_under_steam():
        """
        Checks if the game is running through Steam.
        """
        return "steamapps" in renpy.config.basedir.lower()


    currentuser = get_user_account_name()


    ## Template Functions

    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        """
        Recolorizes the image at the given path with the specified colors and contrast.
        """
        return renpy.im.MatrixColor(
            renpy.im.MatrixColor(
                renpy.im.MatrixColor(
                    path, renpy.im.matrix.desaturate() * renpy.im.matrix.contrast(contr)
                ),
                renpy.im.matrix.colorize("#00f", "#fff") * renpy.im.matrix.saturation(120),
            ),
            renpy.im.matrix.desaturate() * renpy.im.matrix.colorize(blackCol, whiteCol),
        )


    ### Dynamic Super Positioning
    def dsp(original_position_value):
        """
        Dynamically adjusts the position value of an element based on the
        original game's screen size (1280x720) against the set screen size.
        """
        valueIsInt = isinstance(original_position_value, int)
        scale_position_by = renpy.config.screen_width / 1280.0
        if valueIsInt:
            return int(original_position_value * scale_position_by)
        return original_position_value * scale_position_by


    ### Dynamic Super Resolution
    def dsr(image_path):
        """
        Dynamically adjusts the size of the image based on the original game's
        screen size (1280x720) against the set screen size.
        """
        image_bounds = renpy.image_size(image_path)
        return renpy.Transform(
            image_path, size=(dsp(image_bounds[0]), dsp(image_bounds[1]))
        )


    ## Initialize Core Code

    # Setup mapping for the game menu and hide windows.
    if "game_menu" in renpy.config.keymap and "mouseup_3" in renpy.config.keymap["game_menu"]:
        renpy.config.keymap["game_menu"].remove("mouseup_3")
    if "hide_windows" in renpy.config.keymap and "mouseup_3" not in renpy.config.keymap["hide_windows"]:
        renpy.config.keymap["hide_windows"].append("mouseup_3")
    renpy.config.keymap["self_voicing"] = []
    renpy.config.keymap["clipboard_voicing"] = []
    renpy.config.keymap["toggle_skip"] = []

    # Register the music channel for the poem game and poem sharing.
    renpy.music.register_channel("poem", mixer="music", tight=True)
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("page_turn", mixer="music", tight=True)

    # Initialize gesture mapping for Android devices.
    if renpy.android:
        renpy.config.keymap["rollback"] = []
        renpy.config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]

    renpy.pure(dsp)
