# Main randomizer logic module that the front end calls.

import collections
import hashlib
import random
import re
import binascii
import copy
import uuid
import enum


from randomizer import data
from randomizer.data.eventtables import _0x68Flags, _0x60Flags, AreaObjects
from randomizer.data.eventscripts.events import scripts as eventscripts
from randomizer.data.objectsequencetables import SequenceSpeeds, _0x08Flags, _0x10Flags
from randomizer.data.actionscripts.actions import scripts as actionscripts
from randomizer.data.roomobjects.roomobjects import rooms as roomdata
from randomizer.data.npcmodels import models as npcmodels
from randomizer.data.npcmodeltables import VramStore, SpriteName
from randomizer.data.roomobjecttables import RadialDirection
from randomizer.data.dialog_data.dialog_data import dialog_data
from randomizer.data.dialog_data.dialog_pointers import pointers as dialog_pointers
from randomizer.data.locations import Area
from randomizer.data.bosses import SpriteSize, HenchmanType, SequenceType
from . import bosses
from . import bosses_overworld
from . import credits
from . import characters
from . import chests
from . import dialogs
from . import doors
from . import enemies
from . import flags
from . import games
from . import items
from . import keys
from . import map
from . import spells
from . import shops
from . import utils
from .patch import Patch
from .battleassembler import assemble_battle_scripts
from randomizer.logic.flags import BanditsWayGating, ForestMazeGating, BoosterTowerGating, MarrymoreGating, SeaGating, YaridovichGating, MonstroTownGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating, FireworksOptions, EXPChallengeOptions, PlayableCharacters, WinConditions, ShopQualities, WinConditions

from randomizer.data.eventscripts.utils.slot_machine.event import script as slot_machine_commands
from randomizer.data.eventscripts.utils.slot_machine.objects import objects as slot_machine_npcs

from randomizer.data.eventscripts.utils.tower_access.mario import script as tower_mario
from randomizer.data.eventscripts.utils.tower_access.mallow import script as tower_mallow
from randomizer.data.eventscripts.utils.tower_access.geno import script as tower_geno
from randomizer.data.eventscripts.utils.tower_access.bowser import script as tower_bowser
from randomizer.data.eventscripts.utils.tower_access.toadstool import script as tower_toadstool

from randomizer.data.eventscripts.utils.castle_statue_room.bonk import script as statue_bonk
from randomizer.data.eventscripts.utils.castle_statue_room.bonk_mario import script as statue_bonk_mario

from randomizer.data.eventscripts.utils.smithy_room.non_smithy_3792 import script as non_smithy_3792
from randomizer.data.eventscripts.utils.smithy_room.non_smithy_3794 import script as non_smithy_3794
from randomizer.data.eventscripts.utils.smithy_room.non_smithy_room_509 import objects as non_smithy_509_objects


# Current version number
VERSION = '8.2.8'


class Settings:
    def __init__(self, mode, debug_mode=False, flag_string=''):
        """Provide either form data fields or flag string to set flags on creation.

        Args:
            mode (str): Should be standard or open.
            debug_mode (bool): Debug flag.
            flag_string (str): Flag string if parsing flags from string.
        """
        self._mode = mode
        self._debug_mode = debug_mode
        self._enabled_flags = set()
        self._all_flags = []

        # If flag string provided, make fake form data based on it to parse.
        flag_data = {}
        for flag in flag_string.strip().split():
            if flag.startswith('-'):
                # Solo flag that begins with a dash.
                flag_data[flag] = True
            elif flag:
                # Flag that may have a subsection of choices and/or options.
                if flag[0] not in flag_data:
                    flag_data[flag[0]] = []
                flag_data[flag[0]] += [c for c in flag[1:]]

        # Get flags from form data.
        for category in flags.CATEGORIES:
            for flag in category.flags:
                self._check_flag_from_form_data(flag, flag_data)

        # Sanity check.
        if debug_mode:
            provided_parts = set(flag_string.strip().split())
            parsed_parts = set(self.flag_string.split())
            if provided_parts != parsed_parts:
                raise ValueError("Generated flags {!r} don't match provided {!r} - difference: {!r}".format(
                    parsed_parts, provided_parts, provided_parts - parsed_parts))

    def _check_flag_from_form_data(self, flag, flag_data):
        """

        Args:
            flag (randomizer.logic.flags.Flag): Flag to check if enabled.
            flag_data (dict): Form data dictionary.

        """
        # change this to access all set values in _all_flags

        if flag.available_in_mode(self.mode):
            if flag.value.startswith('-'):
                # Solo flag that begins with a dash.
                if flag_data.get(flag.value):
                    self._enabled_flags.add(flag)
            else:
                # Flag that may be on its own with choices and/or suboptions.
                if flag.value.startswith('@'):
                    if flag.value[1] in flag_data:
                        self._enabled_flags.add(flag)
                else:
                    char = flag.value[0]
                    rest = flag.value[1:]

                    # Single character flag, just check if it's enabled.  Otherwise, make sure the small char is there.
                    if rest:
                        if rest in flag_data.get(char, []):
                            self._enabled_flags.add(flag)
                    elif char in flag_data:
                        self._enabled_flags.add(flag)

            # If flag was enabled, check choices/options recursively.
            if self.is_flag_enabled(flag):
                for choice in flag.choices:
                    self._check_flag_from_form_data(choice, flag_data)
                for option in flag.options:
                    self._check_flag_from_form_data(option, flag_data)

    @property
    def mode(self):
        """:rtype: str"""
        return self._mode

    @property
    def debug_mode(self):
        """:rtype: bool"""
        return self._debug_mode

    def _build_flag_string_part(self, flag, flag_strings):
        """

        Args:
            flag (randomizer.logic.flags.Flag): Flag to process.
            flag_strings (dict): Dictionary for flag strings.

        Returns:
            str: Flag string piece for this flag.

        """
        if self.is_flag_enabled(flag):
            # Solo flag that begins with a dash.
            if flag.value.startswith('-'):
                flag_strings[flag.value] = True
            # Flag that may have a subsection of choices and/or options.
            else:
                rest = ''
                if flag.value.startswith('@'):
                    char = flag.value[1]
                    flag_strings['@'].append(char)
                else:
                    char = flag.value[0]
                    rest = flag.value[1:]

                # Check if this key is in the map yet.
                if char not in flag_strings:
                    flag_strings[char] = []
                if rest:
                    flag_strings[char].append(rest)

                for choice in flag.choices:
                    self._build_flag_string_part(choice, flag_strings)

                for option in flag.options:
                    self._build_flag_string_part(option, flag_strings)

    @property
    def flag_string(self):
        """
        Returns:
            str: Computed flag string for these settings.
        """
        flag_strings = collections.OrderedDict()
        flag_strings['@'] = []

        for category in flags.CATEGORIES:
            for flag in category.flags:
                self._build_flag_string_part(flag, flag_strings)

        flag_string = ''
        for key, vals in flag_strings.items():
            if key != '@':
                if key.startswith('-'):
                    flag_string += key + ' '
                elif vals or key not in flag_strings['@']:
                    flag_string += key + ''.join(vals) + ' '

        return flag_string.strip()

    def is_flag_enabled(self, flag):
        """
        Args:
            flag: Flag class to check.

        Returns:
            bool: True if flag is enabled, False otherwise.
        """
        return self.is_flag_value(flag, True)

    def get_flag(self, flag):
        """
        Args:
            flag: Flag class to check.

        Returns:
            bool: True if flag is enabled at value, False otherwise.
        """
        narrowed = [i for i in self._all_flags if i[0] == flag]
        _, val = narrowed[0]
        return val

    def is_flag_value(self, flag, value):
        """
        Args:
            flag: Flag class to check.

        Returns:
            bool: True if flag is enabled at value, False otherwise.
        """
        narrowed = [i for i in self._all_flags if i[0] == flag]
        _, val = narrowed[0]
        return val == value

    def get_flag_choice(self, flag):
        """
        Args:
            flag: Flag class to get choice for.

        Returns:
            randomizer.logic.flags.Flag: Selected choice for this flag.
        """
        for choice in flag.choices:
            if self.is_flag_enabled(choice):
                return choice
        return None

class CommandTypes(enum.Enum):
    Action = enum.auto()
    Event = enum.auto()

def new_animation(event_id, command, npc_id, subscript):
    cmd = new_command(event_id, command, [npc_id + 0x14])
    cmd["subscript"] = subscript
    return cmd

def new_command(event_id, command, args=None, t=CommandTypes.Event):
    if t == CommandTypes.Action:
        cmdType = "ACTION"
    else:
        cmdType = "EVENT"
    cmd = {
        "identifier": "%s_%i_%s" % (cmdType, event_id, str(uuid.uuid4())),
        "command": command
    }
    if args is not None:
        cmd["args"] = args
    return cmd

def is_animation_header(command, npc_id):
    return command["command"] in ['action_queue_async', 'action_queue_sync', 'start_embedded_action_script_async_F0', 'start_embedded_action_script_async_F1', 'start_embedded_action_script_sync_F0', 'start_embedded_action_script_sync_F1'] and command["args"][0] == npc_id + 0x14

def is_mario_animation_header(command):
    return command["command"] in ['action_queue_async', 'action_queue_sync', 'start_embedded_action_script_async_F0', 'start_embedded_action_script_async_F1', 'start_embedded_action_script_sync_F0', 'start_embedded_action_script_sync_F1'] and command["args"][0] == AreaObjects.MARIO

def remove_sequence_changes_from_action_script(script):
    return [a for a in script if a["command"] != 'set_sprite_sequence' and a["command"] != "reset_properties"]

def fix_script_for_scarecrow(script):
    s = [a for a in script if a["command"] != "reset_properties"]
    output = []
    for command in s:
        if command["command"] == "face_northwest":
            command["command"] = "face_southwest"
            output.append(command)
        elif command["command"] == "face_northeast":
            command["command"] = "face_southeast"
            output.append(command)
        elif command["command"] == "face_southeast":
            command["command"] = "face_northwest"
            output.append(command)
        elif command["command"] == "face_southwest":
            command["command"] = "face_northeast"
            output.append(command)
        elif command["command"] == "face_mario":
            pass # could possibly substitute a series of "ifs" comparing coord to mario's, and set direction based on that info, but that would be hella complicated and i dont know what temp vars would make sense for it
        elif command["command"] in ["walk_1_step_east", "walk_1_step_northeast", "shift_east_steps", "shift_northeast_steps", "shift_east_pixels", "shift_northeast_pixels"]:
            output.append({"identifier": "dummy", "command": "face_southwest"})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_southeast", "shift_southeast_steps", "shift_southeast_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northeast"})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_south", "shift_south_steps", "shift_south_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northeast"})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append({"identifier": "dummy", "command": "set_sprite_sequence", "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_west", "walk_1_step_southwest", "shift_west_steps", "shift_southwest_steps", "shift_west_pixels", "shift_southwest_pixels"]:
            output.append({"identifier": "dummy", "command": "face_northwest"})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["walk_1_step_north", "walk_1_step_northwest", "shift_north_steps", "shift_northwest_steps", "shift_north_pixels", "shift_northwest_pixels"]:
            output.append({"identifier": "dummy", "command": "face_southeast"})
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] in ["shift_f_direction_steps", "shift_z_20_steps", "shift_z_up_steps", "shift_z_down_steps", "shift_z_up_20_steps", "shift_z_down_20_steps", "shift_f_direction_pixels", "walk_f_direction_16_pixels", "shift_z_up_pixels", "shift_z_down_pixels", "shift_to_xy_coords", "shift_xy_steps", "shift_xy_pixels", "walk_1_step_f_direction", "walk_f_direction_16_pixels", "walk_to_xy_coords", "walk_xy_steps", "walk_to_7016_7018", "walk_to_7016_7018_701A"]:
            output.append({"identifier": "dummy", "command": "fixed_f_coord_on"})
            output.append(command)
            output.append({"identifier": "dummy", "command": "fixed_f_coord_off"})
        elif command["command"] == "set_sprite_sequence" and command["args"][0] == 1:
            command["args"][0] = 0
            if _0x08Flags.MIRROR_SPRITE in ["args"][0][2]:
                command["args"][2] = [c for c in command["args"][2] if c != _0x08Flags.MIRROR_SPRITE]
            else:
                command["args"][2].append(_0x08Flags.MIRROR_SPRITE)
            output.append(command)
        else:
            output.append(command)
    return output

