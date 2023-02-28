## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## achievements.rpy
# This file contains the code for the achievements menu and notification that 
# shows your progress throughout the mod.

default persistent.achievements = {}

init -1 python in achievements:
    from store import persistent, im
    achievementList = {}
    
    # This class declares the code to make a achievement (Non-Counting).
    # Syntax:
    #   name - This variable contains the human-readable name of the achievement.
    #   description - This variable contains the human-readable description of your
    #       achievement.
    #   image - This variable contains the path or image tag of the achievement.
    #   persistent - This variable contain the name of a in-game variable to check if the
    #       achievement has been completed or not.
    #   count - This variable checks if the achievement declared requires a number to match.
    #   locked_desc - This variable contains the human-readable description of your
    #       achievement when it is locked.
    #   show_desc_while_locked - This variable determines whether to show the actual description
    #       of the achievement or a locked one.
    class Achievement(object):

        def __init__(self, name, description, image, locked_desc="???", show_desc_while_locked=False):
            # The human readable name of the achievement.
            self.name = name

            # The description of the achievement.
            self.description = description

            # The image variable or path of the achievement image.
            self.image = image

            # The image variable or path of the achievement image if the 
            # achievement hasn't been unlocked.
            self.locked = im.MatrixColor(image, im.matrix.desaturate())
            self.locked_desc = locked_desc

            self.show_desc_while_locked = show_desc_while_locked

            if self.name not in persistent.achievements:
                persistent.achievements[self.name] = {
                    "unlocked": False,
                    "current_count": 0,
                }

            self.unlocked = persistent.achievements[self.name]['unlocked']

            achievementList[self.name] = self
        
        def unlock(self):
            self.unlocked = True
            persistent.achievements[self.name]['unlocked'] = True
            renpy.show_screen("achievement_notify", self)
    
    # This class declares the code to make a achievement (Non-Counting).
    # This class has the same syntax as Achievement but 1 more argurment.
    # Refer to Achievement for the rest of the argurments here.
    # Syntax:
    #   max_count = The total counts needed to unlock the achievement
    class AchievementCount(Achievement):
        def __init__(self, name, description, image, show_desc_while_locked=False, max_count=100):
            Achievement.__init__(self, name, description, image, show_desc_while_locked)

            self.current_count = persistent.achievements[self.name]['current_count']
            self.max_count = max_count
        
        def increase_count(self):
            self.current_count += 1
            persistent.achievements[self.name]['current_count'] += 1
            if self.current_count == self.max_count:
                self.unlock()

init python:
    selectedAchievement = None
    # This section declares the achievements. See the 'Achievements' class
    # syntax to declare one.
    startup = Achievement("Welcome to DDLC!", "Thanks for accepting the TOS.",
            "gui/logo.png")
    steam = Achievement("Steam", "Steam User.",
            "gui/logo.png")
    lets_count = AchievementCount("Count", "1-3",
            "gui/logo.png", max_count=3)

    # Fast Sort (DO NOT REMOVE)
    achievementList = {k: achievementList[k] for k in sorted(achievementList)}

## Achievements Screen #############################################################
##
## This screen is used to make a achievements view of all possible achievements
## the mod has in the main menu.
##
## Syntax:
##   al.image - This variable contains the path or image tag of the achievement.
##   al.locked - This variable contains the locked image of the achievement.
##   al.persistent - This variable contains the name of the in-game variable to check
##                      if the achievement is completed or not.
##   al.maxCount - This variable contains the number needed for the achievement to be
##                  unlocked.
##   gl.description - This variable contains the description of the achievement.
screen achievements():

    tag menu
    style_prefix "achievements"

    use game_menu(_("Awards")):

        fixed:
            # This vbox is responsible for the achievement display above the list
            # of possible achievements to display the selected achievements' info.
            vbox:
                xpos 0.26
                ypos -0.1

                hbox:

                    if selectedAchievement:

                        add ConditionSwitch(
                                selectedAchievement.unlocked, selectedAchievement.image, "True",
                                selectedAchievement.locked) at achievement_scaler(128)
                    else:
                        null height 128

                    spacing 20

                    vbox:
                        xsize 400
                        ypos 0.2

                        if selectedAchievement:

                            text selectedAchievement.name:
                                font gui.name_font
                                color "#fff"
                                outlines [(2, "#505050", 0, 0)]

                            if not selectedAchievement.unlocked and not selectedAchievement.show_desc_while_locked:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.locked_desc] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.locked_desc
                            else:
                                if isinstance(selectedAchievement, AchievementCount):
                                    text "[selectedAchievement.description] ([selectedAchievement.current_count] / [selectedAchievement.max_count])"
                                else:
                                    text selectedAchievement.description
                        else:
                            null height 128

            # This vpgrid is responsible for the list of achievements in the game.
            vpgrid:
                id "avp"
                rows math.ceil(len(achievementList) / 6.0)
                if len(achievementList) > 6: 
                    cols 6
                else: 
                    cols len(achievementList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.85
                ysize 410

                for name, al in achievementList.items():

                    imagebutton:
                        idle Transform(ConditionSwitch(
                                al.unlocked, al.image, "True",
                                al.locked), size=(128,128))
                        action SetVariable("selectedAchievement", al)

            vbar value YScrollValue("avp") xalign 1.01 ypos 0.2 ysize 400

        textbutton "?":
            style "return_button"
            xpos 0.99 ypos 1.1
            action ShowMenu("dialog", "{b}Help{/b}\nGray icons indicate that this achievement is locked.\nContinue your progress in [config.name]\nto unlock all the achievements possible.", ok_action=Hide("dialog"))

        if config.developer:
            textbutton "Test Notif":
                style "return_button"
                xpos 0.8 ypos 1.1
                action ShowMenu("achievement_notify", startup)

## Achievements Notify Screen #############################################################
##
## This screen is used to notify a user of a unlocked achievement.
##
## Syntax:
##   reward.image - This variable contains the path or image tag of the achievement.
##   reward.name - This variable contains the locked image of the achievement.
## 
## To call on this menu, do 'show screen achievement_notify(X)' where X is the achievement in question itself.
## Make sure to set the variable assign to it or else it will show up as locked.
screen achievement_notify(reward):
    
    style_prefix "achievements"

    frame at achievement_notif_transition:
        xsize 300
        ysize 90
        xpos 0.4

        hbox:
            xalign 0.27
            yalign 0.5
            add reward.image at achievement_scaler(50)
            spacing 20
            vbox:
                spacing 5
                text "Achievement Unlocked!" size 16
                text reward.name size 14
    
    timer 4.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]

style achievements_text is gui_text
style achievements_text:
    color "#000"
    outlines []
    size 20

transform achievement_scaler(x):
    size(x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0

style achievements_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
