## script-poemgame.rpy

# Commented to absurdity, blame Terra.

# Worth noting how the game gets here in the first place:
    # This script is called via "call poem" in script.rpy.
    # All of the Act 1 instances are done simply with "call poem".
    # Some of the Act 2 instances are done with "call poem (False)"
        # This is how we get the abrupt cut-in to the mini-game in Act 2.
# Images are defined after the main poem game loop.

init python: # This whole block runs when DDLC is started (as opposed to when the poem minigame is called)
    import random

    # This if/else statement checks if we are on Android and on 6.99.12.4
    # to write 'poemwords.txt' to Android/data/[mod_name]/game for reading.
    if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187): 
        poem_txt = os.environ['ANDROID_PUBLIC'] + "/game/poemwords.txt"
        try:
            if not os.access(os.environ['ANDROID_PUBLIC'] + "/game/", os.F_OK):
                os.mkdir(os.environ['ANDROID_PUBLIC'] + "/game")
            file(poem_txt)
        except: open(poem_txt, "wb").write(renpy.file("poemwords.txt").read())
    else:
        poem_txt = "poemwords.txt"

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch

    # Static variables for characters' poem appeal: Dislike, Neutral, Like
    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45

    # Building the word list
    full_wordlist = []
    with renpy.file(poem_txt) as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1
##################################################################################
#These functions define random pause lengths for each of the stickers' movements.
#renpy.random.random() returns a random floating point number between 0 and 1
#So the -Doki-Time variable for each is a random decimal ranging from 4 to 8.
#These are used in the image definitions.

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0
##############These functions define random movements for the stickers.#######
    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0

##################################################################################


label poem(transition=True):
    stop music fadeout 2.0
    if persistent.playthrough == 3: #Takes us to the glitched notebook if we're in Just Monika Mode.
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu #This allows the player to pull up the save menu during the poem minigame.
    if persistent.playthrough == 3: 
        show m_sticker at sticker_mid #Just Monika.
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left #Only show Sayori's sticker in Act 1.
        show n_sticker at sticker_mid #Natsuki's sticker
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right #Replace Yuri's sticker with the "cut arms" sticker..
        else:
            show y_sticker at sticker_right #Yuri's sticker
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch #Monika's sticker
    if transition:
        with dissolve_scene_full #Gives the dissolve transition if the minigame isn't called with False.
    if persistent.playthrough == 3:
        play music ghostmenu #Change the music in Just Monika.
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False #Not completely sure why skipping has to be explicitly disabled, but apparently it does..
    if persistent.playthrough == 0 and chapter == 0: #Shows the below dialogue the first time the minigame is played.
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    python: #Variable initialization here. Important to note, these initialize at the start of the mini-game.
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1




        # Main loop for drawing and selecting words
        while True:
            ystart = 160
##################This block of code controls the word counter.###########################################
            if persistent.playthrough == 2 and chapter == 2:
                #This makes the counter do the "111111111" thing in Act 2.
                pstring = ""
                for i in range(progress):
                    pstring += "1" #Appends "1" to pstring each loop.
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000') #This is the word counter.
##################This block of code puts the poem words on the screen.###################################
            for j in range(2): #In python, range() is not inclusive. So j loops from 0 to 1.
                if j == 0: x = 440 #These two lines build columns out of the words. The first column is at 440px and the second at 680px.
                else: x = 680
                ui.vbox() #This is outdated UI code to create a vbox. It adds things to the vbox until it hits a ui.close()
                for i in range(5):
                    if persistent.playthrough == 3: #This sets all the words to "Monika" in Just Monika.
                        s = list("Monika")
                        for k in range(6): #This gives random corruption effects to the "Monika" words.
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, True) #This gives a chance for a random word in Act 2 to be the glitched word.
                    else: #Normal circumstances
                        word = random.choice(wordlist) #Pick a random word out the wordlist
                        wordlist.remove(word) #Remove the word from the list. This prevents a word from being on the screen twice.
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close() #Closes the vbox from above
##################This block controls what happens when words are selected.############################
            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch: #This conditional controls what happens when the glitch word is selected.
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    #The below three lines are just a scene statement in python. It's exactly the same as 'scene bg white'.
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0: #Act 1. This makes the stickers hop when words are picked.
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else: #Act 2
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
            #Add the word's point values to the running total
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            progress += 1
            if progress > numWords: #This stops the minigame once we've picked all the words.
                break
##################End of main loop.##################################################################

        if persistent.playthrough == 0:
            # For chapter 1, add 5 points to whomever we sided with
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            # Logic for taking point totals and assigning poem appeal, scene order, etc.
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            # Set poemwinner to the highest scorer
            poemwinner[chapter] = pointlist[2]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
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
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
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
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
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