
# __imports__.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

default persistent.enable_discord = True

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

    # For Discord RPC
    if enable_discord:
        from discord_rpc import DiscordRPC
        RPC = DiscordRPC("979471077187125248")