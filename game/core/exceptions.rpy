
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

python early:

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "'" + self.archive + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from this folder as it is a OneDrive or another cloud folder.\nMove your mod/mod project to another location and try again."