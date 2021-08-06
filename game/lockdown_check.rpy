# Lockdown_check.rpy

# This file is not part of DDLC. This file is mainly designed to 
# warn new users about template issues with certain Ren'Py versions
# or warn them about Quality Assurance with Ren'Py versions higher 
# than the one the mod template was tested for.
## DO NOT MODIFY THIS FILE! ##

label lockdown_check:

    if renpy.version_tuple >= (7, 4, 6, 1693):
        scene black
        "{b}Warning:{/b} A recent bug was introduced with the release of \"Ren'Py 7.4.6\" that breaks DDLC transforms heavily."
        "This bug is semi-present still into Ren'Py 7.4.7 and higher with high uncertainty for future releases."
        "Currently, there is yet no fix to this issue. Due to this, the DDLC Mod Template has been disabled on any Ren'Py version higher than 7.4.5."
        "For now, if you want to mod DDLC in Ren'Py 7, you should mod under {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a} and wait until the issue is mitigated in a new release and is tested by GanstaKingofSA."
        "Sorry for the modding inconvenience. Happy modding though!"
        $ renpy.quit()
    else:
        $ persistent.lockdown_warning = True
        return
