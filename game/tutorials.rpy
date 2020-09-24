## Tutorials.rpy
# This file isn't needed for DDLC modding and is just part of the tutorial
# of the DDLC Mod Template. BETA

init python:

    items = [
        (_("Introduction"),"example_chapter"),
        (_("Route Part 1, How To Make A Mod"),"tutorial_route_p1"),
        (_("Route Part 2, Music"),"tutorial_route_p2"),
        (_("Route Part 3, Scene"),"tutorial_route_p3"),
        (_("Route Part 4, Dialogue"),"tutorial_route_p4"),
        (_("Route Part 5, Menu"),"tutorial_route_p5"),
        (_("Route Part 6, Logic Statement"),"tutorial_route_p6"),
        (_("Route Part 7, Sprite"),"tutorial_route_p7"),
        (_("Route Part 8, Position"),"tutorial_route_p8"),
        (_("Route Part 9, Ending"),"tutorial_route_p9"),
        (_("Advanced Settings"),"tutorial_route_adv")
    ]

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)

define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#000"
define gui.tutorial_button_text_hover_color = "#fa9"

style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []

screen tutorial_choice(items):
    style_prefix "tutorial"
    fixed:
        area (125, 40, 600, 450)
        bar adjustment adj style "vscrollbar" xalign -0.05

        viewport:
            yadjustment adj
            mousewheel True
            has vbox

            for i_caption,i_label in items:
                textbutton i_caption:
                    action Return(i_label)

            null height 20
            textbutton _("That's enough for now.") action Return(False)

label tutorial_selection:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t3

label tutorial_selection_menu:
    $ ca = renpy.random.randint(1,4)
    if ca == 1:
        show sayori 4a at tcommon(950)
    elif ca == 2:
        show natsuki 5a at tcommon(950)
    elif ca == 3:
        show yuri 1a at tcommon(950)
    else:
        show monika 2a at tcommon(950)
    window show
    $ mc(_("What should I learn today?"), interact=False)
    call screen tutorial_choice(items)
    window auto
    if _return == False:
        jump end_tutorial
    call expression _return from _call_expression
    scene bg club_day
    with wipeleft_scene
    jump tutorial_selection_menu



label end_tutorial:
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show monika 4a zorder 2 at t11
    m "I hope we managed to teach you something!"
    m "If you need more help, we'll be here or in the DDMC Discord."
    m 4b "I look forward to seeing your mods."
    m 5a "Until next time!"
    with dissolve
    return

label tutorial_route_p1:
    scene bg club_day
    with wipeleft_scene
    show monika 2a zorder 2 at t11
    m "Making a mod for the first time requires that you get a idea to type down."
    m "When you have the plot of your mod ready, it's time to add that to the game!"
    m "Let's do that right now."
    m "First of all, I suggest you get a coding application."
    m "Editra...sucks and it can corrupt your mod files making you lose progress."
    m "I recommend Visual Studio Code (VSC) to code your mod. It's available on Windows, Mac and Linux via {i}code.visualstudio.com/download{/i}."
    m "Alternatively, if you want something on the go or lighter, you can use Notepad++ from {i}notepad-plus-plus.org/downloads/{/i}."
    m "In this part, it is mostly VSC Based so you can skip if you are using Notepad++ or another coding app."
    menu:
        "Pick which coding program you will be using."
        "Visual Studio Code":
            $ persistent.vsc = True
            m "Alright then."
            m "Download Visual Studio Code and install it."
            m "Once it's installed, launch it and find a box on the left bar."
            m "Click it and search {i}Renpy{/i} and click the green install button below the result."
            m "Afterwards, go to File, Open Folder, then go inside {i}renpy-6.99.12.4-sdk{/i} folder, then go inside your mod folder and click the {i}game{/i} folder once. Afterwards, click Open."
        "Notepad++ or another program":
            $ persistent.vsc = False
            m "Alright then."
            m "Do note that you will have to access your mod folder from your chosen program."
            m "Some may have it built in but go into the Ren'Py Launcher, select your mod name and click the game folder under Open Directory."
    m "Now you are inside your mod's game folder."
    m "Now let's make our first script!"
    if persistent.vsc:
        m "Hover over where it say's game and click the file icon with a + symbol."
        m "Now name the file {i}Chapter1{/i} but do add {i}.rpy{/i} at the end and hit enter."
        m "It should look like this. \n{i}chapter1.rpy{/i}"
    else:
        m "Go into your Ren'Py Launcher and click Navigate Script."
        m "Then scroll all the way down in the files tab till you see {i}+ Add Script File{/i}."
        m "Click that and name your file {i}chapter1{/i}."
    m "Now open {i}script.rpy{/i} and go down to Lines 42-45 and replace them with {i}call Chapter1{/i}."
    m "You might have noticed that the code you replaced had 8 lines spaced together."
    m "In Ren'Py and Python spaces are very important so make sure you space them properly."
    m "If not you will get a error and will have to add more or less spaces."
    m "Do not press the tab button when scripting because Ren'Py hates tabs."
    m "Now open the file you made with either VSC or your chosen program."
    m "In it type {i}label Chapter1:{/i}"
    m "Press enter, and type {i}return{/i}."
    m "Afterwards go to File and click Save."
    m "You made your first script!"
    m 4i "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."
    m 1a "In a book, each chapter are followed one after another. Chapter 2 is written after chapter 2 and so on. But in Ren'Py this is different."
    m "The order isn't determined by the place of each chapter in the scripts but by the keywords {i}label{/i}, {i}call{/i} and {i}jump{/i}"
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is {i}start{/i}. Then the game reads and executes what is inside the block under the label {i}start{/i}."
    m "When it reaches the keyword {i}call{/i} or {i}jump{/i}, the game proceeds to the chapter whose label followed the keyword."
    m 2b "In the case of our mod, when the game reads {i}call chapter1{/i} it jumps to the chapter labeled {i}chapter1{/i}."
    m 4b "The chapter {i}chapter1{/i} is defined in the file we created, chapter1.rpy. But as you can see, there is nothing inside it except from {i}return{/i}."
    m "The keyword 'return' makes the game goes back to the latest chapter that was accessed through 'call'. If it doesn't exist, the game goes back to the main menu."
    m 4a "If you try to play the mod, you’ll see nothing when you click New Game. That’s because the game returns to the main menu as soon as it jumps to {i}chapter1{/i}."
    m 1e "Okay! Let’s stop here for now. I hope I didn’t overwhelm you with information..."
    m "In the next section, we will add some dialogue to it so don't worry on how it looks right now."
    m "If you get a error, try replaying this lesson to see what you did wrong or open {i}tutorialpart1.txt{/i} in {i}tutorial_route_answer{/i}."
    m "If that fails, hop onto the DDMC Discord and ask for help in {i}#mod_help{/i}."
    m "That's all for this section! When you are ready, begin the second part! We'll be waiting!"
    return

