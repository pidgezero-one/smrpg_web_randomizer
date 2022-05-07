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
from randomizer.data.rooms.rooms import rooms as roomdata
from randomizer.data.npcmodels import models as npcmodels
from randomizer.data.dialog_data.dialog_data import dialog_data
from randomizer.data.dialog_data.dialog_pointers import pointers as dialog_pointers
from randomizer.helpers.flag_helpers import (
    ItemQualities,
    FireworksOptions,
    BanditsWayGating,
    ForestMazeGating,
    BoosterTowerGating,
    MarrymoreGating,
    SeaGating,
    YaridovichGating,
    BelomeTempleGating,
    MonstroTownGating,
    BarrelVolcanoGating,
    BowsersKeepGating,
    FactoryGating,
    EXPChallengeOptions,
    PlayableCharacters,
    ShopQualities,
    WinConditions,
    PipeVaultGating,
    Moleville1Gating,
)
from randomizer.data.sprites.objects.sprites import sprites as commonsprites
from randomizer.data.utils import palette_to_bytes
from randomizer.data.packets import packets as dpackets
from randomizer.logic.flags import LearnableSpells
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
from .patch import Patch
from .battleassembler import assemble_battle_scripts

from randomizer.data.eventscripts.utils.tower_access.mario import script as tower_mario
from randomizer.data.eventscripts.utils.tower_access.mallow import (
    script as tower_mallow,
)
from randomizer.data.eventscripts.utils.tower_access.geno import script as tower_geno
from randomizer.data.eventscripts.utils.tower_access.bowser import (
    script as tower_bowser,
)
from randomizer.data.eventscripts.utils.tower_access.toadstool import (
    script as tower_toadstool,
)
from randomizer.data.eventscripts.utils.tower_access.mario_self import (
    script as tower_mario_self,
)
from randomizer.data.eventscripts.utils.tower_access.mallow_self import (
    script as tower_mallow_self,
)
from randomizer.data.eventscripts.utils.tower_access.geno_self import (
    script as tower_geno_self,
)
from randomizer.data.eventscripts.utils.tower_access.bowser_self import (
    script as tower_bowser_self,
)
from randomizer.data.eventscripts.utils.tower_access.toadstool_self import (
    script as tower_toadstool_self,
)

from randomizer.helpers.roomobjecttables import RadialDirection
from randomizer.helpers.eventtables import AreaObjects, Rooms, _0x60Flags

from .enscript import EventScript
from .osscript import ObjectSequenceScript
from .rooms import Rooms as RoomObjects
from .rooms import set_partitions
from .packets import Packets

# Current version number
VERSION = "9.0.0"

