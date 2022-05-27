
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

init -200 python:

    class DDLCRPAsMissing(Exception):
        def __str__(self, archive):
            return "'" + archive + ".rpa' found in the game folder. Check your installation and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again."