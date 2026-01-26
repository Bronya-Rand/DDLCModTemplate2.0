# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains utility functions for screen adjustments in the Mod Template (some used for DDLC Mobile features).

"""renpy
init python:
"""

TABS = 4  # Default number of tabs in preferences.

# (230 - 300) / (4 - 3) from DDLC Mobile to Mod Template defaults
# If adding more tabs, adjust accordingly.
WIDTH_LINEAR_SLOPE = -70


def get_pref_tab_button_width():
    """
    Docstring for get_button_width

    :param tabs: Description
    :type tabs: int
    """
    # y - 300 = WIDTH_LINEAR_SLOPE(x - 3) using DDLC Mobile original
    # width of 300 at 3 tabs (or y = WIDTH_LINEAR_SLOPE * x + 510)
    width = WIDTH_LINEAR_SLOPE * TABS + 510

    # Ensure the width is within reasonable bounds
    min_width = 150
    return max(width, min_width)
