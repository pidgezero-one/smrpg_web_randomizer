import random, hashlib
from copy import deepcopy
import re
from typing import Any, Dict, List, Optional, Type, Union
import yaml
from randomizer.entities.dialogs.overworld_dialogs.classes.dialog import (
    DialogCollection,
)
from randomizer.types.shops.classes import Shop
from randomizer.types.sprites.classes.collection import SpriteCollection
from randomizer.utils.number import coin_flip
from randomizer.types.battle_animation_scripts.classes import (
    AnimationScriptBankCollection,
)
from randomizer.types.battles.formations.classes import Formation
from randomizer.types.battles.packs.classes import FormationPack
from randomizer.types.characters.classes import Character
from randomizer.types.enemies.classes import Enemy
from randomizer.types.items.classes import Item, SpottedCharacter
from randomizer.types.monster_scripts.classes import MonsterScriptBank
from randomizer.types.overworld_scripts.event_scripts.classes import (
    EventScriptController,
)
from randomizer.types.overworld_scripts.action_scripts.classes import ActionScriptBank
from randomizer.types.patch.classes import Patch
from randomizer.types.progress_locations.classes import (
    BossFightLocation,
    BossStarPiecePrize,
    CharacterRecruitLocation,
    CharacterSpellSlot,
    CharacterSpottedLocation,
    ChestLocation,
    FreestandingLocation,
    GrantLocation,
    TProgressLocation,
)

