# Options.rpy

# This is where you will name your mod!
# Change "DDLC Mod Template 2.0" to your mod name (e.g. "Yuri")
define config.name = "DDLC Mod Template 2.0"

# This controls whether you want your mod name to show in the main menu.
# If your mod name is big, it is suggested to turn this off (set to False)
define gui.show_name = True

# This is where you will input the version of your mod.
# If you have multiple releases or versions of your mod, this will be pretty useful to change.
# If you are starting out, set this to "1.0.0"
define config.version = "2.0.0"

# This adds information about your mod in the About section.
# DDLC does not have a about section so you can leave this blank.
define gui.about = _("")

# This is the name of your build that the Ren'Py SDK will read.
# The build name is ASCII only so no numbers, spaces, or semicolons.
# Example: Doki Doki Yuri Time to DokiDokiYuriTime
define build.name = "DDLCModTemplate2.0"

# This configures whether your mod has sound effects (e.g. slap sound effects) or not.
# It is best to leave this set to True default.
define config.has_sound = True

# This configures whether your mod has music (e.g. Your Reality) or not.
# It is best to leave this set to True default.
define config.has_music = True

# This configures whether your mod has voices!
# If your using voice actors in your mod, set this to True, else leave it at False.
define config.has_voice = False

# This configures what song/music will play when you launch your mod.
# audio.t1 is the Doki Doki Literature Club Main Menu Music.
# If you want to change this, change the "t1" to the song you want.
define config.main_menu_music = audio.t1

# These two settings control the transition effects of DDLC on the game menu, whether entering or exiting.
# Dissolve(.2) sets the transition effect you see.
# config.enter_transition controls the effect seen when entering the game menu.
# config.exit_transition controls the effect when returning to the game.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# This controls the transition effect of DDLC when loading a saved game.
# By default, this is set to None and you can customize what transition you want to show.
# If you are unsure about this setting, leave it as is.
define config.after_load_transition = None

# This controls the transition effect of DDLC when your mod has ended.
# Dissolve(.2) sets the transition effect you see.
define config.end_game_transition = Dissolve(.5)

# This controls the textbox that the characters use to speak.
# "auto" sets the textbox to hide during scenes and show when a character speaks
# "show" sets the textbox to show at all times
# "hide" only shows dialogue when a character speaks.
define config.window = "auto"

# This controls the transition effects of the textbox.
# Dissolve(.2) sets the transition effect you see.
# config.window_show_transition controls the effect when the textbox is shown.
# config.window_hide_transition controls the effect when the textbox is hidden.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# This sets the text speed of DDLC.
# By default this is set to 50. 
# Increasing this number will speed up text while decreasing the number slows down text speed.
# 0 is instant text display.
default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
















define config.save_directory = "DDLC-1454445547"







define config.window_icon = "gui/window_icon.png"



define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