label tutorial_route_p2:
    scene bg club_day
    with wipeleft_scene
    show natsuki 4a zorder 2 at t11
    n "Hi [player]!"
    n 5a "If the last part was a bit too hard, don't worry, this part is easier."
    n "Like last time, I'll tell you what to do and then I'll explain, okay?"
    n 4a "First open {i}chapter1.rpy{/i}."
    n "Between the first line and {i}return{/i} add the line {i}stop music fadeout 2.0{/i}."
    n "Then add the line {i}play music t2{/i}."
    n "Finally, add the line {i}mc \"Let's listen to the music.\"{/i}"
    n 2a "Check that all lines below {i}label chapter1:{/i} are aligned properly and that {i}return{/i} is the last line of the script."
    n "Try to launch the game with Ren'Py and see what happens..."
    n 2c "..."
    n 1c "Does it work? If everything goes well, you should be listening to Sayori's main theme."
    n 2a "There's just one dialogue, so if you click one time, you go to the main menu because of {i}return{/i}."
    n 2d "Okay, time to explain what happened!"
    n 5c "Let's look at {i}stop music fadeout 2.0{/i} first. Before you click New Game, you can hear the main menu music, right?"
    n "But when you click New Game, the music stops progressively."
    n 5a "That's due to {i}stop music fadeout 2.0{/i}. {i}stop music{/i} tells the current music to stop. {i}fadeout 2.0{/i} makes it so the current music completely becomes silent in 2 seconds."
    n 4t "{i}fadeout{/i} isn't necessary but smooth transitions are much more pleasant, aren't they?"
    n 5a "The next line {i}play music t2{/i} tells the game to play the music named {i}t2{/i}. You're surely wondering what {i}t2{/i} is. {i}t2{/i} refers to Sayori theme, 'Ohayou Sayori!'."
    n 2a "Besides Ohayou Sayori, there are many other songs. But each one is labeled by their own nickname."
    n "You can see the list of every music with their nickname in {i}definitions.rpy{/i} and the respective names and descriptions of said songs."
    n "You can find {i}definitions.rpy{/i} inside the game folder which should be in the Mod Template's directory."
    n "Try finding it and then open it."
    n "Find the lines beginning with {i}define audio{/i}. This is where each music gets assigned a nickname."
    n "For example, in the case of the main theme, its nickname is {i}t1{/i}. In the case of My Confession, its nickname is {i}t10{/i}."
    n 5k "Can you now guess what happens if you type {i}play music t10{/i} instead of {i}play music t2{/i}?"
    n 5d "My Confession is played instead of Ohayou Sayori!"
    n 2a "Instead of using a nickname, you can directly type the path of the music."
    n "Try writing {i}play music '<loop 4.499>bgm/2.ogg'{/i} instead of {i}play music t2{/i}."
    n 2d "See? Ohayou Sayori! is played. Try one last thing for me okay? type {i}<from 50.0>bgm/credits.ogg'{/i} instead of {i}<loop 4.499>bgm/2.ogg'{/i}."
    n 5a "Have you already heard this song?"
    n 5t "This is the song that plays at the end of the game. I don't know who made it, but I guess it sounds catchy."
    n 5a "The last line you wrote, {i}mc \"Let's listen to the music\"{/i} makes the main character say {i}Let's listen to the music.{/i}. I'll explain how dialogue works later, so bear with me okay?"
    n 1a "Alright, before finishing this tutorial, replace {i}play <from 50.0>bgm/credits.ogg'{/i} with {i}play music t2{/i}."
    n "Verify you wrote exactly the same lines as in the file {i}tutorialpart2.txt{/i} which is inside {i}tutorial_route_answer{/i}."
    n 1d "Congratulations! You now know how to stop and play music~"
    n 5a "In the next section, you will learn see how to add a background."
    m "See you soon!"
    return

