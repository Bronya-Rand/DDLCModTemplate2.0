# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to warn new modders
# about bugs with certain Ren'Py versions or warn them about QA issues with running 
# Ren'Py versions higher than the one the mod template was tested for.

## DO NOT MODIFY THIS FILE! ##

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple > (7, 4, 10, 2178):

        scene black
        "{b}Warning:{/b} The version of Ren'Py you are trying to mod DDLC on has not been tested for modding compatibility."
        "The last recent version of Ren'Py that works for DDLC mods is \"{i}Ren'Py 7.4.10{/i}\"."
        "Running DDLC or your DDLC mod on a higher version than the one tested may introduce bugs and other game breaking features."
        
        menu:
            "By continuing to run your mod on [version!q], you acknoledge that you have read this warning message and understand the possible problems that can happen on a untested Ren'Py version."
            "I agree.":
                $ persistent.lockdown_warning = True
                return
            "I disagree.":
                "You have disagreed to this warning message. In order to mod DDLC on a higher version of Ren'Py than the one tested, you must accept the warning message."
                $ renpy.quit()

    else:
        $ persistent.lockdown_warning = True
        return
