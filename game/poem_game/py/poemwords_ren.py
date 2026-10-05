# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Python code of assigning words to characters in the poem game of DDLC.

# This file replaces the original `poemwords.txt` file and defines the words used in the poem game
# using a Python class structure alongside Ren'Py 8 `_ren.py` approach for Python code.

"""renpy
init python:
"""


class PoemWord:
    """
    A class to represent a word in the poem game.
    """

    def __init__(
        self,
        word: str,
        sayori_points: int,
        natsuki_points: int,
        yuri_points: int,
        glitch_word: bool = False,
    ):
        """
        Initializes a PoemWord instance.

        :param word: The word itself.
        :param sayori_points: The total points the word gives to Sayori.
        :param yuri_points: The total points the word gives to Yuri.
        :param natsuki_points: The total points the word gives to Natsuki.
        :param glitch_word: Whether the word is a glitch word or not.

        :type word: str
        :type sayori_points: int
        :type yuri_points: int
        :type natsuki_points: int
        :type glitch_word: bool

        :raises ValueError: If any of the points are negative.
        """
        self.word = word

        if sayori_points < 0 or yuri_points < 0 or natsuki_points < 0:
            if sayori_points < 0:
                raise ValueError("Sayori's preference points must be 0 or greater.")
            elif yuri_points < 0:
                raise ValueError("Yuri's preference points must be 0 or greater.")
            elif natsuki_points < 0:
                raise ValueError("Natsuki's preference points must be 0 or greater.")

        self.sPoint = sayori_points
        self.yPoint = yuri_points
        self.nPoint = natsuki_points
        self.glitch_word = glitch_word

    def __str__(self):
        """
        Returns a string representation of the PoemWord instance.

        :return str: The word itself.
        """
        return self.word


class PoemWordDB:
    """
    A class to handle the database of words used in the poem game.
    """

    def __init__(self):
        """
        Initializes the PoemWordDB instance with an empty list of words.
        """
        self.words: list[PoemWord] = []

    def add_word(
        self,
        word: str,
        sayori_points: int,
        natsuki_points: int,
        yuri_points: int,
        glitch_word: bool = False,
    ):
        """
        Adds a new word to the PoemWord database.

        :param word: The word to add.
        :param sayori_points: Sayori's preference towards the word.
        :param yuri_points: Yuri's preference towards the word.
        :param natsuki_points: Natsuki's preference towards the word.
        :param glitch_word: Whether the word is a glitch word.

        :type word: str
        :type sayori_points: int
        :type yuri_points: int
        :type natsuki_points: int
        :type glitch_word: bool

        :raises ValueError: If any of the points are negative.
        """
        new_word = PoemWord(
            word, sayori_points, natsuki_points, yuri_points, glitch_word
        )
        self.words.append(new_word)

    def get_words(self):
        """
        Returns the list of words in the PoemWord database.

        :return list[PoemWord]: List of PoemWord instances.
        """
        return self.words.copy()
    
    def get_words_str(self) -> list[str]:
        """
        Returns a list of words as strings from the PoemWord database.

        :return list[str]: List of words as strings.
        """
        return [word.word for word in self.words]

    def get_word(self, word: str) -> PoemWord:
        """
        Retrieves a word from the PoemWord database by its string representation.

        :param word: The word to retrieve.
        :type word: str
        :return: The PoemWord instance if found.
        :rtype: PoemWord

        :raises ValueError: If the word is not found in the database.
        """
        for poem_word in self.words:
            if poem_word.word == word:
                return poem_word

        raise ValueError(f"Word '{word}' not found in the poem word database.")


## Adds the words to the database.
poem_word_db = PoemWordDB()

## Glitch Word
glitch_word = PoemWord("", 0, 0, 0, glitch_word=True)  # Empty word for glitch purposes
## Monika Word
monika_word = PoemWord("", 0, 0, 0)  # Empty word for Monika purposes

