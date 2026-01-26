# This file contains the Python code for the Content Warning system from the mobile version of DDLC.

# The logic for displaying the content warning is handled here,
# while the display code is in `content_warnings.rpy` in the `wip` directory.

## These import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
from game.definitions.py.core_ren import pause, persistent, store
import renpy  # type: ignore

persistent.enable_content_warnings = False

"""renpy
init python:
"""


def show_content_warning(warning_text: str):
    """
    Shows a content warning popup with the given warning text.

    :param warning_text: The content warning text to display.
    :type warning_text: str
    """
    if not persistent.enable_content_warnings:
        return

    store.cw_prev_volume = renpy.store.preferences.get_mixer("music")
    if store.cw_prev_volume > 0:
        renpy.audio.music.set_volume(store.cw_prev_volume / 2)

    renpy.show_screen("content_warning_popup", warning_text=warning_text)
    store.mc.add_history(None, "", (_("Content Warning: ") + warning_text))

    pause(3.0)


def cw_restore_volume():
    """
    Restores the volume levels after the content warning screen is dismissed.
    """
    renpy.music.set_volume(store.cw_prev_volume, 2)

def show_poem_content_warning(special_poem: int):
    """
    Shows a content warning for specific special poems.
    Displays a content warning for certain special poems based on their number
    or None if no warning is needed.

    :param special_poem: The special poem number.
    :type special_poem: int
    """
    poem_warnings = {
        1: "Crude sketch of a stick figure in the likeness of a character hanging from a noose.",
        4: "First-person written account glorifying self-harm via cutting, and considering potential suicide. Visual depiction of blood smeared on paper.",
        9: "First-person written references to implied neglect and potential parental abuse, including withholding food.",
        10: "Brief, first person written account of implied mental health struggles and potential future self harm.",
        11: "First-person written account of implied drowning and accompanying panic, physical struggle, and claustrophobia."
    }

    if special_poem in poem_warnings.keys():
        show_content_warning(poem_warnings[special_poem])
