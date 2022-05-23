
# exceptions.rpy
# This file contains the exceptions for certain DDLC/Template errors
# DO NOT MODIFY THIS FILE!

init -200 python:
    
    class NotRenPyEight(Exception):
        def __str__(self):
            return "This version of the mod template can only run on Ren'Py 8. Install the 'py2' version of the mod template and try again."

    class DDLCRPAsMissing(Exception):
        pass

    class IllegalModLocation(Exception):
        pass
