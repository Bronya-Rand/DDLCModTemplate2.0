# Renpypatches.rpy

# This file handles any patches needed for DDLC to work under
# certain Ren'Py versions. These patches are mainly reserved to patch
# specific Python code in the Ren'Py Engine. DO NOT MESS WITH THIS FILE.

init -100 python:
    if renpy.version_tuple >= (7, 4, 6):
        import transformpatch
        # Changes the path ATLTransform would normally go to the patched class.
        renpy.display.motion.ATLTransform = transformpatch.ATLTransform