b64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class Settings:
    def __init__(self, mode, debug_mode=False, flag_string="", cosmetics_string=""):
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
        flag_words = re.compile("\s+").split(flag_string) + re.compile("\s+").split(
            cosmetics_string
        )
        flag_words = [f for f in flag_words if f.strip() != ""]
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
                    if (
                        subcategory.id in flag_dict
                        and flag.id in flag_dict[subcategory.id]
                    ):
                        if utils.isclass_or_instance(flag, flags.CategorizationFlag):
                            option_booleans = []
                            b64_string = flag_dict[subcategory.id][flag.id]
                            for c in b64_string:
                                b64val = b64_table.index(c)
                                for boss_location in range(0, 6):
                                    option_booleans.append(
                                        (b64val & (1 << boss_location)) != 0
                                    )
                            checked_tuples = zip(option_booleans, flag.options)
                            enabled = [v[1] for v in checked_tuples if v[0]]
                            flag.enabled = enabled
                            flag.disabled = [
                                v for v in flag.options if v not in enabled
                            ]
                        elif utils.isclass_or_instance(flag, flags.NumberThresholdFlag):
                            flag.value = int(flag_dict[subcategory.id][flag.id])
                        elif utils.isclass_or_instance(flag, flags.SelectOneFlag):
                            val = next(
                                (
                                    x
                                    for x in flag.choices
                                    if x.name == flag_dict[subcategory.id][flag.id]
                                ),
                                None,
                            )
                            if val is None:
                                raise Exception(
                                    "invalid property for %s.%s flag: %s"
                                    % (
                                        subcategory.id,
                                        flag.id,
                                        flag_dict[subcategory.id][flag.id],
                                    )
                                )
                            flag.value = val
                        else:
                            flag.value = flag_dict[subcategory.id][flag.id]
                    else:
                        if utils.isclass_or_instance(flag, flags.CategorizationFlag):
                            flag.disabled = [
                                i for i in flag.options if i not in flag.enabled
                            ]
                        else:
                            flag.value = flag.default
                    self._all_flags.append(flag)

        # reject illegal flag combinations
        if (
            self.get_flag(flags.MaxCharacters).value
            < self.get_flag(flags.StartingCharacters).value
        ):
            raise flags.FlagError(
                "Your max characters setting is lower than your starting party size setting"
            )
        if PlayableCharacters.mario in self.get_flag(
            flags.AvailableCharacters
        ).disabled and (
            # self.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mario)
            # or self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario)
            self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario)
            # or self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario)
            # or self.is_flag_value(flags.SeaGate, SeaGating.mario)
        ):
            raise flags.FlagError(
                "Mario is required for one of your Progression settings, but he is excluded from the seed in your Party settings."
            )
        if PlayableCharacters.mallow in self.get_flag(
            flags.AvailableCharacters
        ).disabled and (
            self.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow)
            #            or self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow)
            or self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mallow)
            #            or self.is_flag_value(flags.SeaGate, SeaGating.mallow)
        ):
            raise flags.FlagError(
                "Mallow is required for one of your Progression settings, but he is excluded from the seed in your Party settings."
            )
        if PlayableCharacters.geno in self.get_flag(
            flags.AvailableCharacters
        ).disabled and (
            #            self.is_flag_value(flags.BanditsWayGate, BanditsWayGating.geno)
            #            or self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno)
            self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno)
            or self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.geno)
            #            or self.is_flag_value(flags.SeaGate, SeaGating.geno)
        ):
            raise flags.FlagError(
                "Geno is required for one of your Progression settings, but he is excluded from the seed in your Party settings."
            )
        if PlayableCharacters.bowser in self.get_flag(
            flags.AvailableCharacters
        ).disabled and (
            #            self.is_flag_value(flags.BanditsWayGate, BanditsWayGating.bowser)
            #            or self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser)
            self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.bowser)
            #            or self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.bowser)
            #            or self.is_flag_value(flags.SeaGate, SeaGating.bowser)
        ):
            raise flags.FlagError(
                "Bowser is required for one of your Progression settings, but he is excluded from the seed in your Party settings."
            )
        if PlayableCharacters.toadstool in self.get_flag(
            flags.AvailableCharacters
        ).disabled and (
            #            self.is_flag_value(flags.BanditsWayGate, BanditsWayGating.toadstool)
            #            or self.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool)
            self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool)
            #            or self.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool)
            or self.is_flag_value(flags.SeaGate, SeaGating.toadstool)
        ):
            raise flags.FlagError(
                "Toadstool is required for one of your Progression settings, but she is excluded from the seed in your Party settings."
            )
        # throw error if not enough chars to fill desired party
        if (
            len(self.get_flag(flags.AvailableCharacters).enabled)
            < self.get_flag(flags.StartingCharacters).value
        ):
            raise flags.FlagError(
                "You have excluded too many characters to fill your desired starting party size"
            )
        # don't allow there to be less star pieces than gating allows
        if (
            (
                self.get_flag(flags.TotalStarPieces).value < 4
                and self.is_flag_value(flags.SeaGate, SeaGating.star4)
            )
            or (
                self.get_flag(flags.TotalStarPieces).value < 6
                and self.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.star6)
            )
            or (
                self.get_flag(flags.TotalStarPieces).value < 6
                and self.is_flag_value(flags.FactoryGate, FactoryGating.star6)
            )
        ):
            raise flags.FlagError(
                "Not enough Star Pieces available to unlock world areas with your selected progression settings"
            )
        # don't allow endgame stars to be less than available stats

        if (
            self.get_flag(flags.TotalStarPieces).value
            < self.get_flag(flags.StarPiecesRequired).value
        ):
            raise flags.FlagError(
                "Star Pieces required to access the final Factory boss cannot be higher than the total Star Pieces available in the world"
            )

        # needs at least 1 damaging spell to be enabled
        requires_one_of = [
            LearnableSpells.Jump,
            LearnableSpells.FireOrb,
            LearnableSpells.SuperJump,
            LearnableSpells.SuperFlame,
            LearnableSpells.UltraJump,
            LearnableSpells.UltraFlame,
            LearnableSpells.SleepyTime,
            LearnableSpells.PsychBomb,
            LearnableSpells.Terrorize,
            LearnableSpells.PoisonGas,
            LearnableSpells.Crusher,
            LearnableSpells.BowserCrush,
            LearnableSpells.GenoBeam,
            LearnableSpells.GenoWhirl,
            LearnableSpells.GenoBlast,
            LearnableSpells.GenoFlash,
            LearnableSpells.Thunderbolt,
            LearnableSpells.Shocker,
            LearnableSpells.Snowy,
            LearnableSpells.StarRain,
        ]
        # what to do about actually applying these when seed has limited chars?
        has_required = False
        for s in requires_one_of:
            if s in self.get_flag(flags.AvailableSpells).enabled:
                has_required = True
                break
        if not has_required:
            raise flags.FlagError(
                "At least one spell must be included that can transform Mokura."
            )

        # Clean up flag selections
        # Set max # of chars from allowed chars
        allowed_chars = self.get_flag(flags.AvailableCharacters).enabled
        max_chars = self.get_flag(flags.MaxCharacters).value
        if max_chars < len(allowed_chars):
            available_chars = []
            starter = self.get_flag(flags.StartingCharacter).value
            if starter != PlayableCharacters.random:
                if starter not in allowed_chars:
                    raise flags.FlagError(
                        "Your selected starting character is excluded in your Allowed Characters settings"
                    )
                available_chars.append(starter)
            flag_val = self.get_flag(flags.AvailableCharacters)
            available_chars.extend(
                random.sample(
                    [c for c in allowed_chars if c != starter],
                    k=max_chars - len(available_chars),
                )
            )
            flag_val.enabled = available_chars
            flag_val.disabled = [
                c for c in flag_val.options if c not in available_chars
            ]

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

        for category in [
            f
            for f in flags.CATEGORIES
            if not utils.isclass_or_instance(f, flags.CosmeticCategory)
        ]:
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
                        choice_rep_string = ""
                        for f in flag.options:
                            if f in flag.enabled:
                                choice_rep += 1 << ctr
                            ctr += 1
                            if ctr == 6:
                                choice_rep_string += b64_table[choice_rep]
                                ctr = 0
                                choice_rep = 0
                        if ctr > 0:
                            choice_rep_string += b64_table[choice_rep]
                        flagstring_parts.append("%s:%s" % (flag.id, choice_rep_string))
                if len(flagstring_parts) is not 0:
                    flag_strings.append(
                        "%s.%s" % (subcategory.id, "|".join(flagstring_parts))
                    )
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

    def update_flag(self, flag_class, flag_value):
        ind = [
            (index, f)
            for (index, f) in self._all_flags
            if utils.isclass_or_instance(f, flag_class)
        ][0][0]
        self._all_flags[ind] = flag_value

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
        self.file_select_character = "Mario"
        self.file_select_hash = "MARIO1 / MARIO2 / MARIO3 / MARIO4"
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

        # Dialogs
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
        self.spotted_character_checks = data.chests.get_spotted_character_checks(self)
        self.starting_character = 0

        # Spells
        self.spells = data.spells.get_default_spells(self)
        self.spells_dict = dict([(s.index, s) for s in self.spells])

        # Starting FP.
        self.starting_fp = data.spells.STARTING_FP

        # Items
        self.items = data.items.get_default_items(self)
        self.recruitable_characters = data.items.get_recruitable_characters(self)
        self.shuffler_spells = data.items.get_placeable_spells(self)
        self.shuffler_fights = data.items.get_placeable_boss_fights(self)
        # print(self.shuffler_fights)
        self.items_dict = dict(
            [
                (i.index, i)
                for i in self.items
                + self.recruitable_characters
                + self.shuffler_spells
                + self.shuffler_fights
            ]
        )

        # Shops
        self.shops = data.shops.get_default_shops(self)
        self.special_shops = data.shops.get_event_shops(self)

        # Enemies
        self.enemies = data.enemies.get_default_enemies(self)
        self.enemies_dict = dict([(e.index, e) for e in self.enemies])

        # Get enemy attack data.
        self.enemy_attacks = data.attacks.get_default_enemy_attacks(self)

        # Get enemy formation data.
        (
            self.enemy_formations,
            self.formation_packs,
        ) = data.formations.get_default_enemy_formations(self)
        self.enemy_formations_dict = dict((f.index, f) for f in self.enemy_formations)
        self.formation_packs_dict = dict((p.index, p) for p in self.formation_packs)

        # Get item, character, boss, spell placement data.
        self.chest_locations = data.chests.get_default_chests(self)
        self.freestanding_item_locations = data.chests.get_freestanding_item_checks(
            self
        )
        self.spell_placements = data.chests.get_spell_slots(self)
        self.boss_fight_placements = data.chests.get_boss_fight_placements(self)
        self.starter_character_checks = data.chests.get_starter_character_checks(self)
        self.recruitable_character_checks = (
            data.chests.get_recruitable_character_checks(self)
        )

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

        self.sprites = commonsprites

    @property
    def open_mode(self):
        """Check if this game world is Open mode.

        Returns:
            bool:

        """
        return self.settings.mode == "open"

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

    def get_check_instance(self, cls):
        all_checks = (
            self.chest_locations
            + self.freestanding_item_locations
            + self.spell_placements
            + self.boss_fight_placements
            + self.starter_character_checks
            + self.recruitable_character_checks
        )
        return next((x for x in all_checks if utils.isclass_or_instance(x, cls)), None)

    def get_character_instance(self, cls):
        return next(
            (x for x in self.characters if utils.isclass_or_instance(x, cls)), None
        )

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

    def is_starting_character(self, cls):
        for c in self.starter_character_checks:
            if utils.isclass_or_instance(c, cls):
                return True
        return False

    def randomize(self):
        print("randomizing data...")
        """Randomize this entire game world instance."""
        # Seed the PRNG at the start.
        spells.randomize_all(self)
        chests.randomize_all(self)
        characters.randomize_all(self)
        items.randomize_all(self)
        bosses.randomize_all(self)
        # Bosses might have to go before enemies to make formation rando work as intended?
        enemies.randomize_all(self)
        characters.finalize_all(
            self
        )  # set levels AFTER chest shuffle so that we know who starters are
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
        final_seed += VERSION.encode("utf-8")
        final_seed += self.seed.to_bytes(4, "big")
        final_seed += self.settings.mode.encode("utf-8")
        final_seed += self.settings.flag_string.encode("utf-8")
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
            self.eventscripts[event].insert(
                0, utils.new_command(event, "set_bit", pair)
            )

    def prepend_notice(self, event, dialog):
        self.eventscripts[event].insert(
            0,
            utils.new_command(
                event,
                "run_dialog",
                [dialog, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
            ),
        )

    @property
    def max_chest_quality(self):
        tiers_allowed = 1
        if self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t1):
            tiers_allowed = 4
        elif self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t2):
            tiers_allowed = 3
        elif self.settings.is_flag_value(flags.ItemQuality, ItemQualities.t3):
            tiers_allowed = 2
        return tiers_allowed

    @property
    def max_shop_quality(self):
        tiers_allowed = 1
        if self.settings.is_flag_value(flags.ShopQuality, ShopQualities.t1):
            tiers_allowed = 4
        elif self.settings.is_flag_value(flags.ShopQuality, ShopQualities.t2):
            tiers_allowed = 3
        elif self.settings.is_flag_value(flags.ShopQuality, ShopQualities.t3):
            tiers_allowed = 2
        return tiers_allowed

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
        self.eventscripts[3949][1]["args"] = [required_star_pieces]
        self.dialog_data[1][217] = "%i[await]" % required_star_pieces

        # Alternate star piece win conditions
        if self.settings.is_flag_value(flags.RequireBossFights, True):
            self.prepend_bits(192, [[0x7086, 7]])
            # disable mack skip
            self.rooms[326].objects[10].event_script = 256

        starting_characters = [
            c.item for c in self.starter_character_checks if c.item is not None
        ]

        # Bandit's Way gating
        if self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.open):
            self.prepend_bits(192, [[0x7065, 4], [0x706D, 4]])
        elif self.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.mushroomway
        ):
            self.prepend_bits(199, [[0x7065, 4], [0x706D, 4]])
            self.prepend_notice(199, 2256)
            self.replace_dialog(
                1053,
                """ To get to Bandit's Way, you will\n first need to take care of\n business in Mushroom Way.[await]""",
            )
        # elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mario):
        #     self.prepend_bits(187, [[0x7065, 4], [0x706D, 4]])
        #     if not self.is_starting_character(data.items.MarioRecruit):
        #         self.prepend_notice(187, 2256)
        elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow):
            self.prepend_bits(198, [[0x7065, 4], [0x706D, 4]])
            if not self.is_starting_character(data.items.MallowRecruit):
                self.prepend_notice(198, 2256)
            self.replace_dialog(
                1053,
                """ To get to Bandit's Way, you will\n need to rendezvous with a cloudy\n sorceror.[await]""",
            )
        # elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.geno):
        #     self.prepend_bits(189, [[0x7065, 4], [0x706D, 4]])
        #     if not self.is_starting_character(data.items.GenoRecruit):
        #         self.prepend_notice(189, 2256)
        # elif self.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.bowser):
        #     self.prepend_bits(190, [[0x7065, 4], [0x706D, 4]])
        #     if not self.is_starting_character(data.items.BowserRecruit):
        #         self.prepend_notice(190, 2256)
        # elif self.settings.is_flag_value(
        #     flags.BanditsWayGate, BanditsWayGating.toadstool
        # ):
        #     self.prepend_bits(191, [[0x7065, 4], [0x706D, 4]])
        #     if not self.is_starting_character(data.items.ToadstoolRecruit):
        #         self.prepend_notice(191, 2256)
        elif self.settings.is_flag_value(
            flags.BanditsWayGate, BanditsWayGating.hammerbro
        ):
            self.replace_dialog(
                1053,
                """ To get to Bandit's Way, you will\n need to locate and trounce a pair\n of well-equipped turtles.[await]""",
            )

        # Forest Maze gating, special conditions
        if self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.open):
            self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])
        elif self.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.pie):
            self.prepend_bits(203, [[0x7066, 3], [0x706E, 3]])
            self.prepend_notice(203, 2257)

        # Pipe Vault gating
        if self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.forest):
            self.prepend_bits(211, [[0x7055, 7]])
            self.prepend_notice(211, 2258)
            self.replace_dialog(
                1052,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. The guy\n working on it went to take a break\n in the forest.[await]""",
            )
        # elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mario):
        #     self.prepend_bits(187, [[0x7055, 7]])
        #     if not self.is_starting_character(data.items.MarioRecruit):
        #         self.prepend_notice(187, 2258)
        # elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.mallow):
        #     self.prepend_bits(198, [[0x7055, 7]])
        #     if not self.is_starting_character(data.items.MallowRecruit):
        #         self.prepend_notice(198, 2258)
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.geno):
            self.prepend_bits(189, [[0x7055, 7]])
            if not self.is_starting_character(data.items.GenoRecruit):
                self.prepend_notice(189, 2258)
            self.replace_dialog(
                1052,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. The guy\n working on it went looking for\n someone named “`GENO_NAME`”.[await]""",
            )
        # elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.bowser):
        #     self.prepend_bits(190, [[0x7055, 7]])
        #     if not self.is_starting_character(data.items.BowserRecruit):
        #         self.prepend_notice(190, 2258)
        # elif self.settings.is_flag_value(
        #     flags.PipeVaultGate, PipeVaultGating.toadstool
        # ):
        #     self.prepend_bits(191, [[0x7055, 7]])
        #     if not self.is_starting_character(data.items.ToadstoolRecruit):
        #         self.prepend_notice(191, 2258)
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.open):
            self.prepend_bits(192, [[0x7055, 7]])
        elif self.settings.is_flag_value(flags.PipeVaultGate, PipeVaultGating.bowyer):
            self.replace_dialog(
                1052,
                """ There's a pipe in the road a bit\n west of here. I wonder what's\n down there?[await][page]\n It might be closed, though. The guy\n working on it was hunting for the\n jerk shooting arrows into town.[await]""",
            )

        # Moleville entrance gating
        if self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.forest):
            self.prepend_bits(211, [[0x707B, 3]])
            self.prepend_notice(211, 2269)
            self.replace_dialog(
                1051,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n left to gather up wood in the\n forest.[await]""",
            )
        # elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.mario):
        #     self.prepend_bits(187, [[0x707B, 3]])
        #     if not self.is_starting_character(data.items.MarioRecruit):
        #         self.prepend_notice(187, 2258)
        # elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.mallow):
        #     self.prepend_bits(198, [[0x707B, 3]])
        #     if not self.is_starting_character(data.items.MallowRecruit):
        #         self.prepend_notice(198, 2258)
        elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.geno):
            self.prepend_bits(189, [[0x707B, 3]])
            if not self.is_starting_character(data.items.GenoRecruit):
                self.prepend_notice(189, 2269)
            self.replace_dialog(
                1051,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n left to chat with some fella named\n “`GENO_NAME`”, or somethin'.[await]""",
            )
        # elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.bowser):
        #     self.prepend_bits(190, [[0x707B, 3]])
        #     if not self.is_starting_character(data.items.BowserRecruit):
        #         self.prepend_notice(190, 2258)
        # elif self.settings.is_flag_value(
        #     flags.Moleville1Gate, Moleville1Gating.toadstool
        # ):
        #     self.prepend_bits(191, [[0x707B, 3]])
        #     if not self.is_starting_character(data.items.ToadstoolRecruit):
        #         self.prepend_notice(191, 2258)
        elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.open):
            self.prepend_bits(192, [[0x707B, 3]])
        elif self.settings.is_flag_value(flags.Moleville1Gate, Moleville1Gating.bowyer):
            self.replace_dialog(
                1051,
                """ The menfolk'll help you get inside\n once they come back to town.[await][pause] They\n left to go hunt down some fella\n named “Bowyer”, or somethin'.[await]""",
            )

        # Starting characters - necessary to determine booster tower script
        # maintain the join order to match cursor character
        self.starter_character_checks.reverse()
        populated_starters = [
            c for c in self.starter_character_checks if c.item is not None
        ]
        REMOVE_DUMMY = enum.auto()
        populated_starters.insert(len(populated_starters) - 1, REMOVE_DUMMY)
        for position, c in enumerate(populated_starters):
            if c == REMOVE_DUMMY:
                # remove placeholder member after setting first starter char so party size doesnt unintentionally go over 4 and unlock switch menu too early
                self.eventscripts[192].insert(
                    0, utils.new_command(192, "leave_party", [AreaObjects.DUMMY_0X05])
                )
            else:
                if utils.isclass_or_instance(c, data.chests.StarterCharacter1):
                    # Use first character to join as file select cursor.
                    if utils.isclass_or_instance(c.item, data.items.MallowRecruit):
                        cursor_id = 4
                    elif utils.isclass_or_instance(c.item, data.items.GenoRecruit):
                        cursor_id = 3
                    elif utils.isclass_or_instance(c.item, data.items.BowserRecruit):
                        cursor_id = 2
                    elif utils.isclass_or_instance(c.item, data.items.ToadstoolRecruit):
                        cursor_id = 1
                    else:
                        cursor_id = 0
                    self.starting_character = cursor_id
                    if self.settings.is_flag_enabled(flags.PlayAsStarter):
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_NAME`", c.item.placeholder
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_GENDER`", c.item.gender
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_HONORIFIC`", c.item.honorific
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_HONORIFIC_CAP`",
                            c.item.honorific.capitalize(),
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_HONORIFIC_CAPS`", c.item.honorific.upper()
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_TITLE`", c.item.title
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_TITLE_SHORT`", c.item.title_short
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_GENDER_CASUAL_CAP`",
                            c.item.gender_casual.capitalize(),
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_MOLE_GREETING`", c.item.mole_greeting
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_MBOY_GREETING`", c.item.mboy_greeting
                        )
                        if cursor_id == 1:
                            self.replace_dialog(
                                2320,
                                " Hello, Princess![await][pause] Did you forget\n something in your room?[await]",
                            )
                    else:
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_NAME`", "`MARIO_NAME`"
                        )
                        self.search_replace_dialog("`MAIN_CHARACTER_GENDER`", "man")
                        self.search_replace_dialog("`MAIN_CHARACTER_HONORIFIC`", "sir")
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_HONORIFIC_CAP`", "Sir"
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_HONORIFIC_CAPS`", "SIR"
                        )
                        self.search_replace_dialog("`MAIN_CHARACTER_TITLE`", "mister")
                        self.search_replace_dialog("`MAIN_CHARACTER_TITLE_SHORT`", "Mr")
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_GENDER_CASUAL_CAP`", "Guy"
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_MOLE_GREETING`", "mate"
                        )
                        self.search_replace_dialog(
                            "`MAIN_CHARACTER_MBOY_GREETING`", ", man"
                        )
                # set character
                self.eventscripts[c.event].insert(
                    0,
                    utils.new_command(
                        c.event, "run_event_as_subroutine", [c.item.starter_script]
                    ),
                )
                # check if character gates forest maze
                if (
                    # (
                    #     self.settings.is_flag_value(
                    #         flags.ForestMazeGate, ForestMazeGating.mario
                    #     )
                    #     and utils.isclass_or_instance(c.item, data.items.MarioRecruit)
                    # )
                    # or (
                    #     self.settings.is_flag_value(
                    #         flags.ForestMazeGate, ForestMazeGating.mallow
                    #     )
                    #     and utils.isclass_or_instance(c.item, data.items.MallowRecruit)
                    # )
                    # or (
                    self.settings.is_flag_value(
                        flags.ForestMazeGate, ForestMazeGating.geno
                    )
                    and utils.isclass_or_instance(c.item, data.items.GenoRecruit)
                    # )
                    # or (
                    #     self.settings.is_flag_value(
                    #         flags.ForestMazeGate, ForestMazeGating.bowser
                    #     )
                    #     and utils.isclass_or_instance(c.item, data.items.BowserRecruit)
                    # )
                    # or (
                    #     self.settings.is_flag_value(
                    #         flags.ForestMazeGate, ForestMazeGating.toadstool
                    #     )
                    #     and utils.isclass_or_instance(
                    #         c.item, data.items.ToadstoolRecruit
                    #     )
                    # )
                ):
                    self.prepend_bits(192, [[0x7066, 3], [0x706E, 3]])

        # Booster Tower gating
        if self.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.open):
            self.prepend_bits(192, [[0x7053, 6]])
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.mines
        ):
            self.prepend_bits(199, [[0x7053, 6]])
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.mario
        ):
            self.prepend_bits(187, [[0x7053, 7]])
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n a pretty good jumper for that.[await]""",
            )
            if not self.is_starting_character(data.items.MarioRecruit):
                self.prepend_notice(187, 2259)
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 0:
                self.eventscripts[1331] = copy.deepcopy(tower_mario_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_mario)
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.mallow
        ):
            self.prepend_bits(198, [[0x7053, 7]])
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n some pretty magical fluff for that.[await]""",
            )
            if not self.is_starting_character(data.items.MallowRecruit):
                self.prepend_notice(198, 2259)
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 4:
                self.eventscripts[1331] = copy.deepcopy(tower_mallow_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_mallow)
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.geno
        ):
            self.prepend_bits(189, [[0x7053, 7]])
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n a pretty strong gun for that.[await]""",
            )
            if not self.is_starting_character(data.items.GenoRecruit):
                self.prepend_notice(189, 2259)
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 3:
                self.eventscripts[1331] = copy.deepcopy(tower_geno_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_geno)
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.bowser
        ):
            self.prepend_bits(190, [[0x7053, 7]])
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n a REALLY strong person for that.[await]""",
            )
            if not self.is_starting_character(data.items.BowserRecruit):
                self.prepend_notice(190, 2259)
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 2:
                self.eventscripts[1331] = copy.deepcopy(tower_bowser_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_bowser)
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.toadstool
        ):
            self.prepend_bits(191, [[0x7053, 7]])
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n to track down a for that.[await]""",
            )
            if not self.is_starting_character(data.items.ToadstoolRecruit):
                self.prepend_notice(191, 2259)
            if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id == 1:
                self.eventscripts[1331] = copy.deepcopy(tower_toadstool_self)
            else:
                self.eventscripts[1331] = copy.deepcopy(tower_toadstool)
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.punchinello
        ):
            self.replace_dialog(
                1163,
                """ You can't get inside Booster's\n Tower very easily. You'll need\n to track down a hot-head for that.[await]""",
            )

        if not self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.geno
        ):
            self.rooms[202].objects[4].model.occupant = data.npcs.Empty
        if not self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.toadstool
        ):
            self.rooms[202].objects[5].model.occupant = data.npcs.Empty

        # Marrymore gating
        if self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.open):
            self.prepend_bits(192, [[0x704C, 7]])
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.hill):
            self.prepend_bits(204, [[0x704C, 7]])
            self.prepend_notice(204, 2260)
            self.eventscripts[985] = [
                {
                    "identifier": "EVENT_985_do_hill",
                    "command": "jmp_if_bit_clear",
                    "args": [0x704D, 7, "EVENT_991_hill"],
                },
                {"identifier": "EVENT_985_do_hill_2", "command": "ret"},
            ]
        elif self.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.tower):
            self.prepend_bits(205, [[0x704C, 7]])
            self.prepend_notice(205, 2260)

        # Sea gating
        if self.settings.is_flag_value(flags.SeaGate, SeaGating.open):
            self.prepend_bits(192, [[0x7067, 4], [0x706F, 3], [0x7067, 5], [0x706F, 4]])
        # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.mario):
        #     self.prepend_bits(187, [[0x7067, 4], [0x706F, 3]])
        #     if not self.is_starting_character(data.items.MarioRecruit):
        #         self.prepend_notice(187, 2261)
        # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.mallow):
        #     self.prepend_bits(198, [[0x7067, 4], [0x706F, 3]])
        #     if not self.is_starting_character(data.items.MallowRecruit):
        #         self.prepend_notice(198, 2261)
        # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.geno):
        #     self.prepend_bits(189, [[0x7067, 4], [0x706F, 3]])
        #     if not self.is_starting_character(data.items.GenoRecruit):
        #         self.prepend_notice(189, 2261)
        # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.bowser):
        #     self.prepend_bits(190, [[0x7067, 4], [0x706F, 3]])
        #     if not self.is_starting_character(data.items.BowserRecruit):
        #         self.prepend_notice(190, 2261)
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.toadstool):
            self.prepend_bits(191, [[0x7067, 4], [0x706F, 3]])
            if not self.is_starting_character(data.items.ToadstoolRecruit):
                self.prepend_notice(191, 2261)
                self.replace_dialog(
                    1054,
                    """ Did you know there's a shipwreck\n off the beach to the south?[await]\n `PEACH_NAME` can help you get there.[await]""",
                )
        # else:
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            # if self.settings.is_flag_value(flags.SeaGate, SeaGating.star1):
            #     value = 1
            # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star2):
            #     value = 2
            # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star3):
            #     value = 3
            # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            # if self.settings.is_flag_value(flags.SeaGate, SeaGating.star4):
            value = 4
            # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star5):
            #     value = 5
            # elif self.settings.is_flag_value(flags.SeaGate, SeaGating.star6):
            #     value = 6
            gate_script = copy.deepcopy([{**s} for s in self.eventscripts[206]])
            gate_script[1]["args"][1] = value
            self.eventscripts[206] = gate_script
            self.prepend_bits(192, [[0x7051, 0]])
            self.replace_dialog(
                1054,
                """ Did you know there's a shipwreck\n off the beach to the south?[await]\n It will be pretty easy to find if you\n have four stars to guide you.[await]""",
            )
            # else:
            #     raise Exception("failed to set star piece gate on sea")
        elif self.settings.is_flag_value(flags.SeaGate, SeaGating.bundt):
            self.replace_dialog(
                1054,
                """ Did you know there's a shipwreck\n off the beach to the south?[await]\n You'll need to vanquish a large\n cake in order to make it more\n visible.[await]""",
            )

        # Yaridovich gating
        if self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.open):
            self.prepend_bits(192, [[0x7057, 1]])
        elif self.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.ship):
            self.prepend_bits(210, [[0x7057, 1]])
            # self.prepend_notice(210, 2262)

        # Belome Temple gating
        if self.settings.is_flag_value(flags.BelomeTempleGate, BelomeTempleGating.open):
            self.prepend_bits(192, [[0x7052, 2]])
        elif self.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.seaside
        ) or self.settings.is_flag_value(
            flags.BelomeTempleGate, BelomeTempleGating.yarid
        ):
            self.eventscripts[192].insert(
                0,
                utils.new_command(
                    192,
                    "remove_from_level",
                    [AreaObjects.NPC_3, Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM],
                ),
            )
            if self.settings.is_flag_value(
                flags.BelomeTempleGate, BelomeTempleGating.seaside
            ):
                self.replace_dialog(
                    1274,
                    """ Look for the whirl where the ant\n pops up and proceed after it.[await][page]\n Keep following it and you'll find\n your way underground.[await][page]\n But be careful, you won't be able\n to go very far down there until you\n help out in Seaside Town.[await]""",
                )
                self.eventscripts[1147].insert(
                    len(self.eventscripts[1147]) - 1,
                    utils.new_command(
                        1147,
                        "run_dialog",
                        [
                            2263,
                            AreaObjects.BOWSER,
                            [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC],
                        ],
                    ),
                )
                self.eventscripts[1147].insert(
                    len(self.eventscripts[1147]) - 1,
                    utils.new_command(
                        1147,
                        "set_bit",
                        [0x7052, 2],
                    ),
                )
            else:
                self.replace_dialog(
                    1274,
                    """ Look for the whirl where the ant\n pops up and proceed after it.[await][page]\n Keep following it and you'll find\n your way underground.[await][page]\n But be careful, you won't be able\n to go very far down there until you\n find Yaridovich.[await]""",
                )

        # Monstro Town gating
        if self.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.open):
            self.prepend_bits(192, [[0x7067, 7], [0x706F, 6]])
        elif self.settings.is_flag_value(
            flags.MonstroTownGate, MonstroTownGating.landsend
        ):
            self.eventscripts[1584].insert(
                0,
                utils.new_command(
                    1584,
                    "set_bit",
                    [0x7067, 7],
                ),
            )
            self.eventscripts[1584].insert(
                0,
                utils.new_command(
                    1584,
                    "set_bit",
                    [0x706F, 6],
                ),
            )

        # Volcano gating
        if self.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.open
        ):
            self.prepend_bits(192, [[0x7090, 5], [0x7070, 1], [0x7068, 2]])
        elif self.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.nimbus
        ):
            self.prepend_bits(3660, [[0x7090, 5]])
            self.prepend_notice(3660, 2268)
            self.replace_dialog(
                2474,
                """ Oh, hello there! Are you visiting?[await]\n We don't get tourists here very\n often. I guess our town is a little\n bit out of the way.[await][page]\n If you're looking for something fun\n to do, you should visit our\n volcano![await][pause] You might need to clear\n out the castle first, though.[await]""",
            )
        elif self.settings.is_flag_value(
            flags.BarrelVolcanoGate, BarrelVolcanoGating.valentina
        ):
            self.replace_dialog(
                2474,
                """ Oh, hello there! Are you visiting?[await]\n We don't get tourists here very\n often. I guess our town is a little\n bit out of the way.[await][page]\n If you're looking for something fun\n to do, you should visit our\n volcano![await][pause] You might need\n Valentina's permission to enter,\n though.[await]""",
            )

        # Bowser's Keep gating
        if self.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.open):
            self.prepend_bits(192, [[0x7068, 3]])
            self.search_replace_dialog(
                "`BOWSERS_KEEP_CONDITION`", """from the\n world map."""
            )
        else:
            self.prepend_bits(192, [[0x707A, 3]])
            if self.settings.is_flag_value(
                flags.BowsersKeepGate, BowsersKeepGating.volcano
            ):
                self.prepend_bits(192, [[0x707B, 2]])
                self.search_replace_dialog(
                    "`BOWSERS_KEEP_CONDITION`", """via\n the nearby volcano."""
                )
                self.eventscripts[208].insert(
                    1,
                    utils.new_command(
                        208,
                        "run_dialog",
                        [
                            2264,
                            AreaObjects.BOWSER,
                            [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC],
                        ],
                    ),
                )
            # else:
            # if self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star1
            # ):
            #     value = 1
            #     self.search_replace_dialog(
            #         "`BOWSERS_KEEP_CONDITION`", """with\n 1 Star Piece."""
            #     )
            # elif self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star2
            # ):
            #     value = 2
            #     self.search_replace_dialog(
            #         "`BOWSERS_KEEP_CONDITION`", """with\n 2 Star Pieces."""
            #     )
            # elif self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star3
            # ):
            #     value = 3
            #     self.search_replace_dialog(
            #         "`BOWSERS_KEEP_CONDITION`", """with\n 3 Star Pieces."""
            #     )
            # elif self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star4
            # ):
            #     value = 4
            #     self.search_replace_dialog(
            #         "`BOWSERS_KEEP_CONDITION`", """with\n 4 Star Pieces."""
            #     )
            # elif self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star5
            # ):
            #     value = 5
            #     self.search_replace_dialog(
            #         "`BOWSERS_KEEP_CONDITION`", """with\n 5 Star Pieces."""
            #     )
            # elif self.settings.is_flag_value(
            #     flags.BowsersKeepGate, BowsersKeepGating.star6
            # ):
            elif self.settings.is_flag_value(
                flags.BowsersKeepGate, BowsersKeepGating.star6
            ):
                value = 6
                self.search_replace_dialog(
                    "`BOWSERS_KEEP_CONDITION`", """with\n 6 Star Pieces."""
                )
                keep_script = copy.deepcopy([{**s} for s in self.eventscripts[207]])
                keep_script[1]["args"][1] = value
                self.eventscripts[207] = keep_script
                self.prepend_bits(192, [[0x7051, 1]])
                self.prepend_notice(192, 2264)
            # else:
            #    raise Exception("failed to set star piece gate on keep")

        # Factory gating
        if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.open):
            self.prepend_bits(192, [[0x7070, 5], [0x7068, 5]])
        elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.keep):
            self.prepend_bits(2149, [[0x7070, 5], [0x7068, 5]])
        elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.exor):
            self.replace_dialog(
                3726,
                """ I heard there was a big factory\n behind it. Is that true?[await][pause] I bet Exor\n would know, if you run into him![await]""",
            )
        else:
            # if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star1):
            #     value = 1
            # elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star2):
            #     value = 2
            # elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star3):
            #     value = 3
            # elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star4):
            #     value = 4
            # elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star5):
            #     value = 5
            # elif self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star6):
            if self.settings.is_flag_value(flags.FactoryGate, FactoryGating.star6):
                value = 6
                factory_script = copy.deepcopy([{**s} for s in self.eventscripts[3093]])
                factory_script[1]["args"][1] = value
                self.eventscripts[3093] = factory_script
                self.prepend_bits(192, [[0x7051, 3]])
                self.replace_dialog(
                    3726,
                    """ I heard there was a big factory\n behind it. Is that true?[await][pause] I wish I had\n 6 Star Pieces, so I could find out.[await]""",
                )

            # else:
            #    raise Exception("failed to set star piece gate on factory")

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
        if not self.settings.is_flag_value(flags.WinCondition, WinConditions.factory):
            self.eventscripts[984] = [
                utils.new_command(
                    984,
                    "jmp_if_bit_set",
                    [0x7052, 0, "EVENT_984_ret"]
                ),
                utils.new_command(
                    984,
                    self.eventscripts[1969][0]["command"],
                    self.eventscripts[1969][0]["args"],
                ),
                utils.new_command(
                    984,
                    self.eventscripts[1969][1]["command"],
                    self.eventscripts[1969][1]["args"],
                ),
            ]
            self.eventscripts[984].extend(
                [
                    {
                        "identifier": "EVENT_984_jmp_if_comparison_result_is_lesser_19",
                        "command": "jmp_if_comparison_result_is_lesser",
                        "args": ["EVENT_984_ret"],
                    },
                    {
                        "identifier": "EVENT_984_is_factory_open",
                        "command": "jmp_if_bit_set",
                        "args": [0x7070, 5, "EVENT_991_factory"],
                    },
                    {
                        "identifier": "EVENT_984_is_casino_warp",
                        "command": "jmp_if_bit_clear",
                        "args": [0x7088, 5, "EVENT_984_is_bucket_warp"],
                    },
                    {
                        "identifier": "EVENT_984_-ck2__~",
                        "command": "set_var_to_const",
                        "args": [0x7000, 174],
                    },
                    {
                        "identifier": "EVENT_984_-ck2____~",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_984_-ck2_363~",  # have castle key 2 - display hint
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_casino"]
                    },
                    {
                        "identifier": "EVENT_984_is_bucket_warp",
                        "command": "jmp_if_bit_clear",
                        "args": [0x705E, 6, "EVENT_984_ret"],
                    },
                    {
                        "identifier": "EVENT_984_is_bucket_available",
                        "command": "jmp_if_bit_clear",
                        "args": [0x7057, 4, "EVENT_984_ret"],
                    },
                ]
            )

            if self.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.shuffle1
            ):
                self.eventscripts[984].extend(
                    [
                        {
                            "identifier": "EVENT_984_have_ss",
                            "command": "set_var_to_const",
                            "args": [0x7000, 172],
                        },
                        {
                            "identifier": "EVENT_984_have_ss_2",
                            "command": "store_7000_item_quantity_to_70A7",
                        },
                        {
                            "identifier": "EVENT_984_have_ss_3",  # have fireworks
                            "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                        },
                        {
                            "identifier": "EVENT_984_have_ss-",
                            "command": "set_var_to_const",
                            "args": [0x7000, 138],
                        },
                        {
                            "identifier": "EVENT_984_have_ss_2-",
                            "command": "store_7000_item_quantity_to_70A7",
                        },
                        {
                            "identifier": "EVENT_984_have_ss_3-",  # have shiny stone
                            "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                        },
                        {
                            "identifier": "EVENT_984_have_ss--",
                            "command": "set_var_to_const",
                            "args": [0x7000, 137],
                        },
                        {
                            "identifier": "EVENT_984_have_ss_2--",
                            "command": "store_7000_item_quantity_to_70A7",
                        },
                        {
                            "identifier": "EVENT_984_have_ss_3--",  # have carbo cookie
                            "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                        },
                        {
                            "identifier": "EVENT_984_bucket_open",
                            "command": "jmp_if_object_not_in_level",
                            "args": [
                                AreaObjects.NPC_7,
                                108,
                                "EVENT_991_moleville_proper",
                            ],
                        },
                        {"identifier": "EVENT_984_ret", "command": "ret"},
                    ]
                )
                self.eventscripts[982] = [
                    {
                        "identifier": "EVENT_982_have_ss",
                        "command": "set_var_to_const",
                        "args": [0x7000, 172],
                    },
                    {
                        "identifier": "EVENT_982_have_ss_2",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_982_have_ss_3",  # have fireworks
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                    },
                    {
                        "identifier": "EVENT_982_have_ss-",
                        "command": "set_var_to_const",
                        "args": [0x7000, 138],
                    },
                    {
                        "identifier": "EVENT_982_have_ss_2-",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_982_have_ss_3-",  # have shiny stone
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                    },
                    {
                        "identifier": "EVENT_982_have_ss--",
                        "command": "set_var_to_const",
                        "args": [0x7000, 137],
                    },
                    {
                        "identifier": "EVENT_982_have_ss_2--",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_982_have_ss_3--",  # have cookie
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                    },
                    {
                        "identifier": "EVENT_982_bucket_open",
                        "command": "jmp_if_object_not_in_level",
                        "args": [AreaObjects.NPC_7, 108, "EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_982_ret", "command": "ret"},
                ]
            elif self.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.progressive
            ):
                self.eventscripts[984].extend(
                    [
                        {
                            "identifier": "EVENT_984_have_ss--",
                            "command": "set_var_to_const",
                            "args": [0x7000, 137],
                        },
                        {
                            "identifier": "EVENT_984_have_ss_2--",
                            "command": "store_7000_item_quantity_to_70A7",
                        },
                        {
                            "identifier": "EVENT_984_have_ss_3--",  # have cookie
                            "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                        },
                        {
                            "identifier": "EVENT_984_bucket_open",
                            "command": "jmp_if_object_not_in_level",
                            "args": [
                                AreaObjects.NPC_7,
                                108,
                                "EVENT_991_moleville_proper",
                            ],
                        },
                        {"identifier": "EVENT_984_ret", "command": "ret"},
                    ]
                )
                self.eventscripts[982] = [
                    {
                        "identifier": "EVENT_982_have_ss--",
                        "command": "set_var_to_const",
                        "args": [0x7000, 137],
                    },
                    {
                        "identifier": "EVENT_982_have_ss_2--",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_982_have_ss_3--",  # have cookie
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                    },
                    {
                        "identifier": "EVENT_982_bucket_open",
                        "command": "jmp_if_object_not_in_level",
                        "args": [AreaObjects.NPC_7, 108, "EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_982_ret", "command": "ret"},
                ]
            else:
                self.eventscripts[984].extend(
                    [
                        {
                            "identifier": "EVENT_984_have_ss_3--",  # have access to cookie
                            "command": "jmp",
                            "args": ["EVENT_991_moleville_proper"],
                        },
                        {"identifier": "EVENT_984_ret", "command": "ret"},
                    ]
                )
                self.eventscripts[982] = [
                    {
                        "identifier": "EVENT_982_have_ss_3--",  # have access to cookie
                        "command": "jmp",
                        "args": ["EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_982_ret", "command": "ret"},
                ]

        if self.settings.is_flag_value(flags.WinCondition, WinConditions.stars):
            self.prepend_bits(192, [[0x7051, 6]])
            self.eventscripts[3101][1]["args"][1] = [required_star_pieces]
            self.replace_dialog(
                1050,
                " I wish you the best of luck on your\n quest to collect the Star Pieces.[await]",
            )
        elif self.settings.is_flag_value(flags.WinCondition, WinConditions.sealed):
            self.prepend_bits(192, [[0x7051, 7]])
            self.replace_dialog(
                1050,
                " I wish you the best of luck on your\n quest to conquer Monstro Town.[await]",
            )
        elif self.settings.is_flag_value(flags.WinCondition, WinConditions.smithy):
            self.replace_dialog(
                1050,
                " I wish you the best of luck on your\n quest to defeat Smithy.[await]",
            )

        # Marrymore item shuffle
        if self.settings.is_flag_enabled(flags.ShuffleWeddingGear):
            self.prepend_bits(192, [[0x7086, 2]])
            self.eventscripts[979] = [
                {
                    "identifier": "EVENT_979_set_7000_to_70A0_short_mem_3",
                    "command": "set_7000_to_70A0_short_mem",
                    "args": [0x70B2],
                },
                {
                    "identifier": "EVENT_979_jmp_if_7000_equals_short_4",
                    "command": "jmp_if_var_equals_const",
        "args": [0x7000, 4, "EVENT_991_marrymore"]
                },
                {"identifier": "EVENT_979_fw_3", "command": "ret"},
            ]

        # Fireworks
        if self.settings.is_flag_value(
            flags.FireworksSetting, FireworksOptions.vanilla
        ):
            self.search_replace_dialog(
                "`FIREWORKS_CLAUSE`",
                """I'd have to go all the way through\n the mines to get some “Fireworks”\n to exchange for one of those.""",
            )
            self.eventscripts[986] = [
                {
                    "identifier": "EVENT_986_fw",
                    "command": "jmp_if_bit_set",
                    "args": [0x7057, 4, "EVENT_991_moleville_proper"],
                },
                {"identifier": "EVENT_986_fw_3", "command": "ret"},
            ]
        else:
            # assign one of 3 random fireworks
            fireworks_credits = random.randint(1, 6)
            for script_id in [184, 3399]:
                for index in range(len(self.eventscripts[script_id])):
                    cmd = self.eventscripts[script_id][index]
                    if cmd["command"] == "set" and cmd["args"][0] == 0x70EA:
                        self.eventscripts[script_id][index]["args"][
                            1
                        ] = fireworks_credits
            # append the setting
            if self.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.shuffle1
            ):
                self.prepend_bits(192, [[0x705D, 4]])
                self.search_replace_dialog(
                    "`FIREWORKS_CLAUSE`",
                    """I'd need to exchange some\n “Fireworks” for one of those, and\n I have no idea where those are.""",
                )
                self.eventscripts[986] = [
                    {
                        "identifier": "EVENT_986_have_ss",
                        "command": "set_var_to_const",
                        "args": [0x7000, 172],
                    },
                    {
                        "identifier": "EVENT_986_have_ss_2",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_986_have_ss_3",  # have fireworks
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_monstro"]
                    },
                    {
                        "identifier": "EVENT_986_have_cc",
                        "command": "set_var_to_const",
                        "args": [0x7000, 137],
                    },
                    {
                        "identifier": "EVENT_986_have_cc_2",
                        "command": "store_7000_item_quantity_to_70A7",
                    },
                    {
                        "identifier": "EVENT_986_have_cc_3",  # have cookie
                        "command": "jmp_if_var_equals_const",
        "args": [0x7000, 1, "EVENT_991_moleville_proper"]
                    },
                    {
                        "identifier": "EVENT_949_turned_in_cookie",
                        "command": "jmp_if_bit_clear",
                        "args": [0x705E, 5, "EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_986_fw_3", "command": "ret"},
                ]
                # add fireworks guy to frogfucius' first hint generator
                self.eventscripts[990] = [
                    {
                        "identifier": "EVENT_990_fw",
                        "command": "jmp_if_bit_clear",
                        "args": [0x7057, 4, "EVENT_990_fw_3"],
                    },
                    {
                        "identifier": "EVENT_990_fw_1",
                        "command": "jmp_if_bit_set",
                        "args": [0x705D, 7, "EVENT_990_fw_3"],
                    },
                    {
                        "identifier": "EVENT_990_fw_2",
                        "command": "jmp",
                        "args": ["EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_990_fw_3", "command": "ret"},
                ]
            if self.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.progressive
            ):
                self.prepend_bits(192, [[0x705D, 5]])
                self.search_replace_dialog(
                    "`FIREWORKS_CLAUSE`",
                    """I have absolutely no idea where I\n could find one of those.""",
                )
                # add fireworks guy to frogfucius' second hint generator
                self.eventscripts[981] = [
                    {
                        "identifier": "EVENT_981_fw",
                        "command": "jmp_if_bit_clear",
                        "args": [0x7057, 4, "EVENT_981_fw_3"],
                    },
                    {
                        "identifier": "EVENT_981_fw_1",
                        "command": "jmp_if_bit_set",
                        "args": [0x705D, 7, "EVENT_981_fw_3"],
                    },
                    {
                        "identifier": "EVENT_981_fw_2",
                        "command": "jmp",
                        "args": ["EVENT_991_moleville_proper"],
                    },
                    {"identifier": "EVENT_981_fw_3", "command": "ret"},
                ]

        # EXP progression option
        if self.settings.is_flag_value(
            flags.EXPChallenge, EXPChallengeOptions.easystars
        ) or self.settings.is_flag_value(
            flags.EXPChallenge, EXPChallengeOptions.hardstars
        ):
            self.prepend_bits(192, [[0x7056, 0]])
        elif self.settings.is_flag_value(
            flags.EXPChallenge, EXPChallengeOptions.easybosses
        ) or self.settings.is_flag_value(
            flags.EXPChallenge, EXPChallengeOptions.hardbosses
        ):
            self.prepend_bits(192, [[0x7056, 1]])

        # If star piece exp progression is on, set exp values for each star piece number and enable flag.
        if self.settings.is_flag_value(flags.EXPChallenge, EXPChallengeOptions.vanilla):
            pass
        else:
            if self.settings.is_flag_value(
                flags.EXPChallenge, EXPChallengeOptions.easystars
            ) or self.settings.is_flag_value(
                flags.EXPChallenge, EXPChallengeOptions.easybosses
            ):
                exps = (2, 4, 5, 6, 8, 9, 11)
            elif self.settings.is_flag_value(
                flags.EXPChallenge, EXPChallengeOptions.hardstars
            ) or self.settings.is_flag_value(
                flags.EXPChallenge, EXPChallengeOptions.hardbosses
            ):
                exps = (1, 2, 3, 5, 6, 7, 11)
            elif self.settings.is_flag_value(
                flags.EXPChallenge, EXPChallengeOptions.none
            ):
                exps = (0, 0, 0, 0, 0, 0, 0)
            else:
                raise ValueError("Unrecognized value for star exp challenge")
            patch.add_data(0x39BC44, utils.ByteField(exps[0]).as_bytes())  # 0 stars
            patch.add_data(0x39BC46, utils.ByteField(exps[1]).as_bytes())  # 1 star
            patch.add_data(0x39BC48, utils.ByteField(exps[2]).as_bytes())  # 2 stars
            patch.add_data(0x39BC4A, utils.ByteField(exps[3]).as_bytes())  # 3 stars
            patch.add_data(0x39BC4C, utils.ByteField(exps[4]).as_bytes())  # 4 stars
            patch.add_data(0x39BC4E, utils.ByteField(exps[5]).as_bytes())  # 5 stars
            patch.add_data(0x39BC52, utils.ByteField(exps[6]).as_bytes())  # 6/7 stars
            # patch.add_data(0x1fd32d, utils.ByteField(0xa0).as_bytes())  # Enable flag

        if (
            self.settings.is_flag_enabled(flags.MimicsAnywhere)
            or self.settings.is_flag_enabled(flags.StarPieceAvailability)
            or self.settings.is_flag_enabled(flags.KeyItemsAnywhere)
            or self.settings.is_flag_value(
                flags.FireworksSetting, FireworksOptions.progressive
            )
        ):
            self.eventscripts[947][len(self.eventscripts[947]) - 1]["args"][0] = 949

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
        self.eventscripts[980][1]["args"][0] = value6
        if not (
            value1 < value2
            and value2 < value3
            and value3 < value4
            and value4 < value5
            and value5 < value6
        ):
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
        else:
            self.dialog_data[0][
                387
            ] += """[page]\n One of them might be in this town.\n Have you found it yet?[await]"""
        if self.settings.is_flag_enabled(flags.SkipMustyFearsSequence):
            self.eventscripts[192].insert(
                0,
                {
                    "identifier": "EVENT_192_summon_invisible_flags",
                    "command": "run_event_as_subroutine",
                    "args": [91],
                },
            )

        if self.settings.is_flag_enabled(flags.BetterTips):
            # Boshi odds - always 10:1
            self.eventscripts[1970] = [
                utils.new_command(1970, "set_var_to_random", [0x7000, 5]),
                utils.new_command(1970, "add", [0x7000, 38]),
                utils.new_command(1970, "ret"),
            ]
            # Mushroom Boy: double odds
            self.eventscripts[1972][0]["args"][1] = 5000
            # Mokura cloud: 50% odds
            self.eventscripts[1844][0]["args"][1] = 1

        # perform non-npc sprite replacement for overworld character
        if self.settings.is_flag_enabled(flags.PlayAsStarter) and cursor_id > 0:
            if cursor_id == 4:
                nc = data.characters.Mallow
                from randomizer.data.sprites.insertions.mallow.sprites import (
                    sprites as new_sprites,
                )
                from randomizer.data.sprites.insertions.mallow.map import (
                    map_sprite,
                    map_address,
                )

                patch.add_data(map_address, map_sprite)
            elif cursor_id == 3:
                nc = data.characters.Geno
                from randomizer.data.sprites.insertions.geno.sprites import (
                    sprites as new_sprites,
                )
                from randomizer.data.sprites.insertions.geno.map import (
                    map_sprite,
                    map_address,
                )

                patch.add_data(map_address, map_sprite)
            elif cursor_id == 2:
                nc = data.characters.Bowser
                from randomizer.data.sprites.insertions.bowser.sprites import (
                    sprites as new_sprites,
                )
                from randomizer.data.sprites.insertions.bowser.map import (
                    map_sprite,
                    map_address,
                )

                patch.add_data(map_address, map_sprite)
            else:
                nc = data.characters.Peach
                from randomizer.data.sprites.insertions.toadstool.sprites import (
                    sprites as new_sprites,
                )
                from randomizer.data.sprites.insertions.toadstool.map import (
                    map_sprite,
                    map_address,
                )

                patch.add_data(map_address, map_sprite)
            for gsi, gs in enumerate(new_sprites):
                if gs is not None:
                    self.sprites[gsi] = gs
            patch.add_data(
                data.characters.Mario.battle_sprite_offset, nc.battle_sprite_id
            )
            patch.add_data(
                nc.battle_sprite_offset, data.characters.Mario.battle_sprite_id
            )
            patch.add_data(data.characters.Mario.menu_sprite_offset, nc.menu_sprite_id)
            patch.add_data(nc.menu_sprite_offset, data.characters.Mario.menu_sprite_id)
            patch.add_data(data.characters.Mario.abxy_coord_offset, nc.abxy_coord)
            patch.add_data(nc.abxy_coord_offset, data.characters.Mario.abxy_coord)
            patch.add_data(data.characters.Mario.cursor_coord_offset, nc.cursor_coord)
            patch.add_data(nc.cursor_coord_offset, data.characters.Mario.cursor_coord)
            # patch.add_data(data.characters.Mario.portrait_sprite_offset, nc.portrait_id)
            # patch.add_data(nc.portrait_sprite_offset, data.characters.Mario.portrait_id)
            patch.add_data(data.characters.Mario.item_use_offset, nc.item_use_bytes)
            patch.add_data(nc.item_use_offset, data.characters.Mario.item_use_bytes)
            patch.add_data(data.characters.Mario.runaway_offset, nc.runaway_bytes)
            patch.add_data(nc.runaway_offset, data.characters.Mario.runaway_bytes)
            for addrs, sprite_id in zip(
                data.characters.Mario.sprite_addresses, nc.original_weapon_sprite_ids
            ):
                if addrs is not None:
                    for addr in addrs:
                        patch.add_data(
                            addr + 3,
                            bytearray([sprite_id & 0xFF, (sprite_id >> 8) & 0xFF]),
                        )
            for addrs, sprite_id in zip(
                nc.sprite_addresses, nc.sprite_ids_as_main_character
            ):
                if addrs is not None:
                    for addr in addrs:
                        patch.add_data(
                            addr + 3,
                            bytearray([sprite_id & 0xFF, (sprite_id >> 8) & 0xFF]),
                        )

        # booster tower door animation
        if self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.mario
        ):
            self.rooms[202].objects[0].model.occupant = data.npcs.Mario
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.mallow
        ):
            self.rooms[202].objects[0].model.occupant = data.npcs.Mallow
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.geno
        ):
            self.rooms[202].objects[0].model.occupant = data.npcs.Geno
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.bowser
        ):
            self.rooms[202].objects[0].model.occupant = data.npcs.Bowser
        elif self.settings.is_flag_value(
            flags.BoosterTowerGate, BoosterTowerGating.toadstool
        ):
            self.rooms[202].objects[0].model.occupant = data.npcs.Toadstool

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
            patch.add_data(0x35DC9B, [0x72, 0x04, 0x19])

            # Ice Bomb
            patch.add_data(0x35DCBE, [0x8E, 0x00, 0x01])

            # Solidify
            patch.add_data(0x355721, [0x8E, 0x00, 0x01])

            # Corona
            patch.add_data(0x355DE4, [0x0A, 0x0A])

            # Dark Star
            patch.add_data(0x35C54F, [0x8E, 0x00, 0x01])

            # Shaker, Silver Bullet
            patch.add_data(
                0x35358A,
                [
                    0x3A,
                    0x34,
                    0x0F,
                    0x3F,
                    0x80,
                    0x15,
                    0x00,
                    0x00,
                    0x84,
                    0xA8,
                    0x02,
                    0x00,
                    0x40,
                    0x0F,
                    0xFF,
                    0x73,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                    0x11,
                ],
            )

            # spiked link
            patch.add_data(0x35F5B1, [0x8E, 0x00, 0x01])
            patch.add_data(0x35F5C2, [0x8E, 0x00, 0x01])
            patch.add_data(0x35F5D3, [0x8E, 0x00, 0x01])

            # Static E
            patch.add_data(
                0x354E9B,
                [
                    0x8E,
                    0x00,
                    0x01,
                    0x8E,
                    0x00,
                    0x01,
                    0x8E,
                    0x00,
                    0x01,
                    0x8E,
                    0x00,
                    0x01,
                    0x8E,
                    0x00,
                    0x01,
                ],
            )

            # Smithy
            patch.add_data(0x3AE888, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CAE, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CBB, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(
                0x3AE81F, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01]
            )  # may need to extend by 3 bytes
            patch.add_data(0x3AE888, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6C90, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])
            patch.add_data(0x3A6CAE, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01])

            # meteor swarm - dunno if this is right at all
            patch.add_data(
                0x355CA8, [0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01, 0x8E, 0x00, 0x01]
            )

            # rock candy
            patch.add_data(0x35E051, [0x8E, 0x00, 0x01])

            # meteor blast
            patch.add_data(0x3555C0, [0x8E, 0x00, 0x01])

        # Character stats, dialogs, and such
        character_names = ["Mario", "Toadstool", "Bowser", "Geno", "Mallow"]
        peach_article = ""
        for c_index, character in enumerate(self.characters):
            if self.settings.is_flag_enabled(flags.PaletteSwaps):
                if (
                    character.palette.rename_character
                    and self.settings.is_flag_enabled(flags.ChangeNames)
                ):
                    character_names[character.index] = character.palette.name
                    if character.index == 1:
                        self.search_replace_dialog(
                            "`MALLOW:`", "%s:" % character.palette.name.upper()
                        )
                if character.index == 4:
                    if character.palette.name[0] in [
                        "A",
                        "E",
                        "I",
                        "O",
                        "U",
                        "a",
                        "e",
                        "i",
                        "o",
                        "u",
                    ]:
                        peach_article = "n"
                    self.search_replace_dialog("`PEACH_ARTICLE`", peach_article)
            self.search_replace_dialog(
                character.placeholder, character_names[character.index]
            )
            patch += character.get_patch()

        # Update party join script events for the final order - Linear only
        if not self.open_mode:
            # For standard mode, Mario is the first character.  Update the other four only.
            addresses = [0x1E2155, 0x1FC506, 0x1EDF98, 0x1E8B79]
            for addr, character in zip(addresses, self.character_join_order[1:]):
                patch.add_data(addr, 0x80 + character.index)

            cursor_id = random.randint(0, 4)

            # Update other battle scripts so Belome eats the first one to join.
            for addr in (
                0x394B4D,
                0x394B70,
                0x394B74,
                0x394B7D,
                0x394B7F,
                0x394B83,
                0x3AB93F,
                0x3AB95A,
            ):
                patch.add_data(addr, self.character_join_order[1].index)

        # Learned spells and level-up exp.
        patch += self.levelup_xps.get_patch()

        # Spells
        for spell in self.spells:
            patch += spell.get_patch()

        # These spells are ignored when returning world.spells, so i'm applying the patch here to fix animation lag when randomized spells is turned on
        if self.settings.is_flag_enabled(flags.EnemySpells):
            patch.add_data(0x351415, [0x0A, 0x0A, 0x0A])
            patch.add_data(0x35142D, 0x0A)
            patch.add_data(0x35142F, [0x0A, 0x0A, 0x0A])
            patch.add_data(0x351449, 0x0A)
            patch.add_data(0x35144B, [0x0A, 0x0A, 0x0A])
            patch.add_data(0x351465, 0x0A)
            patch.add_data(0x351467, [0x0A, 0x0A, 0x0A])
            patch.add_data(0x351481, 0x0A)

        # Starting FP (twice for starting/max FP)
        patch.add_data(0x3A00DD, utils.ByteField(self.starting_fp).as_bytes() * 2)

        # For debug mode, start with 9999 coins and 999 frog coins.
        if self.debug_mode or self.settings.is_flag_enabled(flags.FreeShops):
            patch.add_data(0x3A00DB, utils.ByteField(9999, num_bytes=2).as_bytes())
            patch.add_data(0x3A00DF, utils.ByteField(999, num_bytes=2).as_bytes())
        # Add items specified by debug config.
        if self.settings.override is not None:
            if (
                "items" in self.settings.override
                and "start" in self.settings.override["items"]
            ):
                for item in self.settings.override["items"]["start"]:
                    self.eventscripts[192].insert(
                        0,
                        utils.new_command(
                            192, "put_inventory", [eval("data.items.%s.index" % item)]
                        ),
                    )
            # Set debug room specified by override config
            if "house_exit" in self.settings.override:
                self.rooms[189].exit_fields[0].destination = self.settings.override[
                    "house_exit"
                ]["room"]
                self.rooms[189].exit_fields[
                    0
                ].destination_props.x = self.settings.override["house_exit"]["x"]
                self.rooms[189].exit_fields[
                    0
                ].destination_props.y = self.settings.override["house_exit"]["y"]
                self.rooms[189].exit_fields[
                    0
                ].destination_props.z = self.settings.override["house_exit"]["z"]
                self.rooms[189].exit_fields[0].destination_props.f = eval(
                    "RadialDirection.%s"
                    % self.settings.override["house_exit"]["direction"]
                )

        # Items
        for item in self.items:
            patch += item.get_patch()
        patch += data.items.Item.build_descriptions_patch(self)

        # Open mode specific data.
        if self.open_mode:

            # Assign vram partitions
            set_partitions(self)

            print("assembling rooms and events...")

            # Assemble and patch room NPC data, exit data, event tile data, partition data, NPC data, and event data
            (
                npc_code,
                eventtile_code,
                exit_code,
                partition_code,
                model_code,
                event_table,
            ) = RoomObjects.assemble_from_table(self.rooms, self.eventscripts)
            patch.add_data(0x148000, npc_code[0] + npc_code[1])
            patch.add_data(0x20E000, eventtile_code[0] + eventtile_code[1])
            patch.add_data(0x1D2D64, exit_code[0] + exit_code[1])
            patch.add_data(0x1DDE00, partition_code)
            patch.add_data(0x1DB800, model_code)
            event_code = EventScript.assemble_from_table(event_table)
            patch.add_data(0x1E0000, event_code)

            print("assembling animation scripts...")

            # Assemble and patch object sequence bank
            sequence_code = ObjectSequenceScript.assemble_from_table(self.actionscripts)
            patch.add_data(0x210000, sequence_code)

            print("assembling packets...")

            # Assemble and patch packet data
            packet_code = Packets.assemble_from_table(self.packets)
            patch.add_data(0x1DB000, packet_code)

            print("assembling dialogs...")

            # Assemble and patch dialog data
            dialog_ptrs, dialog_code = dialogs.assemble_from_table(
                self.dialog_pointers, self.dialog_data
            )
            patch.add_data(0x37E000, dialog_ptrs)
            patch.add_data(0x220000, dialog_code[0])
            patch.add_data(0x230000, dialog_code[1])
            patch.add_data(0x240000, dialog_code[2])

            print("assembling graphics...")

            # Assemble and patch graphics data
            (
                sprite_data,
                image_data,
                animation_pointers,
                animation_data,
                tiles,
            ) = Sprites.assemble_from_tables(self.sprites)
            patch.add_data(0x250000, sprite_data)
            patch.add_data(0x251800, image_data + animation_pointers)
            for animation_offset, animation in animation_data:
                patch.add_data(animation_offset, animation)
            for tileset_offset, tileset in tiles:
                patch.add_data(tileset_offset, tileset)

        # Unlock the whole map if in debug mode in standard.
        # if self.debug_mode and not self.open_mode:
        #    patch += map.unlock_world_map()

        # This needs to happen after all battle script randomization.
        patch += assemble_battle_scripts(self)

        # Credit update
        patch += credits.update_credits(self)

        # Choose character for the file select screen.
        i = cursor_id
        file_select_char_bytes = [0, 7, 13, 25, 19]
        self.file_select_character = [c for c in self.characters if c.index == i][
            0
        ].__class__.__name__
        if self.settings.is_flag_enabled(flags.PlayAsStarter):
            i = 0
        # Change file select character graphic, if not Mario.
        if i != 0:
            addresses = [0x34757, 0x3489A, 0x34EE7, 0x340AA, 0x3501E]
            for addr, value in zip(addresses, [0, 1, 0, 0, 1]):
                patch.add_data(addr, file_select_char_bytes[i] + value)

        # Patch character names into the levelup screen
        if self.settings.is_flag_enabled(
            flags.ChangeNames
        ) and self.settings.is_flag_enabled(flags.PaletteSwaps):
            char_order = [0, 4, 3, 2, 1]
            names = [self.characters[c] for c in char_order]
            if names[0].palette.rename_character:
                mario_name = names[0].palette.name
            else:
                mario_name = names[0].name
            patch.add_data(0x02D3AF, mario_name + "\x00" * (35 - len(mario_name)))
            other_names = [
                (n.palette.name if n.palette.rename_character else n.name)
                for n in names
            ]
            name_bytes = "\x00".join(other_names[1:]) + "\x00"
            name_index = 0x030000 - len(name_bytes)
            patch.add_data(name_index, name_bytes)
            for i, c in enumerate(other_names[1:]):
                ptr = name_index & 0xFFFF
                patch.add_data(0x2D3A7 + i * 2, [ptr & 0xFF, ptr >> 8])
                name_index += len(c) + 1

        # Japanese ABXY
        if self.settings.is_flag_enabled(flags.JapaneseABXY):
            patch.add_data(
                0x255258,
                bytearray(
                    [
                        0x0C,
                        0x00,
                        0x36,
                        0x16,
                        0x3A,
                        0x27,
                        0x48,
                        0x26,
                        0xE3,
                        0x11,
                        0x07,
                        0x49,
                        0x63,
                        0x44,
                        0x00,
                        0x20,
                        0x3F,
                        0x29,
                        0xDB,
                        0x1C,
                        0xA6,
                        0x04,
                        0xC1,
                        0x08,
                    ]
                ),
            )
            patch.add_data(
                0x255C6C,
                bytearray(
                    [
                        0x0C,
                        0x00,
                        0x52,
                        0x4A,
                        0x29,
                        0x25,
                        0x48,
                        0x26,
                        0xE3,
                        0x11,
                        0x07,
                        0x49,
                        0x63,
                        0x44,
                        0x00,
                        0x20,
                        0x3F,
                        0x29,
                        0xDB,
                        0x1C,
                        0xD1,
                        0x00,
                        0xC1,
                        0x08,
                    ]
                ),
            )

        # Possible names we can use for the hash values on the file select screen.  Needs to be 6 characters or less.
        file_entry_names = {
            "MARIO",
            "MALLOW",
            "GENO",
            "BOWSER",
            "PEACH",
        }
        # Also use enemy names, if they're 6 characters or less.
        for e in self.enemies:
            if isinstance(e, data.enemies.K9):
                name = e.name
            else:
                name = re.sub(r"[^A-Za-z]", "", e.name.upper())
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
            addr = 0x3EF528 + (i * 7)
            val = name.encode().ljust(7, b"\x00")
            patch.add_data(addr, val)

        # Save file select hash text to show the user on the website, but the game uses '}' instead of dash.
        self.file_select_hash = " / ".join(file_select_names).replace("}", "-")

        # Update ROM title and version.
        title = "SMRPG-R {}".format(self.seed).ljust(20)
        if len(title) > 20:
            title = title[:19] + "?"

        # Add version number on name entry screen.
        version_text = ("v" + VERSION).ljust(10)
        if len(version_text) > 10:
            raise ValueError("Version text is too long: {!r}".format(version_text))
        patch.add_data(0x3EF140, version_text)

        # Add title and major version number to SNES header data.
        patch.add_data(0x7FC0, title)
        v = VERSION.split(".")
        patch.add_data(0x7FDB, int(v[0]))

        # a = patch.addresses
        # a.sort()

        # for p in a:
        #     if p >= 0x37A000 and p < 0x37C000:
        #         print(
        #             hex(p),
        #             len(patch.get_data(p)),
        #             #"first byte:",
        #             #hex(patch.get_data(p)[0]),
        #             patch.get_data(p)
        #         )
        #         print("")

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
            spoiler["Boss Locations"] = bosses.get_spoiler(self)
            spoiler["Item Locations"] = items.get_spoiler(self)
            spoiler["Moved Invisible Items"] = chests.get_spoiler(self)
            spoiler["Shop Items"] = shops.get_spoiler(self)
            spoiler["Character Spells"] = characters.get_spoiler(self)
            spoiler["Puzzles"] = games.get_spoiler(self)

        return spoiler
