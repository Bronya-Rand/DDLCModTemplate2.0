## Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# 0imports.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

python early:
    # For Effects
    import math

    # For the Credits Screen
    import datetime

    # For Glitchtext
    import random
    import unicodedata

    # For Splash
    import re
    import os

    # For BSOD
    import subprocess
    import platform

init -1 python:
    # Achievements/Gallery
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ImportError:
        pass
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ImportError:
        pass