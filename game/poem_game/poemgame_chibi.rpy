## Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# poemgame_chibi.rpy
# This file contains the transform code for the Chibi animations in the DDLC poem game.

init -2 python:

    class ChibiTransform(object):
        """
        This class handles the transform animations for the Chibi characters in the poem game.
        """

        def __init__(self):
            self.charTime = renpy.random.random() * 4 + 4
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def produce_random(self):
            return renpy.random.random() * 4 + 4

        def reset_trans(self):
            self.charTime = self.produce_random()
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def randomPauseTime(self, trans, st, at):
            if st > self.charTime:
                self.charTime = self.produce_random()
                return None
            return 0

        def randomMoveTime(self, trans, st, at):
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
            self, name, poem_dislike_threshold=29, poem_like_threshold=45
        ):
            super(Chibi, self).__init__()
            self.name = name
            self.poem_dislike_threshold = poem_dislike_threshold
            self.poem_like_threshold = poem_like_threshold

            self.charPointTotal = 0

        def reset(self):
            self.charPointTotal = 0
            self.reset_trans()

        def add_points(self, points):
            self.charPointTotal += points

        def calculate_appeal(self):
            if self.charPointTotal < self.poem_dislike_threshold:
                return -1
            elif self.charPointTotal > self.poem_like_threshold:
                return 1
            return 0

        def __call__(self):
            return self.name

        @property
        def appeal(self):
            """
            Backward-compatible property accessing the character's poem appeal.
            """
            return get_appeal(self.name)


    class ChibiDB(object):
        """
        This class defines a database of Chibi characters used in the poem game.
        """

        def __init__(self):
            self.chibis = []

        def add_chibi(self, name):
            self.chibis.append(Chibi(name))

        def get_chibi(self, name):
            for chibi in self.chibis:
                if chibi.name == name:
                    return chibi

            raise ValueError("Chibi character '{0}' not found in the database.".format(name))

        def reset(self):
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
    chibi_m = ChibiTransform()
