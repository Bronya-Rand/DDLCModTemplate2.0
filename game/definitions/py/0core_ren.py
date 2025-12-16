# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file handles locking the game to ensure that only one instance is running at a time.
# This is basically a revamped version of `singleton.py` to allow enabling/disabling singleton behavior.

"""renpy
python early:
"""

import os
import tempfile
import sys

if sys.platform == "win32":
    import msvcrt  # For Windows systems
else:
    import fcntl  # For Unix/Linux systems

# Enables/Disables running only one instance of the game at a time.
# Set to False to allow multiple instances.
# Note: This is not recommended for most DDLC mods.
ENABLE_SINGLETON = True


class SingleInstance:
    """
    A class to ensure that only one instance of the game is running at a time.
    """

    def __init__(self):
        lock_file = "ddlc.lock"
        temp_dir = os.path.join(tempfile.gettempdir(), lock_file)

        self.lock_file = temp_dir
        self.lock_fd = None

        if not self.acquire_lock():
            sys.exit(-1)

    def acquire_lock(self):
        """
        Acquire a lock on the lock file to ensure only one instance runs.

        :return bool: True if the lock was acquired, False otherwise.
        """
        if not ENABLE_SINGLETON:
            return True

        try:
            self.lock_fd = open(self.lock_file, "w+")
            if sys.platform == "win32":
                msvcrt.locking(self.lock_fd.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except (IOError, OSError):
            if self.lock_fd:
                self.lock_fd.close()
                self.lock_fd = None
            return False

    def release_lock(self):
        """
        Release the lock on the lock file.
        """
        if not ENABLE_SINGLETON:
            return

        if self.lock_fd:
            if sys.platform == "win32":
                msvcrt.locking(self.lock_fd.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
            self.lock_fd.close()
            try:
                os.remove(self.lock_file)
            except OSError:  # Someone removed it...
                pass
        self.lock_fd = None

    def __del__(self):
        self.release_lock()


# Create a singleton instance to enforce single instance behavior.
# Do not remove this line. If you wish to disable singleton behavior, set
# `ENABLE_SINGLETON` to False above.
_singleton = SingleInstance()
