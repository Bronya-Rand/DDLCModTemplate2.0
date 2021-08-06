# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users and such about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher than the
# one the mod template was tested for.
## DO NOT MODIFY THIS FILE!


label lockdown_check:

    if renpy.version_tuple >= (7, 4, 6, 1693):
        scene black
        "{b}Warning:{/b} A recent bug was introduced with the release of \"Ren'Py 7.4.6\" that breaks DDLC transforms heavily."
        "This bug is semi-present still into Ren'Py 7.4.7 and higher with high uncertainty for future releases."
        "Currently, there is yet no fix to this issue. Due to this, the DDLC Mod Template has been disabled on any Ren'Py version higher than 7.4.5."
        "For now, if you want to mod DDLC in Ren'Py 7, you should mod under {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a} and wait until the issue is mitigated in a new release and is tested by GanstaKingofSA."
        "Sorry for the modding inconvenience. Happy modding though!"
        $ renpy.quit()
    # elif renpy.version_tuple >= (7, 4, 5, 1621) and renpy.version_tuple not in blacklisted_renpy_versions and not persistent.lockdown_warning:
    #     scene black
    #     "{b}Warning:{/b} The DDLC Mod Template has detected that you are running the mod template under a version of Ren'Py that has not been tested on."
    #     "The last version of Ren'Py the mod template was tested on was {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a}."
    #     "Running the DDLC Mod Template on this version of Ren'Py may introduce compatibility issues or errors while you develop your mod."
    #     menu:
    #         "By proceeding to mod DDLC under this version of Ren'Py, you agree that you have acknoledged this disclaimer and accept any possible bugs or errors that may be introduced."
    #         "I agree.":
    #             $ persistent.lockdown_warning = True
    #             "You have agreed to this disclaimer. You may now proceed to mod DDLC under this version of Ren'Py. Happy modding!"
    #             return
    #         "I disagree.":
    #             "You have disagreed to this disclaimer. Due to this, the DDLC Mod Template will not run under this version of Ren'Py until you agree to the disclaimer."
    #             "If you want to mod DDLC, you should stick with modding DDLC under {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a} for now."
    #             "If you later decide to agree to the disclamer, you may run the Mod Template under this version again and agree to the disclaimer when asked."
    #             "Sorry for the modding inconvenience. Happy modding though!"
    #             $ renpy.quit()
    else:
        $ persistent.lockdown_warning = True
        return
