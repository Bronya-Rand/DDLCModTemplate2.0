# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users and such about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher than the
# one the mod template was tested for.
## DO NOT MODIFY THIS FILE!

label lockdown_check:
    if renpy.version_tuple == (7, 4, 6, 1693):
        scene black
        "{b}Warning:{/b} A recent bug was introduced with the release of \"Ren'Py 7.4.6\" that breaks DDLC transforms heavily."
        "Currently, there is no available fix for this issue. Due to this, the DDLC Mod Template has been disabled on this version of Ren'Py until further notice."
        "For more information on this bug, you may visit this Ren'Py Issue Page over on {a=https://github.com/renpy/renpy/issues/2860}Github{/a} by clicking 'Github' in this textbox."
        "For now, if you want to mod DDLC in Ren'Py 7, you should mod under \"Ren'Py 7.4.5\" and wait until the template is tested on the latest version of Ren'Py from GanstaKingofSA."
        "Sorry for the modding inconvenience. Happy modding though!"
        $ renpy.quit()

    if renpy.version_tuple >= (7, 4, 5, 1621) and renpy.version_tuple != (7, 4, 6, 1693) and not lockdown_warning:
        scene black
        "{b}Warning:{/b} The DDLC Mod Template has detected that you are running the mod template under a version of Ren'Py that has not been tested on."
        "The last version of Ren'Py the mod template was tested on was \"Ren'Py 7.4.5\"."
        "Running the DDLC Mod Template on this version of Ren'Py may introduce compatibility issues or errors while you develop your mod."
        menu:
            "By proceeding to mod DDLC under this version of Ren'Py, you agree that you have acknoledged this disclaimer and accept any possible bugs or errors that may be introduced."
            "I agree.":
                $ lockdown_warning = True
                "You have agreed to this disclaimer. You may now proceed to mod DDLC under this version of Ren'Py. Happy modding!"
                return
            "I disagree.":
                "You have disagreed to this disclaimer. Due to this, the DDLC Mod Template will not run under this version of Ren'Py until you agree to the disclaimer."
                "If you want to mod DDLC, you should stick with modding DDLC under \"Ren'Py 7.4.5\" for now."
                "If you later decide to agree to the disclamer, you may run the Mod Template under this version again and agree to the disclaimer when asked."
                "Sorry for the modding inconvenience. Happy modding though!"
                $ renpy.quit()
        return