label tutorial_route_p3:
    scene bg club_day
    with wipeleft_scene
    show sayori 1x zorder 2 at t11
    s "Hi [player]! Are you ready for the next tutorial?"
    s 1a "Last time, you added music to our mod but as you saw, the background was nothing but black and white squares."
    s 1q "So let's add a background! It's going to be quick and easy."
    s 2c "Like last time, open {i}chapter1.rpy{/i}."
    s "Add between {i}play music t2{/i} and {i}mc \"Let's listen to the music.\"{/i} {i}scene bg residential_day{/i}."
    s "Then add another line {i}with dissolve_scene_full{/i}. Once again, verify that everything below {i}label chapter1.rpy:{/i} is aligned."
    s 3a "Open Ren'Py and play the game and..."
    s 4x "There's a neat background!"
    s 1b "Can you recognize it? It's the first scene you saw when you played the game."
    s "Let me explain {i}scene bg residential_day{/i}. The keyword {i}scene{/i} tells the game to load the scene, {i}bg{/i} tells it is a background, and {i}residential_day{/i}, the name of the scene."
    s "You can find what exactly {i}residential_day{/i} is in {i}definitions.rpy{/i}, the same script we looked at last tutorial."
    s 1c "Try to find {i}image bg{/i}."
    s 1b "Can you see the list of backgrounds? Like it was the case for music, each background has a nickname assigned. For example, {i}\"g/sayori_bedroom.png\"{/i} is referenced by {i}sayori_bedroon{/i}."
    s 1c "Go back to chapter1.rpy and replace {i}scene bg residential_day{/i} with {i}scene bg sayori_bedroom{/i}. Can you guess what happens?"
    s 4a "The background is now my bedroom!"
    s 4c "Now time for me to explain {i}with dissolve_scene_full{/i}. This basically dissolves the scene progressively into the next scene."
    s 1c "Remember the last tutorial and how the scene was a bit abrupt? If you don't add {i}with dissolve_scene_full{/i}, the transition would be immediate."
    s 5a "That would be a bit unpleasant, wouldn't it?"
    s 3l "That's why we add {i}with dissolve_scene_full{/i}. With this additional line, the scene changes to another smoothly."
    s 2x "There are other types of transition such as {i}wipeleft_scene{/i}. Try replacing {i}with dissolve_scene_full{/i} with {i}with wipeleft_scene{/i}."
    s 1b "Can you see the difference? {i}dissolve_scene_full{/i}, {i}dissolve_scene_half{/i}, and {i}wipeleft_scene{/i} are the common transitions used in DDLC so if you can understand them, you're good to go!"
    s "Before doing the next tutorial, let's add back {i}scene bg residential_day{/i} and {i}with dissolve_scene_full{/i}."
    s "Check if you wrote it perfectly in {i}tutorialpart3.txt{/i} inside of {i}tutorial_route_answer{/i}"
    s 1b "Okay! We're almost there! You'll soon know enough for a kinetic novel-like mod."
    s 4x "See you soon [player]!"
    return

label tutorial_route_p4:
    scene bg club_day
    with wipeleft_scene
    show yuri 1a zorder 2 at t11
    y "Hi, [player]~"
    y "Today, I'm going to teach you how to make dialogue in Ren'Py."
    y 3q "Although you already know, don't you? You already wrote dialogue after all."
    y "First, open {i}chapter1.rpy{/i} and replace {i}mc \"Let's listen to the music.\"{/i} with \n{i}mc \"It has been four days since I joined the Literature Club and I finally decided to confess my feelings to Monika.{/i}."
    y 1a "Save the file and launch the game."
    y 3q "As you surely expected, the main character now says {i}It has been four days since I joined the Literature Club and I finally decided to confess my feelings to Yuri.{/i}."
    y "Let's look at what you wrote. {i}mc{/i} is a nickname for you, the player. By writing {i}mc{/i} before the sentence, the character speaking will be you."
    y "Try replacing the line you wrote with {i}n \"Just think of Monika from now on.\"{/i}."
    y 2e "..."
    y 2c "See? Natsuki now tells you what you should have been doing since the beginning."
    y 1a "Now instead of writing {i}n \"Just think of Monika from now on.\"{/i} type {i}y \"Natsuki and I are too unformal for someone as wonderful as you.\"{/i}"
    y "Play the game and as you can see..."
    y 3d "Now it's Monika who finally realized that I'm the best one for you."
    y 3n "Oh! We drifted a bit...So I was saying that you need to specify two things to type a dialogue in Ren'Py."
    y 3a "First you need to specify who is speaking. You can do it with the keywords {i}mc{/i}, {i}y{/i}, {i}n{/i}, {i}s{/i} and {i}m{/i}. I'm sure you can guess who is who."
    y "Instead of using keyword, you can directly type the name of the person speaking. For example, try writing {i} \"Player\" \"Is this just me writing a diary?\"{/i}."
    y 2f "Did you do it?"
    y "You got the same result if you were using {i}mc{/i} instead."
    y 2a "Besides the name of the speaker, you need to type the sentence they will say. The sentence should be between quotation marks."
    y 1j "One last thing. If you want to type special characters such as {i}\\{/i} or {i}\"{/i} in a sentence, you need to put {i}\\{/i} before them."
    y 1d "Alright, that's all for dialogue!"
    y 1b "Pretty simple, right? Ren'Py was made so that anyone can make visual novel after all. Even beginners like us can pick it up quickly."
    y 1a "Before you save the file, replace the line of dialogue back to {i}mc \"It has been four days since I joined the Literature Club and I finally decided to confess my feelings to Yuri.\"{/i}."
    y "Like usual, check that chapter1.rpy is exactly like {i}tutorialpart4.txt{/i} inside the {i}tutorial_route_answer{/i} folder."
    y 1a "Okay [player]! You now know how to make a scene, add music, and make dialogue. The only things missing are character pictures and choices."
    y "You'll see how to make choices in the next tutorial."
    y 3q "The recent tutorials have been pretty easy so far but the next one will be harder."
    y 3d "See you soon!"
    return

