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
            $ pronoun1 = "he"
            $ pronoun2 = "him"
            $ pronoun1C = pronoun1.capitalize()
            $ pronoun2C = pronoun2.capitalize()
            $ persistent.pronoun1 = pronoun1
            $ persistent.pronoun2 = pronoun2

            "Set Pronoun to He/Him."
            $ renpy.jump('pronoun_menu')
        "She/Her":
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun1C = pronoun1.capitalize()
            $ pronoun2C = pronoun2.capitalize()
            $ persistent.pronoun1 = pronoun1
            $ persistent.pronoun2 = pronoun2

            "Set Pronoun to She/Her."
            $ renpy.jump('pronoun_menu')
        "They/Them":
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun1C = pronoun1.capitalize()
            $ pronoun2C = pronoun2.capitalize()
            $ persistent.pronoun1 = pronoun1
            $ persistent.pronoun2 = pronoun2

            "Set Pronoun to They/Them."
            $ renpy.jump('pronoun_menu')
        "Current Pronoun":
            if not pronoun1 and not pronoun2:
                "You have yet set a pronoun."
            else:
                "Your current pronoun is [pronoun1C]/[pronoun2C]."
            $ renpy.jump('pronoun_menu')
        "Play a sample.":
            if not pronoun1 and not pronoun2:
                "You have yet set a pronoun. Set one up before proceeding."
                $ renpy.jump('pronoun_menu')
            mc "My pronouns are [pronoun1]/[pronoun2]."
            if pronoun1 == "they":
                m "[pronoun1C] are here to learn about how dense [pronoun1] really are."
            else:
                m "[pronoun1C] is here to learn about how dense [pronoun1] really is."
            s "Don't say mean things to [pronoun2]!"
            n "I don't like the looks of [pronoun2]."
            if pronoun1 == "they":
                y "A-Are [pronoun1] going to be okay?"
            else:
                y "I-Is [pronoun1] going to be okay?"
            $ renpy.jump('pronoun_menu')
        "Clear Pronouns":
            $ pronoun1 = ""
            $ pronoun2 = ""
            $ pronoun1C = ""
            $ pronoun2C = ""
            $ persistent.pronoun1 = pronoun1
            $ persistent.pronoun2 = pronoun2

            "Cleared all Pronouns."
            $ renpy.jump('pronoun_menu')
        "Exit":
            return
    return