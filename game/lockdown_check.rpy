# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher 
# than the one the mod template was tested for.
## DO NOT MODIFY THIS FILE! ##

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple >= (7, 4, 6, 1693) and renpy.version_tuple < (7, 4, 9, 2142):

        scene black
        "{b}Warning:{/b} A bug was introduced with the release of Ren'Py 7.4.6 that breaks DDLC transforms heavily."
        "This bug is semi-present still into Ren'Py 7.4.7 up to 7.4.8."
        "If you want to mod DDLC in Ren'Py 7, you should mod under {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a} or {a=https://renpy.org/release/7.4.9}{i}Ren'Py 7.4.9{/i}{/a}{a=https://renpy.org/release/7.4.10}{i}Ren'Py 7.4.10{/i}{/a}."
        "Sorry for the modding inconvenience. Happy modding though!"
        $ renpy.quit()

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