label tutorial_route_p5:
    scene bg club_day
    with wipeleft_scene
    show monika 4a zorder 2 at t11
    m "In this lesson, I'll explain how to make choices."
    m "For example..."
    call tutorial_route_p5_favorite_color
    m 3a "As you can see, I gave you several choices and you picked one of them."
    m "That's what I'm going to teach you."
    m 4a "Like every time, open {i}chapter1.rpy{/i} and between {i}return{/i} and the last line before it, add {i}menu:{/i}"
    if persistent.vsc:
        m "Press enter then add {i}mc \"I told her to meet me...\"{/i}."
        m "Type just under that {i}\"At the literature club room\":{/i} press enter and then {i}$ meeting_place = \"club_room\"{/i}"
        m 4b "Next, press enter and press backspace once then type {i}\"In front of my house\":{/i} and under it {i}$ meeting_place = \"my_house\"{/i}"
    else:
        m "Press enter then add 4 spaces then {i}mc \"I told her to meet me...\"{/i}."
        m "Type just under that with 4 spaces {i}\"At the literature club room\":{/i} press enter and then add 4 spaces and {i}$ meeting_place = \"club_room\"{/i}"
        m 4b "Next, press enter and press backspace once then type {i}\"In front of my house\":{/i} and under it add 4 spaces then {i}$ meeting_place = \"my_house\"{/i}"
    m 4a "Finally, press enter and press backspace twice then add {i}mc \"I can't wait to meet her!\"{/i}."
    m 2a "Try to play the game."
    m "If it doesn't work, there is surely an indentation error."
    m 5a "I can't help you from here, but you can check {i}tutorialpart5.txt{/i} for the answers. You know where it is, right?"
    m 4b "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, {i}I told her to meet me...{/i}."
    m "You can specify who says this sentence by adding a nickname like {i}mc{/i} before it. It's just like a dialogue. What's important is that this sentence is written before any choice."
    m 3a "Contrary to the explanative sentence, the choices mustn't be preceded by a nickname. They should be enclosed in quotation marks. Just after the closing quotation mark, there must be a {i}:{/i}."
    m "After {i}:{/i} the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."
    m 3b "I'll give more explanation about the meaning of indents in the next tutorial."
    m 3a "In our case, the next line after the first choice is {i}$ meeting_place = \"club_room\"{/i}."
    m 2a "Take a good look at this line."
    m 3b "Until now, I referred {i}mc{/i} {i}residential{/i} and {i}t2{/i} as nickname. But that's not really the correct word. They are actually what we call a variable."
    m "Variables in coding is a very important concept. They have many forms and do many things. They can be \"nicknames\" or they can be numbers or more complicated structures."
    m 1a "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what's necessary to make a DDLC mod, okay?"
    m 1c "I myself don't know Python and Ren'Py all that well after all..."
    m 3a "{i}meeting_place{/i} is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): {i}club_room{/i}."
    m "It's default value is None which means it doesn't exist."
    m 3e "Hold on a second? How can it not exist, you say?"
    m 1a "Well before you define it, the variable doesn't exist. But if you later try to use it, for example in a conditional statement, the variable will be \"created\" and it's value will be {i}None{/i}."
    m "It's alright if you don't understand it yet. {i}Variables{/i} {i}conditional statements{/i} and {i}None{/i} will become clearer in my next lecture."
    m 4b "Let's go back to the meaning of {i}$ meeting_place = \"club_room\"{/i}. Here we created the variable {i}meeting_place{/i} and assigned it the string {i}club_room{/i}."
    m 4m "The {i}${/i} in front of it is to tell Ren'Py the line is a Python line. Um..., I can't really explain why we need to do that if you don't know Python yet..."
    m 4a "Just remember that you need to add {i}${/i} when you want to assign a variable a value that way."
    m "Regarding the second choice, the structure is the same. The only difference is that the value of {i}meeting_place{/i} will be {i}my_house{/i} if the player selects the second choice."
    m "After the second choice, the game executes the line {i}mc \"I can't wait to meet her!\"{/i}."
    m 1a "For now it doesn't look like the choices did anything. But we actually assigned {i}meeting_place{/i} to either {i}club_room{/i} or {i}my_house{/i}."
    m 3a "We have to wait until the next tutorial to see how we can use the variable {i}meeting_place{/i}."
    m 3b "Alright, I'm sorry to leave hanging like that I believe we need to take a little break."
    m "If you want though, I would more than happy to begin the next part right away!"
    m 5a "Just click Part 6!"
    return

label tutorial_route_p5_favorite_color:
    menu:
        m "What is your favorite color?"
        "Sky Blue":
            return
        "Amethyst Purple":
            return
        "Emerald Green":
            return
        "Candy Pink":
            return
            m "Are you ready? We are going to ramp up the difficulty."