## Sayori Words
poem_word_db.add_word("happiness", 3, 2, 1)
poem_word_db.add_word("sadness", 3, 2, 1)
poem_word_db.add_word("death", 3, 1, 2)
poem_word_db.add_word("tragedy", 3, 1, 2)
poem_word_db.add_word("alone", 3, 1, 2)
poem_word_db.add_word("love", 3, 2, 1)
poem_word_db.add_word("adventure", 3, 2, 1)
poem_word_db.add_word("sweet", 3, 2, 1)
poem_word_db.add_word("excitement", 3, 2, 1)
poem_word_db.add_word("fireworks", 3, 2, 1)
poem_word_db.add_word("romance", 3, 2, 1)
poem_word_db.add_word("tears", 3, 1, 2)
poem_word_db.add_word("depression", 3, 1, 2)
poem_word_db.add_word("heart", 3, 2, 1)
poem_word_db.add_word("marriage", 3, 2, 1)
poem_word_db.add_word("passion", 3, 2, 1)
poem_word_db.add_word("childhood", 3, 2, 1)
poem_word_db.add_word("fun", 3, 2, 1)
poem_word_db.add_word("color", 3, 2, 1)
poem_word_db.add_word("hope", 3, 1, 2)
poem_word_db.add_word("friends", 3, 2, 1)
poem_word_db.add_word("family", 3, 2, 1)
poem_word_db.add_word("party", 3, 2, 1)
poem_word_db.add_word("vacation", 3, 2, 1)
poem_word_db.add_word("lazy", 3, 2, 1)
poem_word_db.add_word("daydream", 3, 1, 2)
poem_word_db.add_word("pain", 3, 1, 2)
poem_word_db.add_word("holiday", 3, 2, 1)
poem_word_db.add_word("bed", 3, 2, 1)
poem_word_db.add_word("feather", 3, 2, 1)
poem_word_db.add_word("shame", 3, 1, 2)
poem_word_db.add_word("fear", 3, 1, 2)
poem_word_db.add_word("warm", 3, 2, 1)
poem_word_db.add_word("flower", 3, 2, 1)
poem_word_db.add_word("comfort", 3, 2, 1)
poem_word_db.add_word("dance", 3, 2, 1)
poem_word_db.add_word("sing", 3, 2, 1)
poem_word_db.add_word("cry", 3, 1, 2)
poem_word_db.add_word("laugh", 3, 2, 1)
poem_word_db.add_word("dark", 3, 1, 2)
poem_word_db.add_word("sunny", 3, 2, 1)
poem_word_db.add_word("raincloud", 3, 2, 1)
poem_word_db.add_word("calm", 3, 1, 2)
poem_word_db.add_word("silly", 3, 2, 1)
poem_word_db.add_word("flying", 3, 2, 1)
poem_word_db.add_word("wonderful", 3, 2, 1)
poem_word_db.add_word("unrequited", 3, 1, 2)
poem_word_db.add_word("rose", 3, 1, 2)
poem_word_db.add_word("together", 3, 2, 1)
poem_word_db.add_word("promise", 3, 2, 1)
poem_word_db.add_word("charm", 3, 2, 1)
poem_word_db.add_word("beauty", 3, 2, 1)
poem_word_db.add_word("cheer", 3, 2, 1)
poem_word_db.add_word("smile", 3, 2, 1)
poem_word_db.add_word("broken", 3, 1, 2)
poem_word_db.add_word("precious", 3, 2, 1)
poem_word_db.add_word("prayer", 3, 1, 2)
poem_word_db.add_word("clumsy", 3, 2, 1)
poem_word_db.add_word("forgive", 3, 1, 2)
poem_word_db.add_word("nature", 3, 2, 1)
poem_word_db.add_word("ocean", 3, 2, 1)
poem_word_db.add_word("dazzle", 3, 2, 1)
poem_word_db.add_word("special", 3, 2, 1)
poem_word_db.add_word("music", 3, 2, 1)
poem_word_db.add_word("lucky", 3, 2, 1)
poem_word_db.add_word("misfortune", 3, 1, 2)
poem_word_db.add_word("loud", 3, 2, 1)
poem_word_db.add_word("peaceful", 3, 1, 2)
poem_word_db.add_word("joy", 3, 1, 2)
poem_word_db.add_word("sunset", 3, 2, 1)
poem_word_db.add_word("fireflies", 3, 2, 1)
poem_word_db.add_word("rainbow", 3, 2, 1)
poem_word_db.add_word("hurt", 3, 1, 2)
poem_word_db.add_word("play", 3, 2, 1)
poem_word_db.add_word("sparkle", 3, 2, 1)
poem_word_db.add_word("scars", 3, 1, 2)
poem_word_db.add_word("empty", 3, 1, 2)
poem_word_db.add_word("amazing", 3, 2, 1)
poem_word_db.add_word("grief", 3, 1, 2)
poem_word_db.add_word("embrace", 3, 1, 2)
poem_word_db.add_word("extraordinary", 3, 2, 1)
poem_word_db.add_word("awesome", 3, 2, 1)
poem_word_db.add_word("defeat", 3, 1, 2)
poem_word_db.add_word("hopeless", 3, 1, 2)
poem_word_db.add_word("misery", 3, 1, 2)
poem_word_db.add_word("treasure", 3, 2, 1)
poem_word_db.add_word("bliss", 3, 2, 1)
poem_word_db.add_word("memories", 3, 2, 1)

