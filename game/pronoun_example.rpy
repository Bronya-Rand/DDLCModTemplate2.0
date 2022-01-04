## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

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
            jump pronoun_menu
        "Current Pronoun":
            if not he:
                "You have yet set a pronoun."
            else:
                "Your current pronoun is [heC]/[himC]."
            jump pronoun_menu
        "Play a sample.":
            if not he:
                "You have yet set a pronoun. Set one up before proceeding."
                jump pronoun_menu
            mc "My pronouns are [he]/[him]."
            m "[hesC] here to learn about how dense [he] really [are]."
            s "Don't say mean things to [him]!"
            n "I don't like the looks of [him]."
            y "[areC[0]]-[areC] [he] going to be okay?"
            jump pronoun_menu
        "Clear Pronouns":
            $ he = ""
            $ him = ""
            $ are = ""
            $ hes = ""
            python:
                finishPronouns()

            "Cleared all Pronouns."
            jump pronoun_menu
        "Exit":
            pass
    return

label set_pronoun:
    menu:
        "What is your pronoun?"
        "He/Him":
            $ he = "he"
            $ him = "him"
            $ are = "is"
            $ hes = "he's"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()

            "Set Pronoun to He/Him."
            return
        "She/Her":
            $ he = "she"
            $ him = "her"
            $ are = "is"
            $ hes = "she's"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()
            python:
                finishPronouns()

            "Set Pronoun to She/Her."
            return
        "They/Them":
            $ he = "they"
            $ him = "them"
            $ are = "are"
            $ hes = "they're"
            $ heC = he.capitalize()
            $ himC = him.capitalize()
            $ areC = are.capitalize()
            $ hesC = hes.capitalize()
            python:
                finishPronouns()

            "Set Pronoun to They/Them."
            return
        "Return":
            pass
    return