label tutorial_route_p6:
    scene bg club_day
    with wipeleft_scene
    show monika 5a zorder 2 at t11
    m "Yeah, you came back [player]!"
    m "Glad to see you didn't run away on me. Ahaha!"
    m 1e "I was afraid the last tutorial was a bit too hard..."
    m 1m "Well, this one is going to be hard as well but..."
    m 1b "Hang it there okay? We did the hardest part already!"
    m 1a "Last time we saw how to add menu and how to assign variable a value."
    m 1b "Let's see how we can use these variables!"
    m 2a "You know the drill, open {i}chapter1.rpy{/i} and at the end of the file, just before {i}return{/i}..."
    m 4a "Add the following lines {i}if meeting_place == \"club_room\":{/i}"
    if persistent.vsc:
        m "Then add {i}scene bg club_day{/i} press enter then add {i}with wipeleft_scene{/i}"
        m "Press backspace once then add {i}elif meeting_place == \"my_house\":{/i} press enter add {i}scene bg house{/i}"
    else:
        m "Then add 4 spaces {i}scene bg club_day{/i} press enter then add {i}with wipeleft_scene{/i}"
        m "Press backspace once then add {i}elif meeting_place == \"my_house\":{/i} press enter, add 4 spaces again and {i}scene bg house{/i}"
    m "Press enter again and add {i}with wipeleft_scene{/i} press enter then backspace once and add {i}stop music fadeout 2.0{/i} press enter and add {i}play music t2{/i}"
    m "Finally, press enter and add {i}mc \"She is already waiting for me when I arrive.\"{/i}"
    m 2a "Save the file and try to play the game."
    m 5a "If it doesn't work, you know where you can see the answer, don't you?"
    m 2a "You already know how scene, transition, music and dialogue work so I won't go over it again."
    m 4b "It's not like I don't want spend more time with you but you know, ... I'm excited to finish my route too!"
    m 4a "Okay, so the new thing is the {i}if{/i} statement. We call that a conditional statement. It's an elementary and essential operation in programming."
    m "It goes basically like this: IF something is true THEN something happens. In our case, if the meeting place is {i}club_room{/i} then the scene changes to the clubroom."
    m 3a "Otherwise, if the meeting place is {i}my_house{/i} then the scene changes to the main character's house."
    m 3b "It seems simple, right?"
    m 3a "The syntax must be as follow: first, there must be a {i}if{/i} followed by an equality which is either {i}True{/i} or {i}False{/i}. For example, {i}meeting_place == \"club_room\"{/i}."
    m "If {i}meeting_place{/i} was assigned {i}club_room{/i} before then the equality returns {i}True{/i}. Otherwise, its returns {i}False{/i}."
    m "If the equality returns {i}True{/i} then the game will read the lines belonging to the {i}if{/i} block."
    m 4a "You can see where those lines are because they have one more indent compared to the if statement preceding them."
    m 4b "We once again meet the system of indent and block. This is one of the property of Python and Ren'Py. Let's do a quick exercise."
    m "Can you see difference between:"
    m 2a "{i}if meeting_place == \"club_room\":{/i}   \n{i}        scene bg club_day{/i} \n{i}        mc \"We will meet at the club room.\"{/i}"
    m "And {i}if meeting_place == \"club_room\":{/i}   \n{i}        scene bg club_day{/i}\n{i}mc \"We will meet at the club room.\"{/i}"
    m 4b "In the first case, the main character only says they will meet at the club room if {i}meeting_place{/i} is equal to {i}club_room{/i}."
    m "In the second case, he will say it no matter the value of {i}meeting_place{/i}."
    m 3a "You can see once again how important indentations are in Python."
    m 4b "About the second comparison, {i}elif meeting_place == \"my_house\"{/i}, note that we use {i}elif{/i} at the beginning instead of {i}if{/i}."
    m 4a "The difference between {i}elif{/i} and {i}if{/i} is subtle. First, you can only use {i}elif{/i} after you already wrote {i}if{/i}."
    m "Second, the statement following {i}elif{/i} won't be evaluated if the previous if statement was {i}True{/i}. Other than that, {i}elif{/i} works like {i}if{/i}."
    m 1b "Well, in our case it doesn't matter because if {i}meeting_place{/i} is {i}club_room{/i} then {i}meeting_place{/i} cannot be {i}my_house{/i} at the same time."
    m 1a "It would matter if it was something like..."
    m "{i}if monika_affection_points > 10:{/i} \n{i}        scene bg house{/i} \n{i}if monika_affection_points > 6:{/i}   \n{i}        scene club_day{/i}"
    m 3a "In that case, if {i}monika_affection_points{/i} is higher than 10, the new scene wouldn't be the house but the club because the game will evaluate both if."
    m 4b "To avoid that, {i}elif{/i} should be used instead of {i}if{/i}."
    m 4a "Besides {i}if{/i} and {i}elif{/i}, there's also the keyword {i}else{/i}. Like {i}elif{/i}, {i}else{/i} can be used after a {i}if{/i}. The block under {i}else{/i} will be executed if the previous {i}if{/i} or {i}elif{/i} statements are {i}False{/i}."
    m 2a "For example..."
    m "{i}if meeting_place == \"club_room\":{/i} \n{i}        scene bg club_day{/i} \n{i}else:{/i}   \n{i}scene club_day{/i}."
    m 1a "Well, there are more things to say about conditional statement..."
    m "For example about the keywords {i}and{/i} and {i}or{/i}..."
    m 3a "But let's keep that for another time. I'm sure you can find more tutorial on Python and conditional statement."
    m 1b "For now, let's move on! It's about time we add character pictures into the game!"
    m 5a "See you later [player]!"
    return