def is_vanilla(boss, location):
    return (utils.isclass_or_instance(location, data.bosses.HammerBros) and utils.isclass_or_instance(boss, data.bosses.HammerBroBoss)) or (utils.isclass_or_instance(location, data.bosses.Croco1) and utils.isclass_or_instance(boss, data.bosses.Croco1Boss)) or (utils.isclass_or_instance(location, data.bosses.Mack) and utils.isclass_or_instance(boss, data.bosses.MackBoss)) or (utils.isclass_or_instance(location, data.bosses.Pandorite) and utils.isclass_or_instance(boss, data.bosses.PandoriteBoss)) or ((utils.isclass_or_instance(location, data.bosses.Belome1) or utils.isclass_or_instance(location, data.bosses.Belome2)) and (utils.isclass_or_instance(boss, data.bosses.Belome1Boss) or utils.isclass_or_instance(boss, data.bosses.Belome2Boss))) or (utils.isclass_or_instance(location, data.bosses.Bowyer) and utils.isclass_or_instance(boss, data.bosses.BowyerBoss)) or (utils.isclass_or_instance(location, data.bosses.Croco2) and utils.isclass_or_instance(boss, data.bosses.Croco2Boss)) or (utils.isclass_or_instance(location, data.bosses.Punchinello) and utils.isclass_or_instance(boss, data.bosses.PunchinelloBoss)) or (utils.isclass_or_instance(location, data.bosses.Booster) and utils.isclass_or_instance(boss, data.bosses.BoosterBoss)) or (utils.isclass_or_instance(location, data.bosses.ClownBros) and utils.isclass_or_instance(boss, data.bosses.GrateGuyBoss)) or (utils.isclass_or_instance(location, data.bosses.Bundt) and utils.isclass_or_instance(boss, data.bosses.Bundt)) or (utils.isclass_or_instance(location, data.bosses.KingCalamari) and utils.isclass_or_instance(boss, data.bosses.KingCalamariBoss)) or (utils.isclass_or_instance(location, data.bosses.Hidon) and utils.isclass_or_instance(boss, data.bosses.HidonBoss)) or (utils.isclass_or_instance(location, data.bosses.Johnny) and utils.isclass_or_instance(boss, data.bosses.JohnnyBoss)) or (utils.isclass_or_instance(location, data.bosses.Yaridovich) and utils.isclass_or_instance(boss, data.bosses.YaridovichBoss)) or (utils.isclass_or_instance(location, data.bosses.Mokura) and utils.isclass_or_instance(boss, data.bosses.MokuraBoss)) or (utils.isclass_or_instance(location, data.bosses.Jagger) and utils.isclass_or_instance(boss, data.bosses.JaggerBoss)) or ((utils.isclass_or_instance(location, data.bosses.Jinx1) or utils.isclass_or_instance(location, data.bosses.Jinx2) or utils.isclass_or_instance(location, data.bosses.Jinx3)) and (utils.isclass_or_instance(boss, data.bosses.Jinx1Boss) or utils.isclass_or_instance(boss, data.bosses.Jinx2Boss) or utils.isclass_or_instance(boss, data.bosses.Jinx3Boss))) or (utils.isclass_or_instance(location, data.bosses.Culex) and utils.isclass_or_instance(boss, data.bosses.Culex)) or (utils.isclass_or_instance(location, data.bosses.BoxBoy) and utils.isclass_or_instance(boss, data.bosses.BoxBoyBoss)) or (utils.isclass_or_instance(location, data.bosses.MegaSmilax) and utils.isclass_or_instance(boss, data.bosses.MegaSmilaxBoss)) or (utils.isclass_or_instance(location, data.bosses.Dodo) and utils.isclass_or_instance(boss, data.bosses.DodoBoss)) or (utils.isclass_or_instance(location, data.bosses.Birdetta) and utils.isclass_or_instance(boss, data.bosses.BirdettaBoss)) or (utils.isclass_or_instance(location, data.bosses.Valentina) and utils.isclass_or_instance(boss, data.bosses.ValentinaBoss)) or (utils.isclass_or_instance(location, data.bosses.CzarDragon) and utils.isclass_or_instance(boss, data.bosses.CzarBoss)) or (utils.isclass_or_instance(location, data.bosses.AxemRangers) and utils.isclass_or_instance(boss, data.bosses.AxemRangersBoss)) or (utils.isclass_or_instance(location, data.bosses.Chester) and utils.isclass_or_instance(boss, data.bosses.ChesterBoss)) or (utils.isclass_or_instance(location, data.bosses.Magikoopa) and utils.isclass_or_instance(boss, data.bosses.MagikoopaBoss)) or (utils.isclass_or_instance(location, data.bosses.Boomer) and utils.isclass_or_instance(boss, data.bosses.BoomerBoss)) or (utils.isclass_or_instance(location, data.bosses.Exor) and utils.isclass_or_instance(boss, data.bosses.ExorBoss)) or (utils.isclass_or_instance(location, data.bosses.Countdown) and utils.isclass_or_instance(boss, data.bosses.CountdownBoss)) or (utils.isclass_or_instance(location, data.bosses.CloakerDomino) and utils.isclass_or_instance(boss, data.bosses.CloakerDominoBoss)) or (utils.isclass_or_instance(location, data.bosses.Clerk) and utils.isclass_or_instance(boss, data.bosses.ClerkBoss)) or (utils.isclass_or_instance(location, data.bosses.Manager) and utils.isclass_or_instance(boss, data.bosses.ManagerBoss)) or (utils.isclass_or_instance(location, data.bosses.Director) and utils.isclass_or_instance(boss, data.bosses.DirectorBoss)) or (utils.isclass_or_instance(location, data.bosses.Gunyolk) and utils.isclass_or_instance(boss, data.bosses.GunyolkBoss)) or (utils.isclass_or_instance(location, data.bosses.Smithy) and utils.isclass_or_instance(boss, data.bosses.SmithyBoss))


""" def is_vanilla_strict(boss, location):
    return (utils.isclass_or_instance(location, data.bosses.HammerBros) and utils.isclass_or_instance(boss, data.bosses.HammerBroBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Croco1) and utils.isclass_or_instance(boss, data.bosses.Croco1Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Mack) and utils.isclass_or_instance(boss, data.bosses.MackBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Pandorite) and utils.isclass_or_instance(boss, data.bosses.PandoriteBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Belome1) and utils.isclass_or_instance(boss, data.bosses.Belome1Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Bowyer) and utils.isclass_or_instance(boss, data.bosses.BowyerBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Croco2) and utils.isclass_or_instance(boss, data.bosses.Croco2Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Punchinello) and utils.isclass_or_instance(boss, data.bosses.PunchinelloBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Booster) and utils.isclass_or_instance(boss, data.bosses.BoosterBoss)) or
    (utils.isclass_or_instance(location, data.bosses.ClownBros) and utils.isclass_or_instance(boss, data.bosses.GrateGuyBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Bundt) and utils.isclass_or_instance(boss, data.bosses.Bundt)) or
    (utils.isclass_or_instance(location, data.bosses.KingCalamari) and utils.isclass_or_instance(boss, data.bosses.KingCalamariBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Hidon) and utils.isclass_or_instance(boss, data.bosses.HidonBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Johnny) and utils.isclass_or_instance(boss, data.bosses.JohnnyBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Yaridovich) and utils.isclass_or_instance(boss, data.bosses.YaridovichBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Mokura) and utils.isclass_or_instance(boss, data.bosses.MokuraBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Belome2) and utils.isclass_or_instance(boss, data.bosses.Belome2Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Jagger) and utils.isclass_or_instance(boss, data.bosses.JaggerBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Jinx1) and utils.isclass_or_instance(boss, data.bosses.Jinx1Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Jinx2) and utils.isclass_or_instance(boss, data.bosses.Jinx2Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Jinx3) and utils.isclass_or_instance(boss, data.bosses.Jinx3Boss)) or
    (utils.isclass_or_instance(location, data.bosses.Culex) and utils.isclass_or_instance(boss, data.bosses.Culex)) or
    (utils.isclass_or_instance(location, data.bosses.BoxBoy) and utils.isclass_or_instance(boss, data.bosses.BoxBoyBoss)) or
    (utils.isclass_or_instance(location, data.bosses.MegaSmilax) and utils.isclass_or_instance(boss, data.bosses.MegaSmilaxBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Dodo) and utils.isclass_or_instance(boss, data.bosses.DodoBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Birdetta) and utils.isclass_or_instance(boss, data.bosses.BirdettaBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Valentina) and utils.isclass_or_instance(boss, data.bosses.ValentinaBoss)) or
    (utils.isclass_or_instance(location, data.bosses.CzarDragon) and utils.isclass_or_instance(boss, data.bosses.CzarBoss)) or
    (utils.isclass_or_instance(location, data.bosses.AxemRangers) and utils.isclass_or_instance(boss, data.bosses.AxemRangersBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Chester) and utils.isclass_or_instance(boss, data.bosses.ChesterBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Magikoopa) and utils.isclass_or_instance(boss, data.bosses.MagikoopaBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Boomer) and utils.isclass_or_instance(boss, data.bosses.BoomerBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Exor) and utils.isclass_or_instance(boss, data.bosses.ExorBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Countdown) and utils.isclass_or_instance(boss, data.bosses.CountdownBoss)) or
    (utils.isclass_or_instance(location, data.bosses.CloakerDomino) and utils.isclass_or_instance(boss, data.bosses.CloakerDominoBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Clerk) and utils.isclass_or_instance(boss, data.bosses.ClerkBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Manager) and utils.isclass_or_instance(boss, data.bosses.ManagerBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Director) and utils.isclass_or_instance(boss, data.bosses.DirectorBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Gunyolk) and utils.isclass_or_instance(boss, data.bosses.GunyolkBoss)) or
    (utils.isclass_or_instance(location, data.bosses.Smithy) and utils.isclass_or_instance(boss, data.bosses.SmithyBoss))
 """

def sanitize_animation_script(boss, boss_location, script, model):
    # leave script alone if character is vanilla
    if not is_vanilla(boss, boss_location):
        new_script = []
        for subscript_command_index, subscript_command in enumerate(script):
            # Pretty much all of these animations are based around sequence setting
            # if a specific mold or sequence doesn't have an equivalent, just don't include it in the sanitized script
            if subscript_command["command"] == 'set_sprite_sequence':
                # molds
                if _0x08Flags.READ_AS_MOLD in subscript_command["args"][2]:
                    # if setting mold to 0, that's ok, just reset to the right default mold for scarecrow or culex
                    if subscript_command["args"][0] == 0:
                        subscript_command["args"][0] = model.mold
                        new_script.append(subscript_command)
                    # otherwise, it's subject to animation-specific rules
                    else:
                        if utils.isclass_or_instance(boss_location, data.bosses.Booster):
                            if subscript_command["args"][0] == 12:
                                new_script.append({"identifier": "dummy", "command": "face_northeast"})

                # sequences
                else:
                    # if setting sequence to 1, that's ok IF the sprite in question supports NW/NE
                    # for scarecrows, this is adjusted in post
                    # if subscript_command["args"][0] == 1:
                    #     if model.directional_capability == VramStore._02_SWSE:
                    #         subscript_command["args"][0] = 0
                    #     else:
                    #         subscript_command["args"][0] = 1
                    #     new_script.append(subscript_command)

                    # bandit's way distraction
                    if utils.isclass_or_instance(boss_location, data.bosses.Croco1) and model.animations.bandits_way_distracted is not None:
                        if subscript_command["args"][0] == 5:
                            subscript_command["args"][0] = model.animations.bandits_way_distracted.sequence_id
                            # no support for sprite offsets, but not necessary with the sprites we're using
                            new_script.append(subscript_command)
                    # moleville mines punch
                    elif utils.isclass_or_instance(boss_location, data.bosses.Punchinello):
                        if model.animations.mines_punch is not None:
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][0] = model.animations.mines_punch.sequence_id
                                new_script.append(subscript_command)
                    # chapel laughing
                    elif utils.isclass_or_instance(boss_location, data.bosses.Booster):
                        if model.animations.chapel_laugh is not None:
                            if subscript_command["args"][0] == 2:
                                subscript_command["args"][0] = model.animations.chapel_laugh.sequence_id
                                new_script.append(subscript_command)
                    # marrymore kitchen
                    elif utils.isclass_or_instance(boss_location, data.bosses.Bundt):
                        if model.animations.kitchen_prep is not None:
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][0] = model.animations.kitchen_prep.sequence_id
                                if model.animations.kitchen_prep.total_duration is not None:
                                    subscript_command["args"][2].append(_0x08Flags.LOOPING_OFF)
                                new_script.append(subscript_command)
                    # ship beckon
                    elif utils.isclass_or_instance(boss_location, data.bosses.KingCalamari):
                        if model.animations.ship_beckon is not None:
                            if subscript_command["args"][0] == 1:
                                subscript_command["args"][0] = model.animations.ship_beckon.sequence_id
                                subscript_command["args"][2].append(_0x08Flags.LOOPING_OFF)
                                new_script.append(subscript_command)
                    # ship chair
                    elif utils.isclass_or_instance(boss_location, data.bosses.Johnny):
                        if model.animations.ship_chair is not None:
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][0] = model.animations.ship_chair.sequence_id
                                new_script.append(subscript_command)
                    # jagger
                    elif utils.isclass_or_instance(boss_location, data.bosses.Jagger):
                        if model.animations.dojo_challenge is not None:
                            if subscript_command["args"][0] == 4:
                                subscript_command["args"][0] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # jinx
                    elif utils.isclass_or_instance(boss_location, data.bosses.Jinx1) or utils.isclass_or_instance(boss_location, data.bosses.Jinx2) or utils.isclass_or_instance(boss_location, data.bosses.Jinx3):
                        if model.animations.dojo_challenge is not None:
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][0] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # magikoopa - challenge only. sequence #10 also used in battle doors, which will be handled separately
                    elif utils.isclass_or_instance(boss_location, data.bosses.Magikoopa):
                        if model.animations.keep_challenge is not None:
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][0] = model.animations.keep_challenge.sequence_id
                                new_script.append(subscript_command)
            else:
                new_script.append(subscript_command)
        return new_script
    else:
        return script


