## poem_special.rpy

# This file defines the special poems that the player can see during Act 2.
# Only three poems are ever shown to the player which are selected at random
# by 'splash.rpy'.
image poem_special1 = "poem_special/poem_special1.png" # Hxppy Thoughts
image poem_special2 = "poem_special/poem_special2.png" # Can You Hear Me?
image poem_special3 = "poem_special/poem_special3.png" # Nothing is Real
image poem_special4 = "poem_special/poem_special4.png" # Cutting Memento
image poem_special5: # Stare at the dot/I love you
    "poem_special/poem_special5a.png"
    10.0
    "poem_special/poem_special5b.png"
image poem_special6 = "poem_special/poem_special6.png" # A Joke
image poem_special7a = "poem_special/poem_special7a.png" # Corrupted Monika
image poem_special7b = "poem_special/poem_special7b.png" # Corrupted Monika 2
image poem_special8 = "poem_special/poem_special8.png" # A Dream
image poem_special9 = "poem_special/poem_special9.png" # Things I Like About Papa
image poem_special10 = "poem_special/poem_special10.png" # Go to Therapy
image poem_special11 = "poem_special/poem_special11.png" # A Dream 2

# This image defines the ending poem where we can either get Monika's or Dan's
# message.
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

# This label shows the special poems the player can see during their playthrough
# of the mod. 
# To use this, use 'call poem_special(X)' where X is the poem number to show from
# the poem list above.
label poem_special(poem=1):
    $ quick_menu = False
    play sound page_turn

    if poem == 7:
        show poem_special7a as ps with Dissolve(1.0)
    else:
        show expression "poem_special" + str(poem) as ps with Dissolve(1.0)

    $ pause()

    if poem == 2:
        play sound "sfx/giggle.ogg"
    elif poem == 7:
        show poem_special7b as ps
        $ pause(0.01)

    $ quick_menu = True
    return
