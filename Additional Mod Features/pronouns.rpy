## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## pronoun_example.rpy
# This file asks the user for their pronoun input.

default pronoun_temp = ""

init python:
    def SetPronoun(type):
        global pronoun_temp
        if not pronoun_temp: return
        if type == "he":
            persistent.he = pronoun_temp.lower()
            he = pronoun_temp.lower()
            he_capital = pronoun_temp.lower().capitalize()
        elif type == "he's":
            persistent.hes = pronoun_temp.lower()
            hes = pronoun_temp.lower()
            hes_capital = pronoun_temp.lower().capitalize()
        elif type == "are":
            persistent.are = pronoun_temp.lower()
            are = pronoun_temp.lower()
            are_capital = pronoun_temp.lower().capitalize()
        elif type == "him":
            persistent.him = pronoun_temp.lower()
            him = pronoun_temp.lower()
            him_capital = pronoun_temp.lower().capitalize()
        pronoun_temp = ""

label pronoun_screen:
    $ renpy.call_screen("pronoun_input", message="Enter your first pronoun (He/She/They)", ok_action=Function(SetPronoun, type="he"))
    $ renpy.call_screen("pronoun_input", message="Enter your second pronoun (He's/She's/They're)", ok_action=Function(SetPronoun, type="he's"), hes=True)
    $ renpy.call_screen("pronoun_input", message="Enter your third pronoun (Him/Her/Them)", ok_action=Function(SetPronoun, type="him"))
    $ renpy.call_screen("pronoun_input", message="Enter your fourth pronoun (Is/Are)", ok_action=Function(SetPronoun, type="are"))
    return

screen pronoun_input(message, ok_action, hes=False):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            
            python:
                allowList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                if hes:
                    allowList = allowList + "'"

            input default "" value VariableInputValue("pronoun_temp") length 12 allow allowList

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action [ok_action, Return(0)]