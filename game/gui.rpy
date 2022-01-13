## gui.rpy

# This file defines all the positions, colors, paths and more of DDLC's GUI
# interface.

## NOTE: To configure settings for Android, scroll down to the init python block
## on line 379

init -2 python:
    # This sets the resolution of DDLC to 1280x720p
    gui.init(1280, 720)

## GUI Sounds
# These variables set the sound effects for the GUI elements in the game.
define -2 gui.hover_sound = "gui/sfx/hover.ogg" # Hover Sound Effect
define -2 gui.activate_sound = "gui/sfx/select.ogg" # Click Sound Effect
define -2 gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg" # Glitched Sound Effect

## Colors!
# These variables set the color for DDLC's text in-game.

# This color is used to label and highlight text.
define -2 gui.accent_color = '#ffffff'

# This color is used for a text button when it is neither selected nor hovered.
define -2 gui.idle_color = '#aaaaaa'

# The small color is used for small text, which needs to be brighter/darker to
# achieve the same effect.
define -2 gui.idle_small_color = '#333'

# This color is that is used for buttons and bars that are hovered.
define -2 gui.hover_color = '#cc6699'

# This color is used for a text button when it is selected but not focused.
define -2 gui.selected_color = '#bb5588'

# This color is used for a text button when it cannot be selected.
define -2 gui.insensitive_color = '#aaaaaa7f'

# These colors are used for bars that are not filled in completely. They are not
# used directly, but are used when re-generating bar image files.
define -2 gui.muted_color = '#6666a3'
define -2 gui.hover_muted_color = '#9999c1'

# This color is used for dialogue and menu choice text.
define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'

# Fonts and Font Sizes
# These variables set the font and its' size for DDLC's text in-game.

# This font is used for in-game text.
define -2 gui.default_font = "gui/font/Aller_Rg.ttf"

# This font is used for character names.
define -2 gui.name_font = "gui/font/RifficFree-Bold.ttf"

# This font is used for out-of-game text.
define -2 gui.interface_font = "gui/font/Aller_Rg.ttf"

# The text size of normal dialogue text.
define -2 gui.text_size = 24

# This determines the text size of character names.
define -2 gui.name_text_size = 24

# This determines the text size of the game's user interface.
define -2 gui.interface_text_size = 24

# This determines the text size of the game's label in the user interface.
define -2 gui.label_text_size = 28

# This determines the text size of the notification screen.
define -2 gui.notify_text_size = 16

# This determines the text size of the game's title on the bottom-right.
define -2 gui.title_text_size = 38

## Main Menu and Game Menu
# These variables set what is shown in the game menu.

# This sets the background for the main menu
define -2 gui.main_menu_background = "menu_bg"

# This sets background for the pause/game menu
define -2 gui.game_menu_background = "game_menu_bg"

## Dialogue
# These variables set the dialogue box positions and placement in-game.

# This controls the height of the textbox containing dialogue.
define -2 gui.textbox_height = 182

# This controls the placement of the textbox vertically on the screen. 
# 0.0 is the top, 0.5 is the center, and 1.0 is the bottom.
define -2 gui.textbox_yalign = 0.99

# This controls the placement of the speaking character's name.
define gui.name_xpos = 350
define gui.name_ypos = -3

# This controls the horizontal alignment of the character's name.
define gui.name_xalign = 0.5

# This controls the width, height, and borders of the box containing the 
# characters' name.
define gui.namebox_width = 168
define gui.namebox_height = 39

# This controls the borders of the box containing the characters' name in 
# left, top, right, and bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 2)

# This controls the display of the frame containing the namebox.
define gui.namebox_tile = False

# This controls the placement of dialogue relative to the textbox.
define gui.text_xpos = 268
define gui.text_ypos = 62

# This controls the maximum width of dialogue text.
define gui.text_width = 744

# This controls the horizontal alignment of the dialogue text.
define gui.text_xalign = 0.0

## Buttons
# These variables set the buttons in-game.

# This controls the width and height of a button. 
# If None is declared, Ren'Py computes a size for it automatically.
define gui.button_width = None
define gui.button_height = 36

# This controls the borders on each side of the button 
# in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

# This controls whether the button background is tiled and 
# increase/decrease its' size or are centered and scaled.
#  True - Button BG is Tiled | False - Button BG is centered.
define gui.button_tile = False

# This controls the font that the button will use.
define gui.button_text_font = gui.interface_font

# This controls the font size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

# This controls the color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

# This controls the horizontal alignment of the button text.
define gui.button_text_xalign = 0.0

# This controls the borders on each side of the 
# check/radio buttons in left, top, right, bottom order.
define gui.radio_button_borders = Borders(28, 4, 4, 4)
define gui.check_button_borders = Borders(28, 4, 4, 4)

# This controls the horizontal alignment of the confirm button.
define gui.confirm_button_text_xalign = 0.5

# This controls the borders on each side of the page buttons 
# in left, top, right, bottom order.
define gui.page_button_borders = Borders(10, 4, 10, 4)

## Quick Buttons
# These variables set the buttons in the quick menu and it's text.

define gui.quick_button_text_size = 14

