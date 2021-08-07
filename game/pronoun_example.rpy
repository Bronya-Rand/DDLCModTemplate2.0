# pronoun_example.rpy

# This file serves as a example to the pronoun feature.
# Use this as a example on how to use the pronoun feature.

label pronoun_example:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    $ renpy.jump('pronoun_menu')
    
label pronoun_menu:
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
            $ renpy.jump('pronoun_menu')
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
            $ renpy.jump('pronoun_menu')
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
            $ renpy.jump('pronoun_menu')
        "Current Pronoun":
            if not he:
                "You have yet set a pronoun."
            else:
                "Your current pronoun is [heC]/[himC]."
            $ renpy.jump('pronoun_menu')
        "Play a sample.":
            if not he:
                "You have yet set a pronoun. Set one up before proceeding."
                $ renpy.jump('pronoun_menu')
            mc "My pronouns are [he]/[him]."
            m "[hesC] here to learn about how dense [he] really [are]."
            s "Don't say mean things to [him]!"
            n "I don't like the looks of [him]."
            y "[areC[0]]-[areC] [he] going to be okay?"
            $ renpy.jump('pronoun_menu')
        "Clear Pronouns":
            $ he = ""
            $ him = ""
            $ are = ""
            $ hes = ""
            python:
                finishPronouns()

            "Cleared all Pronouns."
            $ renpy.jump('pronoun_menu')
        "Exit":
            return
    return