from randomizer.types.rooms.classes import Room
from randomizer.types.spells.classes import CharacterSpell, Spell
from randomizer.types.world.flags.categories.categories import CosmeticCategory
from randomizer.types.world.flags.categories.constants import CATEGORIES
from randomizer.types.world.flags.classes import (
    BooleanFlag,
    CategorizationFlag,
    Flag,
    FlagError,
    NumberThresholdFlag,
    SelectOneFlag,
)
from randomizer.types.world.flags.enums import (
    BanditsWayGating,
    BoosterTowerGating,
    BowsersKeepGating,
    FactoryGating,
    FlagOptions,
    ForestMazeGating,
    LearnableSpells,
    PlayableCharacters,
    SeaGating,
)
from randomizer.types.world.flags.flags import (
    AvailableCharacters,
    AvailableSpells,
    BanditsWayGate,
    BoosterTowerGate,
    BowsersKeepGate,
    FactoryGate,
    ForestMazeGate,
    MaxCharacters,
    SeaGate,
    StarPiecesRequired,
    StartingCharacter,
    StartingCharacters,
    TotalStarPieces,
    TFlag,
)
from randomizer.types.world.utils import (
    set_flag_from_settings_string,
    separate_flag_string,
    get_flag_string_from_flag_collection,
)
class Settings:
    _debug_mode: bool = False
    _override: dict = {}
    _all_flags: List[Flag] = []

    @property
    def override(self) -> dict:
        return self._override

    @property
    def flag_string(self):
        """
        Returns:
            str: Computed flag string for these settings.
        """

        non_cosmetic_categories = [
            category
            for category in CATEGORIES
            if not isinstance(category, CosmeticCategory)
        ]

        return get_flag_string_from_flag_collection(non_cosmetic_categories)

    def get_flag(self, flag_class: Type[TFlag]) -> TFlag:
        return next(f for f in self._all_flags if isinstance(f, flag_class))

    def is_flag_value(self, flag_class: Type[Flag], value: Any) -> bool:
        flag = self.get_flag(flag_class)
        if (
            isinstance(flag, BooleanFlag)
            or isinstance(flag, NumberThresholdFlag)
            or isinstance(flag, SelectOneFlag)
        ):
            return flag.value == value
        elif isinstance(flag, CategorizationFlag):
            return value in flag.enabled
        else:
            raise Exception("is_flag_value unknown flag type %r" % type(flag))

    def is_boolean_flag_enabled(self, flag_class: Type[BooleanFlag]) -> bool:
        return self.is_flag_value(flag_class, True)

    def update_single_value_flag(self, flag_class: Type[Flag], value: Any) -> None:
        flag = self.get_flag(flag_class)
        if (
            isinstance(flag, BooleanFlag)
            or isinstance(flag, NumberThresholdFlag)
            or isinstance(flag, SelectOneFlag)
        ):
            flag.set_value(value)
        elif isinstance(flag, CategorizationFlag):
            raise Exception(
                "is_flag_value illegal flag type CategorizationFlag, use append_categorization_flag_options, remove_categorization_flag_options, or overwrite_categorization_flag_options"
            )
        else:
            raise Exception("is_flag_value illegal flag type %r" % type(flag))

    def append_categorization_flag_options(
        self,
        flag_class: Type[CategorizationFlag],
        options_to_append: Union[FlagOptions, List[FlagOptions]],
    ) -> None:
        flag = self.get_flag(flag_class)
        enabled = deepcopy(flag.enabled)
        if isinstance(options_to_append, FlagOptions):
            options_to_append = [options_to_append]
        enabled.extend(options_to_append)
        flag.set_enabled(enabled)

    def remove_categorization_flag_options(
        self,
        flag_class: Type[CategorizationFlag],
        options_to_remove: Union[FlagOptions, List[FlagOptions]],
    ) -> None:
        flag = self.get_flag(flag_class)
        if isinstance(options_to_remove, FlagOptions):
            options_to_remove = [options_to_remove]
        enabled = [opt for opt in flag.enabled if opt not in options_to_remove]
        flag.set_enabled(enabled)

    def overwrite_categorization_flag_options(
        self, flag_class: Type[CategorizationFlag], options: List[FlagOptions]
    ) -> None:
        flag = self.get_flag(flag_class)
        flag.set_enabled(options)

    def reject_illegal_flag_combos(self):
        # max chars less than starting party size
        max_char_setting: int = self.get_flag(MaxCharacters).value
        if max_char_setting < self.get_flag(StartingCharacters).value:
            raise FlagError(
                "Your max characters setting is lower than your starting party size setting"
            )
        # not enough chars to fill desired party
        if (
            len(self.get_flag(AvailableCharacters).enabled)
            < self.get_flag(StartingCharacters).value
        ):
            raise FlagError(
                "You have excluded too many characters to fill your desired starting party size"
            )
        required_char_settings = [
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.mario),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.mallow)
            or self.is_flag_value(BanditsWayGate, BanditsWayGating.mallow),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.geno)
            or self.is_flag_value(ForestMazeGate, ForestMazeGating.geno),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.bowser),
            self.is_flag_value(BoosterTowerGate, BoosterTowerGating.toadstool)
            or self.is_flag_value(SeaGate, SeaGating.toadstool),
        ]
        num_required = len([s for s in required_char_settings if s])
        if num_required > max_char_setting:
            raise FlagError(
                "Your Progression settings require %i different characters, but you have set your max to %s"
                % (num_required, max_char_setting)
            )

        # don't allow there to be less star pieces than gating allows
        if (
            (
                self.get_flag(TotalStarPieces).value < 4
                and self.is_flag_value(SeaGate, SeaGating.star4)
            )
            or (
                self.get_flag(TotalStarPieces).value < 6
                and self.is_flag_value(BowsersKeepGate, BowsersKeepGating.star6)
            )
            or (
                self.get_flag(TotalStarPieces).value < 6
                and self.is_flag_value(FactoryGate, FactoryGating.star6)
            )
        ):
            raise FlagError(
                "Not enough Star Pieces available to unlock world areas with your selected progression settings"
            )
        # don't allow endgame stars to be less than available stats
        if (
            self.get_flag(TotalStarPieces).value
            < self.get_flag(StarPiecesRequired).value
        ):
            raise FlagError(
                "Star Pieces required to access the final Factory boss cannot be higher than the total Star Pieces available in the world"
            )
        # don't allow empty shops
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
            if s in self.get_flag(AvailableSpells).enabled:
                has_required = True
                break
        if not has_required:
            raise FlagError(
                "At least one spell must be included that can transform Mokura."
            )

        # Clean up flag selections
        # Set max # of chars from allowed chars
        allowed_chars = self.get_flag(AvailableCharacters).enabled
        max_chars = self.get_flag(MaxCharacters).value
        available_chars = []
        if required_char_settings[0]:
            available_chars.append(PlayableCharacters.Mario)
        if required_char_settings[1]:
            available_chars.append(PlayableCharacters.Mallow)
        if required_char_settings[2]:
            available_chars.append(PlayableCharacters.Geno)
        if required_char_settings[3]:
            available_chars.append(PlayableCharacters.Bowser)
        if required_char_settings[4]:
            available_chars.append(PlayableCharacters.Toadstool)
        starter = self.get_flag(StartingCharacter).value
        if starter != PlayableCharacters.Random and starter not in available_chars:
            available_chars.append(available_chars)
        for c in available_chars:
            if c not in allowed_chars:
                raise FlagError(
                    "Your settings exclude a character that is required by one of your other settings."
                )
        if max_chars < len(available_chars):
            raise FlagError(
                "your settings require more characters than you've indicated should be allowed in the seed"
            )
        if len(available_chars) < max_chars:
            available_chars.extend(
                random.sample(
                    [c for c in allowed_chars if c not in available_chars],
                    k=max_chars - len(available_chars),
                )
            )
        if max_chars != len(available_chars):
            raise FlagError(
                "too many characters are restricted to make your settings possible"
            )
        flag_val = self.get_flag(AvailableCharacters)
        flag_val.set_enabled(available_chars)

    def __init__(
        self,
        debug_mode: bool = False,
        flag_string: str = "",
        cosmetics_string: str = "",
    ):
        self._debug_mode = debug_mode

        if self._debug_mode:
            with open("randomizer/debug/config.yml", "r") as stream:
                try:
                    self._override = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

        flag_dict: Dict[str, dict[str, Any]] = separate_flag_string(
            flag_string, cosmetics_string
        )

        # Set flags from form data.
        for category in CATEGORIES:
            for subcategory in category().subcategories:
                for flag in subcategory.flags:
                    set_flag_from_settings_string(flag_dict, flag, subcategory)
                    self._all_flags.append(flag)

        self.reject_illegal_flag_combos()


