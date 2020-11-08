# Explanation of the RPY files 
The '.rpy' files in the game folder are copies of important script files found in DDLC's `scripts.rpa` archive that are necessary to change for the most basic modding projects.

### **cgs.rpy**

This file contains the defintions for the CGs in the original game to be called on when needed.

### **console.rpy**

This file contains the definitions and label calls needed to prompt Monika's "Python Console" from within the game.

### **credits.rpy**

This file contains the definitions, text and label calls needed to play the credits of the game when the game is finished.

### **definitions.rpy**

This file contains the definitions and python defines to define the character's images, the background, music, variables, and story python code to execute in the game when needed.

### **effects.rpy**

This file contains the python classes, define, and definitions needed to show some different effects in the game like blood and such.

### **gui.rpy**

This file controls the definitions used for the main menu and game interface such as color, audio to be played at startup, positions of text and other inteface elements and more. This is also where the android interface code is located in to define the interface for mobile users.

### **monika.chr**, **natsuki.chr**, **sayori.chr** & **yuri.chr**

These files are in the game directory so the game can re-add the characters files to the `characters` folder when the defines in `definitions.rpy` are called to restore them.

### **options.rpy**

This file contains options that can be changed to customize your game. This file also includes the build options used when exporting your game for others to download.

### **poems_special.rpy**

This file defines the images and label calls needed to display the special poems that are prompted in Act 2 of the original game. Make sure if you add a new special poem to change line 361 to how many additional poems you added i.e. 2 new poems would make line 361 be `a = range(1,14)`.

### **poems.rpy**

This file defines the Poem class and poems that are used in the poem sharing game in the original game and the labels to show the poem to the user.

### **poemwords.txt**

This text file contains all the poem words, and points that the character likes said word to determine who's exclusive scene you get in the next day.

### **screens.rpy**

This file controls the main menu and settings interface look for images, transforms, styles and such in the original game. This should be the file you look into if you want to customize your menu to be something different.

### **script-poemgame.rpy**

This is where the game runs all the code needed to play the poem game in the original game.

### **script-poemresponses.rpy**

This is where the game runs all the code needed to play the poem sharing game in the original game. `script-poemresponses2.rpy` is mainly additional text for the game in Act 2 in response to your poems there and is located in `original_scripts`.

### **script.rpy**

This is used to call scripts and set defaults to the game on startup. It should not include any actual events or scripting; only logic and calling other labels. 
**This is the place to start for building your mod.**

### **splash.rpy**

This splash screen is the first thing that DDLC will show the player. It also defines a lot of the behavior when first loading the game, such as checking for character files and 
jumping to scenes currently in progress.

### **transforms.rpy**

This file defines the transfors and transition code used in the game to position characters, prepare a new scene with a transition effect and more.
