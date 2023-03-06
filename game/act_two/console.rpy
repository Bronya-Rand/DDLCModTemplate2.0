## console.rpy

# This file defines the Monika Console contents that appears in the game when
# Monika deletes characters.

# This file has heavily changed from DDLC to provide better access to call the 
# console than via labels. To call, do $ run_input(input="Text", output="Output").
# To only show, the console, just do `show screen console_screen`.
# Thank you Lezalith for assistance in making this new console!

init -1:

    # None or tuple with (input, output).
    default new_input = None

    # List with outputs.
    default console_history = []

    # Not to be changed midgame.
    # Delay after input has finished showing, before output is displayed.
    define console_delay = 0.5

    define console_cps = 30

init python:

    # Make the console display the given input and output.
    def run_input(input, output):
        global new_input

        new_input = (input, output)

        if renpy.get_screen("console_screen"):
            renpy.hide_screen("console_screen")
        renpy.call_screen("console_screen", finish=True)
        renpy.show_screen("console_screen")

    # Add the output to history.
    def add_to_history(input):
        global console_history

        console_history.insert(0, input[1])
        if len(console_history) > 5:
            console_history.pop(5)

    # Add the output to history after code is done
    def input_finished():
        global new_input

        add_to_history(new_input)
        new_input = None
        
        renpy.restart_interaction()

    def clear_history():
        global console_history

        console_history = []

screen console_screen(finish=False):

    style_prefix "console_screen"

    default finish_actions = [Function(input_finished), SetScreenVariable("in_progress", False), Return()]

    # String of input to show.
    # It is put outside of the new_input variable so it doesn't
    # start over and over.
    default new_input_code = "_"

    # Changes to True once a new code_text 
    default in_progress = False

    # If text is not in the process of showing.
    if not in_progress:

        $ new_input_code = "_"

        # If a new_input is available, set it as code to display.
        if store.new_input:

            $ in_progress = True
            $ new_input_code = store.new_input[0]

    # New code is showing.
    if in_progress:

        timer ( float(len(renpy.filter_text_tags(new_input_code, deny = []))) / float(console_cps) + console_delay ) action finish_actions

    frame:

        vbox:
            hbox:
                text ">" xpos 5 ypos 10

                text new_input_code xpos 15 ypos 10:
                    slow_cps 30
                    xmaximum 460

            vbox:
                xpos 26 ypos 30 
                spacing 5
                for x in store.console_history:
                    text x

style console_screen_frame:
    background Frame(Transform(Solid("#333"), alpha=0.75))
    xsize 480
    ysize 180

# This style declares the text appearance of the text shown in the console in-game.
style console_screen_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []

# This label clears all console history and commands from the console in-game.
# Decided to keep this for now as it just pauses stuff.
label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return