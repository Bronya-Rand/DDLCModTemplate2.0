# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa' are in the
# game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs
# and decompile them for the builds to work.

import os
from game.core.py.template_checks_ren import DDLCRPAsMissing, IllegalModLocation
import renpy  # type: ignore

"""renpy
init -100 python:
"""

if not renpy.android:
    for archive in ["audio", "images", "fonts"]:
        if archive not in renpy.config.archives:
            raise DDLCRPAsMissing(archive)

    if renpy.windows:
        onedrive_path = os.environ.get("OneDrive")
        if onedrive_path is not None:
            if onedrive_path in renpy.config.basedir:
                raise IllegalModLocation
