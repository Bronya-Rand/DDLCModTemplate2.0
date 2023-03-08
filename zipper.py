from zipfile import ZipFile, ZIP_DEFLATED
from zipper_env import PY3, EXTRAS
import sys
import os

PRIMARY_NAME = "DDLCModTemplate-"
EXCLUDE_LIST = [
    ".github",
    ".git",
    ".gitattributes",
    ".gitignore",
    "requirements.txt",
    "ZIPs",
    "Additional Mod Features",
    "zipper.py",
    "zipper_env.py",
    "__pycache__",
]


def main():
    try:
        version = sys.argv[1]
    except IndexError:
        raise Exception("Version number not provided.")

    if len(tuple(version.strip().split("."))) != 3:
        raise Exception('Invalid version number. Valid version number is "X.X.X".')

    if PY3:
        print("We building Py3 tonight.\n")
    else:
        print("We building Py2 tonight.\n")

    # Create ZIP Directory
    if not os.path.exists("./ZIPs"):
        os.makedirs("./ZIPs")

    main_zip_name = str(PRIMARY_NAME + version)
    if PY3:
        main_zip_name += "-Py3"

    print("Creating Template ZIP file.")
    with ZipFile(
        os.path.join(".", "ZIPs", main_zip_name + ".zip"),
        "w",
        ZIP_DEFLATED,
        compresslevel=5,
    ) as main_template:
        for src, dirs, files in os.walk("."):
            for f in files:
                path = os.path.join(src, f)
                validLocation = True
                for x in EXCLUDE_LIST:
                    if x in path:
                        validLocation = False
                if validLocation:
                    main_template.write(path)

    print("Finished writing the Mod Template ZIP package.\n")

    if EXTRAS:
        print("Creating Extra Template content ZIP file.")
        extras_zip_name = str(PRIMARY_NAME + version)
        if PY3:
            extras_zip_name += "-Py3Extras"
        else:
            extras_zip_name += "-Extras"

        with ZipFile(
            os.path.join(".", "ZIPs", extras_zip_name + ".zip"),
            "w",
            ZIP_DEFLATED,
            compresslevel=5,
        ) as extras_template:
            for src, dirs, files in os.walk("."):
                for f in files:
                    path = os.path.join(src, f)
                    if "Additional Mod Features" in path:
                        extras_template.write(path)

        print("Finished writing the Mod Template Extras ZIP package.\n")

    print("Finished packaging.")


if __name__ == "__main__":
    main()
