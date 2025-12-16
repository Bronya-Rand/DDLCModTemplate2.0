# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Python code for DDLC's poem game.

# The code logic has been rewritten to use the Ren'Py `_ren.py` approach for Python code.

# For the Ren'Py code, see `script-poemgame.rpy` in the `poem_game` directory.

## Not included in the game, but used for IDEs to avoid multiple warnings.
from game.poem_game.py.poemgame_chibi_ren import chibis, chibi_s, chibi_n, chibi_y
from game.poem_game.py.poemwords_ren import poem_word_db, glitch_word, monika_word
from game.definitions.py.core_ren import persistent, store
import renpy  # type: ignore

poemwinner: dict[int, str] = {
    0: "sayori",
    1: "sayori",
    2: "sayori",
}

poemappeal: dict[str, dict[int, int]] = {
    "sayori": {0: 0, 1: 0, 2: 0},
    "natsuki": {0: 0, 1: 0, 2: 0},
    "yuri": {0: 0, 1: 0, 2: 0},
    "monika": {0: 0, 1: 0, 2: 0},
}

"""renpy
init python:
"""

POEM_CLICK_GLITCH_SOUND = store.audio.t4g
POEM_CLICK_SOUND = store.gui.activate_sound


class PoemGame:
    """
    This class handles the logic for the poem game in DDLC.
    """

    def __init__(self, testing: bool = False):
        """
        Initializes the poem game with default values.

        :param testing: If True, bypasses Ren'Py functions and screens for testing purposes. Unused in DDLC. Used for Github Actions to test code logic.
        :type testing: bool
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

        self.testing = testing

    def reset(self):
        """
        Resets the poem game to its initial state.
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

    def start(self):
        """
        Starts the poem game.
        This method should be called to initiate the poem game logic.
        """
        self.reset()

        # Resets the points for each character.
        chibis.reset()

        wordList = poem_word_db.get_words()
        if len(wordList) == 0:
            raise ValueError(
                "No words found in the poem word database. Please check `poemwords_ren.py` for poem word declarations."
            )

        while self.poem_progress <= 20:
            random_words: list[str] = []
            for _ in range(10):
                try:
                    word = renpy.random.choice(wordList)
                except IndexError:
                    raise IndexError(
                        "Not enough words in the poem word database. Add more words to `poemwords_ren.py`."
                    )
                random_words.append(word.__str__())
                wordList.remove(
                    word
                )  # Remove the word to avoid duplicates in the same poem game.

            # Display the poem game screen with the random words.
            if self.testing:
                if renpy.persistent.playthrough == 2:
                    act_two_words = random_words[:9]
                    act_two_words.append(glitch_word.word)
                    poemword_str = renpy.random.choice(act_two_words)
                elif renpy.persistent.playthrough == 3:
                    act_three_words = []
                    for _ in range(10):
                        act_three_words.append(monika_word.word)
                    poemword_str = renpy.random.choice(act_three_words)
                else:
                    poemword_str = renpy.random.choice(random_words)
            else:
                poemword_str = renpy.call_screen(
                    "poem_test",
                    words=random_words,
                    progress=self.poem_progress,
                    poemgame_glitch=self.poemgame_glitch,
                )

            # Checks if the word exists in the word database.
            if poemword_str in poem_word_db.get_words_str():
                selected_poemword = poem_word_db.get_word(poemword_str)
            else:
                if renpy.persistent.playthrough == 2:
                    selected_poemword = glitch_word
                else:
                    selected_poemword = monika_word

            if not self.testing:
                if not self.poemgame_glitch:
                    if selected_poemword.glitch_word:
                        self.poemgame_glitch = True
                        renpy.music.play(POEM_CLICK_GLITCH_SOUND)
                        renpy.show("white")
                        # renpy.show("y_sticker_glitch", at_list=[sticker_glitch], zorder=10)
                    elif persistent.playthrough != 3:
                        renpy.play(POEM_CLICK_SOUND)

                        # Act 1
                        if persistent.playthrough == 0:
                            if selected_poemword.sPoint >= 3:
                                renpy.show("s_sticker hop")
                            elif selected_poemword.nPoint >= 3:
                                renpy.show("n_sticker hop")
                            elif selected_poemword.yPoint >= 3:
                                renpy.show("y_sticker hop")
                        else:
                            # Act 2
                            if (
                                persistent.playthrough == 2
                                and store.chapter == 2
                                and renpy.random.randint(0, 10) == 0
                            ):
                                renpy.show(
                                    "m_sticker hop"
                                )  # 1/10 chance to see Monika hopping under the game screen.
                            elif selected_poemword.nPoint > selected_poemword.yPoint:
                                renpy.show(
                                    "n_sticker hop"
                                )  # In Act 2, Natsuki hops if she has more points than Yuri.
                            elif (
                                persistent.playthrough == 2
                                and not persistent.seen_sticker
                                and renpy.random.randint(0, 100) == 0
                            ):
                                renpy.show(
                                    "y_sticker hopg"
                                )  # "y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                                renpy.persistent.seen_sticker = True
                            elif persistent.playthrough == 2 and store.chapter == 2:
                                renpy.show(
                                    "y_sticker_cut hop"
                                )  # Yuri's cut arms sticker
                            else:
                                renpy.show("y_sticker hop")
                else:
                    r = renpy.random.randint(
                        0, 10
                    )  # 1/10 chance to hear a "baa" sound.
                    if r == 0 and not self.played_baa:
                        renpy.play("gui/sfx/baa.ogg")
                        self.played_baa = True
                    elif r <= 5:
                        renpy.play(store.gui.activate_sound_glitch)

            chibi_s.add_points(selected_poemword.sPoint)
            chibi_n.add_points(selected_poemword.nPoint)
            chibi_y.add_points(selected_poemword.yPoint)
            self.poem_progress += 1

    def finish(self):
        """
        Finishes the poem game.
        This method should be called to conclude the poem game logic.
        """
        chapter = store.chapter

        if persistent.playthrough == 0:
            # Add 5 points to whoever we side with in Act 1 - Chapter 1.
            if chapter == 1:
                chibi = chibis.get_chibi(store.ch1_choice)
                chibi.add_points(5)

        # Determine the poem winner.
        if persistent.playthrough == 0:
            # Act 1 Calculations
            poemwinner[chapter] = max(
                chibis.chibis, key=lambda c: c.charPointTotal
            ).name
        else:
            # Act 2 Calculations
            if chibi_n.charPointTotal > chibi_y.charPointTotal:
                poemwinner[chapter] = "natsuki"
            else:
                poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner.
        poemwinner_chibi = chibis.get_chibi(poemwinner[chapter])

        # Set poem appeal
        if persistent.playthrough == 0 and poemwinner_chibi.name != "sayori":
            poemappeal["sayori"][chapter] += chibi_s.calculate_appeal()
        if poemwinner_chibi.name != "natsuki":
            poemappeal["natsuki"][chapter] += chibi_n.calculate_appeal()
        if poemwinner_chibi.name != "yuri":
            poemappeal["yuri"][chapter] += chibi_y.calculate_appeal()

        # Poem winner always gets +1 appeal.
        poemappeal[poemwinner_chibi.name][chapter] += 1


