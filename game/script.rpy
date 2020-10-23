# Script.rpy
# This is the main script that DDLC/Ren'Py calls upon to start
# your mod's story! 

# Imports stuff needed for the android build of DDLC
init python:
    if renpy.android:
        import os

label start:

    # Configures your mod to use a ID to prevent users from cheating.
    # Leave this as default and only change the value 'persistent.anticheat' has
    # in definitions.rpy if you want to change it
    $ anticheat = persistent.anticheat

    # Controls what chapter the game starts for the poem game.
    $ chapter = 0

    # This makes sure if the user quits during pause, 
    # it is set to false after restarting the game. Precaution.
    $ _dismiss_pause = config.developer

    # Names of the Characters
    # To add a character -> $ mi_name = "Mike". Don't forget to
    # add them also in definitions.rpy!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # Controls whether we have a menu in the textbox or not.
    $ quick_menu = True

    # Controls whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited' than 'style.normal'
    $ style.say_dialogue = style.normal

    # Controls whether Sayori is dead. Leave this alone unless needed.
    $ in_sayori_kill = None
    
    # Controls whether we allow skipping dialogue.
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Start of the script
    # 'persistent.playthrough' controls the playthrough number the player is on
    if persistent.playthrough == 0:
        # '$ chapter = 0' controls the chapter number the game is on for the poem game.
        # 'call tutorial_selection' controls what label to call from in your script files
        # Make sure to change this when coding your mod, else your player will face a script error

        $ chapter = 0
        call ch0_main

        # 'call poem' calls the poemgame
        call poem

        # Day 1
        $ chapter = 1
        call ch1_main
        # 'call poemresponse_start' calls the poem response game
        call poemresponse_start
        call ch1_end

        call poem

        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end

        call poem

        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        $ chapter = 4
        call ch4_main

        ## try: renpy.file(config.basedir + "/hxppy thxughts.png") checks if there is a file
        # where DDLC.exe (.app/.sh for MacOS/Linux) called 'hxppy thxughts.png'
        ## except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        # writes 'hxppy thxughts.png' to the main directory if not found.
        python:
            if renpy.android:
                # for android, the try and excepts must be formatted like so with this but replace
                # hxppy thxughts.png with the file you want to write.
                ## try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"))
                ## except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
                try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"))
                except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/hxppy thxughts.png"), "wb").write(renpy.file("hxppy thxughts.png").read())
            else:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        $ chapter = 5
        call ch5_main

        #ends the game (not credits)
        call endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        # jump calls upon a label. like call but won't ever return
        # back here.
        jump playthrough2


    elif persistent.playthrough == 2:
        $ chapter = 0
        call ch20_main

        label playthrough2:

            call poem
            python:
                try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/CAN YOU HEAR ME.txt"))
                except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/CAN YOU HEAR ME.txt"), "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end

            call poem(False)
            python:
                try: file(os.path.realpath("/sdcard/Android/data/"+package_name+"/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt"))
                except: open(os.path.realpath("/sdcard/Android/data/"+package_name+"/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt"), "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            # 'call poem(False)' calls the poemgame but with no fancy transitions
            call poem(False)

            $ chapter = 3
            call ch23_main
            # if y_appeal >= 3: checks if our appeal with Yuri is > or = to 3
            # if yes then it calls a special poem response game, else normal.
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start
            # this is old Dan leftover code when DDLC was a demo.
            # if you wanted to you can re-use it as a demo showcase of your own mod.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main
        jump credits

# the end label of the game. Not the credits.    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

