
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

init -200 python:
    
    class NotRenPyEight(Exception):
        def __str__(self):
            return "This version of the mod template can only run on Ren'Py 8. Install the 'py2' version of the mod template and try again."

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "'" + self.archive + ".rpa' was not found in the game folder. Check your installation and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again."
