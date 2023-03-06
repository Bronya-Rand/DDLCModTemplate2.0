
## depreciated.rpy
## This file stores old code from DDLC that is now depreciated from use in
## the mod template.
## This file is temporary and may disappear in the near future.
###############################################################################

# Former Monika Console Calls
label updateconsole(text="", history=""):
    call screen dialog(message="{b}Warning{/b}\nThis feature has been depreciated. Use the following in order to\nregain this back.\n {i}$ run_input(\"[text]\", \"[history]\"){/i}."
        ok_action=Hide("dialog"))
    return

# This label adds certain text to the console history.
label updateconsolehistory(text=""):
    call screen dialog(message="{b}Warning{/b}\nThis feature has been depreciated and requires an additional argurment.\nUse the following in order to regain this back.\n {i}$ add_to_history((\"[text]\", \"output\")){/i}."
        ok_action=Hide("dialog"))
    return

# This label hides the console in-game.
label hideconsole:
    call screen dialog(message="{b}Warning{/b}\nThis feature has been depreciated. Use the following in order to\nregain this back.\n {i}hide screen console_screen{/i}."
        ok_action=Hide("dialog"))
    return