# Contents
> These files are crucial to DDLC/the mod template itself. **DO NOT** delete or edit these files (except `credits.rpy`) unless you know what you are doing.

## 0imports.rpy
This file imports the needed python modules necessary for DDLC and the template to run properly.

## credits.rpy
This file defines the code for the credits that play at the end of Act Four.

## exceptions.rpy
This file stores the exceptions that the mod template can throw to you during development. The following exceptions stored in this file that can occur are:

- `NotRenPyEight` - You are attempting to run this mod project on Ren'Py 6 or 7.
   > Solution: Run your mod in Ren'Py 8 or download the Python 2 template and make your mod from scratch with it.
- `DDLCRPAsMissing` - You are missing a RPA file in the *game* folder which the game requires in order to load the game properly. 
   > Solution: Add the missing RPA and try relaunching the game again.
- `IllegalModLocation` - You have placed your mod/mod project in a location that the mod template prohibits (usually the OneDrive folder). 
   > Solution: Move the mod/mod project to a different location and try relaunching the game again.

## lockdown_check.rpy
This file checks to see if you are running the mod template on a prohibited Ren'Py version, Ren'Py 8 or a untested Ren'Py version and warns you about it.

## renpy_patches.rpy
This file contains patches necessary for DDLC to run properly on higher versions of Ren'Py.