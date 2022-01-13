## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.
## You may only use this file/feature only for DDLC mods and not for DDLC patchers,
## unofficial fixes, etc.

## pronoun_example.rpy

# This file serves as a example to the pronoun feature.
# Use this as a example on how to use the pronoun feature.

label pronoun_example:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    jump pronoun_menu
    
label pronoun_menu:
    menu:
        "Select a option."
        "Select a Pronoun":
            call set_pronoun

        "Current Pronoun":
            if not he:
                "You have yet set a pronoun."
            else:
                "Your current pronoun is [he_capital]/[him_capital]."
            jump pronoun_menu

        "Play a sample.":
            if not he:
                "You have yet set a pronoun. Set one up before proceeding."
                jump pronoun_menu
            mc "My pronouns are [he]/[him]."
            m "[hes_capital] here to learn about how dense [he] really [are]."
            s "Don't say mean things to [him]!"
            n "I don't like the looks of [him]."
            y "[are_capital[0]]-[are_capital] [he] going to be okay?"
            jump pronoun_menu

        "Clear Pronouns":
            $ he = ""
            $ him = ""
            $ are = ""
            $ hes = ""
            $ he_capital = ""
            $ him_capital = ""
            $ are_capital = ""
            $ hes_capital = ""
            python:
                finishPronouns()

            "Cleared all Pronouns."
            jump pronoun_menu
            
        "Exit":
            return
    return

label set_pronoun:
    menu:
        "What is your pronoun?"
        "He/Him":
            $ he = "he"
            $ him = "him"
            $ are = "is"
            $ hes = "he's"
            python:
                finishPronouns()

            "Set Pronoun to He/Him."

        "She/Her":
            $ he = "she"
            $ him = "her"
            $ are = "is"
            $ hes = "she's"
            python:
                finishPronouns()

            "Set Pronoun to She/Her."

        "They/Them":
            $ he = "they"
            $ him = "them"
            $ are = "are"
            $ hes = "they're"
            python:
                finishPronouns()

            "Set Pronoun to They/Them."

    $ he_capital = he.capitalize()
    $ him_capital = him.capitalize()
    $ are_capital = are.capitalize()
    $ hes_capital = hes.capitalize()
    jump pronoun_menu