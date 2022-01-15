## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.
## You may only use this file/feature only for DDLC mods and not for DDLC patchers,
## unofficial fixes, etc.

## achievements.rpy

# This file is not part of DDLC. This file contains the code for the achievements
# menu and notification that shows your progress throughout the mod.

init python:
    import math

    achievementList = []
    selectedAchievement = None

    # This class declares the code to make a achievement.
    # Syntax:
    #   name - This variable contains the human-readable name of the achievement.
    #   description - This variable contains the human-readable description of your
    #                   achievement.
    #   image - This variable contains the path or image tag of the achievement.
    #   persistent - This variable contain the name of a in-game variable to check if the
    #                   achievement has been completed or not.
    #   count - This variable checks if the achievement declared requires a number to match.
    #   maxCount - This variable stores the maxCount a achievement needs to be completed.
    class Achievements:

        def __init__(self, name, description, image, persistent, count=False, maxCount=100):
            # The human readable name of the achievement.
            self.name = name

            # The description of the achievement.
            self.description = description

            # The image variable or path of the achievement image.
            self.image = image

            # The image variable or path of the achievement image if the 
            # achievement hasn't been unlocked.
            self.locked = im.MatrixColor(image, im.matrix.desaturate())

            # A condition to see if a set number is needed to unlock the achievement.
            self.count = count

            # The name of the variable to check if it's T/F | meets the maxCount or more.
            self.persistent = persistent
            
            # The max number of items the user needs to unlock the achievements.
            self.maxCount = maxCount

    # This section declares the achievements. See the 'Achievements' class
    # syntax to declare one.
    startup = Achievements("Welcome to DDLC!", "Thanks for accepting the TOS.",
            "gui/logo.png", "persistent.first_run")
    achievementList.append(startup)

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

    use game_menu(_("Achievements")):
        
        style_prefix "achievements"

        # This vbox is responsible for the achievement display above the list
        # of possible achievements to display the selected achievements' info.
        vbox:
            xpos 0.26
            ypos -0.1

            hbox:

                if selectedAchievement:

                    python:
                        currentVal = eval(selectedAchievement.persistent)

                        if not currentVal:
                            currentVal = False

                    if selectedAchievement.count:
                        add ConditionSwitch(
                                currentVal >= selectedAchievement.maxCount, selectedAchievement.image, "True",
                                selectedAchievement.locked) at achievement_scaler(128)
                    else:
                        add ConditionSwitch(
                                currentVal, selectedAchievement.image, "True",
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

                        if selectedAchievement.count:
                            text "[selectedAchievement.description] ([currentVal] / [selectedAchievement.maxCount])"
                        else:
                            text selectedAchievement.description
                    else:
                        null height 128

        # This vpgrid is responsible for the list of achievements in the game.
        vpgrid:
            id "avp"
            rows math.ceil(len(achievementList) / 6.0)
            cols 6

            spacing 25
            mousewheel True

            xalign 0.5
            ypos 0.2
            ysize 410

            for al in achievementList:

                python:
                    currentVal = eval(al.persistent)

                    if not currentVal:
                        currentVal = False

                if al.count:
                    
                    imagebutton:
                        idle Transform(ConditionSwitch(
                                currentVal >= al.maxCount, al.image, "True",
                                al.locked), size=(128,128))
                        action SetVariable("selectedAchievement", al)
                else:
                    imagebutton:
                        idle Transform(ConditionSwitch(
                                currentVal, al.image, "True",
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
        ysize 100
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
    
    timer 5.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]

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
