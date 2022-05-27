
# __imports__.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

init -1 python:
    # For Achievements/Gallery
    import math
    from collections import OrderedDict 

    # For Credits
    import datetime

    # For Glitchtext
    import random

    # For Splash
    import re
    import os

    # For BSOD
    import subprocess
    import platform

    # For Gallery
    import threading
    import renpy.display.image as imgcore
