# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains code that manages parts of the poem response minigame.

## Not included in the game, but used for IDEs to avoid multiple warnings.
readpoem: dict[str, bool] = {
    "sayori": False,
    "natsuki": False,
    "yuri": False,
    "monika": False,
}

"""renpy
init python:
"""


def get_read_poem_status(character: str) -> bool:
    """
    Get the read poem status for a given character.

    :param character: The character's name as a string.
    :type character: str
    :return: The read poem status as a boolean.
    :rtype: bool

    :raises ValueError: If the character is not found in the read poem data.
    """
    character = character.lower()
    if character not in readpoem:
        raise ValueError(f"Read poem status for character '{character}' not found.")

    return readpoem[character]


def set_read_poem_status(character: str) -> None:
    """
    Set the read poem status for a given character to True.

    :param character: The character's name as a string.
    :type character: str

    :raises ValueError: If the character is not found in the read poem data.
    """
    character = character.lower()
    if character not in readpoem:
        raise ValueError(f"Read poem status for character '{character}' not found.")

    readpoem[character] = True


def reset_read_poem_status() -> None:
    """
    Resets the read poem status for all characters to False.
    """
    for character in readpoem.keys():
        readpoem[character] = False
