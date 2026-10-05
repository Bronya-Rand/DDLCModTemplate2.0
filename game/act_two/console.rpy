## console.rpy

# This file defines the Monika Console contents that appears in the game when
# Monika deletes characters.

# This file has heavily changed from DDLC to provide better access to call the 
# console than via labels. To call, do $ console(input_text="Text", output_text="Output").
# To only show the console, just do `show screen console_screen`.
# Legacy calls like `run_input(...)` and `call updateconsole(...)` are also supported.
# Thank you Lezalith for assistance in making this new console!

init python:

    class Console(object):
        """
        Handles the console logic for DDLC's "terminal".
        """

        def __init__(
            self,
            console_delay,
            console_cps,
            max_log_history=5,
            testing=False,
        ):
            """
            Initializes the console with the given delay and characters per second (cps).

            :param console_delay: Delay after input has finished showing, before output is displayed.
            :param console_cps: Characters per second for output display.
            :param max_log_history: Maximum number of log entries to keep.
            :param testing: Bypasses Ren'Py's screen system for testing purposes. Unused in DDLC.

            :type console_delay: float
            :type console_cps: int
            :type max_log_history: int
            :type testing: bool
            """

            self.console_delay = console_delay
            self.console_cps = console_cps
            self.max_log_history = max_log_history

            # Initialize the console history as an empty dictionary.
            self.console_history = {}

            self.testing = testing

        def __call__(self, input_text, output_text, cps=None, delay=None):
            """
            Processes the input and output text for the console.
            If you want specific stuff to happen whilst the input is being displayed,
            you should add it here.

            :param input_text: The input text to be processed.
            :param output_text: The output text to be displayed after the input.
            :param cps: Characters per second for output display. If None, uses the console's default cps.
            :param delay: Delay after input has finished showing, before output is displayed. If None, uses the console's default delay.
            :type input_text: str
            :type output_text: str
            :type cps: int | None
            :type delay: float | None
            """

            # If console history exceeds the maximum with a new entry, remove the oldest entry.
            if len(self.console_history) + 1 > self.max_log_history:
                oldest_key = min(self.console_history.keys())
                del self.console_history[oldest_key]

            # Show the console screen with the input and output.
            if not self.testing:
                if renpy.get_screen("console_screen"):
                    renpy.hide_screen("console_screen")
                renpy.call_screen(
                    "console_screen",
                    console=self,
                    input_text=input_text,
                    output_text=output_text,
                    cps=cps,
                    delay=delay,
                )

            # Store the input and output in the console history.
            self.console_history[input_text] = output_text
            self.show_screen()

            renpy.restart_interaction()

        def clear_history(self):
            """
            Clears the console history.
            """
            self.console_history.clear()

        def show_screen(self):
            """
            Shows the console screen.
            """
            if not self.testing:
                renpy.show_screen("console_screen", console=self)

    ## Backward-compatibility functions for DDLC / older mod scripts
    def run_input(input, output):
        console(input, output)

    def clear_history():
        console.clear_history()

init -1:
    default console = Console(console_delay=0.5, console_cps=30, max_log_history=5)

screen console_screen(console=console, input_text=None, output_text=None, cps=None, delay=None):
    style_prefix "console_screen"

    default finish_actions = [SetScreenVariable("in_progress", False), Return()]

    python:
        used_cps = cps if cps is not None and type(cps) == int else console.console_cps
        used_delay = delay if delay is not None and type(delay) == float else console.console_delay

    # String of input to show.
    # It is put outside of the new_input variable so it doesn't
    # start over and over.
    default new_input_code = "_"

    # Changes to True once a new code_text 
    default in_progress = False

    # If text is not in the process of showing.
    if not in_progress:

        $ new_input_code = "_"

        if input_text:
            $ in_progress = True
            $ new_input_code = input_text

    # New code is showing.
    if in_progress:

        timer ( (float(len(renpy.filter_text_tags(new_input_code, deny = []))) / float(used_cps)) + used_delay ) action finish_actions

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

                for output in console.console_history.values():
                    text output

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

# Backward compatibility labels for original DDLC scripts
label updateconsole(text="", history=""):
    $ console(text, history)
    return

label hideconsole:
    hide screen console_screen
    return

label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return