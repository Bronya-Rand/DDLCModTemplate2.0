# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This is where the splashscreen, disclaimer and menu code reside in.

# This image text shows the splash message when the game loads.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Main Menu Images
# These image transforms store the images and positions of the game logo,
# the menu character sprites and main menu/pause menu screen images.

# This image shows the DDLC logo in the normal DDLC position.
image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    # im.Composite((512, 512), (0, 0), recolorize("mod_assets/logo_bg.png"), (0, 0), "mod_assets/logo_fg.png")
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# This image shows the main menu polka-dot image.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_move

# This image shows the pause menu polka-dot image.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    # recolorize("gui/menu_bg.png", "#ffdbf0", "#fff", 1)
    menu_bg_loop

# This image transform shows the white fading effect in the main menu.
image menu_fade:
    "white"
    menu_fadeout

# These images show each respective characters' menu sprite and positions/animations.
image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# These images are the same as above but ghost themed for the secret ghost menu
# that appears rarely in-game .
image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# This image sprite shows a glitched Sayori menu sprite after Act 1 finishes.
image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

# This image shows the main menu screen in the main/pause menu.
image menu_nav:
    "gui/overlay/main_menu.png"
    #recolorize("gui/overlay/main_menu.png", "#ffbde1")
    menu_nav_move

## Main Menu Effects
# These transforms and image transform store the effects that appear in the
# main menu on startup.

# This image transform shows a particle burst effect image to the main menu when
# the game starts.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

# This transform fades out the particle effects of the main menu
transform particle_fadeout:
    easeout 1.5 alpha 0

# This transform moves the polka-dot menu background to the upper-left.
transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

# This transform loops the polka-dot moving effect.
transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

# This transform moves the menu logo down to it's intended placement in-game.
transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

# This transform moves the main menu screen in-game to be visible.
transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

# This transform fades out the main menu screen. 
transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

# This transform takes in a z-axis, x-axis and zoom numbers and moves the menu
# sprites to where they appear in the game.
transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

## Team Salvato Splash Screen
# This image stores the Tean Salvato logo image that appears when the game starts.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# This image is a left over from DDLC's development that shows the splash message
# when the game starts.
image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

## These images are the background images shown in-game during the disclaimer.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## This sets the persistent to false in order to choose a language.
default persistent.has_chosen_language = False

## This sets the first run variable to False to show the disclaimer.
default persistent.first_run = False

## Startup Disclaimer
## This label calls the disclaimer screen that appears when the game starts.
label splashscreen:
    $ initialize_characters_folder()
    ## Shows the option to delete existing save data if conditions are met.
    if not persistent.first_run and len(renpy.list_saved_games(fast=True)) > 0:
        $ quick_menu = False
        scene black

        menu:
            "A previous save file has been found. Would you like to delete your save data and start over?"
            "Yes, delete my existing data.":
                "Deleting save data...{nw}"
                python:
                    delete_all_saves()
                    renpy.utter_restart()
            "No, continue where I left off.":
                python:
                    restore_characters()
                    persistent.first_run = True

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        # Switch to the language selector before showing the disclaimer if translations
        # are available and the player hasn't chosen a language yet.
        if not persistent.has_chosen_language and translations:
            if _preferences.language is None:
                call screen language_selector

        # You can edit this message but you MUST declare that your mod is 
        # unaffiliated with Team Salvato, requires that the player must 
        # finish DDLC before playing, has spoilers for DDLC, and where to 
        # get DDLC (preferably https://ddlc.moe).
        #
        # ...Yes this even applies if your mod has no spoilers whatsoever.
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated in anyway with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: https://ddlc.moe or on Steam."

        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                $ persistent.first_run = True

        scene tos2
        with Dissolve(1.5)
        pause 1.0

        # Check if a streaming/recording program is running and let the player know.
        if is_user_streaming():
            call screen dialog("A streaming/recording program has been detected. Let's Play Mode has been enabled to protect your privacy.",
                [Hide("dialog"), Return()])
        scene white

    # This python statement controls whether the Sayori Kill Early screen shows 
    # in-game. This feature has been commented out for mod safety reasons but can 
    # be used if needed.

    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: renpy.file("../characters/sayori.chr")
    #         except IOError: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: renpy.file("../characters/monika.chr")
    #             except IOError: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: renpy.file("../characters/natsuki.chr")
    #             except IOError: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: renpy.file("../characters/yuri.chr")
    #             except IOError: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: renpy.file("../characters/sayori.chr")
    #             except IOError: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    # Sets up the random special poems that appears during Act 2 of the game.
    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            
            # This sets the range of poem numbers to pick from. In base DDLC,
            # there are 11 special poems.
            a = list(range(1,12))

            # Set three unique random poems to appear in Act 2.
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    # Stores the path to the base directory of the game. Used in Act 3.
    $ basedir = config.basedir.replace('\\', '/')

    # Load the autoload label if the variable is set.
    if persistent.autoload:
        jump autoload

    $ config.allow_skipping = False
    # Shows the ghost menu if the player is in Act II and conditions are met.
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    # This checks if 'sayori.chr' was deleted after the disclaimer page and if so,
    # show a premature death scene. This feature has been commented out for mod safety reasons but can
    # be used if needed.

    # if s_kill_early:
    #     show black
    #     play music "bgm/s_kill_early.ogg"
    #     $ pause(1.0)
    #     show end with dissolve_cg
    #     $ pause(3.0)
    #     scene white
    #     show expression "images/cg/s_kill_early.png":
    #         yalign -0.05
    #         xalign 0.25
    #         dizzy(1.0, 4.0, subpixel=False)
    #     show white as w2:
    #         choice:
    #             ease 0.25 alpha 0.1
    #         choice:
    #             ease 0.25 alpha 0.125
    #         choice:
    #             ease 0.25 alpha 0.15
    #         choice:
    #             ease 0.25 alpha 0.175
    #         choice:
    #             ease 0.25 alpha 0.2
    #         choice:
    #             ease 0.25 alpha 0.225
    #         choice:
    #             ease 0.25 alpha 0.25
    #         choice:
    #             ease 0.25 alpha 0.275
    #         choice:
    #             ease 0.25 alpha 0.3
    #         pass
    #         choice:
    #             pass
    #         choice:
    #             0.25
    #         choice:
    #             0.5
    #         choice:
    #             0.75
    #         repeat
    #     show noise:
    #         alpha 0.1
    #     with Dissolve(1.0)
    #     show expression Text("Now everyone can be happy.", style="sayori_text"):
    #         xalign 0.8
    #         yalign 0.5
    #         alpha 0.0
    #         600
    #         linear 60 alpha 0.5
    #     pause
    #     $ renpy.quit()

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    $ pause(1.5)
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ pause(0.5)
    $ config.allow_skipping = True
    return

