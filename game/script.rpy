


label start:

    # Configures your mod to use a ID to prevent users from cheating.
    # Leave this as default.
    $ anticheat = persistent.anticheat

    # Controls what chapter we start.
    $ chapter = 0

    # If the user quits during pause, this sets it to false after restarting.
    $ _dismiss_pause = config.developer

    # Names of the Characters
    # To add a character -> $ mi_name = "Mike"
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    # Controls whether we have a Menu in the Textbox
    $ quick_menu = True

    # Controls whether we want normal or glitched dialogue
    $ style.say_dialogue = style.normal

    # Controls whether Sayori is Dead. Leave this alone
    $ in_sayori_kill = None
    
    # Controls whether we allow skipping.
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Start of the script
    if persistent.playthrough == 0:
        # 'call tutorial_selection' controls what label to call 
        # from in your script files
        call tutorial_selection

    if persistent.playthrough == 1:
        return
    
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
