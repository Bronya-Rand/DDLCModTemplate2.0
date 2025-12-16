# This file contains the Python code that is needed for DDLC to function correctly on Ren'Py 8.

## These imports are not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import os
import renpy  # type: ignore

"""renpy
python early:
"""

# Patches old DDLC Windows commands to use PowerShell for compatibility with Windows 11.
if renpy.windows:
    os.environ["wmic process get Description"] = "powershell (Get-Process).ProcessName"
    os.environ["wmic os get version"] = (
        "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"
    )

## An ATL displayable will now start its animation when it first
## appears, rather than when the screen itself is shown.
## We will disable this for DDLC's transform's sakes.
if renpy.version_tuple >= (7, 4, 7, 1862):
    renpy.config.atl_start_on_show = False