## Natsuki Words
poem_word_db.add_word("cute", 2, 3, 1)
poem_word_db.add_word("fluffy", 2, 3, 1)
poem_word_db.add_word("pure", 1, 3, 2)
poem_word_db.add_word("candy", 2, 3, 1)
poem_word_db.add_word("shopping", 2, 3, 1)
poem_word_db.add_word("puppy", 2, 3, 1)
poem_word_db.add_word("kitty", 2, 3, 1)
poem_word_db.add_word("clouds", 2, 3, 1)
poem_word_db.add_word("lipstick", 1, 3, 2)
poem_word_db.add_word("parfait", 2, 3, 1)
poem_word_db.add_word("strawberry", 2, 3, 1)
poem_word_db.add_word("pink", 2, 3, 1)
poem_word_db.add_word("chocolate", 2, 3, 1)
poem_word_db.add_word("heartbeat", 1, 3, 2)
poem_word_db.add_word("kiss", 1, 3, 2)
poem_word_db.add_word("melody", 2, 3, 1)
poem_word_db.add_word("ribbon", 2, 3, 1)
poem_word_db.add_word("jumpy", 2, 3, 1)
poem_word_db.add_word("doki-doki", 2, 3, 1)
poem_word_db.add_word("kawaii", 2, 3, 1)
poem_word_db.add_word("skirt", 2, 3, 1)
poem_word_db.add_word("cheeks", 2, 3, 1)
poem_word_db.add_word("email", 2, 3, 1)
poem_word_db.add_word("sticky", 2, 3, 1)
poem_word_db.add_word("bouncy", 2, 3, 1)
poem_word_db.add_word("shiny", 2, 3, 1)
poem_word_db.add_word("nibble", 2, 3, 1)
poem_word_db.add_word("fantasy", 1, 3, 2)
poem_word_db.add_word("sugar", 2, 3, 1)
poem_word_db.add_word("giggle", 2, 3, 1)
poem_word_db.add_word("marshmallow", 2, 3, 1)
poem_word_db.add_word("hop", 2, 3, 1)
poem_word_db.add_word("skipping", 2, 3, 1)
poem_word_db.add_word("peace", 2, 3, 1)
poem_word_db.add_word("spinning", 2, 3, 1)
poem_word_db.add_word("twirl", 2, 3, 1)
poem_word_db.add_word("lollipop", 2, 3, 1)
poem_word_db.add_word("poof", 2, 3, 1)
poem_word_db.add_word("bubbles", 2, 3, 1)
poem_word_db.add_word("whisper", 2, 3, 1)
poem_word_db.add_word("summer", 2, 3, 1)
poem_word_db.add_word("waterfall", 1, 3, 2)
poem_word_db.add_word("swimsuit", 2, 3, 1)
poem_word_db.add_word("vanilla", 2, 3, 1)
poem_word_db.add_word("headphones", 2, 3, 1)
poem_word_db.add_word("games", 2, 3, 1)
poem_word_db.add_word("socks", 2, 3, 1)
poem_word_db.add_word("hair", 2, 3, 1)
poem_word_db.add_word("playground", 2, 3, 1)
poem_word_db.add_word("nightgown", 1, 3, 2)
poem_word_db.add_word("blanket", 1, 3, 2)
poem_word_db.add_word("milk", 2, 3, 1)
poem_word_db.add_word("pout", 2, 3, 1)
poem_word_db.add_word("anger", 2, 3, 1)
poem_word_db.add_word("papa", 2, 3, 1)
poem_word_db.add_word("valentine", 2, 3, 1)
poem_word_db.add_word("mouse", 1, 3, 2)
poem_word_db.add_word("whistle", 2, 3, 1)
poem_word_db.add_word("boop", 2, 3, 1)
poem_word_db.add_word("bunny", 2, 3, 1)
poem_word_db.add_word("anime", 2, 3, 1)
poem_word_db.add_word("jump", 2, 3, 1)

