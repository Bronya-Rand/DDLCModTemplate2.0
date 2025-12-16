# This file contains the Python code for Monika's console in DDLC.

# The logic for the console has been changed drastically compared to the original
# game to allow for better management of console inputs and outputs and display.
# It also follows the Ren'Py approach of using the new `_ren.py` file for Python code.

# For the console display code, see `console.rpy` in the `act_two` directory.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import renpy  # type: ignore

"""renpy
init python:
"""


class Console(object):
    """
    Handles the console logic for DDLC's "terminal".
    """

    def __init__(
        self,
        console_delay: float,
        console_cps: int,
        max_log_history: int = 5,
        testing: bool = False,
    ) -> None:
        """
        Initializes the console with the given delay and characters per second (cps).

        :param console_delay: Delay after input has finished showing, before output is displayed.
        :param console_cps: Characters per second for output display.
        :param max_log_history: Maximum number of log entries to keep.
        :param testing: Bypasses Ren'Py's screen system for testing purposes. Unused in DDLC. Used for Github Actions to test code logic.

        :type console_delay: float
        :type console_cps: int
        :type max_log_history: int
        :type testing: bool
        """

        self.console_delay = console_delay
        self.console_cps = console_cps
        self.max_log_history = max_log_history

        # Initialize the console history as an empty dictionary.
        self.console_history: dict[str, str] = {}

        self.testing = testing

    def __call__(self, input_text: str, output_text: str, cps: int | None = None, delay: float | None = None) -> None:
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

    def clear_history(self) -> None:
        """
        Clears the console history.
        """
        self.console_history.clear()

    def show_screen(self) -> None:
        """
        Shows the console screen.
        """
        if not self.testing:
            renpy.show_screen("console_screen", console=self)