define gui.quick_button_text_idle_color = "#522"
define gui.quick_button_text_hover_color = "#fcc"
define gui.quick_button_text_selected_color = gui.accent_color
define gui.quick_button_text_insensitive_color = "#a66"

## Choice Buttons
# These variables set the buttons of the choice (menu) buttons.

define gui.choice_button_width = 420
define gui.choice_button_height = None

define gui.choice_button_tile = False

define gui.choice_button_borders = Borders(100, 5, 100, 5)

define gui.choice_button_text_font = gui.default_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5

define gui.choice_button_text_idle_color = "#000"
define gui.choice_button_text_hover_color = "#fa9"

## File Slot Buttons 
# This controls the file slot buttons in the save/load menu. 

define gui.slot_button_width = 276
define gui.slot_button_height = 206

define gui.slot_button_borders = Borders(10, 10, 10, 10)

define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_hover_color = gui.hover_color

# This controls the width and height of the thumbnails screenshots of
# the saves.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

# This controls the number of columns and rows in the save slot page.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Positioning and Spacing
# These variables control the positioning and spacing of various user interface
# elements.

define gui.navigation_xpos = 80
define gui.skip_ypos = 10
define gui.notify_ypos = 45

# This controls the spacing between each menu/choice option in the choice screen.
define gui.choice_spacing = 22

# This controls the spacing between each navigation option in the navigation screen.
define gui.navigation_spacing = 6

# This controls the spacing between each preference and preference button option 
# in the preference screen.
define gui.pref_spacing = 10
define gui.pref_button_spacing = 0

# This controls the spacing between each page option in the page screen.
define gui.page_spacing = 0

# This controls the spacing between each save/load slot option in the save/load screen.
define gui.slot_spacing = 10

## Frames
# These variables control the border of frames in-game such as the confirm prompt.

# This controls the default frame size of prompts.
define gui.frame_borders = Borders(4, 4, 4, 4)

# This controls the frame size of confirm prompts.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

# This controls the frame size of skip prompts.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

# This controls the frame size of notification prompts.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

# This controls whether the frames should be tiled or scaled.
#  True - Button BG is Tiled | False - Button BG is centered.
define gui.frame_tile = False

## Bars, Scrollbars, and Sliders

# These variables control the look and size of bars, scrollbars, and sliders.

# This controls size of bars, scrollbars, and sliders.
define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30

# This controls whether the frames should be tiled or scaled.
#  True - Button BG is Tiled | False - Button BG is centered.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

# This controls the default frame size of bars, scrollbars, and sliders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

# This controls the default frame size of vertical bars, scrollbars, and sliders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

# This controls what to do with bars that cannot be scrolled. 
#   "hide" - hides the bar | None - keeps the bar shown
define gui.unscrollable = "hide"

## History
# These variables control how the history screen is shown in-game.

# This controls how many lines of dialogue Ren'Py stores in the 
# menu to the player.
define config.history_length = 50

# This controls the height of the history screen box.
# None will make the height vary at a cost to performance.
define gui.history_height = None

# This controls the position, width, and alignment of the characters' name in
# the history menu.
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0

# This controls the position, width, and alignment of the characters' dialogue in
# the history menu.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 5
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

## NVL
# These variables control the look of the NVL screen.

# This controls the default frame size of the NVL window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

# This controls the height of the NVL dialogue entry. 
#   None will allow each NVL entry to vary in size.
define gui.nvl_height = 115

# This controls the spacing of the NVL dialogue entries in the NVL screen.
define gui.nvl_spacing = 10

# This controls the position, width, and alignment of the characters' name in
# the NVL screen.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

# This controls the position, width, and alignment of the characters' dialogue
# in the NVL screen.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

# This controls the position, width, and alignment of the narrator's dialogue
# in the NVL screen.
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

# This controls the position of the NVL screen buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## Mobile Phones & Tablets
# These variables control how DDLC is displayed on a mobile platform.

init python:

    # This increases the size of the quick buttons to make them easier to touch
    # on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(20, 14, 20, 0)

    # This changes the size and spacing of various GUI elements to ensure they
    # are easily visible on smaller devices.
    if renpy.variant("small"):

        ## Font Size
        gui.text_size = 24
        gui.name_text_size = 24
        gui.notify_text_size = 24
        gui.interface_text_size = 26
        gui.button_text_size = 26
        gui.label_text_size = 28

        ## Dialogue Box/Name Box Positions, Heights and Alignments.
        gui.textbox_height = 182
        gui.name_xpos = 350
        gui.text_xpos = 268
        gui.text_ypos = 62
        gui.text_width = 744
        gui.text_xalign = 0.0

        ## Choice Button Width
        gui.choice_button_width = 420

        ## Spacing
        gui.navigation_spacing = 6
        gui.pref_button_spacing = 10

        ## History 
        gui.history_height = None
        gui.history_text_width = 740

        ## Save/Load File Slots
        gui.file_slot_cols = 3
        gui.file_slot_rows = 2

        ## NVL
        gui.nvl_height = 115

        gui.nvl_name_width = 150
        gui.nvl_name_xpos = 430

        gui.nvl_text_width = 590
        gui.nvl_text_xpos = 450
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 780
        gui.nvl_thought_xpos = 240

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 450

        ## Quick Menu
        gui.quick_button_text_size = 14
