## cgs.rpy

# This file defines all the character graphics (CGs) in DDLC such as Yuri's
# Chocolate CG and Natsuki's Manga CG.

## Yuri's Chocolate CG [Yuri Route 2]
# This is the background of the CG (Classroom Wall).
image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
    6.0
    "images/cg/y_cg2_bg2.png" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.png" with Dissolve(1)
    1
    repeat

# This is the base of Yuri reading her book with chocolate.
image y_cg2_base:
    "images/cg/y_cg2_base.png"

# This image hides the chocolate in Yuri's base image with a open mouth. 
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0

# This image transform adds some details to the CG to make the scene sparkle
# a bit more.
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# This image makes Yuri appear shocked in the CG
image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# This image makes Yuri appear embarrassed in the CG
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# These image transform adds a dust layer to the CG to make the scene sparkle
# a bit more.
image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

## Natsuki Reading Manga CG [Natsuki Route 1]
# This is the background of the CG (Classroom Wall).
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"

# This is the base of Natsuki watching you read manga.
image n_cg1_base:
    "images/cg/n_cg1_base.png"

# This image makes Natsuki look happy in the CG.
image n_cg1_exp1:
    "images/cg/n_cg1_exp1.png"

# This image makes Natsuki look pouty in the CG.
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.png"

# This image makes Natsuki look happy in the CG.
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.png"

# This image makes Natsuki look sleepy in the CG.
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.png"

# This image makes Natsuki look half-awake in the CG.
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.png"

# This image makes Natsuki look glitched in the CG during Act 2.
image n_cg1b = Composite((1280,720), (0,0), "images/cg/n_cg1b.png", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

# These image transforms covers Natsuki's eyes with black squares during Act 2.
image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    xysize (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    xysize (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    xysize (30, 20)

## Natsuki's Closet CG [Natsuki Route 2]
# This is the background of the CG (Closet).
image n_cg2_bg:
    "images/cg/n_cg2_bg.png"

# This is the base of Natsuki moving her manga up the shelf.
image n_cg2_base:
    "images/cg/n_cg2_base.png"

# This image makes Natsuki look concerned in the CG.
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.png"

# This image makes Natsuki look shouty in the CG.
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.png"

## Natsuki's Kitchen Incident CG [Natsuki Route 3]
# This is the background of the CG (Kitchen Floor).
image n_cg3_base:
    "images/cg/n_cg3_base.png"

# This adds cake frosting to Natsuki's finger.
image n_cg3_cake:
    "images/cg/n_cg3_cake.png"

# This image makes Natsuki look like she is laughing in the CG.
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.png"

# This image makes Natsuki look embarrassed in the CG.
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.png"

## Yuri's Reading Together CG [Yuri Route 1]
# This is the background and base of Yuri in the CG (Classroom Desk).
image y_cg1_base:
    "images/cg/y_cg1_base.png"

# This image makes Yuri look at MC in the CG.
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.png"

# This image makes Yuri smile in the CG.
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.png"

# This image makes Yuri panic as a yandere in the CG.
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.png"

## Yuri's Ink Incident CG [Yuri Route 3]
# This is the background and base of Yuri in the CG (MC's Room).
image y_cg3_base:
    "images/cg/y_cg3_base.png"

# This image makes Yuri close her eyes in the CG.
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.png"

## Sayori's Blazer CG [Sayori Route 1]
# This is the background and base of Sayori in the CG (Classroom).
image s_cg1:
    "images/cg/s_cg1.png"

## Sayori's Head Bump Incident CG [Sayori Route 2]
# This is the background and base of Sayori in the CG (Classroom Closet).
image s_cg2_base1:
    "images/cg/s_cg2_base1.png"

# This is a alternative background and base of Sayori with a apple juice drink
# in her hand.
image s_cg2_base2:
    "images/cg/s_cg2_base2.png"

# This image makes Sayori look hurt in the CG.
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.png"

# This image makes Sayori look upset in the CG.
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.png"
    
# This image makes Sayori close her eyes in the CG.
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.png"

## Sayori's Hug CG [Day 4]
# This is the background and base of Sayori of the CG (Outside MC's House).
image s_cg3:
    "images/cg/s_cg3.png"

## Sayori Suicide CG
# This is the background of the CG (Sayori's Room).
image s_kill_bg:
    subpixel True
    "images/cg/s_kill_bg.png"

# This image shows Sayori hanging in the CG.
image s_kill:
    subpixel True
    "images/cg/s_kill.png"

# This is the glitched background of the CG's original background.
image s_kill_bg2:
    subpixel True
    "images/cg/s_kill_bg2.png"

# This is the glitched sprite of Sayori hanging in the CG.
image s_kill2:
    subpixel True
    "images/cg/s_kill2.png"

## Yuri Stab CG
# This image condition displays certain images of Yuri's
# stab CG given how much time has passed in-game.
image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 1180", "images/cg/y_kill/3c.png",
    "persistent.yuri_kill >= 1120", "images/cg/y_kill/3b.png",
    "persistent.yuri_kill >= 920", "images/cg/y_kill/3a.png",
    "persistent.yuri_kill >= 720", "images/cg/y_kill/2c.png",
    "persistent.yuri_kill >= 660", "images/cg/y_kill/2b.png",
    "persistent.yuri_kill >= 460", "images/cg/y_kill/2a.png",
    "persistent.yuri_kill >= 260", "images/cg/y_kill/1c.png",
    "persistent.yuri_kill >= 200", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png",

    )

# This transform starts off the animation for the background in Sayori's 
# hanging CG.
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

# This transform starts off the animation for Sayori's hanging sprite in 
# Sayori's hanging CG.
transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

# This image transform zooms in on the background in Sayori's hanging CG.
image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

# This transform makes the image or sprite shake as if the player was dizzy.
transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

# This image transform zooms in on Sayori's hanging sprite in Sayori's hanging
# CG.
image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

# This image transform zooms in on the glitched background in Sayori's hanging
# CG.
image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

# This image transform zooms in on the glitched Sayori hanging sprite in 
# Sayori's hanging CG.
image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