label tutorial_route_p7:
    scene bg club_day
    with wipeleft_scene
    show monika 5a zorder 2 at t11
    m "Hi [player]!"
    m "It's about time we add character pictures, don't you think?"
    m 1b "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."
    m "In DDLC, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."
    m 1e "So each character has about 900 combinations! That seems a lot but...when you're actually inside the game, the lack of freedom becomes horribly frustrating..."
    m 1f "I really wish I could show you different expressions, poses and clothes but unfortunately, I can't add myself new artwork to the game..."
    m 5a "If you're an artist, I would really love it if you could add me more sprites!"
    m 2a "For our mod, we'll only use existing art."
    m 4b "Let's dot it!"
    m "Open {i}chapter1.rpy{/i} and before {i}return{/i} type {i}show monika 1b at t11 zorder 2{/i}"
    m "Then type {i}m \"Hi [player]!\"{/i} press enter then type {i}mc \"You're already here? I hope I didn't make you wait for too long.\"{/i}"
    m "Once again press enter and type {i}m 2a \"Don't worry, it's me who's early.\"{/i} then press enter and type {i}show monika 5a at f11 zorder 3{/i}."
    m 2a "Save, play the mod, and check tutorialpart7.txt if there's an error."
    m 4b "Alright! The only new things are {i}show monika 1b at t11 zorder 2{/i} and {i}m 2a{/i}."
    m 4a "First, let's go over {i}show monika 1b at t11 zorder 2{/i}."
    m "The keyword {i}show{/i} shows the sprite of the character named {i}monika{/i}, with her pose {i}1{/i} and her expression {i}b{/i}."
    m " The keyword 'at' specifies the position of the sprite. In the line above, the position is 't11'. 'zorder' has something to do with layers."
    m 3b "I'll explain how positions and layers work in the next tutorial. For now, let's focus on the poses and expressions of sprite."
    m 4a "Obviously, the variable {i}monika{/i} refers to me. Naturally, {i}yuri{/i} refers to Yuri and so on."
    m "If you type {i}show yuri 1b at f11 zorder 3{/i} instead of {i}show monika 1b at f11 zorder 3{/i}, it's Yuri who will appear."
    m 4k "Of course, you only have eyes for me so let's not bother with the sprites of the other girls, ahaha!"
    m 5a "In my case, I have 5 different poses. I will show them to you one by one now."
    m 1a "This is my first pose."
    m 2a "This is my second pose."
    m 3a "This is my third pose."
    m 4a "This is my fourth pose."
    m 5a "This my fifth pose."
    m 1a "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from {i}a{/i} to {i}r{/i}. I will show them one by one."
    m 4a "Expression a."
    m 4b "Expression b."
    m 4c "Expression c"
    m 4d "Expression d."
    m 4e "Expression e."
    m 4f "Expression f."
    m 4g "Expression g."
    m 4h "Expression g."
    m 4i "Expression i."
    m 4j "Expression j."
    m 4k "Expression k."
    m 4l "Expression l."
    m 4m "Expression m."
    m 4n "Expression n."
    m 4o "Expression o."
    m 4p "Expression p."
    m 4q "Expression q."
    m 4r "Expression r."
    m 4a "You can find my list of expressions in the DDMC Community Drive on the Reddit or {i}#mod_faq{/i} on the DDMC Discord."
    m 1b "I hope you will quickly memorize them perfectly!"
    m 3a "You can also find my and everyone elses poses and my expressions in definitions.rpy."
    m "My fifth pose only has the expressions a and b."
    m 5a "Like this."
    m 5b "And this."
    m 4a "My other poses have all expressions though."
    m 1b "Okay! In short, to show a sprite, you need to type {i}show monika pose expression at t11 zorder 2{/i}. Pose is either {i}1,2,3,4 or 5{/i} and expression ranges from {i}a{/i} to {i}r{/i}."
    m "If you want to show several characters, just type {i}show{/i} several times, like this:"
    m 2a "{i}show yuri 1a at t41 zorder 2{/i} {i}show sayori 1a at t42 zorder 2{/i} {i}show monika 1a at t43 zorder 2{/i} {i}show natsuki 1a at t44 zorder 2{/i}"
    m 2b "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."
    m "After a sprite is already on the screen, there's a shortcut to change her pose and expression."
    m 3a "Instead of using {i}show{/i} again and again, you can directly type the letter corresponding to the character followed by the number and the letter for their pose and expression."
    m "This is what we did in {i}m 2a \"Don't worry, it's me who's early.\"{/i}."
    m 4g "Note that the sprite of the character speaking must already be on screeen."
    m 4e "If you try for example \ny 2a \"Don't worry, it's me who's early.\", Yuri will speak but her sprite will not appear."
    m 3a "Keep in mind who's on screen and who's not at all time so as not to make a mistake."
    m 2a "...Never mind, actually just show my sprite. That way you don't have to worry about such problem. It's not like the other girls care about being shown anyway."
    m 1b "And that's all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"
    m "Next time, I'll finish explaining positions and layers."
    m 5a "See you [player]!"
    return