# This label script is used when 'monika.chr' is deleted from the game after the 
# at the beginning of a new game. This feature has been commented out for mod safety 
# reasons but can be used if needed.

# label ch0_kill:
#     $ s_name = "Sayori"
#     show sayori 1b zorder 2 at t11
#     s "..."
#     s "..."
#     s "W-What..."
#     s 1g "..."
#     s "This..."
#     s "What is this...?"
#     s "Oh no..."
#     s 1u "No..."
#     s "This can't be it."
#     s "This can't be all there is."
#     s 4w "What is this?"
#     s "What am I?"
#     s "Make it stop!"
#     s "PLEASE MAKE IT STOP!"

#     $ delete_character("sayori")
#     $ delete_character("natsuki")
#     $ delete_character("yuri")
#     $ delete_character("monika")
#     $ renpy.quit()
#     return

## This label handles special logic that should happen after a save is loaded.
label after_load:
    $ restore_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    
    # Check if we are in the Yuri Death CG scene in Act 2 and if so, redirect
    # back to the scene. This feature has been commented out for mod safety reasons 
    # but can be used if needed.

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     if persistent.yuri_kill >= 1380:
    #         $ persistent.yuri_kill = 1440
    #     elif persistent.yuri_kill >= 1180:
    #         $ persistent.yuri_kill = 1380
    #     elif persistent.yuri_kill >= 1120:
    #         $ persistent.yuri_kill = 1180
    #     elif persistent.yuri_kill >= 920:
    #         $ persistent.yuri_kill = 1120
    #     elif persistent.yuri_kill >= 720:
    #         $ persistent.yuri_kill = 920
    #     elif persistent.yuri_kill >= 660:
    #         $ persistent.yuri_kill = 720
    #     elif persistent.yuri_kill >= 460:
    #         $ persistent.yuri_kill = 660
    #     elif persistent.yuri_kill >= 260:
    #         $ persistent.yuri_kill = 460
    #     elif persistent.yuri_kill >= 200:
    #         $ persistent.yuri_kill = 260
    #     else:
    #         $ persistent.yuri_kill = 200
    #     jump expression persistent.autoload

    # [NOTE: If you uncommented the Yuri Death CG redirect above, add a `elif` statement here.]
    # This checks if the local anti-cheat variable matches the persistent one and 
    # if not, block the load and show a special message.
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "You're so funny."
        else:
            m "You're so funny, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        # Show a hint about the skip button if it's the player's first playthrough.
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return

## This label loads the label saved in the autoload variable. 
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

# This label is used when the game starts to direct back to
# Yuri's Death CG from the main menu. This feature has been commented out for mod 
# safety reasons but can be used if needed.

# label autoload_yurikill:
#     if persistent.yuri_kill >= 1380:
#         $ persistent.yuri_kill = 1440
#     elif persistent.yuri_kill >= 1180:
#         $ persistent.yuri_kill = 1380
#     elif persistent.yuri_kill >= 1120:
#         $ persistent.yuri_kill = 1180
#     elif persistent.yuri_kill >= 920:
#         $ persistent.yuri_kill = 1120
#     elif persistent.yuri_kill >= 720:
#         $ persistent.yuri_kill = 920
#     elif persistent.yuri_kill >= 660:
#         $ persistent.yuri_kill = 720
#     elif persistent.yuri_kill >= 460:
#         $ persistent.yuri_kill = 660
#     elif persistent.yuri_kill >= 260:
#         $ persistent.yuri_kill = 460
#     elif persistent.yuri_kill >= 200:
#         $ persistent.yuri_kill = 260
#     else:
#         $ persistent.yuri_kill = 200
#     jump expression persistent.autoload

# This label sets the main menu music to Doki Doki Literature Club before the
# menu starts.
label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

# This label handles special logic that should happen when the game quits.
label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
