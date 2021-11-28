# Main randomizer logic module that the front end calls.

import collections
import hashlib
import random
import re
import binascii
import copy
import enum
import yaml
import os
from datetime import datetime


from randomizer import data
from randomizer.data.eventscripts.events import scripts as eventscripts
from randomizer.data.actionscripts.actions import scripts as actionscripts
from randomizer.data.roomobjects.roomobjects import rooms as roomdata
from randomizer.data.npcmodels import models as npcmodels
from randomizer.data.dialog_data.dialog_data import dialog_data
from randomizer.data.dialog_data.dialog_pointers import pointers as dialog_pointers
from randomizer.data.helpers import ItemQualities, FireworksOptions, BanditsWayGating, ForestMazeGating, BoosterTowerGating, MarrymoreGating, SeaGating, YaridovichGating, BelomeTempleGating, MonstroTownGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating, EXPChallengeOptions, PlayableCharacters, ShopQualities, WinConditions, PipeVaultGating
from randomizer.data.sprites.objects.sprites import sprites as commonsprites
from randomizer.data.utils import palette_to_bytes
from randomizer.data.packets import packets as dpackets
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
from .sprites import Sprites
from .roomobject import set_partitions
from .patch import Patch
from .battleassembler import assemble_battle_scripts

from randomizer.data.eventscripts.utils.tower_access.mario import script as tower_mario
from randomizer.data.eventscripts.utils.tower_access.mallow import script as tower_mallow
from randomizer.data.eventscripts.utils.tower_access.geno import script as tower_geno
from randomizer.data.eventscripts.utils.tower_access.bowser import script as tower_bowser
from randomizer.data.eventscripts.utils.tower_access.toadstool import script as tower_toadstool
from randomizer.data.eventscripts.utils.tower_access.mario_self import script as tower_mario_self
from randomizer.data.eventscripts.utils.tower_access.mallow_self import script as tower_mallow_self
from randomizer.data.eventscripts.utils.tower_access.geno_self import script as tower_geno_self
from randomizer.data.eventscripts.utils.tower_access.bowser_self import script as tower_bowser_self
from randomizer.data.eventscripts.utils.tower_access.toadstool_self import script as tower_toadstool_self

from randomizer.data.roomobjecttables import RadialDirection
from randomizer.data.eventtables import AreaObjects, Rooms

from .enscript import EventScript
from .osscript import ObjectSequenceScript
from .roomobject import RoomObjects
from .npcmodel import NPCModels
from .packets import Packets

# Current version number
VERSION = '9.0.0'

b64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

