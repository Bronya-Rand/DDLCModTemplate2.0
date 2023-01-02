## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## renpy_patches.rpy
# This file is mainly designed to patch certain versions of Ren'Py that break 
# DDLC/DDLC mods by patching the Ren'Py engine at startup.

python early:
    import os
    ## Readds WMIC using Powershell's Get-WmiObject class (for Win 11)
    os.environ['wmic process get Description'] = "powershell (Get-Process).ProcessName"
    os.environ['wmic os get version'] = "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"

    ## Patches the 7.4.6 - 7.4.8 transform bugs.
    ## using 7.4.9's Scenelists code. 
    if renpy.version_tuple >= (7, 4, 6, 1693) and renpy.version_tuple < (7, 4, 9, 2142):

        class NewSceneLists(renpy.display.core.SceneLists):

            @staticmethod
            def add(self,
                layer,
                thing,
                key=None,
                zorder=0,
                behind=[ ],
                at_list=[ ],
                name=None,
                atl=None,
                default_transform=None,
                transient=False,
                keep_st=False):

                if not isinstance(thing, renpy.display.core.Displayable):
                    raise Exception("Attempting to show something that isn't a displayable:" + repr(thing))

                if layer not in self.layers:
                    raise Exception("Trying to add something to non-existent layer '%s'." % layer)

                if key:
                    self.remove_hide_replaced(layer, key)
                    self.at_list[layer][key] = at_list

                if key and name:
                    self.shown.predict_show(layer, name)

                if transient:
                    self.additional_transient.append((layer, key))

                l = self.layers[layer]

                if atl:
                    thing = renpy.display.motion.ATLTransform(atl, child=thing)

                add_index, remove_index, zorder = self.find_index(layer, key, zorder, behind)

                at = None
                st = None

                if remove_index is not None:
                    sle = l[remove_index]
                    old = sle.displayable

                    at = sle.animation_time

                    if keep_st:
                        st = sle.show_time

                    if (not atl and
                            not at_list and
                            renpy.config.keep_running_transform and
                            isinstance(old, renpy.display.motion.Transform)):

                        thing = sle.displayable._change_transform_child(thing)
                    else:
                        thing = self.transform_state(l[remove_index].displayable, thing)

                    thing.set_transform_event("replace")

                else:

                    if not isinstance(thing, renpy.display.motion.Transform):
                        thing = self.transform_state(default_transform, thing)

                    thing.set_transform_event("show")

                sle = renpy.display.core.SceneListEntry(key, zorder, st, at, thing, name)
                l.insert(add_index, sle)
                
                if remove_index is not None:
                    if add_index <= remove_index:
                        remove_index += 1

                    self.hide_or_replace(layer, remove_index, "replaced")

                # use visit_all than _show() due to depreciation
                thing.visit_all(lambda d : None)
        
        renpy.display.core.SceneLists.add = NewSceneLists.add

    ## An ATL displayable will now start its animation when it first 
    ## appears, rather than when the screen itself is shown.
    ## We will disable this for DDLC's transform's sakes.
    if renpy.version_tuple >= (7, 4, 7, 1862):
        config.atl_start_on_show = False 
