# discord_rpc.py
# This file sets up Discord Rich Presence into your mod.
# This requires that pypresence exists on your mod.

## BEFORE STARTING READ THIS.
## To make RPC work for you, make a new application on Discord's Developer Portal
## https://discord.com/developers/applications
## Follow the comments below in order to setup RPC assets and defining this in DDLC.

init -960:
    define discord.client_id = "979471077187125248"
    default persistent.enable_discord = True

    default discord.discord_rpc_save_state = {}

define config.quit_callbacks += [stop_discord] 
define config.after_load_callbacks += [RPC.update_status_info]

init -950 python in discord:
    from pypresence import Presence
    from store import config, NoRollback
    import time
    import json

    discord_json_path = config.basedir + "/discord_rpc_data.json"

    class DiscordRPC(NoRollback):
        def __init__(self, client_id):
            ## DO NOT TOUCH THIS
            self.client_id = str(client_id)

            ## You may touch this. All values MUST be strings.

            # Details indicates what the player is doing ATM
            # Example: In Main Menu
            self.details = renpy.version()

            # State indicates additional information to details
            # Example: Browsing Settings
            self.state = "Monika Is Watching You Code"

            # Defines the largest image to use in rich presence as the
            # main icon.
            self.large_img = "ddlcmodtemplatelogo"

            # Defines the text when a user hovers on the large icon in
            # a players' status.
            # Example: DDLC Mod Template
            self.large_txt = config.name  # Uses the name of the mod defined in-game.

            # Defines the smallest image to use in rich presence as the
            # secondary icon.
            self.small_img = "test"
            # Defines the text when a user hovers on the small icon in
            # a players' status.
            self.small_txt = config.version  # Uses the version name of the mod

            ## DO NOT TOUCH THIS EITHER
            self.start_time = time.time()
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.update_rpc()
        
        def exit(self):
            self.rpc.close()
            print("SUCCESS: Disconnected from Discord.")

        def update_status_info(self):
            p = discord_rpc_save_state

            self.state = p['state']
            self.details = p['details']
            self.large_img = p['large_img']
            self.large_txt = p['large_txt']
            self.small_img = p['small_img']
            self.small_txt = p['small_txt']
            
            self.update_rpc()
        
        def update_rpc(self):
            self.rpc.update(
                state=self.state,
                details=self.details,
                start=self.start_time,
                large_image=self.large_img,
                large_text=self.large_txt,
                small_image=self.small_img,
                small_text=self.small_txt,
            )

init -940 python:
    from pypresence import DiscordNotFound, DiscordError
    import json

    RPC = None

    def start_discord():
        global RPC
        print("Processing Discord RPC Transaction...")
        try:
            RPC = discord.DiscordRPC(discord.client_id)
            print("SUCCESS: Connected to Discord.")
        except DiscordNotFound:
            print("FAILURE: Cannot find Discord running on the PC. Disabling RPC.")
            RPC = None
        except DiscordError:
            print("FAILURE: Failure when processing RPC transaction. Disabling RPC.")
            RPC = None
    
    def stop_discord():
        global RPC
        if RPC is None: 
            print("Discord RPC is not active. Exiting 'stop_discord'.")
            return
        RPC.exit()
        RPC = None

    def update_discord(state, details, large_img=None, large_txt=None, small_img=None, small_txt=None):
        global RPC
        if RPC is None: 
            print("Discord RPC is not active. Exiting 'updatediscord'.")
            return
        
        discord.discord_rpc_save_state = {
            "state": state,
            "details": details,
            "large_img": str(large_img) if large_img else RPC.large_img,
            "large_txt": large_txt if large_txt else RPC.large_txt,
            "small_img": str(small_img) if small_img else RPC.small_img,
            "small_txt": small_txt if small_txt else RPC.small_txt,
        }
        
        RPC.update_status_info()

    if persistent.enable_discord:
        start_discord()