class GameWorld:
    """Master container class representing the entire game world to be randomized.  This class doesn't do much on its
    own, but it holds all the data being randomized so the actual logic can look at and change different things across
    a single instance of the world.
    """

    def __init__(self, seed, settings):
        """
        :type seed: int
        :type settings: randomizer.logic.main.Settings
        """
        self.seed = seed
        self.settings = settings
        self.file_select_character = 'Mario'
        self.file_select_hash = 'MARIO1 / MARIO2 / MARIO3 / MARIO4'
        self._rebuild_hash()

        # Bundt palette swap flag.
        self.chocolate_cake = False

        # *** Get vanilla data for randomizing.
        # Characters
        self.characters = data.characters.get_default_characters(self)
        self.character_join_order = self.characters[:]
        self.meta_join_order = self.character_join_order.copy()
        self.levelup_xps = data.characters.LevelUpExps()
        self.starter_character_checks = data.chests.get_starter_character_checks(self)
        self.recruitable_character_checks = data.chests.get_recruitable_character_checks(self)
        self.spotted_character_checks = data.chests.get_spotted_character_checks(self)

        # Spells
        self.spells = data.spells.get_default_spells(self)
        self.spells_dict = dict([(s.index, s) for s in self.spells])

        # Starting FP.
        self.starting_fp = data.spells.STARTING_FP

        # Items
        self.items = data.items.get_default_items(self)
        self.recruitable_characters = data.items.get_recruitable_characters(self)
        self.items_dict = dict([(i.index, i) for i in self.items])

        # Shops
        self.shops = data.shops.get_default_shops(self)
        self.special_shops = data.shops.get_event_shops(self)

        # Enemies
        self.enemies = data.enemies.get_default_enemies(self)
        self.enemies_dict = dict([(e.index, e) for e in self.enemies])

        # Get enemy attack data.
        self.enemy_attacks = data.attacks.get_default_enemy_attacks(self)

        # Get enemy formation data.
        self.enemy_formations, self.formation_packs = data.formations.get_default_enemy_formations(self)
        self.enemy_formations_dict = dict((f.index, f) for f in self.enemy_formations)
        self.formation_packs_dict = dict((p.index, p) for p in self.formation_packs)

        # Get item location data.
        # self.key_locations = data.keys.get_default_key_item_locations(self)
        self.chest_locations = data.chests.get_default_chests(self)
        self.freestanding_item_locations = data.chests.get_freestanding_item_checks(self)
        

        # Get boss location data.
        self.boss_locations = data.bosses.get_default_boss_locations(self)
        self.boss_star_checks = data.chests.get_boss_star_piece_checks(self)

        # Events
        self.eventscripts = copy.copy(eventscripts)
        self.actionscripts = copy.copy(actionscripts)

        # Get default npc and model data. Keep them for reference. 
        self.original_models = copy.copy(npcmodels)
        self.original_rooms = copy.copy(roomdata)
        # Malleable versions
        self.models = copy.copy(npcmodels)
        self.rooms = copy.copy(roomdata)

        #Dialogs
        self.dialog_pointers = copy.copy(dialog_pointers)
        self.dialog_data = copy.copy(dialog_data)

        # Minigame data.
        self.ball_solitaire = data.games.BallSolitaireGame(self)
        self.magic_buttons = data.games.MagicButtonsGame(self)

        # String data.
        self.wishes = data.dialogs.Wishes(self)
        self.quiz = data.dialogs.Quiz(self)

        # Credits for specifically chosen tadpole pond and sunken ship submissions
        self.tadpole_submitters = []
        self.password_submitter = ""

        # Music (moved this into its own classes to make exclusion easier)
        self.music_pool = data.music.get_default_music

    @property
    def open_mode(self):
        """Check if this game world is Open mode.

        Returns:
            bool:

        """
        return self.settings.mode == 'open'

    @property
    def debug_mode(self):
        """Get debug mode flag.

        Returns:
            bool:

        """
        return self.settings.debug_mode

    def get_item_instance(self, cls):
        """
        Args:
            cls: Item class to get this world's instance of.

        Returns:
            randomizer.data.items.Item: Item instance for this world.
        """
        return self.items_dict[cls.index]

    def get_enemy_instance(self, cls):
        """
        Args:
            cls: Enemy class to get this world's instance of.

        Returns:
            randomizer.data.enemies.Enemy: Enemy instance for this world.
        """
        return self.enemies_dict[cls.index]

    def get_enemy_formation_by_index(self, index):
        """
        :type index: int
        :rtype: randomizer.data.formations.EnemyFormation
        """
        return self.enemy_formations_dict[index]

    def get_formation_pack_by_index(self, index):
        """
        :type index: int
        :rtype: randomizer.data.formations.FormationPack
        """
        return self.formation_packs_dict[index]

    def randomize(self):
        """Randomize this entire game world instance."""
        # Seed the PRNG at the start.
        random.seed(self.seed)

        characters.randomize_all(self)
        spells.randomize_all(self)
        items.randomize_all(self)
        chests.randomize_all(self)
        shops.randomize_all(self)
        bosses.randomize_all(self)
        # Bosses might have to go before enemies to make formation rando work as intended?
        enemies.randomize_all(self)
        doors.randomize_all(self)
        games.randomize_all(self)
        dialogs.randomize_all(self)

        # Rebuild hash after randomization.
        self._rebuild_hash()

        # move cosmetics to after hash build

    def _rebuild_hash(self):
        """Build hash value for choosing file select character and file name hash.
        Use the same version, seed, mode, and flags used for the database hash.
        """
        final_seed = bytearray()
        final_seed += VERSION.encode('utf-8')
        final_seed += self.seed.to_bytes(4, 'big')
        final_seed += self.settings.mode.encode('utf-8')
        final_seed += self.settings.flag_string.encode('utf-8')
        self.hash = hashlib.md5(final_seed).hexdigest()

    def replace_dialog(self, id, content):
        dialog_info = self.dialog_pointers[id]
        index = dialog_info["index"]
        if dialog_info["bank"] == 0x22:
            self.dialog_data[0][index] = content
        elif dialog_info["bank"] == 0x23:
            self.dialog_data[1][index] = content
        elif dialog_info["bank"] == 0x24:
            self.dialog_data[2][index] = content

    def search_replace_dialog(self, search, replace):
        for bank_id in range(len(self.dialog_data)):
            for index in range(len(self.dialog_data[bank_id])):
                self.dialog_data[bank_id][index] = self.dialog_data[bank_id][index].replace(search, replace)

    def prepend_bits(self, event, pairs):
        for pair in pairs:
            self.eventscripts[event].insert(0, new_command(event, "set_bit", pair))

    def build_patch(self):
        """Build patch data for this instance.

        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Remove commands from game loader that are required to make the base rom run properly on its own
        # These commands will be replaced according to the user's settings
        self.eventscripts[192].pop(0)
        self.eventscripts[192].pop(0)

        # Set number of star pieces required for win condition
        required_star_pieces = self.settings.get_flag(flags.TotalStarPieces).value
        self.eventscripts[1969][0]["args"] = [required_star_pieces]

        # Alternate star piece win conditions
        if self.settings.is_flag_value(flags.RequireBossFights, True):
            self.prepend_bits(192, [[0x7086, 7]])
            # disable mack skip
            chancellor_index = len(self.rooms[326]["objects"])
            self.rooms[326]["objects"][chancellor_index - 1]["event"] = 256

        # Bandit's Way gating
        if self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.prepend_bits(199, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMario):
            self.prepend_bits(187, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMallow):
            self.prepend_bits(198, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitGeno):
            self.prepend_bits(189, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitBowser):
            self.prepend_bits(190, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitToadstool):
            self.prepend_bits(191, [[0x7065, 4], [0x706D, 4]])

        # Forest Maze gating, special conditions
        if self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])
        elif self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.ExchangeCricketPie):
            self.prepend_bits(203, [[0x7066, 3], [0x706E, 3]])

        # Booster Tower gating
        if self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7053, 6]])
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.FinishMoleville):
            self.prepend_bits(198, [[0x7053, 6]])
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMario):
            self.prepend_bits(187, [[0x7053, 7]])
            self.eventscripts[1331] = tower_mario
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMallow):
            self.prepend_bits(198, [[0x7053, 7]])
            self.eventscripts[1331] = tower_mallow
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitGeno):
            self.prepend_bits(189, [[0x7053, 7]])
            self.eventscripts[1331] = tower_geno
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitBowser):
            self.prepend_bits(190, [[0x7053, 7]])
            self.eventscripts[1331] = tower_bowser
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitToadstool):
            self.prepend_bits(191, [[0x7053, 7]])
            self.eventscripts[1331] = tower_toadstool

        # Marrymore gating
        if self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.AlwaysOpen):
            self.prepend_bits(192, [[0x704C, 7]])
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.FinishBoosterHill):
            self.prepend_bits(204, [[0x704C, 7]])
            self.replace_dialog(2116, '''You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy on Booster Hill.''')
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.FinishBoosterTower):
            self.prepend_bits(205, [[0x704C, 7]])
            self.replace_dialog(2116, '''You want to know why we're\n standing around?\n I'm waiting for something\n interesting to happen, but I think\n the usual troublemakers are busy up atop Booster Tower.''')

        # Sea gating
        if self.settings.is_flag_value(flags.SeaGate, SeaGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7067, 4], [0x706F, 3], [0x7067, 5], [0x706F, 4]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMario):
            self.prepend_bits(187, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMallow):
            self.prepend_bits(198, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitGeno):
            self.prepend_bits(189, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitBowser):
            self.prepend_bits(190, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitToadstool):
            self.prepend_bits(191, [[0x7067, 4], [0x706F, 3]])
        else:
            if self.settings.is_flag_value(flags.SeaGate, SeaGating.Find1Star):
                value = 1
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.Find2Star):
                value = 2
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.Find3Star):
                value = 3
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.Find4Star):
                value = 4
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.Find5Star):
                value = 5
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.Find6Star):
                value = 6
            else:
                raise Exception("failed to set star piece gate on sea")
            gate_script = copy.copy(self.eventscripts[206])
            gate_script[1]["args"][1] = value
            self.eventscripts[206] = gate_script
            self.prepend_bits(192, [[0x7051, 0]])

        # Yaridovich gating
        if self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7051, 1]])
        elif self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.FinishSunkenShip):
            self.prepend_bits(210, [[0x7051, 1]])

        # Monstro Town gating
        if self.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7067, 7], [0x706F, 6]])
        elif self.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.FinishLandsEnd):
            pass

        # Volcano gating
        if self.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7090, 0], [0x7070, 1], [0x7068, 2]])
        elif self.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.FinishNimbusLand):
            pass

        # Bowser's Keep gating
        if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7068, 3]])
        else:
            self.prepend_bits(192, [[0x707A, 3]])
            if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.FinishBarrelVolcano):
                self.prepend_bits(192, [[0x707B, 2]])
            else:
                if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find1Star):
                    value = 1
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find2Star):
                    value = 2
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find3Star):
                    value = 3
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find4Star):
                    value = 4
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find5Star):
                    value = 5
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.Find6Star):
                    value = 6
                else:
                    raise Exception("failed to set star piece gate on keep")
                keep_script = copy.copy(self.eventscripts[207])
                keep_script[1]["args"][1] = value
                self.eventscripts[207] = keep_script
                self.prepend_bits(192, [[0x7051, 1], [0x707A, 3]])

        # Factory gating
        if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.AlwaysOpen):
            self.prepend_bits(192, [[0x7070, 5], [0x7068, 5]])
        elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.FinishBowsersKeep):
            self.prepend_bits(2149, [[0x7070, 5], [0x7068, 5]])
        else:
            if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find1Star):
                value = 1
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find2Star):
                value = 2
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find3Star):
                value = 3
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find4Star):
                value = 4
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find5Star):
                value = 5
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.Find6Star):
                value = 6
            else:
                raise Exception("failed to set star piece gate on factory")
            factory_script = copy.copy(self.eventscripts[3093])
            factory_script[1]["args"][1] = value
            self.eventscripts[3093] = factory_script
            self.prepend_bits(192, [[0x7051, 3]])

        # Casino warp
        if self.settings.is_flag_value(flags.CasinoWarp, True):
            self.prepend_bits(192, [[0x7088, 5]])
            casino_script = copy.copy(self.eventscripts[2645])
            casino_script[2]["args"][1] = required_star_pieces
            self.eventscripts[2645] = casino_script

        # Bucket warp
        if self.settings.is_flag_value(flags.BucketWarp, True):
            self.prepend_bits(192, [[0x705E, 6]])
            bucket_script = copy.copy(self.eventscripts[2651])
            bucket_script[0]["args"][1] = required_star_pieces
            self.eventscripts[2651] = bucket_script

        # Fast travel
        if self.settings.is_flag_value(flags.FastTravel, True):
            self.prepend_bits(192, [[0x708B, 0]])

        # Win condition
        if self.settings.is_flag_value(flags.WinCondition, WinConditions.StarPieces):
            self.prepend_bits(192, [[0x7051, 6]])
            self.eventscripts[3101][1]["args"][1] = [required_star_pieces]
        elif self.settings.is_flag_value(flags.WinCondition, WinConditions.Culex):
            self.prepend_bits(192, [[0x7051, 7]])

        # Fireworks
        if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.Vanilla):
            pass
        else:
            # assign one of 3 random fireworks
            fireworks_credits = random.randint(1, 6)
            for script_id in [184, 3399]:
                for index in range(len(self.eventscripts[script_id])):
                    cmd = self.eventscripts[script_id][index]
                    if cmd["command"] == "set" and cmd["args"][0] == 0x70EA:
                        self.eventscripts[script_id][index]["args"][1] = fireworks_credits
            # append the setting
            if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
                self.prepend_bits(192, [[0x705D, 4]])
            if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
                self.prepend_bits(192, [[0x705D, 5]])

        # EXP progression option
        if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easystars) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardstars):
            self.prepend_bits(192, [[0x7056, 0]])
        elif self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easybosses) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardbosses):
            self.prepend_bits(192, [[0x7056, 1]])

        # If star piece exp progression is on, set exp values for each star piece number and enable flag.
        if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.default):
            pass
        else:
            if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easystars) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easybosses):
                exps = (2, 4, 5, 6, 8, 9, 11)
            elif self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardstars) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardbosses):
                exps = (1, 2, 3, 5, 6, 7, 11)
            elif self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.none):
                exps = (0, 0, 0, 0, 0, 0, 0)
            else:
                raise ValueError("Unrecognized value for star exp challenge")
            patch.add_data(0x39bc44, utils.ByteField(exps[0]).as_bytes())  # 0 stars
            patch.add_data(0x39bc46, utils.ByteField(exps[1]).as_bytes())  # 1 star
            patch.add_data(0x39bc48, utils.ByteField(exps[2]).as_bytes())  # 2 stars
            patch.add_data(0x39bc4a, utils.ByteField(exps[3]).as_bytes())  # 3 stars
            patch.add_data(0x39bc4c, utils.ByteField(exps[4]).as_bytes())  # 4 stars
            patch.add_data(0x39bc4e, utils.ByteField(exps[5]).as_bytes())  # 5 stars
            patch.add_data(0x39bc52, utils.ByteField(exps[6]).as_bytes())  # 6/7 stars
            patch.add_data(0x1fd32d, utils.ByteField(0xa0).as_bytes())  # Enable flag

        # Grate Guy threshold
        value = self.settings.get_flag(flags.GrateGuyPrizeThreshold).value
        self.eventscripts[2650][0]["args"] = [value]
        self.search_replace_dialog('`GRATE_GUY_PRIZE_CAP`', value)

        # Knife Guy threshold
        value = self.settings.get_flag(flags.KnifeGuyPrizeThreshold).value
        self.eventscripts[2671][0]["args"] = [value]

        # Suite Prize thresholds
        value1 = self.settings.get_flag(flags.SuitePrize1Threshold).value
        value2 = self.settings.get_flag(flags.SuitePrize2Threshold).value
        value3 = self.settings.get_flag(flags.SuitePrize3Threshold).value
        value4 = self.settings.get_flag(flags.SuitePrize4Threshold).value
        value5 = self.settings.get_flag(flags.SuitePrize5Threshold).value
        value6 = self.settings.get_flag(flags.SuitePrize6Threshold).value
        self.eventscripts[708][0]["args"][0] = value1
        self.eventscripts[708][1]["args"][0] = value2
        self.eventscripts[708][2]["args"][0] = value3
        self.eventscripts[708][3]["args"][0] = value4
        self.eventscripts[708][4]["args"][0] = value5
        self.eventscripts[708][5]["args"][0] = value6
        if not (value1 < value2 and value2 < value3 and value3 < value4 and value4 < value5 and value5 < value6):
            raise Exception("marrymore item thresholds must be in increasing order")

        # Attack Scarf threshold
        value = self.settings.get_flag(flags.SuperJump1Threshold).value
        self.eventscripts[3393][0]["args"] = [value]
        self.search_replace_dialog('`SUPER_JUMP_PRIZE_1_CAP`', value)

        # Super Suit threshold
        value = self.settings.get_flag(flags.SuperJump2Threshold).value
        if value <= self.settings.get_flag(flags.SuperJump1Threshold).value:
            raise Exception("2nd super jump threshold must be higher than 1st")
        self.eventscripts[3394][0]["args"] = [value]
        self.search_replace_dialog('`SUPER_JUMP_PRIZE_2_CAP`', value)

        # disable sj dog checks if SJ not learnable in seed
        if flags.LearnableSpells.SuperJump in self.settings.get_flag(flags.AvailableSpells).disabled:
            self.eventscripts[2063] = [
                new_command(2063, 'run_dialog', [2049, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]),
                new_command(2063, 'ret')
            ]
    

        # Bowser's Keep threshold
        value = self.settings.get_flag(flags.BowserDoorRequirements).value
        for c in range(len(self.eventscripts[3350])):
            cmd = self.eventscripts[3350][c]
            if cmd[c]["command"] == 'jmp_if_var_equals_byte' and cmd[c]["args"][0] == 0x70b6 and cmd[c]["args"][1] == 4:
                cmd = self.eventscripts[3350][c]["args"][1] = value
        

        # Skip Minecart
        if self.settings.is_flag_value(flags.SkipMinecart, True):
            self.prepend_bits(192, [[0x707B, 6]])

        # Invisible Checks Anywhere
        if self.settings.is_flag_value(flags.InvisibleFlagsSetting, True):
            self.prepend_bits(192, [[0x7060, 2]])
        else:
            self.prepend_bits(192, [[0x705F, 2]])

        # some more dialogs
        if self.settings.is_flag_value(flags.EXPStarsAnywhere, True):
            self.replace_dialog(1222, ''' I have a chest to sell, but you\n don't have enough coins.[await]''')
            self.replace_dialog(1223, ''' You're looking for chests?\n I'll sell one for 400 coins.\n Are you interested?[await]\n  [select] (Yes)\n  [select] (No)[await]''')
            self.replace_dialog(1224, ''' You want another chest?[await]\n  [select] (Yes)\n  [select] (No)[await]''')
            self.replace_dialog(1227, ''' I found another chest.\n I'll sell it for 800 coins.[await]\n  [select] (Buy it)\n  [select] (Pass)[await]''')


        # Starting characters
        for c in self.starter_character_checks:
            if c.item is not None:
                # set character
                self.eventscripts[c.event].insert(0, new_command(c.event, "run_event_as_subroutine", [c.item.starter_script]))
                # check if character gates forest maze
                if (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario) and utils.isclass_or_instance(c.item, data.items.MarioRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow) and utils.isclass_or_instance(c.item, data.items.MallowRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno) and utils.isclass_or_instance(c.item, data.items.GenoRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser) and utils.isclass_or_instance(c.item, data.items.BowserRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool) and utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                    self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])
 
        # Use first character to join as file select cursor.
        if (self.settings.is_flag_value(flags.StartingCharacter, PlayableCharacters.Mallow)):
            cursor_id = 4
        elif (self.settings.is_flag_value(flags.StartingCharacter, PlayableCharacters.Geno)):
            cursor_id = 3
        elif (self.settings.is_flag_value(flags.StartingCharacter, PlayableCharacters.Bowser)):
            cursor_id = 2
        elif (self.settings.is_flag_value(flags.StartingCharacter, PlayableCharacters.Toadstool)):
            cursor_id = 1
        else:
            cursor_id = 0

        # Star Hill wishes
        for id, wish in self.wishes.wishes:
            self.replace_dialog(id, wish)



        ######### Minigames

        # Dr Topper quiz
        if self.settings.is_flag_value(flags.QuizShuffle, True):
            for id, question in self.quiz.questions:
                self.replace_dialog(id, question)



        ######### write character/item/star piece granters

        grant_builders = {}

        # recruitable characters
        for c in self.recruitable_character_checks:
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            self.replace_dialog(id, dat)
                if c.event not in grant_builders:
                    grant_builders[c.event] = {
                        "jumps": [new_command(c.event, 'set_7000_to_current_level')],
                        "executions": []
                    }
                cmd = new_command(c.event, 'jmp_to_event', [c.item.container_script])
                grant_builders[c.event]["executions"].append(cmd)
                for r in c.rooms:
                    jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmd["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
                # forest maze gating
                if utils.isclass_or_instance(c, data.chests.MushroomWayCharacter):
                    if (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario) and utils.isclass_or_instance(c.item, data.items.MarioRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow) and utils.isclass_or_instance(c.item, data.items.MallowRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno) and utils.isclass_or_instance(c.item, data.items.GenoRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser) and utils.isclass_or_instance(c.item, data.items.BowserRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool) and utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                        self.prepend_bits(202, [[0x7066, 3], [0x706E, 3]])
                elif utils.isclass_or_instance(c, data.chests.MolevilleMinesCharacter):
                    if (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario) and utils.isclass_or_instance(c.item, data.items.MarioRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow) and utils.isclass_or_instance(c.item, data.items.MallowRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno) and utils.isclass_or_instance(c.item, data.items.GenoRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser) and utils.isclass_or_instance(c.item, data.items.BowserRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool) and utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                        self.prepend_bits(201, [[0x7066, 3], [0x706E, 3]])
                elif utils.isclass_or_instance(c, data.chests.MarrymoreCharacter):
                    # What to do about this if you DON'T get a character here?
                    self.search_replace_dialog("`MARRYMORE_CHARACTER`", c.item.description)
                    random_character = random.choice([i.description for i in [data.items.MarioRecruit, data.items.MallowRecruit, data.items.GenoRecruit, data.items.BowserRecruit, data.items.ToadstoolRecruit] if not utils.isclass_or_instance(c.item, i)])
                    self.search_replace_dialog("`RANDOM_CHARACTER_NAME`", random_character)
                    if (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario) and utils.isclass_or_instance(c.item, data.items.MarioRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow) and utils.isclass_or_instance(c.item, data.items.MallowRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno) and utils.isclass_or_instance(c.item, data.items.GenoRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser) and utils.isclass_or_instance(c.item, data.items.BowserRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool) and utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                        self.prepend_bits(200, [[0x7066, 3], [0x706E, 3]])
        
        # chests
        for c in self.chest_locations:
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            self.replace_dialog(id, dat)
                if c.event not in grant_builders:
                    grant_builders[c.event] = {
                        "jumps": [],
                        "executions": []
                    }
                cmds = []
                # physical chests
                if utils.isclass_or_instance(c, data.chests.Chest): 
                    # slot machines - doesn't take a 70A7 value
                    if utils.isclass_or_instance(c.item, data.items.SlotMachineChest): 
                        for i in range(len(c.rooms)):
                            # count NPCs in room
                            r = c.rooms[i]
                            ctr = 0
                            for object_id in range(len(self.rooms[r]["objects"])):
                                o = self.rooms[r]["objects"][object_id]
                                ctr += 1
                                for clone_id in range(len(o["clones"])):
                                    ctr += 1
                            # insert a slot machine script with the NPC IDs adjusted to this room
                            slot_logic = copy.copy(slot_machine_commands)
                            for j in range(len(slot_logic)):
                                cmd = slot_logic[j]
                                if cmd["command"] in ["stop_embedded_action_script", "pause_action_script", "set_action_script_sync", "summon_to_current_level", "action_queue_async", "action_queue_sync"] and cmd["args"][0] >= 0x16 and cmd["args"][0] <= 0x1A:
                                    cmd["args"][0] = cmd["args"][0] - 0x16 + ctr
                                slot_logic[j] = cmd
                            cmds.extend(slot_logic)
                            # add slot machine NPCs to this room
                            self.rooms[r]["objects"].extend(slot_machine_npcs)
                            grant_builders[c.event]["executions"].extend(cmds)
                            jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                    else:
                        if c.manual_70A7 or len([r for r in c.item.rooms if r > 509]) > 0:
                            # set 70A7 manually if chest is used multiple times
                            manual_70A7 = (c.item.chest_70A7_upper << 4) + c.item.chest_70A7_lower
                            cmds.append(new_command(c.event, 'set', [0x70A7, manual_70A7]))
                        else:
                            # set 70A7 on chest itself
                            for i in range(len(c.rooms)):
                                r = c.rooms[i]
                                ctr = 0
                                for object_id in range(len(self.rooms[r]["objects"])):
                                    o = self.rooms[r]["objects"][object_id]
                                    if ctr == c.npc_ids[i]:
                                        self.rooms[r]["objects"][object_id]["item_offset"] = c.item.chest_70A7_upper
                                        self.rooms[r]["objects"][object_id]["star_offset"] = c.item.chest_70A7_lower
                                    ctr += 1
                                    for clone_id in range(len(o["clones"])):
                                        if ctr == c.npc_ids[i]:
                                            self.rooms[r]["objects"][object_id]["clones"][clone_id]["item_offset"] = c.item.chest_70A7_upper
                                            self.rooms[r]["objects"][object_id]["clones"][clone_id]["star_offset"] = c.item.chest_70A7_lower
                                        ctr += 1
                        if utils.isclass_or_instance(c.item, data.items.Coins) or utils.isclass_or_instance(c.item, data.items.MultiFrogCoin):
                            cmds.append(new_command(c.event, 'set', [0x70BC, 0]))
                        elif utils.isclass_or_instance(c.item, data.items.StarPiece):
                            hint_variable, hint_bit = c.item.hint_bit
                            cmds.append(new_command(c.event, 'set_bit', [hint_variable, hint_bit]))
                            cmds.append(new_command(c.event, 'run_event_as_subroutine', [3092]))
                        # jump based on type
                        if self.settings.is_flag_value(flags.QuickHitCoins, True) and (utils.isclass_or_instance(c.item, data.items.Coins) or utils.isclass_or_instance(c.item, data.items.MultiFrogCoin)):
                            cmds.append(new_command(c.event, 'jmp_to_event', [c.item.quick_chest_event]))
                        elif c.item.chest_event:
                            cmds.append(new_command(c.event, 'jmp_to_event', [c.item.get_chest_event(c.event)]))
                        # add jumps
                        grant_builders[c.event]["executions"].extend(cmds)
                        for r in c.rooms:
                            jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                # npc rewards
                else:
                    # starter items
                    if utils.isclass_or_instance(c, data.chests.StarterItem):
                        self.eventscripts[192].insert(0, new_command(c.event, 'put_inventory', [c.item.index]))
                    else:
                        if utils.isclass_or_instance(c.item, data.items.RegularItem):
                            # set 70A7 for granting a normal item
                            cmds.append(new_command(c.event, 'set', [0x70A7, c.item.chest_70A7_lower]))
                        elif utils.isclass_or_instance(c.item, data.items.Coins) or utils.isclass_or_instance(c.item, data.items.MultiFrogCoin):
                            # set 7000 for quantity
                            cmds.append(new_command(c.event, 'set', [0x7000, c.item.amount]))
                        cmds.append(new_command(c.event, 'jmp_to_event', [c.item.npc_event]))
                        grant_builders[c.event]["executions"].extend(cmds)
                        for r in c.rooms:
                            jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                        # coin snake considerations
                        if utils.isclass_or_instance(c, data.chests.SunkenShipCoinSnake):
                            model_id = c.item.model.model
                            action_script = model_id = c.item.model.action_script
                            for r in c.rooms:
                                ctr = 0
                                for object_id in range(len(self.rooms[r]["objects"])):
                                    o = self.rooms[r]["objects"][object_id]
                                    if ctr in c.npc_ids:
                                        self.rooms[r]["objects"][object_id]["model"] = model_id
                                    ctr += 1
                                    for clone_id in range(len(o["clones"])):
                                        ctr += 1
                            # set the right sequence on the object in AS 199 and 200
                            action_script_contents = copy.copy([s for s in self.actionscripts[action_script] if s["command"] != "ret"])
                            as_199 = copy.copy(self.actionscripts[199]).pop()
                            as_200 = copy.copy(self.actionscripts[200]).pop()
                            self.actionscripts[199] = action_script_contents + as_199
                            self.actionscripts[200] = action_script_contents + as_200
                            # remove coin sequences if necessary
                            if not utils.isclass_or_instance(c.item, data.items.Coins) and not utils.isclass_or_instance(c.item, data.items.FrogCoin) and not utils.isclass_or_instance(c.item, data.items.MultiFrogCoin):
                                e_3215 = copy.copy(self.eventscripts[3215])
                                for command_index in range(len(e_3215)):
                                    command = e_3215[command_index]
                                    if "subscript" in command:
                                        subscript = [ss for ss in command["subscript"] if ss["command"] != 'set_sprite_sequence']
                                        e_3215[command_index]["subscript"] = subscript
                                e_3216 = copy.copy(self.eventscripts[3216])
                                for command_index in range(len(e_3216)):
                                    command = e_3216[command_index]
                                    if "subscript" in command:
                                        subscript = [ss for ss in command["subscript"] if ss["command"] != 'set_sprite_sequence']
                                        e_3216[command_index]["subscript"] = subscript
                                self.eventscripts[3215] = e_3215
                                self.eventscripts[3216] = e_3216
                                
        # freestanding items
        for c in self.freestanding_item_locations:
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            self.replace_dialog(id, dat)
                if c.event not in grant_builders:
                    grant_builders[c.event] = {
                        "jumps": [new_command(c.event, 'set_7000_to_current_level')],
                        "executions": []
                    }
                cmds = []
                if utils.isclass_or_instance(c, data.chests.PacketItem): 
                    # generate the right packet for the item
                    generator = copy.copy(self.eventscripts[c.script_id])
                    generator[0]["args"][0] = c.item.packet
                    self.eventscripts[c.script_id] = generator
                else:
                    # set the NPC and action script for the item
                    model_id = c.item.model.model
                    action_script = model_id = c.item.model.action_script
                    for r in c.rooms:
                        ctr = 0
                        for object_id in range(len(self.rooms[r]["objects"])):
                            o = self.rooms[r]["objects"][object_id]
                            if ctr in c.npc_ids:
                                self.rooms[r]["objects"][object_id]["model"] = model_id
                                self.rooms[r]["objects"][object_id]["action_script"] = action_script
                            ctr += 1
                            for clone_id in range(len(o["clones"])):
                                if ctr in c.npc_ids:
                                    self.rooms[r]["objects"][object_id]["clones"][clone_id]["action_offset"] = 0
                                    self.rooms[r]["objects"][object_id]["clones"][clone_id]["npc_id_offset"] = 0
                                ctr += 1
                # sett the item grant
                if utils.isclass_or_instance(c.item, data.items.RegularItem):
                    # set 70A7 for granting a normal item
                    cmds.append(new_command(c.event, 'set', [0x70A7, c.item.chest_70A7_lower]))
                if utils.isclass_or_instance(c, data.chests.MidasRiverTunnelItem): 
                    # midas river grant
                    cmds.append(new_command(c.event, 'jmp_to_event', [c.item.overworld_midas_event]))
                else:
                    # all other overworld item grant
                    cmds.append(new_command(c.event, 'jmp_to_event', [c.item.overworld_event]))
                grant_builders[c.event]["executions"].extend(cmds)
                # generate room-based jumps
                for r in c.rooms:
                    jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
                # edit action script 43 if midas runnel #3 item is not a coin
                if utils.isclass_or_instance(c, data.chests.MidasRiverBottomLeftCave) and not utils.isclass_or_instance(c.item, data.items.Coins) and not utils.isclass_or_instance(c.item, data.items.FrogCoin) and not utils.isclass_or_instance(c.item, data.items.MultiFrogCoin):
                    self.actionscripts[43] = [a for a in self.actionscripts[43] if a["command"] != 'set_sprite_sequence']

        # boss star pieces
        for c in self.boss_star_checks:
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            self.replace_dialog(id, dat)
                if c.event not in grant_builders:
                    grant_builders[c.event] = {
                        "jumps": [new_command(c.event, 'inc', [0x70E6])],
                        "executions": []
                    }
                cmd = new_command(c.event, 'jmp_to_event', 3092)
                grant_builders[c.event]["executions"].append(cmd)
                for r in c.rooms:
                    jmp = new_command(c.event, 'jmp_if_7000_equals_short', [r, cmd["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
            elif utils.isclass_or_instance(c, data.chests.StarHillStarPiece1):
                # remove freestanding star if empty
                self.eventscripts[2405].pop(0)
                
        # finalize granter scripts
        for e in grant_builders:
            grant_builders[e]["jumps"].append(new_command(e, "ret"))
            self.eventscripts[e] = copy.copy(grant_builders[e]["jumps"]) + copy.copy(grant_builders[e]["executions"])

        # if star piece signal ring hints turned on, set the appropriate bit checks in each area
        if self.settings.is_flag_value(flags.StarPieceHints, True):
            for c in [c in self.recruitable_character_checks + self.chest_locations + self.freestanding_item_locations + self.boss_star_checks]:
                if utils.isclass_or_instance(c.item, data.items.StarPiece):
                    hint_event = None
                    if c.area == Area.MariosPad:
                        hint_event = 3887
                    elif c.area == Area.MushroomWay:
                        hint_event = 3888
                    elif c.area == Area.MushroomKingdom:
                        hint_event = 3889
                    elif c.area == Area.BanditsWay:
                        hint_event = 3890
                    elif c.area == Area.KeroSewers:
                        hint_event = 3891
                    elif c.area == Area.MidasRiver:
                        hint_event = 3892
                    elif c.area == Area.TadpolePond:
                        hint_event = 3893
                    elif c.area == Area.RoseWay:
                        hint_event = 3894
                    elif c.area == Area.RoseTown:
                        hint_event = 3895
                    elif c.area == Area.ForestMaze:
                        hint_event = 3896
                    elif c.area == Area.Moleville or c.area == Area.MolevilleMines:
                        hint_event = 3897
                    elif c.area == Area.BoosterPass:
                        hint_event = 3898
                    elif c.area == Area.BoosterTower:
                        hint_event = 3899
                    elif c.area == Area.PipeVault:
                        hint_event = 3900
                    elif c.area == Area.YosterIsle:
                        hint_event = 3901
                    elif c.area == Area.Marrymore:
                        hint_event = 3902
                    elif c.area == Area.StarHill:
                        hint_event = 3903
                    elif c.area == Area.SeasideTown:
                        hint_event = 3904
                    elif c.area == Area.Sea:
                        hint_event = 3905
                    elif c.area == Area.SunkenShip:
                        hint_event = 3906
                    elif c.area == Area.LandsEnd:
                        hint_event = 3907
                    elif c.area == Area.BelomeTemple:
                        hint_event = 3908
                    elif c.area == Area.MonstroTown:
                        hint_event = 3909
                    elif c.area == Area.Casino:
                        hint_event = 3910
                    elif c.area == Area.BeanValley:
                        hint_event = 3911
                    elif c.area == Area.NimbusLand:
                        hint_event = 3912
                    elif c.area == Area.BarrelVolcano:
                        hint_event = 3913
                    elif c.area == Area.BowsersKeep:
                        hint_event = 3914
                    elif c.area == Area.Factory:
                        hint_event = 3915
                    elif c.area == Area.InnerFactory:
                        hint_event = 3916
                    if hint_event is not None:
                        # get name of sound command
                        sound_command = [cmd for cmd in self.eventscripts[hint_event] if cmd["command"] == 'play_sound'][0]
                        hint_var, hint_bit = c.item.hint_bit
                        self.eventscripts[hint_event].insert(0, new_command(hint_event, "jmp_if_bit_clear", [hint_var, hint_bit, sound_command["identifier"]]))

        ######### shops

        if self.settings.is_flag_value(flags.ShuffleShops, True):
            # block off any shops that ended up with no items
            # if room service menu, replace with a blue dialog that says "It's broken"
            # otherwise, replace with a dialog that says "Sorry, we're all sold out today."
            for s in [s for s in (self.shops + self.special_shops)]:
                if self.settings.is_flag_value(flags.ShopQuality, ShopQualities.Empty) or len(s.items) == 0:
                    if utils.isclass_or_instance(s, data.shops.MolevilleTreasureShop):
                        self.prepend_bits(192, [[0x7088, 0], [0x7088, 1], [0x7088, 2]])
                    elif utils.isclass_or_instance(s, data.shops.DiscipleShop):
                        self.prepend_bits(192, [[0x704A, 4], [0x704A, 5], [0x704A, 6], [0x704A, 7], [0x704B, 0]])
                    elif utils.isclass_or_instance(s, data.shops.RoomServiceShop):
                        self.eventscripts[s.event_id] = [
                            new_command(s.event_id, "run_dialog", [3158, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]),
                            new_command(s.event_id, "ret"),
                        ]
                    else:
                        self.eventscripts[s.event_id] = [
                            new_command(s.event_id, "run_dialog", [3159, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]),
                            new_command(s.event_id, "ret"),
                        ]
                # build room service shop
                elif utils.isclass_or_instance(s, data.shops.RoomServiceShop):
                    # cheaper item should be first
                    if (s.items[0].price < s.items[1].price):
                        rs_item_1 = s.items[0]
                        rs_item_2 = s.items[1]
                    else:
                        rs_item_1 = s.items[1]
                        rs_item_2 = s.items[0]
                    # prices reduced to 75% (kerokerocola baseline)
                    price_1 = max(2, (rs_item_1.price * 0.75) // 1)
                    price_2 = max(2, (rs_item_1.price * 0.75) // 1)
                    menu_string_1 = rs_item_1.room_service
                    if (price_1 < 100):
                        menu_string_1 += "."
                    if (price_1 < 10):
                        menu_string_1 += "."
                    menu_string_2 = rs_item_2.room_service
                    if (price_2 < 100):
                        menu_string_2 += "."
                    if (price_2 < 10):
                        menu_string_2 += "."
                    # write dialog
                    self.replace_dialog(3847, '''[page]\n Here is the menu.[await]\n [select]  (%s%i Coins)\n [select]  (%s%i Coins)\n [select]  (No thanks)[await]''' % (menu_string_1, price_1, menu_string_2, price_2))
                    # replace the item and price values with new ones
                    for c in range(len(self.eventscripts[3657])):
                        cmd = self.eventscripts[3657][c]
                        if cmd[c]["command"] == "set" and cmd[c]["args"][0] == 0x70a7 and cmd[c]["args"][1] == 102:
                            cmd = self.eventscripts[3657][c]["args"][1] = rs_item_1.index
                        elif cmd[c]["command"] == "set" and cmd[c]["args"][0] == 0x70a7 and cmd[c]["args"][1] == 108:
                            cmd = self.eventscripts[3657][c]["args"][1] = rs_item_2.index
                        elif cmd[c]["command"] == "set" and (cmd[c]["args"][0] == 0x7000 or cmd[c]["args"][0] == 0x7024) and cmd[c]["args"][1] == 10:
                            cmd = self.eventscripts[3657][c]["args"][1] = price_1
                        elif cmd[c]["command"] == "set" and (cmd[c]["args"][0] == 0x7000 or cmd[c]["args"][0] == 0x7024) and cmd[c]["args"][1] == 150:
                            cmd = self.eventscripts[3657][c]["args"][1] = price_2
                # build trade shop
                elif utils.isclass_or_instance(s, data.shops.RoomServiceShop):
                    ts_item_1 = s.items[0]
                    ts_item_2 = s.items[1]
                    ts_item_3 = s.items[2]
                    self.replace_dialog(1217, ''' If we total that up, you've got\n [0x7000] points![await][page]\n You have more than 100 points,\n so go ahead and choose an item.[await][page]\n  [select]  (%s)\n  [select]  (%s)\n  [select]  (%s)[await]''' % (ts_item_1.item_name, ts_item_2.item_name, ts_item_3.item_name))
                    self.replace_dialog(1175, '''\n  Bring your unwanted items here![await][page]\n  We'll exchange your Mushrooms\n       and Syrups for points.[await]\n        For every 100 points\n    you'll get an item in return![await][page]\n           You can choose\n     one of the following gifts\n       to take away with you.[await][page]\n  1)“%s”\n  2)“%s”\n  3)“%s”[await]''' % (ts_item_1.item_name, ts_item_2.item_name, ts_item_3.item_name))
                    for c in range(len(self.eventscripts[1636])):
                        cmd = self.eventscripts[1636][c]
                        if cmd[c]["command"] == "set" and cmd[c]["args"][0] == 0x70a7 and cmd[c]["args"][1] == 144:
                            cmd = self.eventscripts[1636][c]["args"][1] = ts_item_1.index
                        elif cmd[c]["command"] == "set" and cmd[c]["args"][0] == 0x70a7 and cmd[c]["args"][1] == 113:
                            cmd = self.eventscripts[1636][c]["args"][1] = ts_item_2.index
                        elif cmd[c]["command"] == "set" and cmd[c]["args"][0] == 0x70a7 and cmd[c]["args"][1] == 114:
                            cmd = self.eventscripts[1636][c]["args"][1] = ts_item_3.index
        
        ########## boss NPCs
        fight_builders = {}
        sequence_setters = []


        for b in self.boss_locations:
            # create boss fight initiation builder
            boss = b.boss
            # 353 is the event ID that houses all the boss battle pack fight initiators
            # events for overworld NPCs/tiles that initiate these fights all reference event 353 in some way shape or form
            if 353 not in fight_builders:
                fight_builders[353] = {
                    "jumps": [],
                    "executions": []
                }
            # fights with forced backgrounds need to have them, otherwise just use whatever the level's default background is
            # this -should- in theory prevent us from having to do tedious work to give "Mimics Anywhere" chest fights the right location backgrounds
            formation = b.formation
            if formation.required_battlefield is not None:
                cmds = [new_command(353, 'set_short', [0x700E, boss.pack_number]), new_command(353, 'start_battle_700E')]
            else:
                cmds = [new_command(353, 'start_battle', [boss.pack_number, formation.required_battlefield])]
            fight_builders[353]["executions"].extend(cmds)
            jmp = new_command(353, 'jmp_if_7000_equals_short', [b.identifier, cmds[0]["identifier"]])
            fight_builders[353]["jumps"].append(jmp)
            
            # put the shuffled boss names in dialogs that use them
            if utils.isclass_or_instance(b, data.bosses.Booster):
                self.search_replace_dialog("`TOWER_BOSS_1`", boss.name)
                random_bosses = random.sample([loc.boss.name for loc in self.boss_locations if not utils.isclass_or_instance(loc, data.bosses.Booster)], 3)
                self.search_replace_dialog("`RANDOM_BOSS_NAME_1`", random_bosses[0])
                self.search_replace_dialog("`RANDOM_BOSS_NAME_2`", random_bosses[1])
                self.search_replace_dialog("`RANDOM_BOSS_NAME_3`", random_bosses[2])

            # prepare overworld to handle shuffled boss sprites
            for boss_location in b.boss_locations:
                occupant = boss_location.occupant

                # some of these operations will apply to clones, so need a completely distinct array
                flattened_object_array = []
                for index, obj in enumerate(self.rooms[boss_location.room_id]["objects"]):
                    clones = copy.copy(obj["clones"])
                    o = copy.copy(obj)
                    o["clones"] = []
                    o["original_index"] = index
                    flattened_object_array.append(o)
                    for index2, obj2 in clones:
                        o2 = copy.copy(obj2)
                        o2["parent_index"] = index
                        o2["clone_index"] = index2
                        flattened_object_array.append(o2)

                # replace and animate the models
                for index, obj in enumerate(flattened_object_array):
                    if index == boss_location.npc_id:
                        preferred_size = None
                        # pick the model from what the incoming boss has available according to what the location prefers
                        if boss_location.preferred_size == SpriteSize.Attack:
                            if occupant.attack_models is not None:
                                preferred_size = SpriteSize.Attack
                            elif occupant.big_model is not None:
                                preferred_size = SpriteSize.Large
                            else:
                                preferred_size = SpriteSize.Small
                        elif boss_location.preferred_size == SpriteSize.Large:
                            if occupant.big_model is not None:
                                preferred_size = SpriteSize.Large
                            else:
                                preferred_size = SpriteSize.Small
                        elif boss_location.preferred_size == SpriteSize.Statue:
                            if occupant.statue_model is not None:
                                preferred_size = SpriteSize.Statue
                            else:
                                preferred_size = SpriteSize.Small
                        else:
                            preferred_size = SpriteSize.Small

                        if preferred_size == SpriteSize.Small:
                            model = occupant.small_model
                        elif preferred_size == SpriteSize.Statue:
                            model = occupant.statue_model
                        elif preferred_size == SpriteSize.Large:
                            model = occupant.big_model
                        elif preferred_size == SpriteSize.Attack:
                            model = occupant.attack_model
                        if model is None:
                            raise Exception("what boss did you try to put here?")

                        # set directional capability
                        if model.model_details is not None:
                            model.directional_capability = model.model_details["vram_store"]
                        else:
                            model.directional_capability = self.models[model.model_id]["vram_store"]


                        # replace the models

                        if obj["original_index"] is not None:

                            if preferred_size == SpriteSize.Small:
                                self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["model"] = model.model_id

                            elif preferred_size == SpriteSize.Statue:
                                self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["model"] = model.model_id
                                
                            elif preferred_size == SpriteSize.Large:
                                model_num = self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["model"]
                                self.models[model_num] = model.model_details

                            elif preferred_size == SpriteSize.Attack:
                                model_num = self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["model"]
                                self.models[model_num] = model.model_details


                        current_direction = self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["direction"]
                        new_direction = current_direction

                        # swap directions for scarecrow sprites
                        if self.models[model_num]["sprite"] == SpriteName._39_RED_SCARECROW:
                            if current_direction == RadialDirection.SOUTHWEST:
                                new_direction = RadialDirection.NORTHWEST
                            elif current_direction == RadialDirection.NORTHWEST:
                                new_direction = RadialDirection.SOUTHEAST
                            elif current_direction == RadialDirection.NORTHEAST:
                                new_direction = RadialDirection.SOUTHWEST
                            elif current_direction == RadialDirection.SOUTHEAST:
                                new_direction = RadialDirection.NORTHEAST
                                
                        if obj["original_index"] is not None:
                            self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["direction"] = new_direction
                        else:
                            self.rooms[boss_location.room_id]["objects"][obj["parent_index"]]["clones"][obj["clone_index"]]["direction"] = new_direction

                        # statues: flip directions where necessary
                        if boss_location.preferred_size == SpriteSize.Statue:

                            self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["set_sequence_playback"] = False

                            if obj["original_index"] is not None:
                                model_num = self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["model"]
                            else:
                                model_num = self.rooms[boss_location.room_id]["objects"][obj["parent_index"]]["model"] + self.rooms[boss_location.room_id]["objects"][obj["parent_index"]]["clones"][obj["clone_index"]]["npc_id_offset"]
                            
                            eligible_directions = self.models[model_num]["vram_store"]

                            # replace directions on original room objects
                            if eligible_directions == VramStore._02_SWSE:
                                new_direction = RadialDirection.SOUTHWEST
                                if obj["original_index"] is not None:
                                    self.rooms[boss_location.room_id]["objects"][obj["original_index"]]["direction"] = new_direction
                                else:
                                    self.rooms[boss_location.room_id]["objects"][obj["parent_index"]]["clones"][obj["clone_index"]]["direction"] = new_direction
                            
                            # guarantee freeze
                            if boss_location.sequence_setter not in sequence_setters:
                                sequence_setters[boss_location.sequence_setter] = []
                            cmd = new_animation(boss_location.sequence_setter, 'action_queue_async', boss_location.npc_id, [{"identifier": "dummy", "command": "sequence_playback_off"}])
                            sequence_setters[boss_location.sequence_setter].append(cmd)

                            # pixel shifts
                            if (new_direction == RadialDirection.SOUTHEAST or new_direction == RadialDirection.SOUTHWEST) and (model.horizontal_pixel_shift > 0 or model.vertical_pixel_shift > 0):
                                horizontal_shift = 0xFF & (0xFF + model.horizontal_pixel_shift + 1)
                                vertical_shift = 0xFF & (0xFF + model.vertical_pixel_shift + 1)
                                cmd = new_animation(boss_location.sequence_setter, 'action_queue_async', boss_location.npc_id, [{"identifier": "dummy", "command": "shift_xy_pixels", "args": [horizontal_shift, vertical_shift]}])
                                sequence_setters[boss_location.sequence_setter].append(cmd)
                            elif (new_direction == RadialDirection.NORTHEAST or new_direction == RadialDirection.NORTHWEST) and (model.north_facing_horizontal_pixel_shift > 0 or model.north_facing_vertical_pixel_shift > 0):
                                if new_direction == RadialDirection.NORTHEAST:
                                    horizontal_shift = 0xFF & (0xFF + (-1 * model.north_facing_horizontal_pixel_shift) + 1)
                                    vertical_shift = 0xFF & (0xFF + (-1 * model.north_facing_vertical_pixel_shift) + 1)
                                elif new_direction == RadialDirection.NORTHWEST:
                                    horizontal_shift = 0xFF & (0xFF + model.north_facing_horizontal_pixel_shift + 1)
                                    vertical_shift = 0xFF & (0xFF + model.north_facing_vertical_pixel_shift + 1)
                                cmd = new_animation(boss_location.sequence_setter, 'action_queue_async', boss_location.npc_id, [{"identifier": "dummy", "command": "shift_xy_pixels", "args": [horizontal_shift, vertical_shift]}])
                                sequence_setters[boss_location.sequence_setter].append(cmd)



                        # if model requires a specific sequence or mold, set it now in room loader subroutine
                        sprite_offset = model.sprite_offset
                        if model.model_details is not None and model.model_details["sprite"] == SpriteName._221_YARIDOVICH_OUT_OF_BATTLE and (utils.isclass_or_instance(b, data.bosses.Boomer) or utils.isclass_or_instance(b, data.bosses.Smithy)):
                            pass # mid-sized yaridovich should NOT be set to sequence 1 in these particular locations
                        elif model.sequence_type == SequenceType.Mold or model.sequence > 0:
                            if boss_location.sequence_setter not in sequence_setters:
                                sequence_setters[boss_location.sequence_setter] = []
                            if model.sequence_type == SequenceType.Mold:
                                cmd = new_animation(boss_location.sequence_setter, 'action_queue_async', boss_location.npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.mold, sprite_offset, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_MOLD]]}])
                            else:
                                cmd = new_animation(boss_location.sequence_setter, 'action_queue_async', boss_location.npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.sequence, sprite_offset, [_0x08Flags.READ_AS_SEQUENCE]]}])
                            sequence_setters[boss_location.sequence_setter].append(cmd)
                            # and then, get rid of any commands that may un-set the sequence or mold
                            for script_id in boss_location.target_scripts:
                                script = self.eventscripts[script_id]
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, boss_location.npc_id):
                                        command["subscript"] = remove_sequence_changes_from_action_script(command["subscript"])
                                        self.eventscripts[script_id][command_index] = command
                            for script_id in boss_location.target_action_scripts:
                                self.actionscripts[script_id] = remove_sequence_changes_from_action_script(self.actionscripts[script_id])
                               

                       
                        # replace model sprite if necessary
                        if utils.isclass_or_instance(b, data.bosses.Croco1) and model.animations.bandits_way_distracted.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.bandits_way_distracted.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Punchinello) and model.animations.mines_punch.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.mines_punch.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Booster) and model.animations.chapel_laugh.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.chapel_laugh.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.KingCalamari) and model.animations.ship_beckon.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.ship_beckon.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Johnny) and model.animations.ship_chair.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.ship_chair.new_sprite_id
                        elif (utils.isclass_or_instance(b, data.bosses.Jinx1) or utils.isclass_or_instance(b, data.bosses.Jinx2) or utils.isclass_or_instance(b, data.bosses.Jinx3) or utils.isclass_or_instance(b, data.bosses.Jagger)) and model.animations.dojo_challenge.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.dojo_challenge.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Dodo) and model.animations.statue_peck.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.statue_peck.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Magikoopa) and model.animations.keep_challenge.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.keep_challenge.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Magikoopa) and model.animations.keep_summon.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.keep_summon.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Boomer) and model.animations.chandelier_challenge.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.chandelier_challenge.new_sprite_id
                        elif utils.isclass_or_instance(b, data.bosses.Smithy) and model.animations.endgame_challenge.new_sprite_id is not None:
                            self.models[model.model_id]["sprite"] = model.animations.endgame_challenge.new_sprite_id

                        if not is_vanilla(boss, boss_location):
                            # hide composite NPCs that aren't used if shuffled
                            if utils.isclass_or_instance(b, data.bosses.Gunyolk):
                                self.rooms[470]["objects"][0]["visible"] = False
                                self.rooms[470]["objects"][0]["clones"][0]["visible"] = False
                                self.rooms[470]["objects"][0]["clones"][1]["visible"] = False
                                self.rooms[470]["objects"][0]["clones"][3]["visible"] = False
                                self.rooms[470]["objects"][0]["clones"][4]["visible"] = False
                                self.rooms[470]["objects"][0]["clones"][5]["visible"] = False

                            # hide composite NPCs that aren't used if shuffled
                            if utils.isclass_or_instance(b, data.bosses.Smithy):
                                self.rooms[509]["objects"] = copy.copy()

                        # TODO: partitions

                        # SPECIAL ANIMATIONS
                        for script_id in boss_location.target_scripts:
                            
                            if not is_vanilla(boss, boss_location):

                                script = self.eventscripts[script_id]


                                # adjust mines punch pause, still perform sanitization at the end
                                if utils.isclass_or_instance(b, data.bosses.Punchinello) and script_id == 860:
                                    pause = 10
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, boss_location.npc_id):
                                            if model.animations.mines_punch is not None:
                                                if model.animations.mines_punch.contact_frame > 0:
                                                    pause = model.animations.mines_punch.contact_frame + 8
                                                else:
                                                    pause = model.animations.mines_punch.total_duration
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if subscript_command["command"] == 'pause':
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                        elif is_mario_animation_header(command):
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if subscript_command["command"] == 'pause':
                                                    subscript_command["args"][0] = pause - 2
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                        elif command["command"] == "pause":
                                            self.eventscripts[script_id][command_index]["args"][0] = pause - 4
                                            
                                # magikoopa needs pauses adjusted, still perform sanitization at the end
                                if utils.isclass_or_instance(b, data.bosses.Magikoopa) and model.animations.keep_summon is not None and script_id == 941:
                                    if model.animations.keep_summon.contact_frame is not None:
                                        self.eventscripts[script_id][1]["args"][0] = model.animations.keep_summon.contact_frame + 16


                                # adjust dojo pause
                                if utils.isclass_or_instance(b, data.bosses.Jagger) and model.animations.dojo_challenge is not None and script_id == 861:
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, boss_location.npc_id):
                                            pause = max(45, model.animations.dojo_challenge.total_duration)
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                elif utils.isclass_or_instance(b, data.bosses.Jinx1) and model.animations.dojo_challenge is not None:
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, boss_location.npc_id):
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if (script_id == 862):
                                                    pause = max(45, model.animations.dojo_challenge.total_duration)
                                                    if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                        subscript_command["args"][0] = pause
                                                        command["subscript"][subscript_command_index] = subscript_command
                                                elif (script_id == 863):
                                                    if subscript_command["command"] == 'pause' and subscript_command["args"] == 18:
                                                        subscript_command["args"][0] = model.animations.dojo_challenge.total_duration
                                                        command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                elif utils.isclass_or_instance(b, data.bosses.Jinx2) and model.animations.dojo_challenge is not None:
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, boss_location.npc_id):
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if (script_id == 864):
                                                    pause = max(45, model.animations.dojo_challenge.total_duration)
                                                    if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                        subscript_command["args"][0] = pause
                                                        command["subscript"][subscript_command_index] = subscript_command
                                                elif (script_id == 865):
                                                    if subscript_command["command"] == 'pause' and subscript_command["args"] == 18:
                                                        subscript_command["args"][0] = model.animations.dojo_challenge.total_duration
                                                        command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                elif utils.isclass_or_instance(b, data.bosses.Jinx3) and model.animations.dojo_challenge is not None and script_id == 866:
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, boss_location.npc_id):
                                            pause = max(45, model.animations.dojo_challenge.total_duration)
                                            for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            self.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                            

                                # dodo statue subroutines need some explicitly written pauses
                                elif utils.isclass_or_instance(b, data.bosses.Dodo) and (script_id == 936):
                                    if model.animations.statue_peck is None:
                                        self.eventscripts[script_id] = statue_bonk
                                    else:
                                        rewritten_peck_subroutine = [
                                            {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                            {"identifier": 'dummy', "command": 'set_animation_speed', "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]},
                                            {"identifier": 'dummy', "command": 'pause', "args": [3]},
                                            {"identifier": 'dummy', "command": 'face_southwest'},
                                            {"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]}
                                        ]

                                        peck_duration = model.animations.statue_peck.contact_frame
                                        if peck_duration > 19 or peck_duration is None:
                                            raise Exception('%s statue peck animation contact frame is illegal value' % boss.name)
                                        animation_wait = 15 + 16 - peck_duration
                                        animation_duration = peck_duration + 3
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_wait]})
                                        
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'sequence_looping_on'})
                                        
                                        # set animation speed & sequence
                                        if model.animations.statue_peck.speed is not None:
                                            rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_animation_speed', "args": [model.animations.statue_peck.speed, [_0x10Flags.SEQUENCE]]})
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.statue_peck.sequence_id, 0, [_0x08Flags.LOOPING_OFF]]}) # no support for increased sprite #, but no use case for it yet
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_duration]})
                                        
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]})
                                        
                                        self.eventscripts[script_id][0]["subscript"] = copy.copy(rewritten_peck_subroutine)
                                
                                elif utils.isclass_or_instance(b, data.bosses.Dodo) and (script_id == 937):
                                    if model.animations.statue_peck is None:
                                        self.eventscripts[script_id] = statue_bonk_mario
                                    else:
                                        rewritten_peck_subroutine = [
                                            {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                            {"identifier": 'dummy', "command": 'sequence_looping_on'},
                                            {"identifier": 'dummy', "command": 'set_animation_speed', "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]}
                                        ]

                                        if peck_duration > 20 or peck_duration is None:
                                            raise Exception('%s statue peck animation contact frame is illegal value' % boss.name)
                                        animation_wait = max(16 - peck_duration, 0)
                                        animation_duration = 20 - animation_wait
                                        if animation_wait > 0:
                                            rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_wait]})
                                        # set animation speed & sequence
                                        if model.animations.statue_peck.speed is not None:
                                            rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_animation_speed', "args": [model.animations.statue_peck.speed, [_0x10Flags.SEQUENCE]]})
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.statue_peck.sequence_id, 0, [_0x08Flags.LOOPING_OFF]]}) # no support for increased sprite #, but no use case for it yet
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_duration]})

                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'sequence_looping_off'})
                                        
                                        self.eventscripts[script_id][0]["subscript"] = copy.copy(rewritten_peck_subroutine)

                                elif utils.isclass_or_instance(b, data.bosses.Dodo) and (script_id == 939) and model.animations.statue_intro is not None:
                                    rewritten_intro_subroutine = [
                                        {"identifier": 'dummy', "command": 'shift_to_xy_coords', 'args': [2, 56]},
                                        {"identifier": 'dummy', "command": 'shift_southwest_pixels', 'args': [5]},
                                        {"identifier": 'dummy', "command": 'shift_southeast_pixels', 'args': [16]},
                                        {"identifier": 'dummy', "command": 'sequence_playback_off'},
                                        {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]},
                                        {"identifier": 'dummy', "command": 'visibility_on'},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [31]},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [31]},
                                        {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]},
                                        {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                        {"identifier": 'dummy', "command": 'sequence_looping_on'}
                                    ]

                                    if model.animations.statue_intro.total_duration is not None:
                                        intro_duration = min(model.animations.statue_intro.total_duration, 66)
                                        if intro_duration < 66:
                                            rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [66 - intro_duration]})
                                        rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_intro.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]})
                                        rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [intro_duration]})
                                    else:
                                        rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_intro.sequence_id, 0, [_0x08Flags.MIRROR_SPRITE]]})
                                        rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [66]})

                                    rewritten_intro_subroutine.extend([
                                        {"identifier": 'dummy', "command": 'sequence_looping_off'},
                                        {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [17]}
                                    ])

                                    self.eventscripts[script_id][0]["subscript"] = copy.copy(rewritten_intro_subroutine)

                                elif utils.isclass_or_instance(b, data.bosses.Dodo) and (script_id == 940) and model.animations.statue_flustered is not None:
                                    rewritten_recoil_subroutine = [
                                        {"identifier": 'dummy', "command": 'shift_to_xy_coords', 'args': [7, 66]},
                                        {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [20]},
                                        {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]},
                                    ]

                                    rewritten_recoil_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_flustered.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]})
                                    rewritten_recoil_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [45]})

                                    self.eventscripts[script_id][0]["subscript"] = copy.copy(rewritten_recoil_subroutine)


                                elif utils.isclass_or_instance(b, data.bosses.Magikoopa) and (script_id == 942):
                                    if model.animations.keep_summon is not None:
                                        rewritten_keep_subscript = [
                                            {"identifier": 'dummy', "command": 'face_southeast'},
                                            {"identifier": 'dummy', "command": 'pause', 'args': [60]},
                                            {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.keep_summon.sequence_id, 0, [_0x08Flags.MIRROR_SPRITE, _0x08Flags.READ_AS_SEQUENCE]]},
                                            {"identifier": 'dummy', "command": 'pause', 'args': [model.animations.keep_summon.total_duration]},
                                        ]
                                    else:
                                        rewritten_keep_subscript = [
                                            {"identifier": 'dummy', "command": 'face_southeast'},
                                            {"identifier": 'dummy', "command": 'pause', 'args': [60]}
                                        ]

                                    rewritten_keep_event = [
                                        {"identifier": 'EVENT_942_action_queue_async', "command": 'action_queue_async', 'args': [AreaObjects.NPC_1], "subscript": rewritten_keep_subscript},
                                        {"identifier": 'EVENT_942_ret_291', "command": 'ret'},
                                    ]

                                    self.eventscripts[script_id] = copy.copy(rewritten_keep_event)

                                # boomer will need pause adjustments
                                elif utils.isclass_or_instance(b, data.bosses.Boomer) and (script_id == 943):
                                    rewritten_chandelier_subscript = [
                                        {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]},
                                        {"identifier": 'dummy', "command": 'fixed_f_coord_on'},
                                        {"identifier": 'dummy', "command": 'pause', "args": [20]},
                                        {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]}
                                    ]
                                    if model.animations.chandelier_challenge is not None:
                                        rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.chandelier_challenge.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]})
                                        if model.animations.total_duration is not None:
                                            rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [model.animations.chandelier_challenge.total_duration + 29]})
                                        else:
                                            rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [45]})
                                    else:
                                        rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [45]})
                                    
                                    self.eventscripts[script_id][0]["subscript"] = copy.copy(rewritten_chandelier_subscript)

                                # smithy needs A LOT of adjustments, to the point of complete script replacement and npc removal
                                elif utils.isclass_or_instance(b, data.bosses.Smithy) and (script_id == 3792):
                                    self.eventscripts[script_id] = copy.copy(non_smithy_3792)
                                elif utils.isclass_or_instance(b, data.bosses.Smithy) and (script_id == 3794):
                                    self.eventscripts[script_id] = copy.copy(non_smithy_3794)
                                    if model.animations.endgame_challenge is not None:
                                        if model.animations.endgame_challenge.total_duration is not None:
                                            challenge_duration = model.animations.endgame_challenge.total_duration
                                            if challenge_duration > 55:
                                                self.eventscripts[945][0]["args"] = challenge_duration
                                                self.eventscripts[946][0]["subscript"].insert(0, {"identifier": "dummy", "command": "pause", "args": [challenge_duration - 55]})
                                            endgame_animation = {"identifier": "EVENT_944_taunt", "command": 'action_queue_sync', "args": [AreaObjects.NPC_6], "subscript": [{"identifier": "dummy", "command": 'set_sprite_sequence', 'args': [model.animations.endgame_challenge.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.LOOPING_OFF]]}]}
                                            self.eventscripts[944].insert(0, endgame_animation)
                                        else:
                                            endgame_animation = {"identifier": "EVENT_944_taunt", "command": 'action_queue_sync', "args": [AreaObjects.NPC_6], "subscript": [{"identifier": "dummy", "command": 'set_sprite_sequence', 'args': [model.animations.endgame_challenge.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE]]}]}
                                            self.eventscripts[944].insert(0, endgame_animation)


                                                

                                else:
                                    # replace all sequences and molds if appropriate, remove if not
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, henchman_location.npc_id):
                                            self.eventscripts[script_id][command_index] = sanitize_animation_script(henchman_location.occupant, b, command, model)



                        # action scripts
                        for script_id in boss_location.target_action_scripts:
                            script = self.actionscripts[script_id]

                            # adjust kitchen animation pauses
                            if utils.isclass_or_instance(b, data.bosses.Magikoopa) and script_id == 1004 and model.animations.keep_summon is not None:
                                for subscript_command_index, subscript_command in enumerate(script):
                                    # set the proper animation for the sprite, and determine if it should loop or not
                                    if subscript_command["command"] == 'set_sprite_sequence':
                                        subscript_command["args"][0] = model.animations.keep_summon.sequence_id
                                        self.actionscripts[script_id][subscript_command_index] = subscript_command

                            # replace all sequences and molds if appropriate, remove if not
                            else:
                                self.actionscripts[script_id] = sanitize_animation_script(boss, b, script, model)


                        # if model is a scarecrow, fix all of its directional commands
                        model_info = self.models[model.model_id]
                        if model_info["sprite"] == SpriteName._39_RED_SCARECROW:
                            for script_id in boss_location.target_scripts:
                                script = self.eventscripts[script_id]
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, boss_location.npc_id):
                                        command["subscript"] = fix_script_for_scarecrow(command["subscript"])
                                        self.eventscripts[script_id][command_index] = command
                            for script_id in boss_location.target_action_scripts:
                                self.actionscripts[script_id] = fix_script_for_scarecrow(self.actionscripts[script_id])
                            


                        # replace relevant dialogs
                        for dialog_id in boss_location.dialogs:
                            for d_id, d_data in occupant.dialog_replacements:
                                if d_id == dialog_id:
                                    self.replace_dialog(d_id, d_data)
                            if self.settings.is_flag_value(flags.BossReplaceMinigameSprites, True):
                                for d_id, d_data in occupant.optional_dialog_replacements:
                                    if d_id == dialog_id:
                                        self.replace_dialog(d_id, d_data)

            # Replace the henchmen in each room
            for u in b.unique_henchmen + b.repeatable_henchmen:
                for henchman_location in u:
                    occupant = henchman_location.occupant
                    

                    # some of these operations will apply to clones, so need a completely distinct array
                    flattened_object_array = []
                    for index, obj in enumerate(self.rooms[henchman_location.room_id]["objects"]):
                        clones = copy.copy(obj["clones"])
                        o = copy.copy(obj)
                        o["clones"] = []
                        o["original_index"] = index
                        flattened_object_array.append(o)
                        for index2, obj2 in clones:
                            o2 = copy.copy(obj2)
                            o2["parent_index"] = index
                            o2["clone_index"] = index2
                            flattened_object_array.append(o2)

                    for index, obj in enumerate(flattened_object_array):
                        if index == henchman_location.npc_id:
                            model = occupant.model

                            model.directional_capability = self.models[model.model_id]["vram_store"]
                            
                            # if model requires a specific sequence or mold, set it now in room loader subroutine
                            sprite_offset = model.sprite_offset
                            if model.sequence_type == SequenceType.Mold or model.sequence > 0:
                                if henchman_location.sequence_setter not in sequence_setters:
                                    sequence_setters[henchman_location.sequence_setter] = []
                                if model.sequence_type == SequenceType.Mold:
                                    cmd = new_animation(henchman_location.sequence_setter, 'action_queue_async', henchman_location.npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.mold, sprite_offset, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_MOLD]]}])
                                else:
                                    cmd = new_animation(henchman_location.sequence_setter, 'action_queue_async', henchman_location.npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.sequence, sprite_offset, [_0x08Flags.READ_AS_SEQUENCE]]}])
                                sequence_setters[henchman_location.sequence_setter].append(cmd)
                                # and then, get rid of any commands that may un-set the sequence or mold
                                for script_id in henchman_location.target_scripts:
                                    script = self.eventscripts[script_id]
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, henchman_location.npc_id):
                                            command["subscript"] = remove_sequence_changes_from_action_script(command["subscript"])
                                            self.eventscripts[script_id][command_index] = command
                                for script_id in henchman_location.target_action_scripts:
                                    self.actionscripts[script_id] = remove_sequence_changes_from_action_script(self.actionscripts[script_id])
                            
                            # replace model sprite if necessary
                            if utils.isclass_or_instance(b, data.bosses.Booster) and model.animations.tower_bullet.new_sprite_id is not None:
                                self.models[model.model_id]["sprite"] = model.animations.tower_bullet.new_sprite_id
                            elif utils.isclass_or_instance(b, data.bosses.Bundt) and model.animations.kitchen_prep.new_sprite_id is not None:
                                self.models[model.model_id]["sprite"] = model.animations.kitchen_prep.new_sprite_id


                            # update model packs & pack container events
                            self.rooms[henchman_location.room_id][index]["model"] = occupant.model_id

                            if henchman_location.model_type == HenchmanType.Event or henchman_location.model_type == HenchmanType.ExternalEvent:
                                if henchman_location.event_id not in fight_builders:
                                    fight_builders[henchman_location.event_id] = {
                                        "jumps": [new_command(henchman_location.event_id, 'set_7000_to_current_level')],
                                        "executions": []
                                    }
                                cmds = [new_command(henchman_location.event_id, 'set_short', [0x700E, occupant.pack_number]), new_command(henchman_location.event_id, 'start_battle_700E')]
                                fight_builders[henchman_location.event_id]["executions"].extend(cmds)
                                jmp = new_command(henchman_location.event_id, 'jmp_if_7000_equals_short', [henchman_location.room_id, cmds[0]["identifier"]])
                                fight_builders[henchman_location.event_id]["jumps"].append(jmp)
                            elif henchman_location.model_type == HenchmanType.Pack:
                                self.rooms[henchman_location.room_id][ctr]["battle_pack"] = occupant.pack_number


                            # SPECIAL ANIMATIONS
                            if not is_vanilla(boss, boss_location):

                                # event scripts
                                for script_id in henchman_location.target_scripts:
                                    # event scripts
                                    script = self.eventscripts[script_id]

                                    # replace all sequences and molds if appropriate, remove if not
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, henchman_location.npc_id):
                                            self.eventscripts[script_id][command_index] = sanitize_animation_script(boss, b, command, model)

                                # action scripts
                                for script_id in henchman_location.target_action_scripts:
                                    script = self.actionscripts[script_id]

                                    # adjust kitchen animation pauses
                                    if utils.isclass_or_instance(b, data.bosses.Bundt) and script_id in [330,331] and model.animations.kitchen_prep is not None:
                                        for subscript_command_index, subscript_command in enumerate(script):
                                            # set the proper animation for the sprite, and determine if it should loop or not
                                            if subscript_command["command"] == 'set_sprite_sequence':
                                                subscript_command["args"][0] = model.animations.kitchen_prep.sequence_id
                                                cmd_flags = subscript_command["args"][2]
                                                cmd_flags = [f for f in cmd_flags if f is not _0x08Flags.LOOPING_OFF]
                                                if model.animations.kitchen_prep.total_duration is not None:
                                                    cmd_flags.append(_0x08Flags.LOOPING_OFF)
                                                subscript_command["args"][2] = copy.copy(cmd_flags)
                                                self.actionscripts[script_id][subscript_command_index] = subscript_command
                                            # set the pause to last for the entirety of the animation, if not looped
                                            elif subscript_command["command"] == 'pause' and subscript_command["args"][0] == 20:
                                                if model.animations.kitchen_prep.total_duration is not None:
                                                    subscript_command["args"][0] = model.animations.kitchen_prep.total_duration
                                                    self.actionscripts[script_id][subscript_command_index] = subscript_command
                                            
                                    # overwrite snifit 3's bullet script
                                    elif utils.isclass_or_instance(b, data.bosses.Booster) and script_id == 386:
                                        # replace the entire contents of snifit bullet script
                                        if model.animations.tower_bullet is None:
                                            self.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [56]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ]
                                        elif model.animations.tower_bullet.total_duration is None:
                                            self.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_set_sprite_sequence_16', "command": 'set_sprite_sequence', "args": [model.animations.tower_bullet.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE]]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [56]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ]
                                        else:
                                            contact = model.animations.tower_bullet.total_duration
                                            if model.animations.tower_bullet.contact_frame is not None:
                                                contact = model.animations.tower_bullet.contact_frame
                                            if contact > 63: # figure out what to do here, how does the math work out if you speed it up...
                                                pass
                                            self.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [64 - contact]},
                                                {"identifier": 'ACTION_386_set_sprite_sequence_16', "command": 'set_sprite_sequence', "args": [model.animations.tower_bullet.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.LOOPING_OFF]]},
                                                {"identifier": 'ACTION_386_pause_intermediate', "command": 'pause', "args": [contact - 8]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ]

                                    # replace all sequences and molds if appropriate, remove if not
                                    else:
                                        self.actionscripts[script_id] = sanitize_animation_script(boss, b, script, model)


                            
        # finalize battle pack scripts and sequence setter scripts
        for e in fight_builders:
            fight_builders[e]["jumps"].append(new_command(e, "ret"))
            self.eventscripts[e] = copy.copy(fight_builders[e]["jumps"]) + copy.copy(fight_builders[e]["executions"])
        for e in sequence_setters:
            sequence_setters[e].append(new_command(e, "ret"))
            self.eventscripts[e] = copy.copy(sequence_setters[e])

        # figure out partitions



        ########## Finally, build patches

        # Shops

        for shop in self.shops:
            patch += shop.get_patch()

        # Patch removes ANDing by current party from shop menu code.
        # Replaces it with ANDing by #$1F, which is all party members.
        if self.settings.is_flag_value(flags.ShowEquips, True):
            patch.add_data(0x033B6D, bytes([0x29, 0x1F, 0xEA]))

        # Enemies
        for enemy in self.enemies:
            patch += enemy.get_patch()
            enemy.patch_script()
        patch += data.enemies.Enemy.build_psychopath_patch(self)

        # Enemy attacks
        for attack in self.enemy_attacks:
            patch += attack.get_patch()

        # Enemy formations
        for formation in self.enemy_formations:
            patch += formation.get_patch()

        # Enemy packs
        for pack in self.formation_packs:
            patch += pack.get_patch()








        # Characters
        for character in self.characters:
            patch += character.get_patch()

        # Update party join script events for the final order.  These are different for standard vs open mode.
        if self.open_mode:
            # Add characters to Mushroom Way and Moleville when NFC is turned on
            if self.settings.is_flag_enabled(flags.NoFreeCharacters):
                addresses = [0x1ef86c, 0x1ffd82, 0x1fc4f1, 0x1e6d58, 0x1e8b71]
            else:
                addresses = [0x1ef86c, 0x1ef86e, 0x1ef870, 0x1fc4f1, 0x1e8b71]
            dialogue_iterator = 0
            for addr, character in zip(addresses, self.meta_join_order):
                dialogue_iterator += 1
                # Character joins and dialogues are 0x9B by default, replaced with this code when populated
                if character is not None:
                    # Write message stating who joined
                    if character.palette is not None and character.palette.rename_character:
                        message = '"' + character.palette.name + '" (' + character.original_name + ') joins!'
                    else:
                        message = character.original_name + " joins!"
                    messagestring = binascii.hexlify(bytes(message, encoding='ascii'))
                    messagebytes = [int(messagestring[i:i + 2], 16) for i in range(0, len(messagestring), 2)]
                    messagebytes.append(0x00)
                    # Append character join event and corresponding message to code
                    if self.settings.is_flag_enabled(flags.NoFreeCharacters):
                        if dialogue_iterator == 2:
                            patch.add_data(0x242c52, messagebytes)
                            patch.add_data(0x1ffd84, [0x60, 0xac, 0xac, 0x00])
                        if dialogue_iterator == 3:
                            patch.add_data(0x221475, messagebytes)
                            patch.add_data(0x1fc8dd, [0x60, 0x48, 0xa2, 0x00])
                            # show character walking around forest maze
                        if dialogue_iterator == 4:
                            patch.add_data(0x242238, messagebytes)
                            patch.add_data(0x1e6d5a, [0x60, 0x89, 0xac, 0x00])
                        if dialogue_iterator == 5:
                            patch.add_data(0x23abf2, messagebytes)
                            patch.add_data(0x1e8b49, [0x60, 0xff, 0xaa, 0x00])
                    else:
                        if dialogue_iterator == 4:
                            patch.add_data(0x242c52, messagebytes)
                            patch.add_data(0x1fc8dd, [0x60, 0xac, 0xac, 0x00])
                        if dialogue_iterator == 5:
                            patch.add_data(0x221475, messagebytes)
                            patch.add_data(0x1e8b49, [0x60, 0x48, 0xa2, 0x00])
                    patch.add_data(addr, [0x36, 0x80 + character.index])
            dialogue_iterator = 0
            for character in self.character_join_order:
                dialogue_iterator += 1
                # replace overworld characters in recruitment spots - there are no partitions identical to 89 that have
                # CBC set to 3 instead of 4, so modify 89 since it's only used by this room

                if self.settings.is_flag_enabled(flags.NoFreeCharacters) and dialogue_iterator == 2:
                    # mushroom way
                    patch.add_data(0x14b3BC, character.mway_1_npc_id)
                    patch.add_data(0x14b411, character.mway_2_npc_id)
                    patch.add_data(0x14b452, character.mway_3_npc_id)
                    # change partition to accommodate mallow's sprite in mway
                    if character.name is "Mallow":
                        patch.add_data(0x1ddf67, 0x80)
                if ((dialogue_iterator == 4 and not self.settings.is_flag_enabled(flags.NoFreeCharacters)) or
                        (self.settings.is_flag_enabled(flags.NoFreeCharacters) and dialogue_iterator == 3)):
                    # forest maze
                    patch.add_data(0x14b8eb, character.forest_maze_sprite_id)
                    if character.name is "Mario":
                        patch.add_data(0x215e4f, 0x42)
                        patch.add_data(0x215e56, 0x12)
                if self.settings.is_flag_enabled(flags.NoFreeCharacters) and dialogue_iterator == 4:
                    # moleville
                    patch.add_data(0x14c491, character.moleville_sprite_id)
                    if character.name in ["Mario", "Peach", "Geno"]:
                        # patch moleville minecart room partition
                        patch.add_data(0x1DDF45, 0x81)
                        if character.name is "Mario":
                            patch.add_data(0x1DB801, 0x00)
                    # make cutscene look less weird
                    if character.name is not "Bowser":
                        patch.add_data(0x201F04, [0x3D, 0x02, 0x63])
                        if character.name is "Mario":
                            patch.add_data(0x201F07, 0x09)
                        elif character.name is "Peach":
                            patch.add_data(0x201F07, 0x0F)
                        elif character.name is "Mallow":
                            patch.add_data(0x201F07, 0x0E)
                        else:
                            patch.add_data(0x201F07, 0x0C)
                    patch.add_data(0x201F5B, 0x00)
                if dialogue_iterator == 5:
                    # show character in marrymore
                    patch.add_data(0x14a94d, character.forest_maze_sprite_id)
                    patch.add_data(0x148f91, character.forest_maze_sprite_id)
                    # fix booster hill solidity
                    if character.name is "Mallow":
                        patch.add_data(0x1DB819, [0x56, 0x2C])
                    elif character.name is "Geno":
                        patch.add_data(0x1DB820, 0x56)
                    elif character.name is "Mario":
                        patch.add_data(0x1DB804, 0x56)
                    elif character.name is "Peach":
                        patch.add_data(0x1DB80B, 0x56)
                    if character.name is not "Peach":
                        # marrymore sequence
                        if character.name is "Mario":
                            # surprised
                            patch.add_data(0x20d338, [0x08, 0x43, 0x00])
                            # on ground
                            patch.add_data(0x20d34e, [0x08, 0x4B, 0x01])
                            # sitting
                            patch.add_data(0x20d43b, [0x08, 0x4a, 0x1f])
                            # looking down
                            patch.add_data(0x20d445, [0x08, 0x48, 0x06])
                            patch.add_data(0x20d459, [0x08, 0x48, 0x06])
                            # crying
                            patch.add_data(0x20d464, [0x10, 0x80])
                            patch.add_data(0x20d466, [0x08, 0x43, 0x03])
                            # surprised
                            patch.add_data(0x20d48c, [0x08, 0x43, 0x00])
                            # looking down
                            patch.add_data(0x20d4d4, [0x08, 0x48, 0x06])
                            # crying
                            patch.add_data(0x20d4d9, [0x10, 0x80])
                            patch.add_data(0x20d4db, [0x08, 0x43, 0x03])
                            # surprised reversed
                            patch.add_data(0x20d5d8, [0x08, 0x43, 0x80])
                            # crying in other direction
                            patch.add_data(0x20d5e3, [0x08, 0x43, 0x84])
                            # booster hill
                            patch.add_data(0x207147, [0x08, 0x43, 0x89])
                            patch.add_data(0x20714E, [0x08, 0x43, 0x09])
                            patch.add_data(0x207160, [0x08, 0x43, 0x89])
                            patch.add_data(0x207165, [0x08, 0x43, 0x88])
                            patch.add_data(0x206b1a, [0x08, 0x43, 0x88])
                            patch.add_data(0x206d19, [0x08, 0x43, 0x89])
                            patch.add_data(0x206d20, [0x08, 0x43, 0x09])
                            patch.add_data(0x206d34, [0x08, 0x43, 0x89])
                            patch.add_data(0x206d39, [0x08, 0x43, 0x88])
                        else:
                            # surprised
                            patch.add_data(0x20d338, [0x08, 0x42, 0x00])
                            patch.add_data(0x20d48c, [0x08, 0x42, 0x00])
                            # surprised reversed
                            patch.add_data(0x20d5d8, [0x08, 0x42, 0x80])
                            # sitting
                            patch.add_data(0x20d43b, [0x08, 0x49, 0x1f])
                            #booster hill
                            patch.add_data(0x207147, [0x08, 0x42, 0x09])
                            patch.add_data(0x20714E, [0x08, 0x42, 0x89])
                            patch.add_data(0x207160, [0x08, 0x42, 0x09])
                            patch.add_data(0x207165, [0x08, 0x42, 0x88])
                            patch.add_data(0x206b1a, [0x08, 0x42, 0x88])
                            patch.add_data(0x206d19, [0x08, 0x42, 0x09])
                            patch.add_data(0x206d20, [0x08, 0x42, 0x89])
                            patch.add_data(0x206d34, [0x08, 0x42, 0x09])
                            patch.add_data(0x206d39, [0x08, 0x42, 0x88])
                            patch.add_data(0x206F40, [0x08, 0x42, 0x09])
                            if character.name is "Geno":
                                # crying
                                patch.add_data(0x20d464, [0x10, 0x80])
                                patch.add_data(0x20d466, [0x08, 0x40, 0x0B])
                                # surprised
                                patch.add_data(0x20d48c, [0x08, 0x42, 0x00])
                                # looking down
                                patch.add_data(0x20d4d4, [0x08, 0x48, 0x06])
                                # crying
                                patch.add_data(0x20d4d9, [0x10, 0x80])
                                patch.add_data(0x20d4db, [0x08, 0x40, 0x0B])
                                # surprised reversed
                                patch.add_data(0x20d5d8, [0x08, 0x42, 0x80])
                                # crying in other direction
                                patch.add_data(0x20d5e3, [0x08, 0x40, 0x8C])
                            else:
                                # surprised
                                patch.add_data(0x20d338, [0x08, 0x42, 0x00])
                                patch.add_data(0x20d48c, [0x08, 0x42, 0x00])
                                # surprised reversed
                                patch.add_data(0x20d5d8, [0x08, 0x42, 0x80])
                                # sitting
                                patch.add_data(0x20d43b, [0x08, 0x49, 0x1f])

        else:
            # For standard mode, Mario is the first character.  Update the other four only.
            addresses = [0x1e2155, 0x1fc506, 0x1edf98, 0x1e8b79]
            for addr, character in zip(addresses, self.character_join_order[1:]):
                patch.add_data(addr, 0x80 + character.index)

            # Update other battle scripts so Belome eats the first one to join.
            for addr in (
                    0x394b4d,
                    0x394b70,
                    0x394b74,
                    0x394b7d,
                    0x394b7f,
                    0x394b83,
                    0x3ab93f,
                    0x3ab95a,
            ):
                patch.add_data(addr, self.character_join_order[1].index)

        # Use first character to join as file select cursor.
        cursor_id = 0
        for character in self.character_join_order:
            if character is not None:
                cursor_id = character.index
                break

        # Learned spells and level-up exp.
        patch += self.levelup_xps.get_patch()

        # Spells
        for spell in self.spells:
            patch += spell.get_patch()

        #These spells are ignored when returning world.spells, so i'm applying the patch here to fix animation lag when randomized spells is turned on
        if self.settings.is_flag_enabled(flags.EnemySpells):
            patch.add_data(0x351415, [0x0a, 0x0a, 0x0a])
            patch.add_data(0x35142d, 0x0a)
            patch.add_data(0x35142f, [0x0a, 0x0a, 0x0a])
            patch.add_data(0x351449, 0x0a)
            patch.add_data(0x35144b, [0x0a, 0x0a, 0x0a])
            patch.add_data(0x351465, 0x0a)
            patch.add_data(0x351467, [0x0a, 0x0a, 0x0a])
            patch.add_data(0x351481, 0x0a)

        # Starting FP (twice for starting/max FP)
        patch.add_data(0x3a00dd, utils.ByteField(self.starting_fp).as_bytes() * 2)

        # For debug mode, start with 9999 coins and 99 frog coins.
        if self.debug_mode or self.settings.is_flag_enabled(flags.FreeShops):
            patch.add_data(0x3a00db, utils.ByteField(9999, num_bytes=2).as_bytes())
            patch.add_data(0x3a00df, utils.ByteField(99, num_bytes=2).as_bytes())

        # No Mack Skip flag
        if self.settings.is_flag_enabled(flags.NoMackSkip):
            patch.add_data(0x14ca6c, bytes([0xA5]))

        # Items
        for item in self.items:
            patch += item.get_patch()
        patch += data.items.Item.build_descriptions_patch(self)

        # Shops
        for shop in self.shops:
            patch += shop.get_patch()

        # Enemies
        for enemy in self.enemies:
            patch += enemy.get_patch()
            enemy.patch_script()
        patch += data.enemies.Enemy.build_psychopath_patch(self)

        # Enemy attacks
        for attack in self.enemy_attacks:
            patch += attack.get_patch()

        # Enemy formations
        for formation in self.enemy_formations:
            patch += formation.get_patch()

        # Open mode specific data.
        if self.open_mode:
            # Item locations.
            # FIXME
            # for location in self.key_locations + self.chest_locations:
            #     print(">>>>>>>> {}".format(location))

            for location in self.key_locations:
                patch += location.get_patch()

            for location in self.chest_locations:
                patch += location.get_patch()

            # Boss locations.
            for boss in self.boss_locations:
                # FIXME
                # print(">>>>>>>>>>>>>>>> {}".format(boss))
                patch += boss.get_patch()

            # Set flags for seven star mode and Bowser's Keep.
            if self.settings.is_flag_enabled(flags.SevenStarHunt):
                patch.add_data(0x1fd341, utils.ByteField(0xa2).as_bytes())

            if self.settings.is_flag_enabled(flags.BowsersKeepOpen):
                patch.add_data(0x1fd343, utils.ByteField(0xa2).as_bytes())

            # Dialogs
            patch += self.wishes.get_patch()
            patch += self.quiz.get_patch()

            # FIXME
            # print(">>>>>>>> WISHES")
            # for wish in self.wishes.wishes:
            #     print(">>>>>>>>>>>>>>>> {}".format(wish))

            # print(">>>>>>>> QUIZ")
            # for question in self.quiz.questions:
            #     print(">>>>>>>>>>>>>>>> {}".format(question))

        # Unlock the whole map if in debug mode in standard.
        if self.debug_mode and not self.open_mode:
            patch += map.unlock_world_map()


        # factory warp
        if self.settings.is_flag_enabled(flags.CasinoWarp):
            # patch the event jump
            # event 2637

            # star piece event check
            # sometimes lazy shell can cause some weirdness with addresses, but we know this event began at 0x1FF451
            # and our custom code should start +3 after that

            # if R7 is turned on, we want this to be a check for 7 star pieces, not 6

            if self.settings.is_flag_enabled(flags.SevenStarHunt):
                patch.add_data(0x1FF454, [0xE0, 0x35, 0x07, 0x5C, 0xF4])
            else:
                patch.add_data(0x1FF454, [0xE0, 0x35, 0x06, 0x5C, 0xF4])

            patch.add_data(0x1FF459, [0xD2, 0x67, 0xF4, 0xD0, 0x48, 0x08])

            original_event_address = 0x1FF467
            start9_b_address = 0x1FF45F
            i = start9_b_address
            while i < original_event_address:
                patch.add_data(i, 0x9B)
                i += 1

            # event 2120
            patch.add_data(0x1F7A4D,
                           [0x60, 0x80, 0xAB, 0xC0, 0x66, 0x58, 0x7A, 0xD2, 0x67, 0xF4, 0xFE, 0x74, 0xD0, 0xCF, 0x0E,
                            0xFE])
            original_end_address = 0x1F7A90
            start9_b_address = 0x1F7A5D
            i = start9_b_address
            while i <= original_end_address:
                patch.add_data(i, 0x9B)
                i += 1

            # Dialog
            patch.add_data(0x23D3CE, [0x44, 0x6F, 0x0F, 0x20, 0x77, 0x61, 0x6E, 0x74, 0x11, 0x67, 0x6F, 0x11, 0x53,
                                      0x6D, 0x69, 0x74, 0x68, 0x79, 0x3F, 0x02, 0x08, 0x07, 0x20, 0x28, 0x4E, 0x6F,
                                      0x29, 0x01, 0x08, 0x07, 0x20, 0x28, 0x59, 0x65, 0x73, 0x29, 0x00])

        # Overworld boss sprites
        if self.open_mode:
            patch += bosses_overworld.patch_overworld_bosses(self)

        # This needs to happen after all battle script randomization.
        patch += assemble_battle_scripts(self)

        # Credit update
        patch += credits.update_credits(self)

        # Choose character for the file select screen.
        i = cursor_id
        file_select_char_bytes = [0, 7, 13, 25, 19]
        self.file_select_character = [c for c in self.characters if c.index == i][0].__class__.__name__

        # Change file select character graphic, if not Mario.
        if i != 0:
            addresses = [0x34757, 0x3489a, 0x34ee7, 0x340aa, 0x3501e]
            for addr, value in zip(addresses, [0, 1, 0, 0, 1]):
                patch.add_data(addr, file_select_char_bytes[i] + value)

        # Possible names we can use for the hash values on the file select screen.  Needs to be 6 characters or less.
        file_entry_names = {
            'MARIO',
            'MALLOW',
            'GENO',
            'BOWSER',
            'PEACH',
        }
        # Also use enemy names, if they're 6 characters or less.
        for e in self.enemies:
            if isinstance(e, data.enemies.K9):
                name = e.name
            else:
                name = re.sub(r'[^A-Za-z]', '', e.name.upper())
            if len(name) <= 6:
                file_entry_names.add(name)
        file_entry_names = sorted(file_entry_names)

        # Replace file select names with "hash" values for seed verification.
        file_select_names = [
            file_entry_names[int(self.hash[0:8], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[8:16], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[16:24], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[24:32], 16) % len(file_entry_names)],
        ]
        for i, name in enumerate(file_select_names):
            addr = 0x3ef528 + (i * 7)
            val = name.encode().ljust(7, b'\x00')
            patch.add_data(addr, val)

        # Save file select hash text to show the user on the website, but the game uses '}' instead of dash.
        self.file_select_hash = ' / '.join(file_select_names).replace('}', '-')

        # Update ROM title and version.
        title = 'SMRPG-R {}'.format(self.seed).ljust(20)
        if len(title) > 20:
            title = title[:19] + '?'

        # Add version number on name entry screen.
        version_text = ('v' + VERSION).ljust(10)
        if len(version_text) > 10:
            raise ValueError("Version text is too long: {!r}".format(version_text))
        patch.add_data(0x3ef140, version_text)

        # Add title and major version number to SNES header data.
        patch.add_data(0x7fc0, title)
        v = VERSION.split('.')
        patch.add_data(0x7fdb, int(v[0]))

        return patch

    @property
    def spoiler(self):
        """

        Returns:
            dict: Spoiler for current game world state in JSON object form (Python dictionary).

        """
        # TODO: Build spoilers that are in all modes first.
        spoiler = {}

        # TODO: Open mode only spoilers.
        if self.open_mode:
            spoiler['Boss Locations'] = bosses.get_spoiler(self)
            spoiler['Item Locations'] = items.get_spoiler(self)

        return spoiler