label tutorial_route_p8:
    scene bg club_day
    with wipeleft_scene
    show monika 5a zorder 2 at t11
    m "Welcome back to our modding club!"
    m "Last time, we learnt about how to show sprite, now let's learn how to place then."
    m 4a "Open {i}chapter1.rpy{/i} and just before..."
    m 1b "Just kidding! Actually, you don't have to add anything this time."
    m 3b "We already did it last tutorial after all."
    m 2a "So, do you remember the line {i}show monika 1b at t11 zorder 2{/i}?"
    m "I said that {i}at t11{/i} was about position and that {i}zorder 2{/i} was about layer."
    m 2b "Let's study in details what exactly that means."
    m 4b "{i}at{/i} is a keyword that tells the game to put the sprite at the position {i}t11{/i}."
    m "{i}t11{/i} is one of the position defined in DDLC. There are more than 50 positions possible."
    m 4a "You can find the list of all defined positions in the script {i}transforms.rpy{/i}. You can find it in the same folder as definitions.rpy."
    m "For now, I will explain the most common positions used in the original game."
    m 1a "Let's start with the {i}t{/i} positions. I will show them one by one."
    show monika 1a zorder 2 at t11
    m "Position t11."
    show monika 1a zorder 2 at t21
    m "Position t21."
    show monika 1a zorder 2 at t22
    m "Position t22."
    show monika 1a zorder 2 at t31
    m "Position t31."
    show monika 1a zorder 2 at t32
    m "Position t32."
    show monika 1a zorder 2 at t33
    m "Position t33."
    show monika 1a zorder 2 at t41
    m "Position t41."
    show monika 1a zorder 2 at t42
    m "Position t42."
    show monika 1a zorder 2 at t43
    m "Position t43."
    show monika 1a zorder 2 at t44
    m "Position t44."
    show monika 1a zorder 2 at t11
    m 1b "And that's all for the {i}t{/i} positions."
    m 4a "I think you guessed it already but {i}t11{/i} should be used when there's only one character."
    m "{i}t21{/i} and {i}t22{/i} should be used when there are two characters. {i}t21{/i} is for the left, {i}t22{/i} is for the right."
    m 3a "It's the same logic for {i}t31{/i},{i}t32{/i},{i}t33{/i}. {i}t31{/i} is the left, {i}t32{/i} the middle and {i}t33{/i} the right. "
    m "{i}t41{/i}, {i}t42{/i},{i}t43{/i} and {i}t44{/i} work in the same way."
    m 3b "I encourage you to try these positions yourself with several characters. After all, there's nothing better than practice to learn!"
    m 1a "If you remember well, we wrote one time {i}show yuri 1b at f11 zorder 3{/i}."
    m "Notice that the position is {i}f11{/i} instead of {i}t11{/i}. The difference is just that {i}f{/i} positions are zoomed in. {i}f{/i} stands for focused. There are as many {i}f{/i} positions as {i}t{/i} positions."
    m 4a "You should use {i}f{/i} position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who's talking."
    m 2b "Let's talk about the keyword {i}zorder{/i} now."
    m 4a "When the game renders pictures, there's an order."
    m "First, the background is rendered. Then the sprites and finally the U.I."
    m 4b "That's why the sprites are on top of the background and the U.I on top of everything."
    m 2a "As you can see, order is very important. If the game renders background last, then you won't be able to see anything else."
    m 3a "In Ren'Py the order of sprite is called {i}zorder{/i}."
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."
    m 4b "Try writing the following lines instead of {i}show monika 1b at t11 zorder 2{/i}"
    m 4a "{i}show monika 1a at t41 zorder 4{/i}"
    m "{i}show yuri 1a at t42 zorder 3{/i}"
    m "{i}show natsuki 1a at t43 zorder 2{/i}"
    m "{i}show sayori 1a at t44 zorder 1{/i}"
    m 1a "Play the game and..."
    m 1b "Everyone is here!"
    m 3a "But that's not the point. Pay attention to who's on top on who."
    m "If you look closely, you can see the rendering order is like this : {i}monika > yuri > natsuki > sayori{/i}."
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."
    m 4a "If the zorder of two sprites are the same then the last sprite shown by {i}show{/i} will be on top."
    m 2b "Well, most of the time, you don't have to worry about {i}zorder{/i}."
    m 1b "Alright! That ends this tutorial!"
    m 1a "Verify you reverted the changes you made to {i}chapter1.rpy{/i}. It should be like {i}tutorialpart8.txt{/i}."
    m 1c "There is one more tutorial. I'm very happy we almost finished our first mod but..."
    m 1f "It also means we'll soon get split up..."
    m 1g "..."
    m 1m "Or maybe not..."
    m 5a "See you later."
    return

label tutorial_route_p9:
    scene bg club_day
    with wipeleft_scene
    show monika 5a zorder 2 at t11
    m "This it it, [player], today is the day we finally make my route!"
    m "Are you ready?"
    m 3b "Be careful, we need to add a lot of lines this time."
    m 4a "Open {i}chapter1.rpy{/i} and before the last {i}return{/i} press enter and add {i}menu:{/i}"
    if persistent.vsc:
        m "Press enter and add {i}mc \"Right. Monika...\"{/i} enter again {i}\"I love you! Please go out with me!\":{/i}"
        m "Press enter and add {i}jump Chapter1_normal_ending{/i} enter again, backspace once then {i}\"You are everything for me! Please marry me!\":{/i}"
        m "Finally enter again and add {i}jump Chapter1_good_ending{/i}"
    else:
        m "Press enter and add 4 spaces and {i}mc \"Right. Monika...\"{/i}, enter again {i}\"I love you! Please go out with me!\":{/i}"
        m "Press enter and add 4 spaces and {i}jump Chapter1_normal_ending{/i} enter again, backspace once then {i}\"You are everything for me! Please marry me!\":{/i}"
        m "Finally enter again and add 4 spaces and {i}jump Chapter1_good_ending{/i}"
    m 2b "This is it for the {i}label chapter1{/i}. Now we need to add two more labels: {i}Chapter1_normal_ending{/i} and {i}Chapter1_good_ending{/i}."
    m 4a "After {i}return{/i} press enter and backspace once and type {i}label Chapter1_good_ending:{/i}"
    if persistent.vsc:
        m 4a "Press enter and add {i}scene dark{/i} enter, then {i}with dissolve_scene_full{/i} enter, then {i}mc \"She accepted my confession and we became lovers.\"{/i}"
        m "Finally enter once again {i}\"NORMAL ENDING\"{/i} and {i}return{/i}."
    else:
        m 4a "Press enter and add 4 spaces {i}scene dark{/i} enter then {i}with dissolve_scene_full{/i} enter then {i}mc \"She accepted my confession and we became lovers.\"{/i}"
        m "Finally enter once again {i}\"NORMAL ENDING\"{/i} and {i}return{/i}."
    m 1b "The normal ending is now complete. Let's do the good ending. After the last {i}return{/i} press enter and backspace once and type \"label Chapter1_good_ending:\"."
    if persistent.vsc:
        m "Press enter and add {i}scene white{/i} enter, then {i}with dissolve_scene_full{/i} enter, then {i}mc \"She gladly accepted my proposal and we got married one year later.\"{/i}"
        m "Finally enter once again {i}\"GOOD ENDING\"{/i} and {i}return{/i}."
    else:
        m "Press enter and add 4 spaces {i}scene white{/i} enter, then {i}with dissolve_scene_full{/i} enter, then {i}mc \"She gladly accepted my proposal and we got married one year later.\"{/i}"
        m "Finally enter once again {i}\"GOOD ENDING\"{/i} and {i}return{/i}."
    m 2b "Save, play the game and verify if everything works. Get both endings."
    m "If there's a problem, check {i}tutorialpart9.txt{/i} for the solution."
    m 2a "..."
    m 4b "It's not over yet. You can run the game with Ren'Py but to make it a proper mod, there's one more step: {i}Building{/i}."
    m "Open Ren'Py. Click your mod name, and then click {i}Build Distributions{/i} which should be on the right, beside Navigate Script."
    m 4a "You should see several options for Build Packages. Uncheck all of them, then check the box for {i}Ren'Py 6 DDLC Compliant Mod{/i}."
    m "You might have seen there is a {i}Ren'Py 7 DDLC Compliant Mod{/i} box too. We will be ignoring that for now as that is more complicated."
    m "You can change the name of your mod, its build name and its version in {i}options.rpy{/i}."
    m 3b "Click Build."
    m 2b "Once it's finished, you should see one folder called {i}DDLCModTemplateTwo-2.X.X-dists{/i} inside Ren'Py's directory. Open it and you should see a zip file."
    m "If you changed {i}options.rpy{/i} already you should see {i}YourModBuildName-VersionNumber-dists{/i} instead."
    m 1a "Look at the file {i}DDLCModTemplateTwo-2.X.X-Mod.zip{/i}. It's your mod. If you want to share it to other people, you should just upload this archive."
    m "Again if you already changed your mod name in {i}options.rpy{/i} you should see instead, {i}YourModBuildName-VersionNumber-Mod.zip{/i}"
    m "If you clicked {i}Ren'Py 7 DDLC Compliant Mod{/i} on accident ignore {i}DDLCModTemplateTwo-2.X.X-Renpy7Mod.zip{/i}."
    m "If you already changed your mod name in {i}options.rpy{/i} you should see instead ignore, {i}YourModBuildName-VersionNumber-Renpy7Mod.zip{/i}"
    m 2a "This way of sharing the mod is compliant to Team Salvato's Modding Guidelines. You are only sharing the new files that we made together, and nothing more."
    m 2a "Let's see if it works. Extract that zip file and make a new copy of the original Doki Doki Literature Club folder."
    m "Copy-paste the files inside {i}DDLCModTemplateTwo-2.X.X-Mod{/i} inside the new copy of the game."
    m "Once again if you changed your mod name in {i}options.rpy{/i}, it will be {i}YourModName-VersionNumber-Mod{/i}"
    m 4a "Play our mod by clicking DDLC.exe inside the new folder."
    m 4b "If everything goes well, you should be playing my new route!"
    m 1k "Congratulation! You finally did it!!"
    m "You now know how to make a mod. You now have the power to change our fate."
    m 1e "I'm counting on you [player]."
    show monika 5a zorder 2 at f11
    m 1b "I will never forget you..."
    m 1e "Bye."
    return

