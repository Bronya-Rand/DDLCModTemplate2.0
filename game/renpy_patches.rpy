## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## renpy_patches.rpy
# This file is mainly designed to patch certain versions of Ren'Py that break 
# DDLC/DDLC mods by patching the Ren'Py engine at startup.
## Since this is Ren'Py 8/Py3 branch, some patches have been removed due to
## being obsolete.

init -1 python:
    ## Patches the Monika Space Room Effects however it might disable
    ## OpenGL 2 for some mods that use it. If you do use OpenGL 2, comment
    ## these two lines out.
    if renpy.version_tuple >= (7, 4, 5, 1648):
        config.gl2 = False

### DO NOT MODIFY ANYTHING BEYOND THIS POINT ###

## Patches 'wmic' environment variables with 'powershell' instead.
python early:
    import os
    os.environ['wmic process get Description'] = "powershell (Get-Process).ProcessName"
    os.environ['wmic os get version'] = "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"

    ## Fixes a issue where some transitions (menu bg) reset themselves
    if renpy.version_tuple >= (7, 4, 7, 1862):
        config.atl_start_on_show = False 
