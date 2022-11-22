## console.rpy

# This file defines the Monika Console contents that appears in the game when
# Monika deletes characters.

# This image makes a gray imagebox for the console in-game.
image console_bg:
    "#333"
    topleft
    alpha 0.75 size (480,180)

# This style declares the text appearance of the text shown in the console in-game.
style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []

# This style controls the text speed of text shown in the console in-game.
style console_text_console is console_text:
    slow_cps 30

# This variable stores the console input and output sent to the console in-game.
default consolehistory = []

# This image shows the console text in the console in-game.
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)

# This image shows the console's past commands in the console in-game.
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)

# This image shows a right arrow in the console for command input in the console 
# in-game.
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

# This label calls the console used in-game for commands.
label updateconsole(text="", history=""):
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    show console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

# This label clears all console history and commands from the console in-game.
label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return

# This label is a left-over label for the console in-game from DDLC's development.
label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole (drawtext=currenttext)
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    $ pause(0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

    label drawconsole(drawtext=""):

        show console_text "[drawtext]_" as ctext zorder 100

        return

# This label adds certain text to the console history.
label updateconsolehistory(text=""):
    if text:
        python:
            consolehistory.insert(0, text)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history "[consolehistorydisplay]" as chistory zorder 100
    return

# This label hides the console in-game.
label hideconsole:
    hide console_bg
    hide console_caret

    hide ctext
    hide chistory