class GameWorld:
    _seed: int = 0
    _settings: Settings
    _file_select_hash: str = "MARIO1 / MARIO2 / MARIO3 / MARIO4"
    _version: str = "9.0.0"

    # scripts
    _event_scripts: EventScriptController
    _action_scripts: ActionScriptBank
    _flower_bonus_and_toad_tutorial_animation_scripts: AnimationScriptBankCollection
    _monsters_attacks_and_items_animation_scripts: AnimationScriptBankCollection
    _battle_event_animation_scripts: AnimationScriptBankCollection
    _monster_scripts: MonsterScriptBank

    # dialogs
    _dialogs: DialogCollection

    # mutable objects
    _enemies: List[Enemy] = []
    _formations: List[Optional[Formation]] = []
    _packs: List[Optional[FormationPack]] = []
    _characters: List[Character] = []
    _spotted_characters: List[SpottedCharacter] = []
    _items: List[Item] = []
    _spells: List[Spell] = []
    _shops: List[Shop] = []

    # rooms
    _rooms: List[Room] = []

    # locations
    _item_locations: List[
        Union[ChestLocation, GrantLocation, FreestandingLocation]
    ] = []
    _boss_locations: List[BossFightLocation] = []
    _boss_star_pieces: List[BossStarPiecePrize] = []
    _character_spotted_locations: List[CharacterSpottedLocation] = []
    _character_recruit_locations: List[CharacterRecruitLocation] = []
    _character_spell_slots: List[CharacterSpellSlot]

    # graphics
    _sprites: SpriteCollection

    # misc
    _chocolate_cake: bool = False

    @property
    def seed(self) -> int:
        return self._seed

    def _set_seed(self, seed: int) -> None:
        self._seed = seed

    @property
    def settings(self) -> Settings:
        return self._settings

    def _set_settings(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def file_select_hash(self) -> str:
        return self._file_select_hash

    def _set_file_select_hash(self, file_select_hash: str) -> None:
        self._file_select_hash = file_select_hash

    @property
    def version(self) -> str:
        return self._version

    @property
    def event_scripts(self) -> EventScriptController:
        return self._event_scripts

    def _set_event_scripts(self, event_scripts: EventScriptController) -> None:
        self._event_scripts = event_scripts

    @property
    def action_scripts(self) -> ActionScriptBank:
        return self._action_scripts

    def _set_action_scripts(self, action_scripts: ActionScriptBank) -> None:
        self._action_scripts = action_scripts

    @property
    def flower_bonus_and_toad_tutorial_animation_scripts(
        self,
    ) -> AnimationScriptBankCollection:
        return self._flower_bonus_and_toad_tutorial_animation_scripts

    def _set_flower_bonus_and_toad_tutorial_animation_scripts(
        self,
        flower_bonus_and_toad_tutorial_animation_scripts: AnimationScriptBankCollection,
    ) -> None:
        self._flower_bonus_and_toad_tutorial_animation_scripts = (
            flower_bonus_and_toad_tutorial_animation_scripts
        )

    @property
    def monsters_attacks_and_items_animation_scripts(
        self,
    ) -> AnimationScriptBankCollection:
        return self._monsters_attacks_and_items_animation_scripts

    def _set_monsters_attacks_and_items_animation_scripts(
        self,
        monsters_attacks_and_items_animation_scripts: AnimationScriptBankCollection,
    ) -> None:
        self._monsters_attacks_and_items_animation_scripts = (
            monsters_attacks_and_items_animation_scripts
        )

    @property
    def battle_event_animation_scripts(self) -> AnimationScriptBankCollection:
        return self._battle_event_animation_scripts

    def _set_battle_event_animation_scripts(
        self, battle_event_animation_scripts: AnimationScriptBankCollection
    ) -> None:
        self._battle_event_animation_scripts = battle_event_animation_scripts

    @property
    def monster_scripts(self) -> MonsterScriptBank:
        return self._monster_scripts

    def _set_monster_scripts(self, monster_scripts: MonsterScriptBank) -> None:
        self._monster_scripts = monster_scripts

    @property
    def dialogs(self) -> DialogCollection:
        return self._dialogs

    def _set_dialogs(self, dialogs: DialogCollection) -> None:
        self._dialogs = dialogs

    @property
    def enemies(self) -> List[Enemy]:
        return self._enemies

    def _set_enemies(self, enemies: List[Enemy]) -> None:
        self._enemies = enemies

    @property
    def formations(self) -> List[Optional[Formation]]:
        return self._formations

    def _set_formations(self, formations: List[Optional[Formation]]) -> None:
        self._formations = formations

    @property
    def packs(self) -> List[Optional[FormationPack]]:
        return self._packs

    def _set_packs(self, packs: List[Optional[FormationPack]]) -> None:
        self._packs = packs

    @property
    def characters(self) -> List[Character]:
        return self._characters

    def _set_characters(self, characters: List[Character]) -> None:
        self._characters = characters

    @property
    def spotted_characters(self) -> List[SpottedCharacter]:
        return self._spotted_characters

    def _set_spotted_characters(
        self, spotted_characters: List[SpottedCharacter]
    ) -> None:
        self._spotted_characters = spotted_characters

    @property
    def items(self) -> List[Item]:
        return self._items

    def _set_items(self, items: List[Item]) -> None:
        self._items = items

    @property
    def spells(self) -> List[Spell]:
        return self._spells

    @property
    def character_spells(self) -> List[CharacterSpell]:
        return [spell for spell in self.spells if isinstance(spell, CharacterSpell)]

    def _set_spells(self, spells: List[Spell]) -> None:
        self._spells = spells

    @property
    def shops(self) -> List[Shop]:
        return self.shops

    def _set_shops(self, shops: List[Shop]) -> None:
        self._shops = shops

    @property
    def rooms(self) -> List[Room]:
        return self._rooms

    def _set_rooms(self, rooms: List[Room]) -> None:
        self._rooms = rooms

    @property
    def item_locations(
        self,
    ) -> List[Union[ChestLocation, GrantLocation, FreestandingLocation]]:
        return self._item_locations

    def _set_item_locations(
        self,
        item_locations: List[Union[ChestLocation, GrantLocation, FreestandingLocation]],
    ) -> None:
        self._item_locations = item_locations

    @property
    def boss_locations(self) -> List[BossFightLocation]:
        return self._boss_locations

    def _set_boss_locations(self, boss_locations: List[BossFightLocation]) -> None:
        self._boss_locations = boss_locations

    @property
    def boss_star_pieces(self) -> List[BossStarPiecePrize]:
        return self._boss_star_pieces

    def _set_boss_star_pieces(self, boss_star_pieces: List[BossStarPiecePrize]) -> None:
        self._boss_star_pieces = boss_star_pieces

    @property
    def character_spotted_locations(self) -> List[CharacterSpottedLocation]:
        return self._character_spotted_locations

    def _set_character_spotted_locations(
        self, character_spotted_locations: List[CharacterSpottedLocation]
    ) -> None:
        self._character_spotted_locations = character_spotted_locations

    @property
    def character_recruit_locations(self) -> List[CharacterRecruitLocation]:
        return self._character_recruit_locations

    def _set_character_recruit_locations(
        self, character_recruit_locations: List[CharacterRecruitLocation]
    ) -> None:
        self._character_recruit_locations = character_recruit_locations

    @property
    def character_spell_slots(self) -> List[CharacterSpellSlot]:
        return self._character_spell_slots

    def _set_character_spell_slots(
        self, character_spell_slots: List[CharacterSpellSlot]
    ) -> None:
        self._character_spell_slots = character_spell_slots

    @property
    def sprites(self) -> SpriteCollection:
        return self._sprites

    def _set_sprites(self, sprites: SpriteCollection) -> None:
        self._sprites = sprites

    @property
    def chocolate_cake(self) -> bool:
        return self._chocolate_cake

    def get_item_instance(self, item_class: Type[Item]) -> Item:
        return next(x for x in self.items if isinstance(x, item_class))

    def get_enemy_instance(self, enemy_class: Type[Enemy]) -> Enemy:
        return next(x for x in self.enemies if isinstance(x, enemy_class))

    def get_character_instance(self, character_class: Type[Character]) -> Character:
        return next(x for x in self.characters if isinstance(x, character_class))

    def get_spotted_character_instance(
        self, spotted_character_class: Type[SpottedCharacter]
    ) -> SpottedCharacter:
        return next(
            x for x in self.spotted_characters if isinstance(x, spotted_character_class)
        )

    def get_spell_instance(self, spell_class: Type[Spell]) -> Spell:
        return next(x for x in self.spells if isinstance(x, spell_class))

    def get_location_instance(
        self,
        location_class: Type[TProgressLocation],
    ) -> TProgressLocation:
        search = (
            self.character_spotted_locations
            + self.character_recruit_locations
            + self.character_spell_slots
            + self.item_locations
            + self.boss_locations
            + self.boss_star_pieces
        )
        return next(x for x in search if isinstance(x, location_class))

    def _rebuild_hash(self):
        """Build hash value for choosing file select character and file name hash.
        Use the same version, seed, mode, and flags used for the database hash.
        """
        final_seed = bytearray()
        final_seed += self.version.encode("utf-8")
        final_seed += self.seed.to_bytes(4, "big")
        final_seed += self.settings.flag_string.encode("utf-8")
        self.hash = hashlib.md5(final_seed).hexdigest()

        file_entry_names = {
            "MARIO",
            "MALLOW",
            "GENO",
            "BOWSER",
            "PEACH",
        }
        # Replace file select names with "hash" values for seed verification.
        for e in self.enemies:
            name = e.name
            if name != "K9":
                name = re.sub(r"[^A-Za-z]", "", e.name.upper())
            if len(name) <= 6:
                file_entry_names.add(name)
        file_entry_names = sorted(file_entry_names)
        file_select_names = [
            file_entry_names[int(self.hash[0:8], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[8:16], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[16:24], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[24:32], 16) % len(file_entry_names)],
        ]

        # Save file select hash text to show the user on the website, but the game uses '}' instead of dash.
        self._file_select_hash = " / ".join(file_select_names).replace("}", "-")

    def __init__(
        self,
        seed: int,
        settings: Settings,
        event_scripts: EventScriptController,
        action_scripts: ActionScriptBank,
        flower_bonus_and_toad_tutorial_animation_scripts: AnimationScriptBankCollection,
        monsters_attacks_and_items_animation_scripts: AnimationScriptBankCollection,
        battle_event_animation_scripts: AnimationScriptBankCollection,
        monster_scripts: MonsterScriptBank,
        dialogs: DialogCollection,
        enemies: List[Enemy],
        formations: List[Optional[Formation]],
        packs: List[Optional[FormationPack]],
        characters: List[Character],
        spotted_characters: List[SpottedCharacter],
        items: List[Item],
        spells: List[Spell],
        shops: List[Shop],
        rooms: List[Room],
        item_locations: List[Union[ChestLocation, GrantLocation, FreestandingLocation]],
        boss_locations: List[BossFightLocation],
        boss_star_pieces: List[BossStarPiecePrize],
        character_spotted_locations: List[CharacterSpottedLocation],
        character_recruit_locations: List[CharacterRecruitLocation],
        character_spell_slots: List[CharacterSpellSlot],
        sprites: SpriteCollection
    ) -> None:
        self._set_seed(seed)
        random.seed(seed)
        self._set_settings(settings)
        self._set_event_scripts(event_scripts)
        self._set_action_scripts(action_scripts)
        self._set_flower_bonus_and_toad_tutorial_animation_scripts(
            flower_bonus_and_toad_tutorial_animation_scripts
        )
        self._set_monsters_attacks_and_items_animation_scripts(
            monsters_attacks_and_items_animation_scripts
        )
        self._set_battle_event_animation_scripts(battle_event_animation_scripts)
        self._set_monster_scripts(monster_scripts)
        self._set_dialogs(dialogs)
        self._set_enemies(enemies)
        self._set_formations(formations)
        self._set_packs(packs)
        self._set_characters(characters)
        self._set_spotted_characters(spotted_characters)
        self._set_items(items)
        self._set_spells(spells)
        self._set_shops(shops)
        self._set_rooms(rooms)
        self._set_item_locations(item_locations)
        self._set_boss_locations(boss_locations)
        self._set_boss_star_pieces(boss_star_pieces)
        self._set_character_spotted_locations(character_spotted_locations)
        self._set_character_recruit_locations(character_recruit_locations)
        self._set_character_spell_slots(character_spell_slots)
        self._set_sprites(sprites)
        # shops

        # misc
        self._chocolate_cake = coin_flip(0.1)

        self._rebuild_hash()

    def _build_patch(self):
        patch = Patch()

        file_select_names = self.file_select_hash.split(" / ")

        for i, name in enumerate(file_select_names):
            addr = 0x3EF528 + (i * 7)
            val = name.encode().ljust(7, b"\x00")
            patch.add_data(addr, val)
