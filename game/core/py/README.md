# Contents of the `core/py` folder

## Folders
- **\_\_pycache\_\_**: Contains the compiled Python files for the code used in the core features of DDLC and the mod template. This should normally not appear in your mod nor in packaged mod templates, but if it exists, ignore it.

## Files
- **README.md**: This file, which provides an overview of the contents of the `py` folder.
- **\_\_init\_\_.py**: An empty file used for testing purposes.
- **[0cleanup_ren.py](./0cleanup_ren.py)**: Contains code that removes deprecated or migrated features from either DDLC or the mod template.
- **[0imports_ren.py](./0imports_ren.py)**: Contains the imports for the core features of DDLC and the mod template to import at bootstrap.
- **[renpy_patches_ren.py](./renpy_patches_ren.py)**: Contains several patches in order for DDLC to run properly on Ren'Py 8.
- **[template_checks_ren.py](./template_checks_ren.py)**: Contains custom exceptions and checks for the Mod Template to look for before DDLc boots up. This file combines the contents of *exceptions.rpy* and *lockdown_check.rpy* in older versions of the Mod Template.