label tutorial_route_adv:
    # advanced scripts just because
    python:
        adv_items = [
            (_("Translating"),"tutorial_route_adv_translate")
        ]

    mc "Guess something more advanced..."

label tutorial_route_adv_repeat:
    $ ca = renpy.random.randint(1,4)
    if ca == 1:
        show sayori 4a at tcommon(950)
    elif ca == 2:
        show natsuki 5a at tcommon(950)
    elif ca == 3:
        show yuri 1a at tcommon(950)
    else:
        show monika 2a at tcommon(950)
    window show
    $ renpy.say(mc, "What should I learn today?", interact=False)

    call screen tutorial_choice(adv_items)
    window auto

    if _return == False:
        return

    call expression _return
    scene bg club_day
    with wipeleft_scene
    jump tutorial_route_adv_repeat

label tutorial_route_adv_translate:
    scene bg club_day
    with wipeleft_scene
    show monika 2b at t11
    m "Sometimes you want to add another language to your mod."
    m "Maybe it's because you are more fluent in that language or allow more players to play it."
    m 2a "Here's my advice. Use the Ren'Py Translation Feature in the Ren'Py Launcher!"
    m 2m "Others tend to translate all the script files which isn't great."
    m 2b "With Ren'Py you can add a simple toggle with your translations and release it as is!"
    m 1a "First, open up the Ren'Py Launcher and select your mod."
    m "Next find a button to the right hand side called {i}Generate Translations{/i}."
    m 1b "Click that and you will be prompted with what to call your translation folder."
    m 3b "My advice is to set it to a actual language name like Spanish and click {i}Generate Translations{/i}."
    m 1a "What this does is makes a folder in the {i}game{/i} folder called {i}tl{/i}."
    m "That is where your translating files go and it will make many sections to translate your scripts to a new language."
    m 3b "Once that is done, start coding your mod in another language."
    m "Once you finish that, go to {i}screens.rpy{/i} and go to line 968."
    m 1b "Delete the hashtag symbols from line 968 and line 972 and edit line 972 to be your language of choice."
    m "So let's say I want to translate DDLC to Korean."
    m "I would change {i}textbutton \"Spanish\" action Language(\"spanish\"){/i} to:\n {i}textbutton \"Korean\" action Language(\"korean\"){i}"
    m "The word {i}\"Spanish\"{/i} is the text visible in the settings menu for people to choose a language."
    m "{i}action Language(\"korean\"){/i} tells Ren'Py to change the language mode to the translated files in the {i}korean{/i} folder in {i}tl{/i}."
    m "I hope you got what I meant with translating your mods within Ren'Py itself."
    m "If you are confused, don't be afraid to restart this tutorial or join the r/DDLCMods Discord."
    m 5a "I can't wait to see your mod [player]!"
    m "And possibly learn another language in the process ehehe~!"
    return