poem_game = PoemGame()


def get_appeal(chibi_name: str) -> int:
    """
    Returns the appeal of the specified character.
    :param chibi_name: The name of the character.
    :type chibi_name: str
    :return: The appeal of the character.
    :rtype: int
    """
    chibi = chibis.get_chibi(chibi_name)
    appeal = 0
    for a in poemappeal[chibi.name].values():
        appeal += a
    return appeal


def get_exclusive_scene(chapter: int) -> str:
    """
    Returns the exclusive scene string based on the poem winner and their appeal.

    :param chapter: The current chapter number.
    :type chapter: int
    :return: The exclusive scene string.
    :rtype: str
    """
    winner = chibis.get_chibi(poemwinner[chapter])
    name = winner.name

    # Normally in DDLC Act II, Sayori code redirects to
    # Yuri so we do it here.
    if persistent.playthrough == 2 and winner.name == "sayori":
        name = "yuri"

    exclusive_scene = f"{name}_exclusive"
    if persistent.playthrough == 2:
        exclusive_scene += "2"
    exclusive_scene += f"_{get_appeal(name)}"
    return exclusive_scene


def get_monika_scene(chapter: int) -> str:
    """
    Returns the Monika scene string based on the chapter number.

    :param chapter: The current chapter number.
    :type chapter: int
    :return: The Monika scene string.
    :rtype: str
    """
    winner = chibis.get_chibi(poemwinner[chapter])
    monika_scene = "m"

    name = winner.name
    if persistent.playthrough == 2:
        monika_scene += "2"
        if winner.name == "sayori":
            name = "yuri"

    monika_scene += f"_{name}_{get_appeal(name)}"
    return monika_scene


def _character_poem_appeal_exists(character: str, chapter: int) -> bool:
    """
    Check if the poem appeal value exists for a given character and chapter.

    :param character: The character's name as a string.
    :type character: str
    :param chapter: The chapter number as an integer starting from 1 onwards.
    :type chapter: int

    :return: True if the poem appeal value exists, False otherwise.
    :rtype: bool
    """

    if character not in poemappeal:
        return False

    if chapter not in poemappeal[character]:
        return False

    return True


def get_character_poem_appeal(character: str, chapter: int) -> int:
    """
    Get the poem appeal value for a given character and chapter.

    :param character: The character's name as a string.
    :type character: str
    :param chapter: The chapter number as an integer starting from 1 onwards.
    :type chapter: int

    :return: The poem appeal value as an integer.
    :rtype: int

    :raises ValueError: If the character and/or chapter is not found in the poem appeal data.
    """
    character = character.lower()
    chapter = chapter - 1  # Adjust chapter to be zero-indexed.
    if not _character_poem_appeal_exists(character, chapter):
        raise ValueError(
            f"Poem appeal value for character '{character}' and/or chapter '{chapter}' not found."
        )

    return poemappeal[character][chapter]


def set_character_poem_appeal(character: str, chapter: int, value: int) -> None:
    """
    Set the poem appeal value for a given character and chapter.

    :param character: The character's name as a string.
    :type character: str
    :param chapter: The chapter number as an integer starting from 1 onwards.
    :type chapter: int
    :param value: The poem appeal value to set as an integer.
    :type value: int

    :raises ValueError: If the character and/or chapter is not found in the poem appeal data.
    """
    character = character.lower()
    chapter = chapter - 1  # Adjust chapter to be zero-indexed.

    if not _character_poem_appeal_exists(character, chapter):
        raise ValueError(
            f"Poem appeal value for character '{character}' and/or chapter '{chapter}' not found."
        )

    poemappeal[character][chapter] = value
