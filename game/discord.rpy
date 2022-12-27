# discord.rpy
# This file sets up Discord Rich Presence into your mod.
# This requires that pypresence is installed in your mod (bundled with this template).

## BEFORE STARTING READ THIS.
## To make RPC work for you, make a new application on Discord's Developer Portal
## https://discord.com/developers/applications
## Follow the comments inside of `set_defaults` in order to setup RPC to your liking.
## To register the your RPC with your mod, scroll down to line 115.

init -960:
    default persistent.enable_discord = True
    default persistent.discord_rpc_save_state = {}

init -950 python in discord:
    from pypresence import Presence, DiscordError, DiscordNotFound
    from store import config, NoRollback, persistent
    import time
    import json

    class DiscordRPC(NoRollback):
        def __init__(self, client_id):
            self.client_id = str(client_id)
            self.start_time = time.time()
            
            self.set_defaults()
            self.auth()
            self.connect()

        # Easy method to reset stuff back to stock RPC info.
        def set_defaults(self):
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

        def auth(self):
            try:
                self.rpc = Presence(self.client_id)
            except (DiscordError, DiscordNotFound):
                self.rpc = None

        def connect(self):
            if self.rpc is None: self.auth()
            if self.rpc is None: return
            self.rpc.connect()
            self.update_rpc()

        def exit(self):
            if self.rpc is None: return
            self.rpc.close()
        
        def update_status(self, state, details, large_img=None, large_txt=None, small_img=None, small_txt=None):
            if self.rpc is None:
                return

            persistent.discord_rpc_save_state = {
                "state": state,
                "details": details,
                "large_img": str(large_img) if large_img else self.large_img,
                "large_txt": large_txt if large_txt else self.large_txt,
                "small_img": str(small_img) if small_img else self.small_img,
                "small_txt": small_txt if small_txt else self.small_txt,
            }
            
            self.update_rpc_info()

        def update_rpc_info(self):
            if self.rpc is None:
                return

            p = persistent.discord_rpc_save_state

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
    # Place your Discord RPC token inside the ""'s
    RPC = discord.DiscordRPC("979471077187125248")

    config.quit_callbacks += [RPC.exit] 
    config.after_load_callbacks += [RPC.update_rpc_info]
