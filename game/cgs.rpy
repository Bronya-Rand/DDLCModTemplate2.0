## cgs.rpy

# This defines all Character Graphics (CGs) in DDLC
# such as Yuri Chocolate CG and Natsuki Manga CG.

# Use this as a base if you want to override the CGs from DDLC with your own.

## Yuri Chocolate CG

# Feeding Yuri Chocolate
# This is the slowly fading background
image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
    6.0
    "images/cg/y_cg2_bg2.png" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.png" with Dissolve(1)
    1
    repeat

#Yuri's Face
image y_cg2_base:
    "images/cg/y_cg2_base.png"
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"
    on hide:
        linear 0.5 alpha 0

# Animated Details to Yuri's CG
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# Expressions

# Surprised Yuri
image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Embarrassed Yuri
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

# Particles during Yuri CG
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

## Natsuki Reading Manga CG

# Background
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"
image n_cg1_base:
    "images/cg/n_cg1_base.png"

# Expressions

# Happy Natsuki
image n_cg1_exp1:
    "images/cg/n_cg1_exp1.png"
# Angry Natsuki
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.png"
# Angry Natsuki 2
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.png"
# Eyes closed
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.png"
# Eyes halflidded
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.png"

# Glitched Natsuki CG
image n_cg1b = LiveComposite((1280,720), (0,0), "images/cg/n_cg1b.png", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    size (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    size (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    size (30, 20)

# Natsuki Closet CG

# Closet Background
image n_cg2_bg:
    "images/cg/n_cg2_bg.png"

# Natsuki herself
image n_cg2_base:
    "images/cg/n_cg2_base.png"
# Surprised Natsuki
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.png"
# Shouting Natsuki
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.png"

# Natsuki Wall CG
# Base Image with Background and Natsuki
image n_cg3_base:
    "images/cg/n_cg3_base.png"
# Cake on Finger
image n_cg3_cake:
    "images/cg/n_cg3_cake.png"

# Expressions

# Laughing Natsuki
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.png"
# Embarrassed Natsuki
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.png"

# Yuri Readtime CG

# Base Image with Yuri and Classroom
image y_cg1_base:
    "images/cg/y_cg1_base.png"

# Expressions

# Side-eye at MC/Camera
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.png"

# Mouth Open Yuri
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.png"

# Yandere Yuri
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.png"

# Yuri MC Room CG
image y_cg3_base:
    "images/cg/y_cg3_base.png"

# Eyes Closed Yuri
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.png"

# Sayori Blazer CG
image s_cg1:
    "images/cg/s_cg1.png"

# Hurt Sayori CG

# Without Apple Juice
image s_cg2_base1:
    "images/cg/s_cg2_base1.png"
# With Apple Juice
image s_cg2_base2:
    "images/cg/s_cg2_base2.png"

# Expressions

# Grimace Sayori
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.png"
# Mouth Closed Sayori
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.png"
# Eye Closed Sayori
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.png"

# Sayori Hug CG
image s_cg3:
    "images/cg/s_cg3.png"

# Sayori Suicide CG

# Sayori Room BG (Normal Lighting)
image s_kill_bg:
    subpixel True
    "images/cg/s_kill_bg.png"

# Sayori Hanging Sprite
image s_kill:
    subpixel True
    "images/cg/s_kill.png"

# Glitch Lighting
image s_kill_bg2:
    subpixel True
    "images/cg/s_kill_bg2.png"

# Glitch Lighting with Sayori Hanging Sprite
image s_kill2:
    subpixel True
    "images/cg/s_kill2.png"

# Yuri Stab CG
# This is displayed using a ConditionSwitch to switch between
# different Yuri stab images
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

# Animations for Sayori Hanging CG
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

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

image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

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
