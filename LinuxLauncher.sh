#!/bin/sh

## Copyright 2019-2024 Azariel Del Carmen (bronya_rand). All rights reserved.
## Based off the original renpy.sh file with Ren'Py 6 removal patch applied.

# The directory containing this shell script - an absolute path.
ROOT=$(dirname "$SCRIPT")
ROOT=$(cd "$ROOT"; pwd)

if [ -z "$RENPY_PLATFORM" ] ; then
    RENPY_PLATFORM="$(uname -s)-$(uname -m)"

    case "$RENPY_PLATFORM" in
        Darwin-*|mac-*)
            RENPY_PLATFORM="mac-x86_64"
            ;;
        *-x86_64|amd64)
            RENPY_PLATFORM="linux-x86_64"
            ;;
        *-i*86)
            RENPY_PLATFORM="linux-i686"
            ;;
        Linux-*)
            RENPY_PLATFORM="linux-$(uname -m)"
            ;;
        *)
            ;;
    esac
fi

LIB="$ROOT/lib/$RENPY_PLATFORM"

# Removes the lib folder left from Ren'Py 6
if [ -d "$LIB/lib" ]; then
    echo "Removing Ren'Py 6 files due to 'future.standard_library' error."
    rm -r "$LIB/lib"
fi

SHFILE="$(ls -I "DDLC.sh" -I "LinuxLauncher.sh" "$ROOT" | grep "\.sh")"

if test -z "$SHFILE"; then
    echo "Error: Unable to find a mod shell script file. Defaulting to 'DDLC.sh'."
    SHFILE="DDLC.sh"
fi

# The name of this shell script without the .sh on the end.
SHNAME=$(basename "$SHFILE" .sh)

echo "Preparing to launch $SHNAME..."
exec "$ROOT/$SHFILE"