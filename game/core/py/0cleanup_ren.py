# This file contains code that removes deprecated or migrated features from either DDLC or the mod template.

import os
import renpy  # type: ignore

"""renpy
python early:
"""

RENPY_PYTHON_PACKAGES = "python-packages"


def cleanup_deprecated_features():
    """
    Cleans up deprecated or migrated features by disabling them.
    """

    # Remove old singleton implementation if it exists
    python_packages_dir = os.path.join(renpy.config.gamedir, RENPY_PYTHON_PACKAGES)
    if os.path.exists(os.path.join(python_packages_dir, "singleton.py")):
        try:
            os.remove(os.path.join(python_packages_dir, "singleton.py"))
        except OSError:
            pass


cleanup_deprecated_features()
