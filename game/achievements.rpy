
init python:
    import math

    achievementList = []
    selectedAchievement = None

    class Achievements:

        def __init__(self, name, description, image, persistent, count=False, maxCount=100):
            self.name = name
            self.description = description
            self.image = image
            self.locked = im.MatrixColor(image, im.matrix.desaturate())
            self.count = count
            self.persistent = persistent
            self.maxCount = maxCount

    startup = Achievements("Welcome to DDLC!", "Thanks for accepting the TOS.",
            "gui/logo.png", "persistent.first_run")
    achievementList.append(startup)

screen achievements:

    tag menu

    use game_menu(_("Achievements")):
        
        style_prefix "achievements"

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
            action ShowMenu("dialog", "{b}Help{/b}\n Gray icons indicate that this achievement is locked.\nContinue your progress in [config.name]\nto unlock all the achievements possible.", ok_action=Hide("dialog"))

        if config.developer:
            textbutton "Test Notif":
                style "return_button"
                xpos 0.8 ypos 1.1
                action [ShowMenu("achievement_notify", startup), With(Dissolve(0.5))]

screen achievement_notify(reward):
    
    style_prefix "achievements"
    frame:
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