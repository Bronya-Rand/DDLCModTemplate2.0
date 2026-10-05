## exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors.
# DO NOT MODIFY THIS FILE!

python early:

    class NotPythonTwoCompatible(Exception):
        def __str__(self):
            return (
                "This version of the mod template is designed for Ren'Py 6.99.12.4 and Ren'Py 7 (Python 2).\n"
                "To develop a DDLC mod on Ren'Py 8, please download the Python 3 version of the DDLC Mod Template."
            )

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return (
                "'"
                + self.archive
                + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."
            )

    class IllegalModLocation(Exception):
        def __str__(self):
            return (
                "DDLC mods/mod projects cannot be run from this folder as it is a OneDrive or another cloud folder.\n"
                "Move your mod/mod project to another location and try again."
            )

    if renpy.version_tuple >= (8, 0, 0, 0):
        raise NotPythonTwoCompatible