## script-poemgame.rpy

# This file contains the code to the DDLC poem game (now improved [finally...])
# Still commented to oblivion by Terra.

## Joke Comments
## Will cause Elckarow to rage for all this garbagio.

init python: # This whole block runs when DDLC is started (as opposed to when the poem minigame is called)
    poem_txt = "poem_game/poemwords.txt"

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch

    # This class handles Chibi Movement in a better way
    class ChibiTrans(object):
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
            if st > .16:
                if self.charPos > 0:
                    self.charPos = renpy.random.randint(-1,0)
                elif self.charPos < 0:
                    self.charPos = renpy.random.randint(0,1)
                else:
                    self.charPos = renpy.random.randint(-1,1)
                if trans.xoffset * self.charPos > 5: self.charPos *= -1
                return None
            if self.charPos > 0:
                trans.xzoom = -1
            elif self.charPos < 0:
                trans.xzoom = 1
            trans.xoffset += .16 * 10 * self.charPos
            self.charOffset = trans.xoffset
            self.charZoom = trans.xzoom
            return 0
    
    # Easy store to reset point totals
    chibis = []

    # This class supers' ChibiTrans and is used to store poem point data
    class Chibi(ChibiTrans):
        POEM_DISLIKE_THRESHOLD = 29
        POEM_LIKE_THRESHOLD = 45

        def __init__(self):
            self.charPointTotal = 0
            super().__init__()
            chibis.append(self)

        def reset(self):
            self.charPointTotal = 0
            self.reset_trans()

        def add(self, point):
            self.charPointTotal += point
        
        def calculate_appeal(self):
            if self.charPointTotal < self.POEM_DISLIKE_THRESHOLD:
                return -1
            elif self.charPointTotal > self.POEM_LIKE_THRESHOLD:
                self.win = True
                return 1
            return 0

    # Building the word list (left untouched for R8)
    full_wordlist = []
    with renpy.file(poem_txt) as wordfile:
        for line in wordfile:
            line = line.decode("utf-8").strip()

            # Ignore lines beginning with '#' and empty lines
            if line == '' or '#' in line: continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    seen_eyes_this_chapter = False

    # Declare Chibi variables for transforms and points (cept Monika), she only needs to move around.
    chibi_s = Chibi()
    chibi_n = Chibi()
    chibi_m = ChibiTrans()
    chibi_y = Chibi()

    # Start of the game (what people should use now)
    # No music ATM but to be added later.
    def poem_game_start(transition=True):
        played_baa = False
        poemgame_glitch = False

        config.allow_skipping = False
        allow_skipping = False

        # Resets points
        for c in chibis:
            c.reset()

        # Scene Set for playthroughs
        if persistent.playthrough == 3:
            poem_scene = "bg notebook-glitch"
        else:
            poem_scene = "bg notebook"
        renpy.show(poem_scene)

        # Add the Chibis
        if persistent.playthrough == 3:
            renpy.show("m_sticker", [sticker_mid])
        else:
            if persistent.playthrough == 0:
                renpy.show("s_sticker", [sticker_left])
            renpy.show("n_sticker", [sticker_mid])
            if persistent.playthrough == 2 and chapter == 2:
                renpy.show("y_sticker_cut", [sticker_right])
            else:
                renpy.show("y_sticker", [sticker_right])
            if persistent.playthrough == 2 and chapter == 2:
                renpy.show("m_sticker", [sticker_m_glitch])

        # Add fancy transformations
        if transition:
            renpy.transition(dissolve_scene_full)
        
        # Tutorial alert (RN it is instant in a new poem game session)
        if not persistent.first_poem:
            renpy.call_screen("dialog", message="It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", 
                ok_action=[SetField(persistent, "first_poem", True), Return()])

        # A way better while loop than Dan did
        progress = 1
        while progress <= 20:
            poemword = renpy.call_screen("poem_test", progress=progress, poemgame_glitch=poemgame_glitch)
            t = poemword  

            # If we are not in a bugged poem game state, do normal stuff, else do buggy stuff
            if not poemgame_glitch:
                if t.glitch: #This conditional controls what happens when the glitch word is selected.
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    # Act 1 Only cuz Sayori
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else:
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop") #1/10 chance for Monika's sticker to show.
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop") #Since there's just Yuri and Natsuki in Act 2, whoever has the higher value for the word hops.
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg") #"y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop") #Yuri's cut arms sticker.
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10) #1/10 chance to hear "baa", one time.
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)

            chibi_s.charPointTotal += t.sPoint
            chibi_n.charPointTotal += t.nPoint
            chibi_y.charPointTotal += t.yPoint
            progress += 1

        # Exits the game and calls the end function
        renpy.transition(dissolve_scene_full)
        renpy.restart_interaction()
        poem_game_finish()
    
    # End of the game
    def poem_game_finish():
        if persistent.playthrough == 0:
            # For chapter 1, add 5 points to whomever we sided with
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            # Logic for taking point totals and assigning poem appeal, scene order, etc.
            unsorted_pointlist = {"sayori": chibi_s.charPointTotal, "natsuki": chibi_n.charPointTotal, "yuri": chibi_y.charPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            # Set poemwinner to the highest scorer
            poemwinner[chapter] = pointlist[2]
        else:
            if chibi_n.charPointTotal > chibi_y.charPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        s_poemappeal[chapter] = chibi_s.calculate_appeal()
        n_poemappeal[chapter] = chibi_n.calculate_appeal()
        y_poemappeal[chapter] = chibi_y.calculate_appeal()

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    # Call the new poem eye scare label if we are in Act 2 and we yet seen eyes
    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        renpy.call("poem_eye_scare")
    config.allow_skipping = True
    allow_skipping = True

screen poem_test(progress, poemgame_glitch):
    default wordList = list(full_wordlist)
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
                            for k in range(6): # This gives random corruption effects to the "Monika" words.
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = PoemWord(glitchtext(80), 0, 0, 0, True) # This gives a chance for a random word in Act 2 to be the glitched word.
                    else:
                        python:
                            wordString = random.choice(wordList)
                            wordList.remove(wordString)

                    textbutton wordString.word:
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
                            for k in range(6): # This gives random corruption effects to the "Monika" words.
                                if random.randint(0, 4) == 0:
                                    s[k] = ' '
                                elif random.randint(0, 4) == 0:
                                    s[k] = random.choice(nonunicode)
                            wordString = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        python:
                            wordString = PoemWord(glitchtext(80), 0, 0, 0, True) # This gives a chance for a random word in Act 2 to be the glitched word.
                    else:
                        python:
                            wordString = random.choice(wordList)
                            wordList.remove(wordString)

                    textbutton wordString.word:
                        action Return(wordString)
                        text_style "poemgame_text"

## RN untested but seems to work fine-ish?
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
