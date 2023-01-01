# discord.rpy
# This file sets up Discord Rich Presence into your mod.
# This requires that pypresence is installed in your mod (bundled with this template).

## BEFORE STARTING READ THIS.
## To make RPC work for you, make a new application on Discord's Developer Portal
## https://discord.com/developers/applications
## Follow the comments inside of `set_defaults` in order to setup RPC to your liking.

## Based similarly off off Lazalith's RPC code: https://github.com/Lezalith/RenPy-Discord-Presence

default persistent.enable_discord = True

init -950 python in discord:
    from pypresence import Presence, DiscordError, DiscordNotFound, InvalidPipe
    from store import config, NoRollback, persistent
    from copy import deepcopy
    import time

    class DiscordRPC(NoRollback):
        def __init__(self, client_id):
            self.client_id = str(client_id)
            self.start = time.time()
            self.rpc_connected = False
            
            self.set_defaults()
            self.original_props = self.self_dict()
            self.props = {}
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
            self.large_image  = "ddlcmodtemplatelogo"

            # Defines the text when a user hovers on the large icon in
            # a players' status.
            # Example: DDLC Mod Template
            self.large_text  = config.name  # Uses the name of the mod defined in-game.

            # Defines the smallest image to use in rich presence as the
            # secondary icon.
            self.small_image = "test"
            # Defines the text when a user hovers on the small icon in
            # a players' status.
            self.small_text = config.version  # Uses the version name of the mod

        def self_dict(self):
            return {
                "state": self.state,
                "details": self.details,
                "large_image": self.large_image,
                "large_text": self.large_text,
                "small_image": self.small_image,
                "small_text": self.small_text,
                "start": self.start,
            }
        
        def reset_time(self):
            self.start = time.time()

        def auth(self):
            if not persistent.enable_discord: 
                self.rpc = None
                return
                
            try:
                self.rpc = Presence(self.client_id)
            except (DiscordError, DiscordNotFound):
                self.rpc = None

        def connect(self, reset=False):
            if self.rpc is None: self.auth()
            if self.rpc is None: return
            try:
                self.rpc.connect()
                self.rpc_connected = True
                if reset:
                    if len(self.props) <= 1: self.set(**self.original_props)
                    else: self.set(**self.props)
            except InvalidPipe:
                self.rpc = None

        def close(self):
            if self.rpc is None: return
            self.rpc.close()
            self.rpc_connected = False

        def reset(self):
            self.set(**self.original_props)
        
        def record_to_rollback(self):
            global rollback_status
            rollback_status = deepcopy(self.props)

        def rollback_check(self):
            global rollback_status

            if self.rpc is None: return
            if self.props != rollback_status:
                self.set(**rollback_status)

        def on_load(self):
            global rollback_status
            self.set(**rollback_status)

        def set(self, **props):
            if self.rpc is None: return
            self.props = deepcopy(props)
            self.props["start"] = self.start

            self.rpc.update(**self.props)
            self.record_to_rollback()

        def update(self, **props):
            if self.rpc is None: return
            for p in props:
                self.props[p] = props[p]
            self.props["start"] = self.start
            
            self.rpc.update(**self.props)
            self.record_to_rollback()

        def clear(self):
            self.props = {}
            self.record_to_rollback()
            self.rpc.clear()

default discord.rollback_status = {}

init -940 python:
    # Place your Discord RPC token inside the ""'s
    RPC = discord.DiscordRPC("979471077187125248")

    config.quit_callbacks += [RPC.close] 
    config.after_load_callbacks += [RPC.on_load]
    config.interact_callbacks += [RPC.rollback_check] 
    config.start_callbacks += [RPC.reset]
