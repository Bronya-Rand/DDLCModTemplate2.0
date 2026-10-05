## Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# script-poemgame.rpy
# This file contains the logic and Ren'Py code for DDLC's poem minigame.

init -1 python:

    poemwinner = {
        0: "sayori",
        1: "sayori",
        2: "sayori",
    }

    poemappeal = {
        "sayori": {0: 0, 1: 0, 2: 0},
        "natsuki": {0: 0, 1: 0, 2: 0},
        "yuri": {0: 0, 1: 0, 2: 0},
        "monika": {0: 0, 1: 0, 2: 0},
    }


    class PoemGame(object):
        """
        This class handles the logic for the poem game in DDLC.
        """

        def __init__(self, testing=False):
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
            """
            self.reset()

            # Resets the points for each character.
            chibis.reset()

            wordList = poem_word_db.get_words()
            if len(wordList) == 0:
                raise ValueError(
                    "No words found in the poem word database. Please check `poemwords.rpy` for poem word declarations."
                )

            while self.poem_progress <= 20:
                random_words = []
                for _ in range(10):
                    try:
                        word = renpy.random.choice(wordList)
                    except IndexError:
                        raise IndexError(
                            "Not enough words in the poem word database. Add more words to `poemwords.rpy`."
                        )
                    random_words.append(str(word))
                    wordList.remove(word)

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
                            renpy.music.play(audio.t4g)
                            renpy.show("white")
                        elif persistent.playthrough != 3:
                            renpy.play(gui.activate_sound)

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
                                    renpy.show("m_sticker hop")
                                elif selected_poemword.nPoint > selected_poemword.yPoint:
                                    renpy.show("n_sticker hop")
                                elif (
                                    persistent.playthrough == 2
                                    and not persistent.seen_sticker
                                    and renpy.random.randint(0, 100) == 0
                                ):
                                    renpy.show("y_sticker hopg")
                                    renpy.persistent.seen_sticker = True
                                elif persistent.playthrough == 2 and store.chapter == 2:
                                    renpy.show("y_sticker_cut hop")
                                else:
                                    renpy.show("y_sticker hop")
                    else:
                        r = renpy.random.randint(0, 10)
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

            # Sync with legacy variables for backward compatibility
            if hasattr(store, "s_poemappeal") and isinstance(store.s_poemappeal, list) and chapter < len(store.s_poemappeal):
                store.s_poemappeal[chapter] = poemappeal["sayori"][chapter]
            if hasattr(store, "n_poemappeal") and isinstance(store.n_poemappeal, list) and chapter < len(store.n_poemappeal):
                store.n_poemappeal[chapter] = poemappeal["natsuki"][chapter]
            if hasattr(store, "y_poemappeal") and isinstance(store.y_poemappeal, list) and chapter < len(store.y_poemappeal):
                store.y_poemappeal[chapter] = poemappeal["yuri"][chapter]


    poem_game = PoemGame()


    def get_appeal(chibi_name):
        """
        Returns the appeal of the specified character.
        """
        chibi = chibis.get_chibi(chibi_name)
        appeal = 0
        for a in poemappeal[chibi.name].values():
            appeal += a
        return appeal


    def get_exclusive_scene(chapter):
        """
        Returns the exclusive scene string based on the poem winner and their appeal.
        """
        winner = chibis.get_chibi(poemwinner[chapter])
        name = winner.name

        # Normally in DDLC Act II, Sayori code redirects to Yuri
        if persistent.playthrough == 2 and winner.name == "sayori":
            name = "yuri"

        exclusive_scene = "{0}_exclusive".format(name)
        if persistent.playthrough == 2:
            exclusive_scene += "2"
        exclusive_scene += "_{0}".format(get_appeal(name))
        return exclusive_scene


    def get_monika_scene(chapter):
        """
        Returns the Monika scene string based on the chapter number.
        """
        winner = chibis.get_chibi(poemwinner[chapter])
        monika_scene = "m"

        name = winner.name
        if persistent.playthrough == 2:
            monika_scene += "2"
            if winner.name == "sayori":
                name = "yuri"

        monika_scene += "_{0}_{1}".format(name, get_appeal(name))
        return monika_scene


    def _character_poem_appeal_exists(character, chapter):
        if character not in poemappeal:
            return False
        if chapter not in poemappeal[character]:
            return False
        return True


    def get_character_poem_appeal(character, chapter):
        """
        Get the poem appeal value for a given character and chapter (1-indexed).
        """
        character = character.lower()
        chapter = chapter - 1
        if not _character_poem_appeal_exists(character, chapter):
            raise ValueError(
                "Poem appeal value for character '{0}' and/or chapter '{1}' not found.".format(character, chapter)
            )
        return poemappeal[character][chapter]


    def set_character_poem_appeal(character, chapter, value):
        """
        Set the poem appeal value for a given character and chapter (1-indexed).
        """
        character = character.lower()
        chapter = chapter - 1
        if not _character_poem_appeal_exists(character, chapter):
            raise ValueError(
                "Poem appeal value for character '{0}' and/or chapter '{1}' not found.".format(character, chapter)
            )
        poemappeal[character][chapter] = value


screen poem_test(words, progress, poemgame_glitch):
    default numWords = 20
    
    if progress is not None:
        fixed:
            xpos 810
            
            python:
                if persistent.playthrough == 2 and chapter == 2:
                    pstring = ""
                    for i in range(progress):
                        pstring += "1"
                else:
                    pstring = str(progress)

            text pstring + "/" + str(numWords):
                style "poemgame_text"
                ypos 80

        # Two fixed areas for the two sections of poemgame we have
        fixed:
            xpos 440
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list("Monika")
                            for k in range(6):
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80)
                    else:
                        python:
                            wordString = words[i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

        fixed:
            xpos 680
            ypos 160

            viewport:
                has vbox
                spacing 56

                for i in range(5):
                    if persistent.playthrough == 3:
                        python:
                            s = list("Monika")
                            for k in range(6):
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = "".join(s)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = glitchtext(80)
                    else:
                        python:
                            wordString = words[5+i]

                    textbutton wordString:
                        action Return(wordString)
                        text_style "poemgame_text"

label poem(transition=True):
    stop music fadeout 2.0

    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        scene bg notebook
    
    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left
        show n_sticker at sticker_mid
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right
        else:
            show y_sticker at sticker_right
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch
        
    if transition:
        with dissolve_scene_full

    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4

    $ config.allow_skipping = False
    $ allow_skipping = False

    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    
    $ poem_game.start()
    $ poem_game.finish()

    if persistent.playthrough == 2 and not persistent.seen_eyes and renpy.random.randint(0,5) == 0:
        call poem_eye_scare

    $ config.allow_skipping = True
    $ allow_skipping = True

    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

label poem_eye_scare:
    $ seen_eyes_this_chapter = True
    $ quick_menu = False
    play sound "sfx/eyes.ogg"
    $ persistent.seen_eyes = True
    stop music
    scene black with None
    show bg eyes_move
    pause 1.2
    hide bg eyes_move
    show bg eyes
    pause 0.5
    hide bg eyes
    show bg eyes_move
    pause 1.25
    hide bg eyes with None
    $ quick_menu = True
    return

############ Image definitions start here. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
        
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    block:
        function chibi_s.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_s.randomMoveTime
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    block:
        function chibi_n.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_n.randomMoveTime
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    block:
        function chibi_m.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_m.randomMoveTime
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom zoom 3.0
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