class Settings:
    def __init__(self, mode, debug_mode=False, flag_string='', cosmetics_string = ''):
        """Provide either form data fields or flag string to set flags on creation.

        Args:
            mode (str): Should be standard or open.
            debug_mode (bool): Debug flag.
            flag_string (str): Flag string if parsing flags from string.
        """
        self._mode = mode
        self._debug_mode = debug_mode
        self._all_flags = []
        self._override = {}
        
        if debug_mode:
            with open("randomizer/debug/config.yml", "r") as stream:
                try:
                    self._override = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

        flag_dict = {}
        flag_words = re.compile("\s+").split(flag_string) + re.compile("\s+").split(cosmetics_string)
        flag_words = [f for f in flag_words if f.strip() != '']
        # index the supplied flag values to be referenced by category loop
        for w in flag_words:
            subcat = w[0]
            flag_dict[subcat] = {}
            params = w[1:]
            flags_with_settings = params.split("|")
            for s in flags_with_settings:
                setting_data = s.split(":")
                if len(setting_data) == 1:
                    flag_dict[subcat][setting_data[0]] = True
                else:
                    flag_dict[subcat][setting_data[0]] = setting_data[1]

        # Get flags from form data.
        for category in flags.CATEGORIES:
            for subcategory in category.subcategories:
                for flag in subcategory.flags:
                    if subcategory.id in flag_dict and flag.id in flag_dict[subcategory.id]:
                        if utils.isclass_or_instance(flag, flags.CategorizationFlag):
                            option_booleans = []
                            b64_string = flag_dict[subcategory.id][flag.id]
                            for c in b64_string:
                                b64val = b64_table.index(c)
                                for boss_location in range(0,6):
                                    option_booleans.append((b64val & (1 << boss_location)) != 0)
                            checked_tuples = zip(option_booleans, flag.options)
                            enabled = [v[1] for v in checked_tuples if v[0]]
                            flag.enabled = enabled
                            flag.disabled = [v for v in flag.options if v not in enabled]
                        elif utils.isclass_or_instance(flag, flags.NumberThresholdFlag):
                            flag.value = int(flag_dict[subcategory.id][flag.id])
                        elif utils.isclass_or_instance(flag, flags.SelectOneFlag):
                            val = next((x for x in flag.choices if x.name == flag_dict[subcategory.id][flag.id]), None)
                            if val is None:
                                raise Exception("invalid property for %s.%s flag: %s" % (subcategory.id, flag.id, flag_dict[subcategory.id][flag.id]))
                            flag.value = val
                        else:
                            flag.value = flag_dict[subcategory.id][flag.id]
                    else:
                        if utils.isclass_or_instance(flag, flags.CategorizationFlag):
                            flag.disabled = [i for i in flag.options if i not in flag.enabled]
                        else:
                            flag.value = flag.default
                    self._all_flags.append(flag)
        
    #    for flag in self._all_flags:
    #        print (flag.id, flag.type, flag.enabled if utils.isclass_or_instance(flag, flags.CategorizationFlag) else flag.value)

    @property
    def mode(self):
        """:rtype: str"""
        return self._mode

    @property
    def debug_mode(self):
        """:rtype: bool"""
        return self._debug_mode

    @property
    def override(self):
        """:rtype: dict"""
        return self._override

    @property
    def flag_string(self):
        """
        Returns:
            str: Computed flag string for these settings.
        """

        flag_strings = []

        for category in [f for f in flags.CATEGORIES if not utils.isclass_or_instance(f, flags.CosmeticCategory)]:
            for subcategory in category.subcategories:
                flagstring_parts = []
                for flag in subcategory.flags:
                    if utils.isclass_or_instance(flag, flags.BooleanFlag):
                        if flag.value:
                            flagstring_parts.append(flag.id)
                    elif utils.isclass_or_instance(flag, flags.SelectOneFlag):
                        flagstring_parts.append("%s:%s" % (flag.id, flag.value.name))
                    elif utils.isclass_or_instance(flag, flags.NumberThresholdFlag):
                        flagstring_parts.append("%s:%i" % (flag.id, flag.value))
                    elif utils.isclass_or_instance(flag, flags.CategorizationFlag):
                        ctr = 0
                        choice_rep = 0
                        choice_rep_string = ''
                        for f in flag.options:
                            if f in flag.enabled:
                                choice_rep += (1 << ctr)
                            ctr += 1
                            if ctr == 6:
                                choice_rep_string += b64_table[choice_rep]
                                ctr = 0
                                choice_rep = 0
                        if ctr > 0:
                            choice_rep_string += b64_table[choice_rep]
                        flagstring_parts.append("%s:%s" % (flag.id, choice_rep_string))
                if len(flagstring_parts) is not 0:
                    flag_strings.append('%s.%s' % (subcategory.id, '|'.join(flagstring_parts)))
        flag_string = "     ".join(flag_strings)

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
        narrowed = [i for i in self._all_flags if i == flag]
        return narrowed[0]

    def is_flag_value(self, flag, value):
        """
        Args:
            flag: Flag class to check.

        Returns:
            bool: True if flag is enabled at value, False otherwise.
        """
        narrowed = [i for i in self._all_flags if i == flag]
        return narrowed[0].value == value

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
        random.seed(seed)
        print(self.seed)
        self.settings = settings
        self.file_select_character = 'Mario'
        self.file_select_hash = 'MARIO1 / MARIO2 / MARIO3 / MARIO4'
        self._rebuild_hash()
        self.version = VERSION

        # Events
        self.eventscripts = copy.deepcopy(eventscripts)
        self.actionscripts = copy.deepcopy(actionscripts)

        # Get default npc and model data. Keep them for reference. 
        self.original_models = copy.deepcopy(npcmodels)
        self.original_rooms = copy.deepcopy(roomdata)
        # Malleable versions
        self.packets = copy.deepcopy(dpackets)
        self.models = copy.deepcopy(npcmodels)
        self.rooms = copy.deepcopy(roomdata)

        #Dialogs
        self.dialog_pointers = copy.deepcopy(dialog_pointers)
        self.dialog_data = copy.deepcopy(dialog_data)

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

        # Minigame data.
        self.ball_solitaire = data.games.BallSolitaireGame(self)
        self.magic_buttons = data.games.MagicButtonsGame(self)

        # String data.
        self.wishes = data.dialogs.Wishes(self)
        self.quiz = data.dialogs.Quiz(self)

        # Credits for specifically chosen tadpole pond and sunken ship submissions
        self.tadpole_songs = []
        self.password = None

        # Music (moved this into its own classes to make exclusion easier)
        self.music_pool = data.music.get_default_music()


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
        if self.items_dict and cls.index in self.items_dict:
            return self.items_dict[cls.index]
        else:
            if type(cls) == type:
                return cls(self)
            else:
                return cls

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
        print("randomizing data...")
        """Randomize this entire game world instance."""
        # Seed the PRNG at the start.
        spells.randomize_all(self)
        characters.randomize_all(self)
        items.randomize_all(self)
        bosses.randomize_all(self)
        # Bosses might have to go before enemies to make formation rando work as intended?
        # Goes before chests so that slot machine scripts can be written
        enemies.randomize_all(self)
        chests.randomize_all(self)
        shops.randomize_all(self)
        doors.randomize_all(self)
        games.randomize_all(self)
        dialogs.randomize_all(self)

        # Rebuild hash after randomization.
        self._rebuild_hash()

        # apply random cosmetics after hash build
        random.seed(datetime.now())
        bosses.randomize_music(self)
        characters.randomize_palettes(self)

        # If palette swap is enabled, give us a 50/50 chance at a chocolate cake.
        if self.settings.is_flag_enabled(flags.PaletteSwaps):
            self.chocolate_cake = utils.coin_flip()

        random.seed(self.seed)

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
        for bank_id, dialog_bank in enumerate(self.dialog_data):
            for index, dialog in enumerate(dialog_bank):
                self.dialog_data[bank_id][index] = dialog.replace(search, replace)

    def prepend_bits(self, event, pairs):
        for pair in pairs:
            self.eventscripts[event].insert(0, utils.new_command(event, "set_bit", pair))

    def update_room_npc_property_by_id(self, room_id, npc_id, prop, value):
        ctr = 0
        for parent_id, npc in enumerate(self.rooms[room_id]["objects"]):
            if ctr == npc_id:
                if prop not in self.rooms[room_id]["objects"][parent_id]:
                    raise Exception("npc %i in room %i has no property %s" % (npc_id, room_id, prop))
                self.rooms[room_id]["objects"][parent_id][prop] = value
                return
            ctr += 1
            if "clones" in npc:
                for clone_id, clone in enumerate(npc["clones"]):
                    if ctr == npc_id:
                        if prop not in clone:
                            if prop in ["model", "event_script", "action_script", "battle_pack"] and prop in npc:
                                base_value_id = npc[prop]
                                offset = value - base_value_id
                                if offset > 7 or offset < 0:
                                    raise Exception("illegal %s value for clone npc %i in room %i: %i (parent is %i)" % (prop, npc_id, room_id, value, npc[prop]))
                                if prop == "model":
                                    self.rooms[room_id]["objects"][parent_id]["clones"][clone_id]["npc_id_offset"] = offset
                                elif prop == "event_script":
                                    self.rooms[room_id]["objects"][parent_id]["clones"][clone_id]["event_offset"] = offset
                                elif prop == "action_script":
                                    self.rooms[room_id]["objects"][parent_id]["clones"][clone_id]["action_offset"] = offset
                                elif prop == "battle_pack":
                                    self.rooms[room_id]["objects"][parent_id]["clones"][clone_id]["pack_offset"] = offset
                            return
                        self.rooms[room_id]["objects"][parent_id]["clones"][clone_id][prop] = value
                        return
                    ctr += 1
        raise Exception("npc %i not found in room %i" % (npc_id, room_id))

    def get_room_npc_property_by_id(self, room_id, npc_id, prop):
        ctr = 0
        for parent_id, npc in enumerate(self.rooms[room_id]["objects"]):
            if ctr == npc_id:
                if prop not in self.rooms[room_id]["objects"][parent_id]:
                    raise Exception("npc %i in room %i has no property %s" % (npc_id, room_id, prop))
                return self.rooms[room_id]["objects"][parent_id][prop]
            ctr += 1
            if "clones" in npc:
                for _, clone in enumerate(npc["clones"]):
                    if ctr == npc_id:
                        if prop not in clone:
                            if prop in ["model", "event_script", "action_script", "battle_pack"]:
                                base_value_id = npc["model"]
                                if prop == "model":
                                    return base_value_id + clone["npc_id_offset"]
                                elif prop == "event_script":
                                    return base_value_id + clone["event_offset"]
                                elif prop == "action_script":
                                    return base_value_id + clone["action_offset"]
                                elif prop == "battle_pack":
                                    return base_value_id + clone["pack_offset"]
                            else:
                                raise Exception("clone npc %i in room %i has no property %s" % (npc_id, room_id, prop))
                        return clone[prop]
                    ctr += 1
        raise Exception("npc %i not found in room %i" %(npc_id, room_id))

    def get_npc_count_by_room_id(self, room_id):
        ctr = 0
        for _, npc in enumerate(self.rooms[room_id]["objects"]):
            ctr += 1
            if "clones" in npc:
                for _ in npc["clones"]:
                    ctr += 1
        return ctr

    def build_patch(self):
        """Build patch data for this instance.

        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()


        ########## First, modify world properties based on flag values which haven't been set in the randomize function
        # This is mostly going to be setting bits at the time of loading a new file, which control the behaviour of some event scripts       

        # Remove commands from game loader that are required to make the base rom run properly on its own
        # These commands will be replaced according to the user's settings
        self.eventscripts[13] = [utils.new_command(13, "ret")]

        # item quality cap
        if self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t1):
            self.prepend_bits(192, [[0x7088, 4]])
            self.prepend_bits(192, [[0x7088, 3]])
        elif self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t2):
            self.prepend_bits(192, [[0x7088, 4]])
        elif self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t3):
            self.prepend_bits(192, [[0x7088, 3]])


        # Set number of star pieces required for win condition
        required_star_pieces = self.settings.get_flag(flags.TotalStarPieces).value
        self.eventscripts[1969][1]["args"] = [required_star_pieces]

        # Alternate star piece win conditions
        if self.settings.is_flag_value(flags.RequireBossFights, True):
            self.prepend_bits(192, [[0x7086, 7]])
            # disable mack skip
            self.update_room_npc_property_by_id(326, 10, "event", 256)

        # Bandit's Way gating
        if self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.open):
            self.prepend_bits(192, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mushroomway):
            self.prepend_bits(199, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mario):
            self.prepend_bits(187, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow):
            self.prepend_bits(198, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.geno):
            self.prepend_bits(189, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.bowser):
            self.prepend_bits(190, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.toadstool):
            self.prepend_bits(191, [[0x7065, 4], [0x706D, 4]])

        # Forest Maze gating, special conditions
        if self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.open):
            self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])
        elif self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.pie):
            self.prepend_bits(203, [[0x7066, 3], [0x706E, 3]])

        # Pipe Vault gating
        if self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.forest):
            self.prepend_bits(211, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mario):
            self.prepend_bits(187, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mallow):
            self.prepend_bits(198, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.geno):
            self.prepend_bits(189, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.bowser):
            self.prepend_bits(190, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.toadstool):
            self.prepend_bits(191, [[0x7055, 7]])
        else:
            self.prepend_bits(192, [[0x7055, 7]])

        # Starting characters - necessary to determine booster tower script
        # maintain the join order to match cursor character
        self.starter_character_checks.reverse()
        populated_starters = [c for c in self.starter_character_checks if c.item is not None]
        REMOVE_DUMMY = enum.auto()
        populated_starters.insert(len(populated_starters)-1, REMOVE_DUMMY)
        for position, c in enumerate(populated_starters):
            if c == REMOVE_DUMMY:
                # remove placeholder member after setting first starter char so party size doesnt unintentionally go over 4 and unlock switch menu too early
                self.eventscripts[192].insert(0, utils.new_command(192, "leave_party", [AreaObjects.DUMMY_0X05]))
            else:
                if utils.isclass_or_instance(c, data.chests.StarterCharacter1):
                    # Use first character to join as file select cursor.
                    if (utils.isclass_or_instance(c.item, data.items.MallowRecruit)):
                        cursor_id = 4
                    elif (utils.isclass_or_instance(c.item, data.items.GenoRecruit)):
                        cursor_id = 3
                    elif (utils.isclass_or_instance(c.item, data.items.BowserRecruit)):
                        cursor_id = 2
                    elif (utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                        cursor_id = 1
                    else:
                        cursor_id = 0
                # set character
                self.eventscripts[c.event].insert(0, utils.new_command(c.event, "run_event_as_subroutine", [c.item.starter_script]))
                # check if character gates forest maze
                if (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario) and utils.isclass_or_instance(c.item, data.items.MarioRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow) and utils.isclass_or_instance(c.item, data.items.MallowRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno) and utils.isclass_or_instance(c.item, data.items.GenoRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser) and utils.isclass_or_instance(c.item, data.items.BowserRecruit)) or (self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool) and utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit)):
                    self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])

        # Booster Tower gating
        if self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.open):
            self.prepend_bits(192, [[0x7053, 6]])
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mines):
            self.prepend_bits(199, [[0x7053, 6]])
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario):
            self.prepend_bits(187, [[0x7053, 7]])
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 0:
                self.eventscripts[1331] = copy.deepcopy(tower_mario_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_mario)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mallow):
            self.prepend_bits(198, [[0x7053, 7]])
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 4:
                self.eventscripts[1331] = copy.deepcopy(tower_mallow_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_mallow)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.geno):
            self.prepend_bits(189, [[0x7053, 7]])
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 3:
                self.eventscripts[1331] = copy.deepcopy(tower_geno_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_geno)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.bowser):
            self.prepend_bits(190, [[0x7053, 7]])
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 2:
                self.eventscripts[1331] = copy.deepcopy(tower_bowser_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_bowser)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool):
            self.prepend_bits(191, [[0x7053, 7]])
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 1:
                self.eventscripts[1331] = copy.deepcopy(tower_toadstool_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_toadstool)

        # Marrymore gating
        if self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.open):
            self.prepend_bits(192, [[0x704C, 7]])
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.hill):
            self.prepend_bits(204, [[0x704C, 7]])
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.prepend_bits(205, [[0x704C, 7]])
        
        # Sea gating
        if self.settings.is_flag_value(flags.SeaGate, SeaGating.open):
            self.prepend_bits(192, [[0x7067, 4], [0x706F, 3], [0x7067, 5], [0x706F, 4]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.mario):
            self.prepend_bits(187, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.mallow):
            self.prepend_bits(198, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.geno):
            self.prepend_bits(189, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.bowser):
            self.prepend_bits(190, [[0x7067, 4], [0x706F, 3]])
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.toadstool):
            self.prepend_bits(191, [[0x7067, 4], [0x706F, 3]])
        else:
            if self.settings.is_flag_value(flags.SeaGate, SeaGating.star1):
                value = 1
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star2):
                value = 2
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star3):
                value = 3
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
                value = 4
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star5):
                value = 5
            elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star6):
                value = 6
            else:
                raise Exception("failed to set star piece gate on sea")
            gate_script = copy.deepcopy([{**s} for s in self.eventscripts[206]])
            gate_script[1]["args"][1] = value
            self.eventscripts[206] = gate_script
            self.prepend_bits(192, [[0x7051, 0]])

        # Yaridovich gating
        if self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.open):
            self.prepend_bits(192, [[0x7057, 1]])
        elif self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.ship):
            self.prepend_bits(210, [[0x7057, 1]])

        # Belome Temple gating
        if self.settings.is_flag_value(flags.BelomeTempleGate, BelomeTempleGating.open):
            self.prepend_bits(192, [[0x7052, 2]])
        elif self.settings.is_flag_value(flags.BelomeTempleGate, BelomeTempleGating.seaside):
            self.eventscripts[192].insert(0, utils.new_command(192, 'remove_from_level', [AreaObjects.NPC_3, Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]))
                        

        # Monstro Town gating
        if self.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.open):
            self.prepend_bits(192, [[0x7067, 7], [0x706F, 6]])
        elif self.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.landsend):
            pass

        # Volcano gating
        if self.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.open):
            self.prepend_bits(192, [[0x7090, 5], [0x7070, 1], [0x7068, 2]])
        elif self.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.nimbus):
            pass

        # Bowser's Keep gating
        if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.prepend_bits(192, [[0x7068, 3]])
        else:
            self.prepend_bits(192, [[0x707A, 3]])
            if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.volcano):
                self.prepend_bits(192, [[0x707B, 2]])
            else:
                if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star1):
                    value = 1
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star2):
                    value = 2
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star3):
                    value = 3
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star4):
                    value = 4
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star5):
                    value = 5
                elif self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star6):
                    value = 6
                else:
                    raise Exception("failed to set star piece gate on keep")
                keep_script = copy.deepcopy([{**s} for s in self.eventscripts[207]])
                keep_script[1]["args"][1] = value
                self.eventscripts[207] = keep_script
                self.prepend_bits(192, [[0x7051, 1], [0x707A, 3]])

        # Factory gating
        if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.open):
            self.prepend_bits(192, [[0x7070, 5], [0x7068, 5]])
        elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.keep):
            self.prepend_bits(2149, [[0x7070, 5], [0x7068, 5]])
        else:
            if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star1):
                value = 1
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star2):
                value = 2
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star3):
                value = 3
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star4):
                value = 4
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star5):
                value = 5
            elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star6):
                value = 6
            else:
                raise Exception("failed to set star piece gate on factory")
            factory_script = copy.deepcopy([{**s} for s in self.eventscripts[3093]])
            factory_script[1]["args"][1] = value
            self.eventscripts[3093] = factory_script
            self.prepend_bits(192, [[0x7051, 3]])

        # Casino warp
        if self.settings.is_flag_value(flags.CasinoWarp, True):
            self.prepend_bits(192, [[0x7088, 5]])
            casino_script = copy.deepcopy([{**s} for s in self.eventscripts[2645]])
            casino_script[2]["args"][1] = required_star_pieces
            self.eventscripts[2645] = casino_script

        # Bucket warp
        if self.settings.is_flag_value(flags.BucketWarp, True):
            self.prepend_bits(192, [[0x705E, 6]])
            bucket_script = copy.deepcopy([{**s} for s in self.eventscripts[2651]])
            bucket_script[0]["args"][1] = required_star_pieces
            self.eventscripts[2651] = bucket_script

        # Fast travel
        if self.settings.is_flag_value(flags.FastTravel, True):
            self.prepend_bits(192, [[0x708B, 0]])

        # Win condition
        if self.settings.is_flag_value(flags.WinCondition,WinConditions.stars):
            self.prepend_bits(192, [[0x7051, 6]])
            self.eventscripts[3101][1]["args"][1] = [required_star_pieces]
        elif self.settings.is_flag_value(flags.WinCondition,WinConditions.sealed):
            self.prepend_bits(192, [[0x7051, 7]])

        # Fireworks
        if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.vanilla):
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
            if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.shuffle1):
                self.prepend_bits(192, [[0x705D, 4]])
            if self.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.progressive):
                self.prepend_bits(192, [[0x705D, 5]])

        # EXP progression option
        if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easystars) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardstars):
            self.prepend_bits(192, [[0x7056, 0]])
        elif self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.easybosses) or self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.hardbosses):
            self.prepend_bits(192, [[0x7056, 1]])

        # If star piece exp progression is on, set exp values for each star piece number and enable flag.
        if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.vanilla):
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
            #patch.add_data(0x1fd32d, utils.ByteField(0xa0).as_bytes())  # Enable flag

        # Grate Guy threshold
        value = self.settings.get_flag(flags.GrateGuyPrizeThreshold).value
        self.eventscripts[2650][0]["args"] = [value]

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
        # verify super jump thresholds
        value = self.settings.get_flag(flags.SuperJump2Threshold).value
        if value <= self.settings.get_flag(flags.SuperJump1Threshold).value:
            raise Exception("2nd super jump threshold must be higher than 1st")

        # Skip Minecart
        if self.settings.is_flag_value(flags.SkipMinecart, True):
            self.prepend_bits(192, [[0x707B, 6]])

        # Invisible Checks Anywhere
        if self.settings.is_flag_enabled(flags.InvisibleFlagsSetting):
            self.prepend_bits(192, [[0x7060, 2]])
        if self.settings.is_flag_enabled(flags.SkipMustyFearsSequence):
            self.eventscripts[192].insert(0, {"identifier": "EVENT_192_summon_invisible_flags", "command": 'run_event_as_subroutine', "args": [91]})
            
        # perform non-npc sprite replacement for overworld character
        if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id > 0:
            if cursor_id == 4:
                nc = data.characters.Mallow
                from randomizer.data.sprites.insertions.mallow.sprites import sprites as new_sprites
            elif cursor_id == 3:
                nc = data.characters.Geno
                from randomizer.data.sprites.insertions.geno.sprites import sprites as new_sprites
            elif cursor_id == 2:
                nc = data.characters.Bowser
                from randomizer.data.sprites.insertions.bowser.sprites import sprites as new_sprites
            else:
                nc = data.characters.Peach
                from randomizer.data.sprites.insertions.toadstool.sprites import sprites as new_sprites
            for gsi, gs in enumerate(new_sprites):
                if gs is not None:
                    commonsprites[gsi] = gs
            patch.add_data(data.characters.Mario.battle_sprite_offset, nc.battle_sprite_id)
            patch.add_data(nc.battle_sprite_offset, data.characters.Mario.battle_sprite_id)
            patch.add_data(data.characters.Mario.menu_sprite_offset, nc.menu_sprite_id)
            patch.add_data(nc.menu_sprite_offset, data.characters.Mario.menu_sprite_id)
            patch.add_data(data.characters.Mario.abxy_coord_offset, nc.abxy_coord)
            patch.add_data(nc.abxy_coord_offset, data.characters.Mario.abxy_coord)
            patch.add_data(data.characters.Mario.cursor_coord_offset, nc.cursor_coord)
            patch.add_data(nc.cursor_coord_offset, data.characters.Mario.cursor_coord)
            #patch.add_data(data.characters.Mario.portrait_sprite_offset, nc.portrait_id)
            #patch.add_data(nc.portrait_sprite_offset, data.characters.Mario.portrait_id)
            patch.add_data(data.characters.Mario.item_use_offset, nc.item_use_bytes)
            patch.add_data(nc.item_use_offset, data.characters.Mario.item_use_bytes)
            patch.add_data(data.characters.Mario.runaway_offset, nc.runaway_bytes)
            patch.add_data(nc.runaway_offset, data.characters.Mario.runaway_bytes)
            for addrs, sprite_id in zip(data.characters.Mario.sprite_addresses, nc.original_weapon_sprite_ids):
                if addrs is not None:
                    for addr in addrs:
                        patch.add_data(addr + 3, bytearray([sprite_id & 0xFF, (sprite_id >> 8) & 0xFF]))
            for addrs, sprite_id in zip(nc.sprite_addresses, nc.sprite_ids_as_main_character):
                if addrs is not None:
                    for addr in addrs:
                        patch.add_data(addr + 3, bytearray([sprite_id & 0xFF, (sprite_id >> 8) & 0xFF]))




            



        # booster tower door animation
        if self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario):
            self.update_room_npc_property_by_id(202, 0, "model", 0)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mallow):
            self.update_room_npc_property_by_id(202, 0, "model", 3)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.geno):
            self.update_room_npc_property_by_id(202, 0, "model", 4)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.bowser):
            self.update_room_npc_property_by_id(202, 0, "model", 2)
        elif self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool):
            self.update_room_npc_property_by_id(202, 0, "model", 1)


        ########## Build patches

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

        # Uncap Super Jumps
        if self.settings.is_flag_enabled(flags.UncapSuperJumps):
            patch.add_data(0x35C758, [0xFF, 0xFF])

        # Substitute Valentina statue sprite
        for l in self.boss_locations:
            model_num = l.boss.small_model.cloneable_all_directions or l.boss.small_model.uncloneable_all_directions or l.boss.small_model.cloneable_south_only or l.boss.small_model.uncloneable_south_only
            
            source_sprite = self.models[model_num]["sprite"]

            palette_addr = 30 * (commonsprites[source_sprite].palette_id + commonsprites[source_sprite].palette_offset) + 0x253000

            if self.settings.is_flag_enabled(flags.DifferentiateRepeatedBosses):
                if l.boss.alt_palette is not None:
                    patch.add_data(palette_addr, palette_to_bytes(l.boss.alt_palette))
            if utils.isclass_or_instance(l, data.bosses.Valentina) and not utils.isclass_or_instance(l.boss, data.bosses.ValentinaBoss):
                model_num = l.boss.statue.reference_model
                dest_sprite = self.models[63]["sprite"]
                
                molds = copy.deepcopy(commonsprites[source_sprite].animation.properties.molds)
                sequences = copy.deepcopy(commonsprites[source_sprite].animation.properties.sequences)

                commonsprites[dest_sprite].animation.properties.molds = molds
                commonsprites[dest_sprite].animation.properties.sequences = sequences

                palette_addr = 30 * (commonsprites[dest_sprite].palette_id + commonsprites[dest_sprite].palette_offset) + 0x253000
                patch.add_data(palette_addr, palette_to_bytes(l.boss.statue.palette))


        # Remove screen flashes
        if self.settings.is_flag_enabled(flags.RemoveFlashes):
            # Thunderbolt
            patch.add_data(0x35BEDF, [0x8E, 0x00, 0x01])
            patch.add_data(0x35BF0E, [0x8E, 0x00, 0x03])

            # Geno Flash
            patch.add_data(0x35BE52, [0x0A, 0x0A])

            # Geno Blast
            patch.add_data(0x35BC75, [0x0A, 0x0A])

            # Crusher
            patch.add_data(0x35B0A1, [0x8E, 0x00, 0x01])

            # Big Bang
            patch.add_data(0x354A04, [0x72, 0x04, 0x19])

            # Fire Bomb
            patch.add_data(0x35DC9b, [0x72, 0x04, 0x19])

            # Ice Bomb
            patch.add_data(0x35DCBe, [0x8E, 0x00, 0x01])

            # Solidify
            patch.add_data(0x355721, [0x8E, 0x00, 0x01])

            # Corona
            patch.add_data(0x355DE4, [0x0A, 0x0A])

            # Dark Star
            patch.add_data(0x35C54F, [0x8E, 0x00, 0x01])

            # Shaker, Silver Bullet
            patch.add_data(0x35358A, [0x3A, 0x34, 0x0F, 0x3F, 0x80, 0x15, 0x00, 0x00, 0x84, 0xA8, 0x02, 0x00, 0x40, 0x0F, 0xFF, 0x73, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x11])

            # spiked link
            patch.add_data(0x35F5B1, [0x8E, 0x00, 0x01])
            patch.add_data(0x35F5C2, [0x8E, 0x00, 0x01])
            patch.add_data(0x35F5D3, [0x8E, 0x00, 0x01])

            # Static E
            patch.add_data(0x354E9B, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])

            # Smithy
            patch.add_data(0x3AE888, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CAE, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CBB, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3AE81F, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01]) # may need to extend by 3 bytes
            patch.add_data(0x3AE888, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6C90, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CAE, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])

            # meteor swarm - dunno if this is right at all
            patch.add_data(0x355CA8, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])

            # rock candy
            patch.add_data(0x35E051, [0x8E, 0x00, 0x01])

            # meteor blast
            patch.add_data(0x3555C0, [0x8E, 0x00, 0x01])


        # Character stats and such
        for character in self.characters:
            patch += character.get_patch()




        # Update party join script events for the final order - Linear only
        if not self.open_mode:
            # For standard mode, Mario is the first character.  Update the other four only.
            addresses = [0x1e2155, 0x1fc506, 0x1edf98, 0x1e8b79]
            for addr, character in zip(addresses, self.character_join_order[1:]):
                patch.add_data(addr, 0x80 + character.index)

            cursor_id = random.randint(0, 4)

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

        # For debug mode, start with 9999 coins and 999 frog coins.
        if self.debug_mode or self.settings.is_flag_enabled(flags.FreeShops):
            patch.add_data(0x3a00db, utils.ByteField(9999, num_bytes=2).as_bytes())
            patch.add_data(0x3a00df, utils.ByteField(999, num_bytes=2).as_bytes())
        # Add items specified by debug config.
        if "items" in self.settings.override and "start" in self.settings.override["items"]:
            for item in self.settings.override["items"]["start"]:
                self.eventscripts[192].insert(0, utils.new_command(192, "put_inventory", [eval('data.items.%s.index' % item)]))
        # Set debug room specified by override config
        if "house_exit" in self.settings.override:
            self.rooms[189]["exit_fields"][0]["destination"] = self.settings.override["house_exit"]["room"]
            self.rooms[189]["exit_fields"][0]["destination_props"]["x"] = self.settings.override["house_exit"]["x"]
            self.rooms[189]["exit_fields"][0]["destination_props"]["y"] = self.settings.override["house_exit"]["y"]
            self.rooms[189]["exit_fields"][0]["destination_props"]["z"] = self.settings.override["house_exit"]["z"]
            self.rooms[189]["exit_fields"][0]["destination_props"]["f"] = eval("RadialDirection.%s" % self.settings.override["house_exit"]["direction"])

        # Items
        for item in self.items:
            patch += item.get_patch()
        patch += data.items.Item.build_descriptions_patch(self)

        # If playing as Bowser, partitions need adjustment.
        if cursor_id == 2 and self.settings.is_flag_enabled(flags.PlayAsStarter):
            for room_index, room in enumerate(self.rooms):
                if room is not None and room["partition"] is not None:
                    room["partition"]["ally_sprite_buffer_size"] += 1
                    self.rooms[room_index] = room

        # Open mode specific data.
        if self.open_mode:

            print("assembling scripts...")

            # Assemble and patch event banks
            event_code = EventScript.assemble_from_table(self.eventscripts)
            patch.add_data(0x1E0000, event_code)

            # Assemble and patch object sequence bank
            sequence_code = ObjectSequenceScript.assemble_from_table(self.actionscripts)
            patch.add_data(0x210000, sequence_code)

            # Assign vram partitions
            set_partitions(self)

            print("assembling rooms...")

            # Assemble and patch room NPC data, exit data, event tile data, and partition data
            npc_code, eventtile_code, exit_code, partition_code = RoomObjects.assemble_from_table(self.rooms)
            patch.add_data(0x148000, npc_code[0] + npc_code[1])
            patch.add_data(0x20E000, eventtile_code[0] + eventtile_code[1])
            patch.add_data(0x1D2D64, exit_code[0] + exit_code[1])
            patch.add_data(0x1DDE00, partition_code)

            print("assembling NPCs...")

            # Assemble and patch packet and NPC model data
            packet_code = Packets.assemble_from_table(self.packets)
            patch.add_data(0x1DB000, packet_code)
            model_code = NPCModels.assemble_from_table(self.models)
            patch.add_data(0x1DB800, model_code)

            print("assembling dialogs...")

            # Assemble and patch dialog data
            dialog_ptrs, dialog_code = dialogs.assemble_from_table(self.dialog_pointers, self.dialog_data)
            patch.add_data(0x37E000, dialog_ptrs)
            patch.add_data(0x220000, dialog_code[0])
            patch.add_data(0x230000, dialog_code[1])
            patch.add_data(0x240000, dialog_code[2])

            print("assembling graphics...")

            # Assemble and patch graphics data
            sprite_data, image_data, animation_pointers, animation_data_bank_1, animation_data_bank_2, tiles = Sprites.assemble_from_tables(commonsprites)
            patch.add_data(0x250000, sprite_data)
            patch.add_data(0x251800, image_data + animation_pointers)
            patch.add_data(0x259000, animation_data_bank_1 + tiles)
            patch.add_data(0x360000, animation_data_bank_2)

        # Unlock the whole map if in debug mode in standard.
        #if self.debug_mode and not self.open_mode:
        #    patch += map.unlock_world_map()

        # This needs to happen after all battle script randomization.
        patch += assemble_battle_scripts(self)

        # Credit update
        patch += credits.update_credits(self)

        # Choose character for the file select screen.
        if self.settings.is_flag_enabled(flags.PlayAsStarter):
            i = 0
        else:
            i = cursor_id
        file_select_char_bytes = [0, 7, 13, 25, 19]
        self.file_select_character = [c for c in self.characters if c.index == i][0].__class__.__name__

        # Change file select character graphic, if not Mario.
        if i != 0:
            addresses = [0x34757, 0x3489a, 0x34ee7, 0x340aa, 0x3501e]
            for addr, value in zip(addresses, [0, 1, 0, 0, 1]):
                patch.add_data(addr, file_select_char_bytes[i] + value)

        # Patch character names into the levelup screen
        if self.settings.is_flag_enabled(flags.ChangeNames) and self.settings.is_flag_enabled(flags.PaletteSwaps):
            char_order = [0, 4, 3, 2, 1]
            names = [self.characters[c] for c in char_order]
            if names[0].palette.rename_character:
                mario_name = names[0].palette.name
            else:
                mario_name = names[0].name
            patch.add_data(0x02D3AF, mario_name + "\x00" * (35 - len(mario_name)))
            other_names = [(n.palette.name if n.palette.rename_character else n.name) for n in names]
            name_bytes = "\x00".join(other_names[1:]) + "\x00"
            name_index = (0x030000 - len(name_bytes))
            patch.add_data(name_index, name_bytes)
            for i, c in enumerate(other_names[1:]):
                ptr = name_index & 0xFFFF
                patch.add_data(0x2D3A7 + i * 2, [ptr & 0xFF, ptr >> 8])
                name_index += len(c) + 1

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
            spoiler['Moved Invisible Items'] = chests.get_spoiler(self)
            spoiler['Shop Items'] = shops.get_spoiler(self)
            spoiler['Character Spells'] = characters.get_spoiler(self)
            spoiler['Puzzles'] = games.get_spoiler(self)

        return spoiler
