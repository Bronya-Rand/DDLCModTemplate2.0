# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the transform code for the Chibi animations in the DDLC poem game.

# The code is designed to work with Ren'Py 8 and uses the `_ren.py` approach for Python code.

## Not included in the original game, but used for IDEs to avoid multiple warnings.
from typing import Literal
import renpy  # type: ignore

"""renpy
init python:
"""


class ChibiTransform(object):
    """
    This class handles the transform animations for the Chibi characters in the poem game.
    """

    def __init__(self) -> None:
        """
        Initializes the animation of the Poem Game Chibi characters.
        """
        self.charTime: float = renpy.random.random() * 4 + 4
        self.charPos: int = 0
        self.charOffset: float = 0
        self.charZoom: float = 1

    def produce_random(self) -> float:
        """
        Produces a random time for the character animation.
        """
        return renpy.random.random() * 4 + 4

    def reset_trans(self) -> None:
        """
        Resets the character animation to its initial state.
        """
        self.charTime = self.produce_random()
        self.charPos = 0
        self.charOffset = 0
        self.charZoom = 1

    def randomPauseTime(self, trans, st, at) -> Literal[None, 0]:
        """
        Randomly pauses the character animation based on the specified time.
        """
        if st > self.charTime:
            self.charTime = self.produce_random()
            return None
        return 0

    def randomMoveTime(self, trans, st, at) -> Literal[None, 0]:
        """
        Randomly moves the character based on the specified time.
        """
        if st > 0.16:
            if self.charPos > 0:
                self.charPos = renpy.random.randint(-1, 0)
            elif self.charPos < 0:
                self.charPos = renpy.random.randint(0, 1)
            else:
                self.charPos = renpy.random.randint(-1, 1)
            if trans.xoffset * self.charPos > 5:
                self.charPos *= -1
            return None
        if self.charPos > 0:
            trans.xzoom = -1
        elif self.charPos < 0:
            trans.xzoom = 1
        trans.xoffset += 0.16 * 10 * self.charPos
        self.charOffset = trans.xoffset
        self.charZoom = trans.xzoom
        return 0


class Chibi(ChibiTransform):
    """
    This class defines a Poem Game Chibi character that is used in the poem game.
    """

    def __init__(
        self, name: str, poem_dislike_threshold: int = 29, poem_like_threshold: int = 45
    ) -> None:
        """
        Initializes the Chibi character

        :param name: The name of the character.
        :param poem_dislike_threshold: The threshold for a character to dislike a word in the poem.
        :param poem_like_threshold: The threshold for a character to like a word in the poem.

        :type name: str
        :type poem_dislike_threshold: int
        :type poem_like_threshold: int
        """
        super().__init__()
        self.name = name
        self.poem_dislike_threshold = poem_dislike_threshold
        self.poem_like_threshold = poem_like_threshold

        self.charPointTotal = 0

    def reset(self) -> None:
        """
        Resets the Chibi character's point total and animation state.
        """
        self.charPointTotal = 0
        self.reset_trans()

    def add_points(self, points: int) -> None:
        """
        Adds points to the Chibi character's total.

        :param points: The number of points to add.
        :type points: int
        """
        self.charPointTotal += points

    def calculate_appeal(self) -> Literal[-1, 0, 1]:
        """
        Calculates the appeal of the Chibi character based on their point total.

        If the total points are below the dislike threshold, the appeal is -1.
        If the total points are above the like threshold, the appeal is 1 and the character wins.
        If the total points are between the dislike and like thresholds, the appeal is 0

        :return appeal: The appeal of the character towards the player's poem.
        :rtype: int
        """
        if self.charPointTotal < self.poem_dislike_threshold:
            return -1
        elif self.charPointTotal > self.poem_like_threshold:
            return 1
        return 0

    def __call__(self) -> str:
        """
        Returns the name of the Chibi character.
        """
        return self.name


class ChibiDB(object):
    """
    This class defines a database of Chibi characters used in the poem game.
    """

    def __init__(self) -> None:
        """
        Initializes the ChibiDB instance with an empty list of characters.
        """
        self.chibis: list[Chibi] = []

    def add_chibi(self, name: str) -> None:
        """
        Adds a Chibi character to the database.

        :param name: The name of the character to add.

        :type name: str
        """
        self.chibis.append(Chibi(name))

    def get_chibi(self, name: str) -> Chibi:
        """
        Retrieves a Chibi character by name.

        :param name: The name of the character to retrieve.
        :type name: str
        :return: The Chibi character if found, otherwise None.
        :rtype: Chibi

        :raises ValueError: If the character with the given name does not exist in the database.
        """
        for chibi in self.chibis:
            if chibi.name == name:
                return chibi

        raise ValueError(f"Chibi character '{name}' not found in the database.")

    def reset(self) -> None:
        """
        Resets all Chibi characters in the database.
        """
        for chibi in self.chibis:
            chibi.reset()


# Initialize the Chibi database and characters.

chibis = ChibiDB()
chibis.add_chibi("sayori")
chibis.add_chibi("natsuki")
chibis.add_chibi("yuri")

chibi_s = chibis.get_chibi("sayori")
chibi_n = chibis.get_chibi("natsuki")
chibi_y = chibis.get_chibi("yuri")
chibi_m = (
    ChibiTransform()
)  # Monika does not participate in the poem game. She only moves around.
