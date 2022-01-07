## splash.rpy

# This is where the splashscreen, disclaimer and menu code reside in.

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder.
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                renpy.error("DDLC archive files not found in /game folder. Check your installation and try again.")

## Splash Message
# This python statement is where the splash messages reside in.
init python:
    menu_trans_time = 1
    # This variable is the default splash message that people will see when
    # the game launches.
    splash_message_default = "This game is an unofficial fan game that is unaffiliated with Team Salvato."
    # This array variable stores different kinds of splash messages you can use
    # to show to the player on startup.
    splash_messages = [
        "Please support Doki Doki Literature Club.",
        "Monika is watching you code."
    ]

# This image text shows the splash message when the game loads.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Main Menu Images
# These image transforms store the images and positions of the game logo,
# the menu character sprites and main menu/pause menu screen images.

# This image shows the DDLC logo in the normal DDLC position.
image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# This image shows the main menu polka-dot image.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

# This image shows the pause menu polka-dot image.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
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

# This init python statement checks if the character files are present in-game
# and writes them to the characters folder depending on the playthrough.
init python:
    if not persistent.do_not_delete:
        restore_all_characters()

## These images are the background images shown in-game during the disclaimer.
image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

## Startup Disclaimer
# This label calls the disclaimer screen that appears when the game starts.
label splashscreen:
    # This python statement grabs the username and process list of the PC.
    python:
        process_list = []
        currentuser = ""

        if renpy.windows:
            try: process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                try:
                    process_list = subprocess.check_output("powershell (Get-Process).ProcessName", shell=True).lower().replace("\r", "").split("\n") # For W11 builds > 22000
                    
                    for x in range(len(process_list)):
                        process_list[x] += ".exe"
                except: pass            
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except: pass

        else:
            try:
                process_list = subprocess.check_output("ps -a --format cmd", shell=True).split(b"\n")

                for x in range(len(process_list)):
                    process_list[x] = process_list[x].decode()
                process_list.pop(0)
            except: pass

            try: 
                user = subprocess.check_output("whoami", shell=True).capitalize().replace("\n", "")
                if user:
                    currentuser = user
            except: pass

    # This if statement checks if we have passed the disclaimer and that the
    # current version of the mod equals the old one or the autoload is set to 
    # the post-credit loop.
    if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
        $ quick_menu = False
        scene black

        menu:
            "A previous save file has been found. Would you like to delete your save data and start over?"
            "Yes, delete my existing data.":
                "Deleting save data...{nw}"
                python:
                    delete_all_saves()
                    renpy.loadsave.location.unlink_persistent()
                    renpy.persistent.should_save_persistent = False
                    renpy.utter_restart()
            "No, continue where I left off.":
                $ restore_relevant_characters()

    # These variables and if statements are for the lockdown feature introduced
    # in 2.4.6 of the template. DO NOT MODIFY THESE LINES.
    default persistent.lockdown_warning = False

    if not persistent.lockdown_warning:
        if config.developer:
            call lockdown_check
        else:
            $ persistent.lockdown_warning = True

    ## This sets the first run variable to False to show the disclaimer.
    default persistent.first_run = False

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        # You can edit this message but you MUST declare that your mod is unaffiliated with Team Salvato,
        # requires that the player must finish DDLC before playing, has spoilers for DDLC, and where to 
        # get DDLC's files."
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated in anyway with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: https://ddlc.moe or on Steam."

        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            "I agree.":
                pass
                
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white

    # This python statement controls whether the Sayori Kill Early screen shows in-game.
    # This feature has been commented out for mod safety reasons but can be used
    # if needed.

    # python:
    #     s_kill_early = None
    #     if persistent.playthrough == 0:
    #         try: renpy.file("../characters/sayori.chr")
    #         except: s_kill_early = True
    #     if not s_kill_early:
    #         if persistent.playthrough <= 2 and persistent.playthrough != 0:
    #             try: renpy.file("../characters/monika.chr")
    #             except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
    #         if persistent.playthrough <= 1 or persistent.playthrough == 4:
    #             try: renpy.file("../characters/natsuki.chr")
    #             except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
    #             try: renpy.file("../characters/yuri.chr")
    #             except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    #         if persistent.playthrough == 4:
    #             try: renpy.file("../characters/sayori.chr")
    #             except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())


    # This if statement controls which special poems are shown to the player in-game.
    if not persistent.special_poems:
        python hide:
            # This variable sets a array of zeroes to assign poem numbers.
            persistent.special_poems = [0,0,0]
            
            # This sets the range of poem numbers to pick from.
            a = range(1,12)

            # This for loop loops 3 times (array number of special_poems) and
            # assigns a random number to the array.
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                # This line makes sure we remove the number chosen from the range
                # list to avoid duplicates.
                a.remove(b)

    # This variable makes sure the path of the base directory is Linux/macOS/Unix 
    # based than Windows as Python/Ren'Py prefers this placement.
    $ basedir = config.basedir.replace('\\', '/')

    # This if statement checks whether we have a auto-load set to load it than
    # start the game screen as-new.
    if persistent.autoload:
        jump autoload

    # This variable sets skipping to False for the splash screen.
    $ config.allow_skipping = False

    # This if statement checks if we are in Act 2, have not seen the ghost menu
    # before and a random number is 0 from 0-63.
    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        # These variables set the splash and menu screen to be a ghost menu.
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return

    # This if statement checks if 'sayori.chr' was deleted after the disclaimer
    # was made. This feature has been commented out for mod safety reasons but
    # can be used if needed.

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
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

# This label is a left-over from DDLC's development that hides the Team Salvato
# logo and shows the splash message.
label warningscreen:
    hide intro
    show warning
    pause 3.0

# This label is used when 'monika.chr' is deleted when the game starts Day 1 of
# Act 1. This feature has been commented out for mod safety reasons but can be
# used if needed.

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

# This label checks if the save loaded matches the anti-cheat stored in the save.
label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"

        $ renpy.utter_restart()
    return

# This label loads the label saved in the autoload variable. 
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

        try: renpy.pop_call()
        except: pass
        
    jump expression persistent.autoload

# This label sets the main menu music to Doki Doki Literature Club before the
# menu starts
label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

# This label is a left-over from DDLC's development that quits the game but shows
# a close-up Monika face before doing so.
label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
