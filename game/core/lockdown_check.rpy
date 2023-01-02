## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## lockdown_check.rpy
# This file is mainly designed to warn new modders about bugs with certain Ren'Py 
# versions or warn them about QA issues with running Ren'Py versions higher than 
# the one the mod template was tested for.
# New in 4.0.0: Add lockout for Ren'Py 6/7 on Py 3 templates.

## DO NOT MODIFY THIS FILE! ##

# Checks if we are on Ren'Py 8
python early:

    if renpy.version_tuple < (8, 0, 0, 22062402):
        raise NotRenPyEight

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple > (8, 0, 3, 22090809):

        scene black
        "{b}Warning:{/b} The version of Ren'Py you are trying to mod DDLC on has not been tested for modding compatibility."
        "The last recent version of Ren'Py 8 that works for DDLC mods is \"{i}Ren'Py 8.0.3{/i}\"."
        "Running DDLC or your DDLC mod on a higher version than the one tested may introduce bugs and other game breaking features."
        
        menu:
            "By continuing to run your mod on [version!q], you acknoledge this disclaimer and the possible problems that can happen on a untested Ren'Py version."
            "I agree.":
                $ persistent.lockdown_warning = True
                return

    else:
        $ persistent.lockdown_warning = True
        return
