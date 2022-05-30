
# __imports__.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

python early:
    # For Achievements/Gallery
    import math 

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


default -20 persistent.enable_discord = True

init -19 python:
    # For Discord RPC
    if persistent.enable_discord:
        from discord_rpc import DiscordRPC
        RPC = DiscordRPC("979471077187125248")