## Yuri Words
poem_word_db.add_word("determination", 1, 1, 3)
poem_word_db.add_word("suicide", 2, 1, 3)
poem_word_db.add_word("imagination", 2, 1, 3)
poem_word_db.add_word("secretive", 2, 1, 3)
poem_word_db.add_word("vitality", 1, 1, 3)
poem_word_db.add_word("existence", 2, 1, 3)
poem_word_db.add_word("effulgent", 1, 1, 3)
poem_word_db.add_word("crimson", 1, 1, 3)
poem_word_db.add_word("whirlwind", 1, 1, 3)
poem_word_db.add_word("afterimage", 1, 1, 3)
poem_word_db.add_word("vertigo", 1, 1, 3)
poem_word_db.add_word("disoriented", 1, 1, 3)
poem_word_db.add_word("essence", 2, 1, 3)
poem_word_db.add_word("ambient", 2, 1, 3)
poem_word_db.add_word("starscape", 2, 1, 3)
poem_word_db.add_word("disarray", 1, 1, 3)
poem_word_db.add_word("contamination", 1, 1, 3)
poem_word_db.add_word("intellectual", 1, 1, 3)
poem_word_db.add_word("analysis", 1, 1, 3)
poem_word_db.add_word("entropy", 1, 1, 3)
poem_word_db.add_word("vivacious", 1, 1, 3)
poem_word_db.add_word("uncanny", 2, 1, 3)
poem_word_db.add_word("incongruent", 1, 1, 3)
poem_word_db.add_word("wrath", 2, 1, 3)
poem_word_db.add_word("heavensent", 2, 1, 3)
poem_word_db.add_word("massacre", 2, 1, 3)
poem_word_db.add_word("philosophy", 1, 1, 3)
poem_word_db.add_word("fickle", 1, 1, 3)
poem_word_db.add_word("tenacious", 1, 1, 3)
poem_word_db.add_word("aura", 2, 1, 3)
poem_word_db.add_word("unstable", 1, 1, 3)
poem_word_db.add_word("inferno", 2, 1, 3)
poem_word_db.add_word("incapable", 2, 1, 3)
poem_word_db.add_word("destiny", 2, 1, 3)
poem_word_db.add_word("infallible", 1, 1, 3)
poem_word_db.add_word("agonizing", 2, 1, 3)
poem_word_db.add_word("variance", 1, 1, 3)
poem_word_db.add_word("uncontrollable", 2, 1, 3)
poem_word_db.add_word("extreme", 1, 1, 3)
poem_word_db.add_word("flee", 2, 1, 3)
poem_word_db.add_word("dream", 2, 2, 3)
poem_word_db.add_word("disaster", 2, 1, 3)
poem_word_db.add_word("vivid", 2, 1, 3)
poem_word_db.add_word("vibrant", 1, 2, 3)
poem_word_db.add_word("question", 1, 2, 3)
poem_word_db.add_word("fester", 2, 1, 3)
poem_word_db.add_word("judgment", 1, 1, 3)
poem_word_db.add_word("cage", 1, 2, 3)
poem_word_db.add_word("explode", 1, 2, 3)
poem_word_db.add_word("pleasure", 1, 2, 3)
poem_word_db.add_word("lust", 1, 2, 3)
poem_word_db.add_word("sensation", 1, 2, 3)
poem_word_db.add_word("climax", 1, 2, 3)
poem_word_db.add_word("electricity", 1, 2, 3)
poem_word_db.add_word("disown", 1, 1, 3)
poem_word_db.add_word("despise", 2, 1, 3)
poem_word_db.add_word("infinite", 2, 1, 3)
poem_word_db.add_word("eternity", 2, 1, 3)
poem_word_db.add_word("time", 2, 1, 3)
poem_word_db.add_word("universe", 2, 1, 3)
poem_word_db.add_word("unending", 2, 1, 3)
poem_word_db.add_word("raindrops", 2, 1, 3)
poem_word_db.add_word("covet", 1, 1, 3)
poem_word_db.add_word("unrestrained", 1, 1, 3)
poem_word_db.add_word("landscape", 2, 1, 3)
poem_word_db.add_word("portrait", 2, 1, 3)
poem_word_db.add_word("journey", 2, 1, 3)
poem_word_db.add_word("meager", 1, 1, 3)
poem_word_db.add_word("anxiety", 2, 1, 3)
poem_word_db.add_word("frightening", 2, 1, 3)
poem_word_db.add_word("horror", 2, 1, 3)
poem_word_db.add_word("melancholy", 2, 1, 3)
poem_word_db.add_word("insight", 2, 1, 3)
poem_word_db.add_word("atone", 2, 1, 3)
poem_word_db.add_word("breathe", 1, 2, 3)
poem_word_db.add_word("captive", 2, 1, 3)
poem_word_db.add_word("desire", 1, 2, 3)
poem_word_db.add_word("graveyard", 2, 1, 3)
