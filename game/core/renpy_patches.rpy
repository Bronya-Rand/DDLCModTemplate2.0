## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## renpy_patches.rpy
# This file is mainly designed to patch certain versions of Ren'Py that break 
# DDLC/DDLC mods by patching the Ren'Py engine at startup.
        
python early:
    import os
    ## Readds WMIC using Powershell's Get-WmiObject class (for Win 11)
    os.environ['wmic process get Description'] = "powershell (Get-Process).ProcessName"
    os.environ['wmic os get version'] = "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"

    ## Games produced with this version use the model-based renderer by
    ## default.
    ## We will disable this to retain Act 3 effects but you may disable
    ## this if you need model-based rendering
    if renpy.version_tuple >= (7, 4, 5, 1648):
        config.gl2 = False

    ## An ATL displayable will now start its animation when it first 
    ## appears, rather than when the screen itself is shown.
    ## We will disable this for DDLC's transform's sakes.
    if renpy.version_tuple >= (7, 4, 7, 1862):
        config.atl_start_on_show = False 
