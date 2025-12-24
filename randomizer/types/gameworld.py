from __future__ import annotations
from copy import deepcopy
from typing import Any, TYPE_CHECKING, TypeVar, cast
import random
import datetime
import hashlib
import re
from concurrent.futures import ThreadPoolExecutor

from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import (
    AnimationScriptBank,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments import *
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import (
    BattleDialogCollection,
)
from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from smrpgpatchbuilder.datatypes.enemies.classes import EnemyCollection
from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttackCollection
from smrpgpatchbuilder.datatypes.items.classes import (
    ItemCollection,
    Equipment,
    RegularItem,
    Weapon,
    Armor,
    Accessory,
    Item as BaseItem,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *
from smrpgpatchbuilder.datatypes.monster_scripts.types import (
    MonsterScriptBank,
    MonsterScript,
)
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import (
    DoNothing,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptController,
    EventScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import (
    PacketCollection,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    PackCollection,
)
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection
from smrpgpatchbuilder.datatypes.shops.classes import ShopCollection
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    CompareVarToConst,
    SummonObjectToSpecificLevel,
    RunEventAsSubroutine,
    SetBit,
    ClearBit,
    JmpIfBitClear,
    JmpIfVarEqualsConst,
    SetVarToConst,
    ActionQueueAsync,
    RunDialog,
    JmpIfVarNotEqualsConst,
    Inc,
    SetVarToRandom,
    JmpIfComparisonResultIsLesser,
    JmpToEvent
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
    Formation,
)
from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from smrpgpatchbuilder.datatypes.levels.classes import RoomObject, Room
from smrpgpatchbuilder.datatypes.spells.enums import Status
from smrpgpatchbuilder.datatypes.world_map_locations.classes import (
    WorldMapLocationCollection,
)
from ..data.items.items import *
from ..data.minigames.star_hill_wishes import WISH_POOL, WISH_DIALOG_IDS
from ..data.minigames.puzzle_games import (
    BallSolitaireGame,
    MagicButtonsGame,
    randomize_ball_solitaire,
    randomize_magic_buttons,
)
from ..data.minigames.quiz_questions import (
    get_quiz_questions,
    option_1_correct,
    option_2_correct,
    option_3_correct,
)
from ..data.minigames.bowser_doors import randomize_bowser_doors
from .item import Item
from .patch import Patch
from .attack import EnemyAttack
from .spell import Spell
from .prize import Prize
from .ally import Ally
from .flags import (
    Flag,
    BooleanFlag,
    RangeFlag,
    SelectOneFlag,
    CategorizationFlag,
    CosmeticCategory,
    CATEGORIES,
    # Cosmetic flags
    BossShuffleMusic,
    ShuffledMusic,
    PaletteSwaps,
    ChangeNames,
    RemakeNames,
    CanonNames,
    Peach,
    JapaneseABXY,
    RemoveFlashes,
    HoldB,
    ShowEquips,
    # Enemy flags
    EnemyAttacks,
    EnemyStats,
    EnemyStatsShuffleOptions,
    EnemyDrops,
    EnemyFormations,
    EnemySpells,
    # Equipment flags
    EquipmentCharacters,
    EquipmentCharactersOptions,
    EquipmentPropertiesOptions,
    IgnoreNamesakeProperties,
    # Shop flags
    ShuffleShops,
    ShopQuality,
    ShopQualities,
    BiasShopShuffle,
    NoPickMeUps,
    FreeShops,
    # EXP flags
    EXPMultiplier,
    EXPMultiplierOptions,
    EXPChallenge,
    EXPChallengeOptions,
    ExperienceNoBosses,
    ExperienceNoRegular,
    # Character flags
    CharacterStats,
    CharacterSpellStats,
    CharacterSpellElements,
    InfuseSpellElements,
    AvailableSpells,
    StartingCharacters,
    UncapSuperJumps,
    # Gating flags
    BanditsWayGate,
    BanditsWayGating,
    KeroSewersGate,
    KeroSewersGating,
    ForestMazeGate,
    ForestMazeGating,
    PipeVaultGate,
    PipeVaultGating,
    Moleville1Gate,
    Moleville1Gating,
    BoosterTowerGate,
    BoosterTowerGating,
    BoosterHillGate,
    BoosterHillGating,
    MarrymoreGate,
    MarrymoreGating,
    SeaGate,
    SeaGating,
    YaridovichGate,
    YaridovichGating,
    LandsEndGate,
    LandsEndGating,
    BelomeTempleGate,
    BelomeTempleGating,
    MonstroTownGate,
    MonstroTownGating,
    NimbusGate,
    NimbusGating,
    BarrelVolcanoGate,
    BarrelVolcanoGating,
    BowsersKeepGate,
    BowsersKeepGating,
    FactoryGate,
    FactoryGating,
    BowserDoorRequirements,
    StarPiecesRequired,
    # Minigame thresholds
    GrateGuyPrizeThreshold,
    KnifeGuyPrizeThreshold,
    SuitePrize1Threshold,
    SuitePrize2Threshold,
    SuitePrize3Threshold,
    SuitePrize4Threshold,
    SuitePrize5Threshold,
    SuitePrize6Threshold,
    SuperJump1Threshold,
    SuperJump2Threshold,
    # Misc flags
    FireworksSetting,
    FireworksOptions,
    WinCondition,
    WinConditions,
    FastTravel,
    CasinoWarp,
    BucketWarp,
    ShuffleWeddingGear,
    SkipBossFights,
    SkipMustyFearsSequence,
    StarPieceHints,
    InvisibleFlagsSetting,
    Remake,
    PoisonMushroom,
    NoGenoWhirlExor,
    FixMagikoopa,
    NoOHKO,
    QuizShuffle,
    BallSolitaireShuffle,
    MagicButtonShuffle,
    ShuffleHillFlowers,
    RandomTadpolePondSong,
    BetterTips,
    RandomSunkenShipPassword,
    BowserDoorShuffle,
    FixKnifeGuy,
    KnifeGuyFixedPrizeThreshold,
    SkipMinecart,
)
from .prizelocation import SIGNAL_RING_EVENT_DICT, PrizeLocation
from ..progression.prizelocations import *
from ..data.variables.dialog_names import *
from ..data.variables.battle_variable_names import *
from ..data.variables.battle_effect_names import *
from ..data.variables.shop_names import *
from ..data.variables.sprite_names import *
from ..data.spells.spells import *
from ..data.minigames.melody_bay import all_songs
from ..data.minigames.ship_password import (
    pool as password_pool,
    suggest_letter_bank,
    box_dialog_ids,
    recitation_ids,
    hint_authors,
)
from ..data.credits.credits import update_credits

from ..data.allies.palettes.types import (
    MarioPalette,
    MallowPalette,
    GenoPalette,
    BowserPalette,
    ToadstoolPalette,
)
from ..data.allies.palettes.mario import all_palettes as MARIO_PALETTES
from ..data.allies.palettes.mallow import all_palettes as MALLOW_PALETTES
from ..data.allies.palettes.geno import all_palettes as GENO_PALETTES
from ..data.allies.palettes.toadstool import all_palettes as TOADSTOOL_PALETTES
from ..data.allies.palettes.bowser import all_palettes as BOWSER_PALETTES
from .enemy import Enemy

PrizeLocationT = TypeVar("PrizeLocationT", bound=PrizeLocation)
from .settings import Settings

if TYPE_CHECKING:
    from .flags import CategorizationOption as FlagOptions


class RandomizerSettingsException(Exception):
    pass


def get_flag_string_from_flag_collection(categories: list) -> str:
    """Placeholder for flag string generation."""
    return ""


class NumberThresholdFlag(RangeFlag):
    """Alias for range flags used as thresholds."""

    pass


class WorldBuildingException(Exception):
    pass


class GameWorld:
    seed: int | str = 0
    settings: Settings
    file_select_names: list[str] = ["MARIO1", "MARIO2", "MARIO3", "MARIO4"]

    version: str = "9.0.0"
    hash: str = ""

    @property
    def file_select_hash(self) -> str:
        return " / ".join(self.file_select_names).replace("}", "-")

    # Raw data types (basis of ROM patches)

    allies: AllyCollection
    battle_animations: dict[int, AnimationScriptBank]
    battle_dialogs: BattleDialogCollection
    overworld_dialogs: DialogCollection
    enemies: EnemyCollection
    enemy_attacks: EnemyAttackCollection
    items: ItemCollection
    monster_scripts: MonsterScriptBank
    event_scripts: EventScriptController
    action_scripts: ActionScriptBank
    packets: PacketCollection
    battle_packs: PackCollection
    rooms: RoomCollection
    shops: ShopCollection
    spells: SpellCollection
    sprites: SpriteCollection
    mario_palette: MarioPalette
    mallow_palette: MallowPalette
    geno_palette: GenoPalette
    bowser_palette: BowserPalette
    toadstool_palette: ToadstoolPalette
    main_character: Ally = MARIO_Ally
    world_map_locations: WorldMapLocationCollection
    password: str = "pearls"
    song_1: str = "So La Mi Re Do Re Do Re"
    song_2: str = "Mi Do So Do Re La Ti Do"
    song_3: str = "La Ti Do Re So Do Re Mi"
    password_author: str = "ANONYMOUS"
    song_authors: list[str] = ["ANONYMOUS"]

    locations: dict[type[PrizeLocation], PrizeLocation]

    def get_item(self, item: int | type[Item]):
        if isinstance(item, int):
            i = next((i for i in self.items.items if i.item_id == item), None)
        else:
            i = next((i for i in self.items.items if isinstance(i, item)), None)
        assert i is not None, f"Item {item} does not exist in ItemCollection"
        return i

    def get_enemy(self, enemy_id: int | type[Enemy]):
        if isinstance(enemy_id, int):
            e = next(
                (e for e in self.enemies.enemies if e.monster_id == enemy_id), None
            )
        else:
            e = next((e for e in self.enemies.enemies if isinstance(e, enemy_id)), None)
        assert e is not None, f"Enemy {enemy_id} does not exist in EnemyCollection"
        return e

    def get_attack(self, attack_id: int | type[Attack]):
        if isinstance(attack_id, int):
            a = next(
                (a for a in self.enemy_attacks.attacks if a.index == attack_id), None
            )
        else:
            a = next(
                (a for a in self.enemy_attacks.attacks if isinstance(a, attack_id)),
                None,
            )
        assert (
            a is not None
        ), f"Attack {attack_id} does not exist in EnemyAttackCollection"
        return a

    def get_spell(self, spell_id: int | type[Spell]):
        if isinstance(spell_id, int):
            s = next((s for s in self.spells.spells if s.index == spell_id), None)
        else:
            s = next((s for s in self.spells.spells if isinstance(s, spell_id)), None)
        assert s is not None, f"Spell {spell_id} does not exist in SpellCollection"
        return s

    def get_dialog(self, dialog_id: int):
        d = self.overworld_dialogs.dialogs[dialog_id]
        assert d is not None, f"Dialog {dialog_id} does not exist in DialogCollection"
        return d

    def update_dialog(self, dialog_id: int, new_dialog: str):
        self.overworld_dialogs.replace_dialog(dialog_id, new_dialog)

    def get_battle_dialog(self, dialog_id: int):
        d = self.battle_dialogs.battle_dialogs[dialog_id]
        assert (
            d is not None
        ), f"Battle Dialog {dialog_id} does not exist in BattleDialogCollection"
        return d

    def get_location(self, location_type: type[PrizeLocationT]) -> PrizeLocationT:
        """Get a location instance with proper typing."""
        return cast(PrizeLocationT, self.locations[location_type])

    def update_battle_dialog(self, dialog_id: int, new_dialog: str):
        self.battle_dialogs.battle_dialogs[dialog_id] = new_dialog

    def get_monster_script(self, script: int | Enemy):
        if isinstance(script, int):
            return self.monster_scripts.scripts[script]
        else:
            return self.monster_scripts.scripts[script.monster_id]

    def update_monster_script(self, script: int | Enemy, new_script: MonsterScript):
        if isinstance(script, int):
            self.monster_scripts.replace_script(script, new_script)
        else:
            self.monster_scripts.replace_script(script.monster_id, new_script)

    def get_event_script(self, event_script_id: int):
        return self.event_scripts.get_script_by_id(event_script_id)

    def get_action_script(self, action_script_id: int):
        return self.action_scripts.scripts[action_script_id]

    def get_battle_animation_command_by_name(self, command_name: str):
        try:
            return self.battle_animations[0x02].get_command_by_name(command_name)
        except IdentifierException:
            try:
                return self.battle_animations[0x35].get_command_by_name(command_name)
            except IdentifierException:
                try:
                    return self.battle_animations[0x3A].get_command_by_name(
                        command_name
                    )
                except IdentifierException:
                    raise WorldBuildingException("No battle animation banks found")

    def get_packet(self, packet_id: int):
        p = self.packets.packets[packet_id]
        assert p is not None, f"Packet {packet_id} does not exist in PacketCollection"
        return p

    def update_packet(self, packet_id: int, new_packet):
        self.packets.packets[packet_id] = new_packet

    def get_battle_pack(self, pack_id: int):
        p = self.battle_packs.packs[pack_id]
        assert p is not None, f"Battle Pack {pack_id} does not exist in PackCollection"
        return p

    def update_battle_pack(self, pack_id: int, new_pack):
        self.battle_packs.packs[pack_id] = new_pack

    def replace_battle_pack_formations(
        self, members: list[FormationMember | None], pack_id: int
    ):
        pack = self.get_battle_pack(pack_id)
        if len(pack.formations) == 0:
            pack._formations = [Formation(members)]
            return
        formation_base = pack.formations[0]
        formation_base._members = members
        pack._formations = [formation_base]
        self.update_battle_pack(pack_id, pack)

    def get_room(self, room_id: int):
        r = self.rooms._rooms[room_id]
        assert r is not None, f"Room {room_id} does not exist in RoomCollection"
        return r

    def update_room(self, room_id: int, new_room):
        self.rooms._rooms[room_id] = new_room

    def get_shop(self, shop_id: int):
        s = self.shops.shops[shop_id]
        assert s is not None, f"Shop {shop_id} does not exist in ShopCollection"
        return s

    def update_shop(self, shop_id: int, new_shop):
        self.shops._shops[shop_id] = new_shop

    def get_sprite(self, sprite_id: int):
        s = self.sprites.sprites[sprite_id]
        assert s is not None, f"Sprite {sprite_id} does not exist in SpriteCollection"
        return s

    def update_sprite(self, sprite_id: int, new_sprite):
        self.sprites.sprites[sprite_id] = new_sprite

    def search_replace_dialog(self, search: str, replace: str):
        for bank_id, dialog_bank in enumerate(self.overworld_dialogs.raw_data):
            for index, dialog in enumerate(dialog_bank):
                self.overworld_dialogs.raw_data[bank_id][index] = dialog.replace(
                    search, replace
                )

    def _get_locations_json(self) -> dict[str, str]:
        """Return a JSON-serializable dict of all locations and their prizes.

        Keys are location class names, values are prize class names or "None".
        """
        result: dict[str, str] = {}
        for loc_type, loc in self.locations.items():
            location_name = loc_type.__name__
            if loc.prize is None:
                prize_name = "None"
            else:
                prize_name = type(loc.prize).__name__
            result[location_name] = prize_name
        return result

    @property
    def spoiler(self) -> dict[str, Any]:
        return {
            "settings": self._get_settings_json(),
            "locations": self._get_locations_json(),
            "password": self.password,
            "songs": [self.song_1, self.song_2, self.song_3],
        }

    def _get_settings_json(self) -> dict[str, Any]:
        """Get JSON representation of all settings with their names and values."""
        result: dict[str, Any] = {}
        for flag_class, flag in self.settings._flags.items():
            flag_name = flag.name
            if isinstance(flag, BooleanFlag):
                result[flag_name] = flag.enabled
            elif isinstance(flag, RangeFlag):
                result[flag_name] = flag.value
            elif isinstance(flag, SelectOneFlag):
                # Get the selected option's display value
                selected = flag.selected
                if hasattr(selected, "value"):
                    result[flag_name] = selected.value
                else:
                    result[flag_name] = str(selected)
            elif isinstance(flag, CategorizationFlag):
                # Get list of enabled options
                enabled_names = []
                for opt in flag.enabled:
                    if hasattr(opt, "value"):
                        val = opt.value
                        # Check if val is a class type (for ClassCategorizationOption)
                        if isinstance(val, type):
                            # For class types, use _title (spell title) or __name__ (class name)
                            if hasattr(val, "_title") and val._title:
                                enabled_names.append(val._title)
                            elif hasattr(val, "_name") and val._name:
                                enabled_names.append(val._name)
                            else:
                                enabled_names.append(val.__name__)
                        elif hasattr(val, "name") and isinstance(val.name, str):
                            enabled_names.append(val.name)
                        elif hasattr(val, "_name") and isinstance(val._name, str):
                            enabled_names.append(val._name)
                        else:
                            enabled_names.append(str(val))
                    elif hasattr(opt, "name"):
                        enabled_names.append(opt.name)
                    else:
                        enabled_names.append(str(opt))
                result[flag_name] = enabled_names
            else:
                result[flag_name] = str(flag)
        return result

    def _rebuild_hash(self):
        """Build hash value for choosing file select character and file name hash.
        Use the same version, seed, mode, and flags used for the database hash.
        """
        final_seed = bytearray()
        final_seed += self.version.encode("utf-8")
        if isinstance(self.seed, int):
            final_seed += self.seed.to_bytes(4, "big")
        else:
            final_seed += str(self.seed).encode("utf-8")
        final_seed += self.settings.flag_string.encode("utf-8")
        self.hash = hashlib.md5(final_seed).hexdigest()

        # Possible names we can use for the hash values on the file select screen.  Needs to be 6 characters or less.
        file_entry_names = {
            "MARIO",
            "MALLOW",
            "GENO",
            "BOWSER",
            "PEACH",
        }
        # Also use enemy names, if they're 6 characters or less.
        e_choices = set(
            [
                re.sub(r"[^A-Za-z9]", "", e.name.upper())
                for e in self.enemies.enemies
                if len(re.sub(r"[^A-Za-z9]", "", e.name.upper())) <= 6
            ]
        )
        file_entry_names = sorted(e_choices)

        # Replace file select names with "hash" values for seed verification.
        self.file_select_names = [
            file_entry_names[int(self.hash[0:8], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[8:16], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[16:24], 16) % len(file_entry_names)],
            file_entry_names[int(self.hash[24:32], 16) % len(file_entry_names)],
        ]

    # Logic
    # TODO

    def __init__(
        self,
        seed: int | str,
        version: str,
        settings: Settings,
        allies: AllyCollection,
        battle_animations: dict[int, AnimationScriptBank],
        battle_dialogs: BattleDialogCollection,
        overworld_dialogs: DialogCollection,
        enemies: EnemyCollection,
        enemy_attacks: EnemyAttackCollection,
        items: ItemCollection,
        monster_scripts: MonsterScriptBank,
        event_scripts: EventScriptController,
        action_scripts: ActionScriptBank,
        packets: PacketCollection,
        battle_packs: PackCollection,
        rooms: RoomCollection,
        shops: ShopCollection,
        spells: SpellCollection,
        sprites: SpriteCollection,
        world_map_locations: WorldMapLocationCollection,
    ):
        self.allies = allies
        self.seed = seed
        self.version = version
        self.settings = settings
        self.battle_animations = battle_animations
        self.battle_dialogs = battle_dialogs
        self.overworld_dialogs = overworld_dialogs
        self.enemies = enemies
        self.enemy_attacks = enemy_attacks
        self.items = items
        self.monster_scripts = monster_scripts
        self.event_scripts = event_scripts
        self.action_scripts = action_scripts
        self.packets = packets
        self.battle_packs = battle_packs
        self.rooms = rooms
        self.shops = shops
        self.spells = spells
        self.sprites = sprites
        self.world_map_locations = world_map_locations

        random.seed(self.seed)
        print(self.seed)

        self._set_all_locations()

        # TODO: Before setting hints, find where the mimic chests are and reassign the world areas for their prize locations

        # prize locations HAVE to all be defined by this point
        # not shuffled, just determined if they exist in the seed or not

        event_2496_startup: list[UsableEventScriptCommand] = []

        if self.settings.isflag_enabled(StarPieceHints):
            for l in self.locations.values():
                if not isinstance(l.prize, StarPiecePrize):
                    continue
                event = SIGNAL_RING_EVENT_DICT[l.world_area]
                script = self.event_scripts.get_script_by_id(event)
                script.insert_before_nth_command(
                    0, JmpIfBitClear(l.prize._hint, [f"EVENT_{event}_play_sound"])
                )

        if self.settings.isflag_enabled(SkipMustyFearsSequence):
            event_2496_startup += [RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER)]

        ### Perform progression gating setup tasks here

        # settings
        if self.settings.is_flag_value(WinCondition, WinConditions.SMITHY):
            event_2496_startup += [SetBit(SMITHY_BOSS_HUNT_WIN_CONDITION)]
        elif self.settings.is_flag_value(WinCondition, WinConditions.STARS):
            event_2496_startup += [SetBit(WIN_CONDITION_STAR_PIECES)]
        elif self.settings.is_flag_value(WinCondition, WinConditions.SEALED):
            event_2496_startup += [SetBit(WIN_CONDITION_MONSTRO_DOOR)]

        if self.settings.isflag_enabled(FastTravel):
            event_2496_startup += [SetBit(FAST_TRAVEL_ENABLED)]
        if self.settings.isflag_enabled(CasinoWarp):
            event_2496_startup += [SetBit(CASINO_WARP_ENABLED)]
        if self.settings.isflag_enabled(BucketWarp):
            event_2496_startup += [SetBit(BUCKET_WARP_ENABLED)]
        if self.settings.isflag_enabled(ShuffleWeddingGear):
            event_2496_startup += [SetBit(CHAPEL_ITEMS_ANYWHERE_ENABLED)]

        if self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.STARS):
            event_2496_startup += [SetBit(PROGRESSIVE_STAR_EXP_ENABLED)]
        elif self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.BOSSES):
            event_2496_startup += [SetBit(PROGRESSIVE_BOSS_EXP_ENABLED)]
        elif self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.NONE):
            self.event_scripts.delete_command_by_identifier("inc_exp_by_packet")

        if self.settings.isflag_enabled(SkipBossFights):
            event_2496_startup += [SetBit(ALTERNATE_STAR_PIECE_WIN_CONDITION)]

        # TODO when assembling grant scripts, set all exp star 70A7 props to 0 if NONE is selected
        # TODO verify that all bosses increase the counter, ie remake bosses

        # gates
        if self.settings.is_flag_value(BanditsWayGate, BanditsWayGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_BANDITS_WAY),
                SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
            ]
        if not self.settings.is_flag_value(KeroSewersGate, KeroSewersGating.OPEN):
            cast(
                RoomObject,
                cast(
                    Room, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE]
                ).get_npc_by_target_id(NPC_0),
            ).set_visible(True)
            cast(
                RoomObject,
                cast(
                    Room, self.rooms._rooms[R333_KERO_SEWERS_ENTRANCE]
                ).get_npc_by_target_id(NPC_1),
            ).set_visible(True)
            event_2496_startup += [SetBit(SEWERS_CLOSED)]

            if self.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
                self.event_scripts.get_script_by_id(
                    E1254_UNLOCK_SEWER_BY_RFC
                ).insert_before_nth_command(0, ClearBit(SEWERS_CLOSED))
        else:
            event_2496_startup += [ClearBit(SEWERS_CLOSED)]
        if self.settings.is_flag_value(ForestMazeGate, ForestMazeGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_FOREST_MAZE),
                SetBit(MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE),
            ]
        elif self.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
            e = self.event_scripts.get_script_by_id(E1255_UNLOCK_FOREST_BY_PIE)
            e.insert_before_nth_command(0, SetBit(MAP_FOREST_MAZE))
            e.insert_before_nth_command(0, SetBit(MAP_FOREST_MAZE))
        if not self.settings.is_flag_value(PipeVaultGate, PipeVaultGating.OPEN):
            event_2496_startup += [
                SetBit(PIPE_VAULT_GATED),
            ]
        if not self.settings.is_flag_value(Moleville1Gate, Moleville1Gating.OPEN):
            event_2496_startup += [
                SetBit(MOLEVILLE_MINES_ENTRANCE_GATING),
            ]
            if self.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
                self.event_scripts.get_script_by_id(
                    E1256_UNLOCK_MOLEVILLE_IF_GATED_BY_BOSHI
                ).insert_before_nth_command(
                    0, ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING)
                )
        if not self.settings.is_flag_value(BoosterHillGate, BoosterHillGating.OPEN):
            event_2496_startup += [
                SetBit(BOOSTER_HILL_CLOSED),
            ]
        if self.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.OPEN):
            event_2496_startup += [
                ApplySolidityModToLevel(
                    permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                ),
                ApplyTileModToLevel(
                    use_alternate=True,
                    room_id=R202_BOOSTER_TOWER_ENTRANCE,
                    mod_id=32,
                ),
                SetBit(TOWER_OPENED),
            ]
        if self.settings.is_flag_value(MarrymoreGate, MarrymoreGating.OPEN):
            event_2496_startup += [
                SetBit(MARRYMORE_BACKDOOR_OPEN),
            ]
        elif self.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
            self.event_scripts.get_script_by_id(
                E1329_HILL_UNLOCKS
            ).insert_before_nth_command(0, SetBit(MARRYMORE_BACKDOOR_OPEN))
        if self.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
            event_2496_startup += [SetBit(SEA_GATED_BY_STAR_PIECES)]
        elif self.settings.is_flag_value(SeaGate, SeaGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_SEA),
                SetBit(MAP_DIRECTIONAL_SEA_SUNKEN_SHIP),
                SetBit(MAP_SUNKEN_SHIP),
                SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
            ]
        if self.settings.is_flag_value(YaridovichGate, YaridovichGating.OPEN):
            event_2496_startup += [SetBit(SEASIDE_BOSS_AVAILABLE)]
        if not self.settings.is_flag_value(LandsEndGate, LandsEndGating.OPEN):
            event_2496_startup += [SetBit(LANDS_END_GATED)]

            if self.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
                self.event_scripts.get_script_by_id(
                    E1169_OPEN_LANDS_END_IF_GATED_BY_ELDER
                ).insert_before_nth_command(0, ClearBit(LANDS_END_GATED))
            if self.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
                event_2496_startup += [SetBit(LANDS_END_GATED_BY_STAR_PIECES)]

        if self.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
            event_2496_startup += [SetBit(TEMPLE_BOSS_GATED)]
        if self.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
            event_2496_startup += [
                SummonObjectToSpecificLevel(
                    NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                )
            ]
        elif self.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
            event_2496_startup += [
                RemoveObjectFromSpecificLevel(
                    NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                ),
                SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                SetBit(MAP_MONSTRO_TOWN),
            ]
        if self.settings.is_flag_value(
            NimbusGate, NimbusGating.OPEN
        ) or self.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
            event_2496_startup += [
                SetBit(NIMBUS_MAINLAND_UNLOCKED),
                RemoveObjectFromSpecificLevel(
                    NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                ),
            ]
        if self.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
            event_2496_startup += [
                SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                SetBit(MAP_BARREL_VOLCANO),
            ]

        if not self.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
            event_2496_startup += [SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL)]
            if self.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
                event_2496_startup += [SetBit(KEEP_GATED_BY_STAR_PIECES)]
                if self.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                    event_2496_startup += [
                        SetBit(FACTORY_MATCHES_KEEP),
                    ]
        else:
            event_2496_startup += [
                SetBit(MAP_VISTA_HILL),
                ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
            ]
            if self.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                event_2496_startup += [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
        if self.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
            event_2496_startup += [SetBit(FACTORY_GATED_BY_STAR_PIECES)]

        event_2496_startup += [Return()]
        self.event_scripts.get_script_by_id(
            E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START
        ).set_contents(event_2496_startup)

        # threshold adjustments
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_1"),
        ).set_value(self.settings.get_flag(SuitePrize1Threshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_2"),
        ).set_value(self.settings.get_flag(SuitePrize2Threshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_3"),
        ).set_value(self.settings.get_flag(SuitePrize3Threshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_4"),
        ).set_value(self.settings.get_flag(SuitePrize4Threshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_5"),
        ).set_value(self.settings.get_flag(SuitePrize5Threshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("suite_threshold_6"),
        ).set_value(self.settings.get_flag(SuitePrize6Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("sj_threshold_1"),
        ).set_value(self.settings.get_flag(SuperJump1Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier("sj_threshold_2"),
        ).set_value(self.settings.get_flag(SuperJump2Threshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier(
                "tower_knife_guy_sidequest_completed"
            ),
        ).set_value(self.settings.get_flag(KnifeGuyPrizeThreshold).value)
        cast(
            CompareVarToConst,
            self.event_scripts.get_command_by_identifier(
                "casino_grate_guy_sidequest_completed"
            ),
        ).set_value(self.settings.get_flag(GrateGuyPrizeThreshold).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("check_doors_complete"),
        ).set_value(self.settings.get_flag(BowserDoorRequirements).value)

        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_1"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_2"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)
        cast(
            JmpIfVarEqualsConst,
            self.event_scripts.get_command_by_identifier("enable_boss_access_3"),
        ).set_value(self.settings.get_flag(StarPiecesRequired).value)

        if self.settings.isflag_enabled(FixKnifeGuy):
            cast(
                CompareVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "tower_knife_guy_fixed_sidequest_completed"
                )
            ).set_value(self.settings.get_flag(KnifeGuyFixedPrizeThreshold).value)

        # other stuff

        if self.settings.isflag_enabled(PoisonMushroom):
            self.items.get_by_type(MushroomItem2).set_status_immunities(
                [
                    random.choice(
                        [
                            Status.MUTE,
                            Status.SLEEP,
                            Status.POISON,
                            Status.FEAR,
                            Status.BERSERK,
                            Status.MUSHROOM,
                            Status.SCARECROW,
                            Status.INVINCIBLE,
                        ]
                    )
                ]
            )
        if self.settings.isflag_enabled(UncapSuperJumps):
            self.battle_animations[0x35].delete_command_by_name("super_jump_cap_1")
            self.battle_animations[0x35].delete_command_by_name("super_jump_cap_2")

        if self.settings.isflag_enabled(NoGenoWhirlExor):
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_1", [SetUntargetable(MONSTER_1_SET)]
            )
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_2", [SetUntargetable(MONSTER_1_SET)]
            )
            self.monster_scripts.replace_command_by_identifier(
                "exor_vulnerability_3", [SetUntargetable(MONSTER_1_SET)]
            )
        if self.settings.isflag_enabled(FixMagikoopa):
            self.monster_scripts.scripts[
                KINGBOMBEnemy._monster_id
            ].insert_after_nth_command(0, ClearVar(BV7EE000))
        sidekicks = [
            BODYGUARDEnemy,
            GOOMBETTEEnemy,
            FAUTSOEnemy,
            BAHAMUTTEnemy,
            BAHAMUTTEnemy2,
            KINGBOMBEnemy,
            JINXCLONEEnemy,
            MARIOCLONEEnemy,
            MARIOCLONESEnemy,
            MALLOWCLONEEnemy,
            MALLOWCOPYSEnemy,
            GENOCLONEEnemy,
            GENOCLONESEnemy,
            BOWSERCLONEEnemy,
            BOWSERCOPYSEnemy,
            TOADSTOOL2Enemy,
            TOADSTOOL3Enemy,
            TENTACLESEnemy,
            TENTACLESEnemy2,
            BOBOMBEnemyHenchman,
            MICROBOMBEnemy,
            MEZZOBOMBEnemy,
            STRONGBOBOMB1Enemy,
            STRONGBOBOMB2Enemy,
            STRONGBOBOMB3Enemy,
            STRONGBOBOMB4Enemy,
            SNIFITEnemyHenchman,
            SNIFIT2Enemy,
            BANDANABLUEEnemy,
            TORTE2Enemy,
            TORTEEnemy,
            SMILAXEnemy,
            EGGBERTEnemy,
            DINGALINGEnemy,
            FIRECRYS3DEnemy,
            FIRECRYSTALEnemy,
            WINDCRYS3DEnemy,
            WINDCRYS3DEnemy,
            WATERCRYS3DEnemy,
            WATERCRYSTALEnemy,
            EARTHCRYS3DEnemy,
            EARTHCRYSTALEnemy,
            MADMALLETEnemyHenchman,
            POUNDEREnemyHenchman,
            POUNDETTEEnemyHenchman,
            HELIOEnemy,
            SHYPEREnemy,
        ]
        bosses = [
            HAMMERBROEnemy,
            CROCO1Enemy,
            MACKEnemy,
            BELOME1Enemy,
            BOWYEREnemy,
            CROCO2Enemy,
            PUNCHINELLOEnemy,
            PUNCHINELLO2Enemy,
            BOOSTEREnemy,
            BOOSTEREnemy2,
            KNIFEGUYEnemy,
            GRATEGUYEnemy,
            BUNDTEnemy,
            BUNDT2Enemy,
            PANDORITEEnemy,
            HIDONEnemy,
            BOXBOYEnemy,
            CHESTEREnemy,
            KINGCALAMARIEnemy,
            JOHNNYEnemy,
            JOHNNYEnemy2,
            YARIDOVICHEnemy,
            YARIDOVICHMirageEnemy,
            BELOME2Enemy,
            BELOMEEnemy3,
            MOKURAEnemy,
            FORMLESSEnemy,
            JAGGEREnemy,
            JINX1Enemy,
            JINX2Enemy,
            JINX3Enemy,
            JINXEnemy4,
            CULEXEnemy,
            CULEX3DEnemy,
            MEGASMILAXEnemy,
            DODOEnemySolo,
            BIRDETTAEnemy,
            DODOEnemy,
            VALENTINAEnemy,
            CZARDRAGONEnemy,
            ZOMBONEEnemy,
            AXEMREDEnemy,
            AXEMPINKEnemy,
            AXEMBLACKEnemy,
            AXEMYELLOWEnemy,
            AXEMGREENEnemy,
            AXEMRANGERSEnemy,
            KAMEKEnemy,
            BOOMEREnemy,
            EXOREnemy,
            RIGHTEYEEnemy,
            LEFTEYEEnemy,
            NEOSQUIDEnemy,
            COUNTDOWNEnemy,
            CLOAKEREnemy,
            CLOAKEREnemy2,
            MADADDEREnemy,
            EARTHLINKEnemy,
            CLERKEnemy,
            MANAGEREnemy,
            DIRECTOREnemy,
            GUNYOLKEnemy,
            FACTORYCHIEFEnemy,
            SMITHY1Enemy,
            SMITHY2Enemy,
            SMITHYBodyEnemy,
            SMITHYChestEnemy,
            SMITHYMageEnemy,
            SMITHYSafeEnemy2,
            SMITHYTankEnemy,
            SMELTEREnemy,
        ]
        if self.settings.isflag_enabled(NoOHKO):
            for ennemytype in sidekicks:
                enemy = self.enemies.get_by_type(ennemytype)
                enemy.set_ohko_immune(True)
                enemy.set_morph_chance(0)
                for cmd in self.monster_scripts.scripts[enemy.monster_id].contents:
                    if isinstance(cmd, IfTargetedByItem):
                        cmd.set_commands([CarboCookieItem])
        if self.settings.isflag_enabled(ExperienceNoBosses):
            for ennemytype in bosses + sidekicks:
                enemy = self.enemies.get_by_type(ennemytype)
                enemy.set_xp(0)
        if self.settings.isflag_enabled(ExperienceNoRegular):
            for ennemytype in [
                type(e)
                for e in self.enemies.enemies
                if type(e) not in bosses + sidekicks
            ]:
                self.enemies.get_by_type(ennemytype).set_xp(0)
        if self.settings.isflag_enabled(EnemySpells):
            spell_pool: list[type[EnemySpell]] = [
                DrainSpell,
                LightningOrbSpell,
                FlameSpell,
                BoltSpell,
                CrystalSpell,
                FlameStoneSpell,
                MegaDrainSpell,
                WillyWispSpell,
                DiamondSawSpell,
                ElectroshockSpell,
                BlastSpell,
                StormSpell,
                IceRockSpell,
                EscapeSpell,
                DarkStarSpell,
                RecoverSpell,
                MegaRecoverSpell,
                FlameWallSpell,
                StaticESpell,
                SandStormSpell,
                BlizzardSpell,
                DrainBeamSpell,
                MeteorBlastSpell,
                LightBeamSpell,
                WaterBlastSpell,
                SolidifySpell,
                PetalBlastSpell,
                AuroraFlashSpell,
                BoulderSpell,
                CoronaSpell,
                MeteorSwarmSpell,
                WeirdMushroomSpell,
                BreakerBeamSpell,
                ShredderSpell,
                SledgeSpell,
                SwordRainSpell,
                SpearRainSpell,
                ArrowRainSpell,
                BigBangSpell,
            ]
            for script in self.monster_scripts.scripts:
                for cmd in script.contents:
                    if isinstance(cmd, CastSpell):
                        if cmd.spell_1 is not None and not isinstance(
                            cmd.spell_1, DoNothing
                        ):
                            cmd.set_spell_1(random.choice(spell_pool))
                        if cmd.spell_2 is not None and not isinstance(
                            cmd.spell_2, DoNothing
                        ):
                            cmd.set_spell_2(random.choice(spell_pool))
                        if cmd.spell_3 is not None and not isinstance(
                            cmd.spell_3, DoNothing
                        ):
                            cmd.set_spell_3(random.choice(spell_pool))

        # equips and things

        if self.settings.isflag_enabled(InfuseSpellElements):
            self.get_spell(GenoBeamSpell).set_element(Element.ICE)
            self.get_spell(GenoFlashSpell).set_element(Element.FIRE)
            self.get_spell(PsychBombSpell).set_element(Element.FIRE)
            self.get_spell(CrusherSpell).set_element(Element.JUMP)
            self.get_spell(BowserCrushSpell).set_element(Element.JUMP)
        if self.settings.isflag_enabled(CharacterSpellElements):
            spells_to_update = [
                s for s in self.spells.spells if s.element != Element.NONE
            ]
            for spell in spells_to_update:
                spell.set_element(
                    random.choice(
                        [Element.ICE, Element.FIRE, Element.JUMP, Element.THUNDER]
                    )
                )

        if self.settings.is_flag_value(
            EquipmentProperties, EquipmentPropertiesOptions.SOME
        ):
            self.items.get_by_type(ShirtItem).append_status_immunity(Status.MUSHROOM)
            self.items.get_by_type(PantsItem).append_status_immunity(Status.MUSHROOM)
            self.items.get_by_type(ThickShirtItem).append_temp_buff(
                TempStatBuff.DEFENSE
            )
            self.items.get_by_type(ThickPantsItem).append_temp_buff(
                TempStatBuff.DEFENSE
            )
            self.items.get_by_type(MegaShirtItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(MegaPantsItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(MegaCapeItem).append_temp_buff(
                TempStatBuff.MAGIC_DEFENSE
            )
            self.items.get_by_type(HappyShirtItem).set_prevent_ko(True)
            self.items.get_by_type(HappyPantsItem).set_prevent_ko(True)
            self.items.get_by_type(HappyCapeItem).set_prevent_ko(True)
            self.items.get_by_type(HappyShellItem).set_prevent_ko(True)
            self.items.get_by_type(PolkaDressItem).set_prevent_ko(True)
            self.items.get_by_type(CourageShellItem).append_status_immunity(Status.FEAR)
            self.items.get_by_type(SailorShirtItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(SailorPantsItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(SailorCapeItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(NauticaDressItem).append_elemental_immunity(
                Element.ICE
            )
            self.items.get_by_type(FuzzyShirtItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyPantsItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyCapeItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FuzzyDressItem).append_elemental_immunity(
                Element.THUNDER
            )
            self.items.get_by_type(FireShirtItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FirePantsItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FireCapeItem).append_elemental_immunity(Element.FIRE)
            self.items.get_by_type(FireShellItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(FireDressItem).append_elemental_immunity(
                Element.FIRE
            )
            self.items.get_by_type(HeroShirtItem).append_status_immunity(
                Status.SCARECROW
            )
            self.items.get_by_type(PrincePantsItem).append_status_immunity(Status.MUTE)
            self.items.get_by_type(RoyalDressItem).append_status_immunity(Status.SLEEP)
            self.items.get_by_type(HealShellItem).append_status_immunity(Status.POISON)
            self.items.get_by_type(StarCapeItem).append_status_immunity(Status.BERSERK)
            self.items.get_by_type(FroggieStickItem).set_magic_attack(
                self.items.get_by_type(FroggieStickItem).attack
            )
            self.items.get_by_type(FroggieStickItem).set_attack(0)
            self.items.get_by_type(RibbitStickItem).set_magic_attack(
                self.items.get_by_type(RibbitStickItem).attack
            )
            self.items.get_by_type(RibbitStickItem).set_attack(0)
            self.items.get_by_type(ParasolItem).set_magic_attack(
                self.items.get_by_type(ParasolItem).attack
            )
            self.items.get_by_type(ParasolItem).set_attack(0)
        elif self.settings.is_flag_value(
            EquipmentProperties, EquipmentPropertiesOptions.RANDOM
        ):
            self._randomize_equipment_properties()

        # Handle EquipmentCharacters options
        equip_chars_setting = self.settings.get_flag(EquipmentCharacters).selected
        if equip_chars_setting != EquipmentCharactersOptions.VANILLA:
            self._randomize_equipment_characters(equip_chars_setting)

        # SHUFFLE CHECKS HERE
        # TODO: exclude frog disciple if shuffle shops turned off
        # TODO: exclude character spells if that setting is turned off
        # TODO: exclude remake items if not enabled. don't have sage stick in the pool
        # TODO: distinguish between "location does not exist" (remake, unused invisibles) and "location exists but is not shuffled" and "location exists and is shuffled but cannot be important"
        # TODO: A disabled boss fight check location = shuffled, but can't have a boss hunt. No guarantees that more progression won't be behind it, i.e. boss item drops. Disable those checks yourself.
        # TODO: A disabled boss FIGHT = appears in their original check spot, forcibly.
        # TODO: A disabled star piece location = obvious
        # TODO: Don't let people be morons and try to exclude megasmilax while also choosing megasmilax as a gate
        # TODO: Regular checks disabled = still shuffle them, just no KIs or SPs. Good non-progress items are fair game, git gud.
        # TODO: KIs anywhere vs not
        # TODO: SPs anywhere vs not
        # TODO: EXP stars anywhere (disabled: chests are NOT shuffled, no exp stars in pool)
        # TODO: Slots anywhere ("" "" "")
        # TODO: Mimics anywhere ("" "" "")
        # TODO: Beetlemania ("" "" "")
        # TODO: Magikoopa chest ("" "" "")
        # TODO: Monstro shuffle
        # TODO: Fireworks settings. Change default item of fireworks guy if you didn't do that already
        # TODO: No Star Egg setting
        # TODO: Annoying/empty chests
        # TODO: Replace bad items with coins
        # TODO: Available spells
        # TODO: Bias item shuffle (still want to keep?)
        # TODO: Option to not even shuffle items at all, or star pieces, or boss fights
        # TODO Stat scaling for boss shuffle
        # TODO: Henchmen vs no henchmen, hill/statue or not
        # TODO: NPCs, dialogs for bosses and henchmen
        # TODO: Don't forget to apply spells and starting levels to recruited allies
        # TODO: starting party, overworld characters, sprite injections. Needs a Random option for starting char
        # TODO NPCs and packets for all item types. Gold paint can be royal syrup
        # TODO: Apply hint text to blue toad in moleville
        # TODO: Do search-and-replace for all pronouns, names, etc related to main characters, positioned bosses, etc
        # TODO: Room service menu
        # TODO: Open issue templat for submitting star hill text. note: uncredited
        # TODO: Open issue template for submitting quiz questions (uncredited)
        # TODO: update spell names and palettes and sounds depending on element

        # Shop shuffling happens after equipment randomization so we can score equipment
        if self.settings.isflag_enabled(ShuffleShops):
            self._shuffle_shops()

        if not self.settings.isflag_enabled(IgnoreNamesakeProperties):
            self.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.SLEEP)
            self.items.get_by_type(WakeUpPinItem).append_status_immunity(Status.MUTE)
            self.items.get_by_type(AntidotePinItem).append_status_immunity(
                Status.POISON
            )
            self.items.get_by_type(TrueformPinItem).append_status_immunity(
                Status.MUSHROOM
            )
            self.items.get_by_type(TrueformPinItem).append_status_immunity(
                Status.SCARECROW
            )
            self.items.get_by_type(FearlessPinItem).append_status_immunity(Status.FEAR)
            has_ko_protection = [
                i for i in self.items.items if isinstance(i, Equipment) and i.prevent_ko
            ]
            if len(has_ko_protection) < 4:
                more_ko_protections = random.sample(
                    [
                        i
                        for i in self.items.items
                        if isinstance(i, Equipment) and not i.prevent_ko
                    ],
                    4 - len(has_ko_protection),
                )
                for i in more_ko_protections:
                    i.set_prevent_ko(True)

        if self.settings.isflag_enabled(EnemyAttacks):
            self._randomize_enemy_attacks_and_spells()

        if (
            self.settings.get_flag(EnemyStats).selected
            != EnemyStatsShuffleOptions.DISABLED
        ):
            self._randomize_enemy_stats()

        # Define consumable groups for enemy drops
        consumables_group_1 = [
            MushroomItem,
            HoneySyrupItem,
            PickMeUpItem,
            AbleJuiceItem,
            BracerItem,
            EnergizerItem,
            YoshiCookieItem,
            PureWaterItem,
            SleepyBombItem,
            BadMushroomItem,
            FlowerTabItem,
            FroggieDrinkItem,
            MukuCookieItem,
            FreshenUpItem,
            FrightBombItem,
            WiltShroomItem,
            RottenMushItem,
            MoldyMushItem,
            MushroomItem2,
        ]

        consumables_group_2 = [
            MidMushroomItem,
            MaxMushroomItem,
            MapleSyrupItem,
            RoyalSyrupItem,
            YoshiAdeItem,
            RedEssenceItem,
            KerokeroColaItem,
            FireBombItem,
            IceBombItem,
            FlowerJarItem,
            FlowerBoxItem,
            YoshiCandyItem,
            ElixirItem,
            MegalixirItem,
            RockCandyItem,
            CrystallineItem,
            PowerBlastItem,
        ]

        if self.settings.isflag_enabled(EnemyDrops):
            self._randomize_enemy_drops(consumables_group_1, consumables_group_2)

        if self.settings.isflag_enabled(EnemyFormations):
            self._randomize_enemy_formations()

        # Randomize character stats
        if self.settings.isflag_enabled(CharacterStats):
            self._randomize_character_stats()

        # Randomize character spell stats
        if self.settings.isflag_enabled(CharacterSpellStats):
            self._randomize_character_spell_stats()

        # Apply EXP multiplier
        self._apply_exp_multiplier()

        # Minigames

        if self.settings.isflag_enabled(QuizShuffle):
            questions = get_quiz_questions()
            for text, d_id in zip(
                questions, option_1_correct + option_2_correct + option_3_correct
            ):
                self.overworld_dialogs.replace_dialog(d_id, text.get_string(d_id))

        if self.settings.isflag_enabled(BallSolitaireShuffle):
            ball_solitaire = BallSolitaireGame()
            randomize_ball_solitaire(ball_solitaire)
            cast(
                SetVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "ball_solitaire_puzzle_value"
                ),
            ).set_value_and_address(value=ball_solitaire.get_puzzle_value())

        if self.settings.isflag_enabled(MagicButtonShuffle):
            magic_buttons = MagicButtonsGame()
            randomize_magic_buttons(magic_buttons)
            cast(
                SetVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "magic_buttons_puzzle_value"
                ),
            ).set_value_and_address(value=magic_buttons.get_puzzle_value())

        if not self.settings.isflag_enabled(SkipMinecart):
            self.event_scripts.delete_command_by_identifier(
                "skip_moleville_minecart_sequence"
            )

        if self.settings.isflag_enabled(RandomTadpolePondSong):
            self._randomize_tadpole_pond()

        if self.settings.isflag_enabled(RandomSunkenShipPassword):
            self._randomize_password()

        if self.settings.isflag_enabled(BowserDoorShuffle):
            randomize_bowser_doors(self)

        if self.settings.isflag_enabled(BetterTips):
            cast(
                SetVarToRandom,
                self.event_scripts.get_command_by_identifier("mushroom_boy_odds")
            ).set_value(5000)
            self.event_scripts.get_script_by_id(
                E0021_FOREST_MAZE_MUSHROOM_GRANT
            ).set_contents(
                [
                    JmpToEvent(E0023_MUSHROOM_SELECTION)
                ]
            )
            self.event_scripts.get_script_by_id(
                E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1
            ).set_contents(
                [
                    JmpToEvent(E0022_BETTER_TIP_GRANTER)
                ]
            )
            self.event_scripts.get_script_by_id(
                E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER
            ).set_contents(
                [
                    JmpToEvent(E0022_BETTER_TIP_GRANTER)
                ]
            )
            self.event_scripts.get_script_by_id(
                E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE
            ).set_contents(
                [
                    JmpToEvent(E0022_BETTER_TIP_GRANTER)
                ]
            )

        # TODO differentiate bosses. not a cosmetic, reveals info
        # Need to find unused palettes for remake bosses
        # move chocoalte cake to postgame bundt
        # blue shirt booster (not purple-y)
        # blue hat punchinello (not purple-y)
        # invert johnny blue and red
        # make culex purple lighter
        # blue hair jinx
        # silver belome

        self._rebuild_hash()

        # Cosmetics have to go at the end and be re-seeded
        random.seed(datetime.datetime.now().timestamp())

        if self.settings.isflag_enabled(CanonNames):
            self.enemies.get_by_type(KAMEKEnemy).set_name("KAMEK")
            self.enemies.get_by_type(BIRDETTAEnemy).set_name("BIRDETTA")
        else:
            self.search_replace_dialog("KAMEK", "MAGIKOOPA")
            self.search_replace_dialog("Kamek", "Magikoopa")
            self.search_replace_dialog("BIRDETTA", "BIRDO")
            self.search_replace_dialog("Birdetta", "Birdo")
        # todo: canon names should override remake
        # todo: search and replace in dialogs for all remake names
        if self.settings.isflag_enabled(Peach):
            self.allies._allies[1].name = "Peach"
        if self.settings.isflag_enabled(RemakeNames):
            for enemy in self.enemies.enemies:
                e = cast(Enemy, enemy)
                if e.remake_name is not None:
                    enemy.set_name(e.remake_name)
            for item in self.items.items:
                it = cast(Item, item)
                if it.remake_name is not None:
                    item.set_name(it.remake_name)
            for spell in self.spells.spells:
                sp = cast(Spell, spell)
                if sp.remake_name is not None:
                    spell._title = sp.remake_name
            for attack in self.enemy_attacks.attacks:
                at = cast(EnemyAttack, attack)
                if at.remake_name is not None:
                    attack.set_attack_name(at.remake_name)
        if self.settings.isflag_enabled(RemoveFlashes):
            screenflashes = [
                "screen_flash_1",  # thunderbolt
                "screen_flash_2",
                "crusher_screenflash",  # crusher
                "darkstar_flash",  # dark star
                "spikedlink_flash_1",
                "spikedlink_flash_2",
                "spikedlink_flash_3",
            ]
            for identifier in screenflashes:
                self.battle_animations[0x35].get_command_by_name(identifier).set_colour(  # type: ignore
                    NO_COLOUR
                )
            deletes = [
                "command_0x35BE52",  # geno flash
                "geno_blast_effect",  # geno blast
                "corona_flash",
                "shaker_delete_1",  # shaker / silver bullet
                "shaker_delete_2",
                "shaker_delete_3",
                "shaker_delete_4",
                "shaker_delete_5",
                "statice_delete_1",
                "statice_delete_2",
                "statice_delete_3",
                "statice_delete_4",
                "statice_delete_5",
                "meteorswarm_delete_maybe",
                "rockcandy_delete",
                "rockcandy_delete_2",
            ]
            for identifier in deletes:
                self.battle_animations[0x35].delete_command_by_name(identifier)
            deletes_3A = ["smithy_delete_1", "smithy_delete_2"]
            for identifier in deletes_3A:
                self.battle_animations[0x3A].delete_command_by_name(identifier)
            self.battle_animations[0x35].get_command_by_name(
                "bigbang_flash"
            ).set_effect(  # type: ignore
                EF0025_PSYCH_BOMB_BG
            )
            self.battle_animations[0x35].get_command_by_name(
                "firebomb_explosion"
            ).set_effect(  # type: ignore
                EF0025_PSYCH_BOMB_BG
            )
            self.battle_animations[0x35].replace_command_by_name(
                "icebomb_explosion", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
            self.battle_animations[0x35].replace_command_by_name(
                "command_0x35358A",
                AttackTimerBegins(
                    identifier="command_0x35358A"
                ),  # shaker / silver bullet
            )
            self.battle_animations[0x35].replace_command_by_name(
                "statice_flash", ScreenFlashWithDuration(NO_COLOUR, 44)  # static e!
            )
            self.battle_animations[0x35].replace_command_by_name(
                "meteorswarm_replace",
                ScreenFlashWithDuration(NO_COLOUR, 16),  # meteor swarm
            )
            self.battle_animations[0x35].replace_command_by_name(
                "rockcandy_replace",
                ScreenFlashWithDuration(NO_COLOUR, 20),  # rock candy
            )
            self.battle_animations[0x35].replace_command_by_name(
                "meteorblast_replace",
                ScreenFlashWithDuration(NO_COLOUR, 20),  # meteor blast
            )

            self.battle_animations[0x3A].replace_command_by_name(
                "smithy_replace_1", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
            self.battle_animations[0x3A].replace_command_by_name(
                "smithy_replace_2", ScreenFlashWithDuration(NO_COLOUR, 1)
            )
        if self.settings.isflag_enabled(PaletteSwaps):
            self.mario_palette = random.choice(MARIO_PALETTES)
            self.mallow_palette = random.choice(MALLOW_PALETTES)
            self.geno_palette = random.choice(GENO_PALETTES)
            self.bowser_palette = random.choice(BOWSER_PALETTES)
            self.toadstool_palette = random.choice(TOADSTOOL_PALETTES)

            if self.settings.isflag_enabled(ChangeNames):
                self.allies._allies[0].name = self.mario_palette.name
                self.enemies.get_by_type(MARIOCLONEEnemy).set_name(
                    self.mario_palette.clone_name
                )
                self.enemies.get_by_type(MARIOCLONESEnemy).set_name(
                    self.mario_palette.strong_clone_name
                )
                self.allies._allies[1].name = self.toadstool_palette.name
                self.enemies.get_by_type(TOADSTOOL2Enemy).set_name(
                    self.toadstool_palette.clone_name
                )
                self.enemies.get_by_type(TOADSTOOL3Enemy).set_name(
                    self.toadstool_palette.strong_clone_name
                )
                self.allies._allies[2].name = self.bowser_palette.name
                self.enemies.get_by_type(BOWSERCLONEEnemy).set_name(
                    self.bowser_palette.clone_name
                )
                self.enemies.get_by_type(BOWSERCOPYSEnemy).set_name(
                    self.bowser_palette.strong_clone_name
                )
                self.allies._allies[3].name = self.geno_palette.name
                self.enemies.get_by_type(GENOCLONEEnemy).set_name(
                    self.geno_palette.clone_name
                )
                self.enemies.get_by_type(GENOCLONESEnemy).set_name(
                    self.geno_palette.strong_clone_name
                )
                self.allies._allies[4].name = self.mallow_palette.name
                self.enemies.get_by_type(MALLOWCLONEEnemy).set_name(
                    self.mallow_palette.clone_name
                )
                self.enemies.get_by_type(MALLOWCOPYSEnemy).set_name(
                    self.mallow_palette.strong_clone_name
                )
        # Initialize selected music IDs (will be populated if BossShuffleMusic is enabled)
        self.selected_music_ids: list[int] = []

        if self.settings.isflag_enabled(BossShuffleMusic):
            from smrpgpatchbuilder.datatypes.battles.enums import BattleMusic

            # Get the enabled music tracks from user selection
            enabled_tracks = self.settings.get_flag(ShuffledMusic).enabled

            # Pick 8 random music IDs from the enabled tracks (with replacement if needed)
            if len(enabled_tracks) >= 8:
                selected_tracks = random.sample(enabled_tracks, 8)
            else:
                # If fewer than 8 tracks selected, sample with replacement
                selected_tracks = random.choices(enabled_tracks, k=8)

            # Store the music IDs for patching in get_patch
            self.selected_music_ids = [track.music_id for track in selected_tracks]

            # The 8 battle music classes (pointers to the IDs we'll write at 0x029F51)
            music_classes = list(BattleMusic)

            for boss_fight in [
                l for l in self.locations if isinstance(l, BossFightLocation)
            ]:
                pack_id = cast(BossFightLocation, boss_fight).pack_id
                # Assign a random battle music class (0-7) to each boss fight
                battle_music = random.choice(music_classes)
                pack = self.get_battle_pack(pack_id)
                for f in pack.formations:
                    f.set_music(battle_music)

        # Assign random Star Hill wishes. This doesn't need to be tied to the seed, so it's truly random!
        wishes = zip(WISH_DIALOG_IDS, random.sample(WISH_POOL, len(WISH_DIALOG_IDS)))
        for dialog_id, wish in wishes:
            self.overworld_dialogs.replace_dialog(dialog_id, wish)

        # set random back to normal
        random.seed(self.seed)

    def _mutate_normal(self, value: int, minimum: int = 0, maximum: int = 255) -> int:
        """Mutate a value simulating a normal distribution.

        Roughly simulates a normal distribution with mean <value>,
        std deviation approximately 1/5 of value.
        """
        value = int(max(minimum, min(value, maximum)))
        if value == 0:
            return value

        # Use gaussian distribution centered on value with std dev = value / 5
        std_dev = max(1, value / 5)
        new_value = int(random.gauss(value, std_dev))
        # Ensure result is always within bounds and is an integer
        return int(max(minimum, min(new_value, maximum)))

    def _set_all_locations(self):
        # establish all functional prize locations
        # regardless if they will have their contents shuffled or not

        self.locations = {
            StartingItem1Location: StartingItem1Location(),
            StartingItem2Location: StartingItem2Location(),
            StartingItem3Location: StartingItem3Location(),
            StartingItem4Location: StartingItem4Location(),
            StartingCharacter1: StartingCharacter1(),
            MushroomWay1LowerChest: MushroomWay1LowerChest(),
            MushroomWay1UpperChest: MushroomWay1UpperChest(),
            MushroomWay1ToadRescue: MushroomWay1ToadRescue(),
            MushroomWay2LedgeChest: MushroomWay2LedgeChest(),
            MushroomWay2ToadRescue: MushroomWay2ToadRescue(),
            MushroomWayRightGoomba: MushroomWayRightGoomba(),
            MushrooomWayBossFight: MushrooomWayBossFight(),
            MushroomWayStarPiece: MushroomWayStarPiece(),
            MushroomWayBossFightRewardItem: MushroomWayBossFightRewardItem(),
            MushroomWayCharacter: MushroomWayCharacter(),
            MushroomKingdomMainHall: MushroomKingdomMainHall(),
            MushroomKingdomLiberatedVaultLeft: MushroomKingdomLiberatedVaultLeft(),
            MushroomKingdomLiberatedVaultRight: MushroomKingdomLiberatedVaultRight(),
            MushroomKingdomLiberatedVaultMiddle: MushroomKingdomLiberatedVaultMiddle(),
            MushroomKingdomChair: MushroomKingdomChair(),
            MushroomKingdomFreeShopItem: MushroomKingdomFreeShopItem(),
            MushroomKingdomShopBasementLeft: MushroomKingdomShopBasementLeft(),
            MushroomKingdomShopBasementRight: MushroomKingdomShopBasementRight(),
            MushroomKingdomWalletGuyFirstRewardLocation: MushroomKingdomWalletGuyFirstRewardLocation(),
            MushroomKingdomWalletGuySecondRewardLocation: MushroomKingdomWalletGuySecondRewardLocation(),
            MushroomKingdomOccupiedOutdoorGuardLocation: MushroomKingdomOccupiedOutdoorGuardLocation(),
            MushroomKingdomOccupiedCastleToadRescueLocation: MushroomKingdomOccupiedCastleToadRescueLocation(),
            MushroomKingdomOccupiedFamilyRescueLocation: MushroomKingdomOccupiedFamilyRescueLocation(),
            MushroomKingdomOccupiedGuestRoomLocation: MushroomKingdomOccupiedGuestRoomLocation(),
            MushroomKingdomBossFight: MushroomKingdomBossFight(),
            MushroomKingdomStarPiece: MushroomKingdomStarPiece(),
            MushroomKingdomStoreExchangeLocation: MushroomKingdomStoreExchangeLocation(),
            MushroomKingdomInnPurchaseLocation: MushroomKingdomInnPurchaseLocation(),
            BanditsWayFlowerJumpLocation: BanditsWayFlowerJumpLocation(),
            BanditsWayCoin1Location: BanditsWayCoin1Location(),
            BanditsWayCoin2Location: BanditsWayCoin2Location(),
            BanditsWayCoin3Location: BanditsWayCoin3Location(),
            BanditsWayDogChestLocation: BanditsWayDogChestLocation(),
            BanditsWayPlatformsLeftChestLocation: BanditsWayPlatformsLeftChestLocation(),
            BanditsWayPlatformsRightChestLocation: BanditsWayPlatformsRightChestLocation(),
            BanditsWayDeadEndChestLocation: BanditsWayDeadEndChestLocation(),
            BanditsWayBossFight: BanditsWayBossFight(),
            BanditsWayStarPiece: BanditsWayStarPiece(),
            BanditsWayBossFirstItemDropLocation: BanditsWayBossFirstItemDropLocation(),
            BanditsWayBossSecondItemDropLocation: BanditsWayBossSecondItemDropLocation(),
            KeroSewersStairRoomLeftChestLocation: KeroSewersStairRoomLeftChestLocation(),
            KeroSewersStairRoomRightChestLocation: KeroSewersStairRoomRightChestLocation(),
            Mimic1BossFight: Mimic1BossFight(),
            Mimic1DropRewardLocation: Mimic1DropRewardLocation(),
            Mimic1StarPiece: Mimic1StarPiece(),
            Mimic1ReloadRewardLocation: Mimic1ReloadRewardLocation(),
            KeroSewersFourRatRoomChestLocation: KeroSewersFourRatRoomChestLocation(),
            KeroSewersBeforeBelomeLowerLocation: KeroSewersBeforeBelomeLowerLocation(),
            KeroSewersBeforeBelomeUpperBeforeFlipLocation: KeroSewersBeforeBelomeUpperBeforeFlipLocation(),
            KeroSewersBeforeBelomeUpperAfterFlipLocation: KeroSewersBeforeBelomeUpperAfterFlipLocation(),
            KeroSewersBossFight: KeroSewersBossFight(),
            KeroSewersStarPiece: KeroSewersStarPiece(),
            MidasRiverFirstCompletionRewardLocation: MidasRiverFirstCompletionRewardLocation(),
            MidasRiverBottomLeftCaveLocation: MidasRiverBottomLeftCaveLocation(),
            MidasRiverBottomRightCaveLocation: MidasRiverBottomRightCaveLocation(),
            TadpolePondCricketPieExchangeLocation: TadpolePondCricketPieExchangeLocation(),
            TadpolePondCricketJamExchangeLocation: TadpolePondCricketJamExchangeLocation(),
            MelodyBayFirstRewardLocation: MelodyBayFirstRewardLocation(),
            MelodyBaySecondRewardLocation: MelodyBaySecondRewardLocation(),
            MelodyBayThirdRewardLocation: MelodyBayThirdRewardLocation(),
            RoseWaySwingingPlatformRoomLocation: RoseWaySwingingPlatformRoomLocation(),
            RoseWayLeftIslandLocation: RoseWayLeftIslandLocation(),
            RoseWayMiddleIslandLocation: RoseWayMiddleIslandLocation(),
            RoseWayCoin1Location: RoseWayCoin1Location(),
            RoseWayCoin2Location: RoseWayCoin2Location(),
            RoseWayCoin3Location: RoseWayCoin3Location(),
            RoseWayCoin4Location: RoseWayCoin4Location(),
            RoseWayCoin5Location: RoseWayCoin5Location(),
            RoseWayFiveChestRoomTopLocation: RoseWayFiveChestRoomTopLocation(),
            RoseWayFiveChestRoomBottomLeftLocation: RoseWayFiveChestRoomBottomLeftLocation(),
            RoseWayFiveChestRoomRightLocation: RoseWayFiveChestRoomRightLocation(),
            RoseWayFiveChestRoomLeftLocation: RoseWayFiveChestRoomLeftLocation(),
            RoseWayFiveChestRoomBottomRightLocation: RoseWayFiveChestRoomBottomRightLocation(),
            RoseTownShopLeftChestLocation: RoseTownShopLeftChestLocation(),
            RoseTownShopRightChestLocation: RoseTownShopRightChestLocation(),
            RoseTownCloudRightChestLocation: RoseTownCloudRightChestLocation(),
            RoseTownCloudLeftChestLocation: RoseTownCloudLeftChestLocation(),
            RoseTownInnToadPrizeLocation: RoseTownInnToadPrizeLocation(),
            RoseTownInnGazPrizeLocation: RoseTownInnGazPrizeLocation(),
            RoseTownTreasureHouseLeftChestLocation: RoseTownTreasureHouseLeftChestLocation(),
            RoseTownTreasureHouseRightChestLocation: RoseTownTreasureHouseRightChestLocation(),
            RoseTownTreasureHouseMazeRewardLocation: RoseTownTreasureHouseMazeRewardLocation(),
            RoseTownTreasureHouseUpperChestLocation: RoseTownTreasureHouseUpperChestLocation(),
            ForestMazeFirstRoomLocation: ForestMazeFirstRoomLocation(),
            ForestMazeFirstUndergroundExitLocation: ForestMazeFirstUndergroundExitLocation(),
            ForestMazeUndergroundWigglerChestLocation: ForestMazeUndergroundWigglerChestLocation(),
            ForestMazeUndergroundBottomRightTrunkChestLocation: ForestMazeUndergroundBottomRightTrunkChestLocation(),
            ForestMazeUndergroundMiddleLeftChestLocation: ForestMazeUndergroundMiddleLeftChestLocation(),
            ForestMazeInnerMazeEntranceLocation: ForestMazeInnerMazeEntranceLocation(),
            ForestMazeSecretTopRightChestLocation: ForestMazeSecretTopRightChestLocation(),
            ForestMazeSecretBottomRightChestLocation: ForestMazeSecretBottomRightChestLocation(),
            ForestMazeSecretTopMiddleChestLocation: ForestMazeSecretTopMiddleChestLocation(),
            ForestMazeSecretBottomMiddleChestLocation: ForestMazeSecretBottomMiddleChestLocation(),
            ForestMazeSecretLeftChestLocation: ForestMazeSecretLeftChestLocation(),
            ForestMazeBossFight: ForestMazeBossFight(),
            ForestMazeStarPiece: ForestMazeStarPiece(),
            ForestMazeCharacter: ForestMazeCharacter(),
            PipeVaultSlidingCoinRoomBackChestLocation: PipeVaultSlidingCoinRoomBackChestLocation(),
            PipeVaultSlidingCoinRoomMiddleChestLocation: PipeVaultSlidingCoinRoomMiddleChestLocation(),
            PipeVaultSlidingCoinRoomFrontChestLocation: PipeVaultSlidingCoinRoomFrontChestLocation(),
            PipeVaultSlidingCoinRoomCoin1Location: PipeVaultSlidingCoinRoomCoin1Location(),
            PipeVaultSlidingCoinRoomCoin2Location: PipeVaultSlidingCoinRoomCoin2Location(),
            PipeVaultSlidingCoinRoomCoin3Location: PipeVaultSlidingCoinRoomCoin3Location(),
            PipeVaultSlidingCoinRoomCoin4Location: PipeVaultSlidingCoinRoomCoin4Location(),
            PipeVaultSlidingCoinRoomCoin5Location: PipeVaultSlidingCoinRoomCoin5Location(),
            PipeVaultSlidingCoinRoomCrouchItemLocation: PipeVaultSlidingCoinRoomCrouchItemLocation(),
            PipeVaultGoombaThumpinFirstPrizeLocation: PipeVaultGoombaThumpinFirstPrizeLocation(),
            PipeVaultGoombaThumpinSecondPrizeLocation: PipeVaultGoombaThumpinSecondPrizeLocation(),
            PipeVaultRisingPlatformChestLocation: PipeVaultRisingPlatformChestLocation(),
            PipeVaultChompweedChestLocation: PipeVaultChompweedChestLocation(),
            YosterEntranceChestLocation: YosterEntranceChestLocation(),
            YosterRacePrize1Location: YosterRacePrize1Location(),
            YosterRacePrize2Location: YosterRacePrize2Location(),
            YosterRacePrize3Location: YosterRacePrize3Location(),
            BucketGirlRewardLocation: BucketGirlRewardLocation(),
            TreasureShopItem1: TreasureShopItem1(),
            TreasureShopItem2: TreasureShopItem2(),
            TreasureShopItem3: TreasureShopItem3(),
            OuterMinesTrampolineHenchmanLocation: OuterMinesTrampolineHenchmanLocation(),
            OuterMinesLeftHenchmanLocation: OuterMinesLeftHenchmanLocation(),
            OuterMinesRightHenchmanLocation: OuterMinesRightHenchmanLocation(),
            OuterMinesBossPrizeLocation: OuterMinesBossPrizeLocation(),
            OuterMinesBossFight: OuterMinesBossFight(),
            OuterMinesStarPiece: OuterMinesStarPiece(),
            InnerMinesTracksChestLocation: InnerMinesTracksChestLocation(),
            InnerMinesShyguyCartLocation: InnerMinesShyguyCartLocation(),
            InnerMinesBoxesChestLocation: InnerMinesBoxesChestLocation(),
            InnerMinesSaveBlockChestLocation: InnerMinesSaveBlockChestLocation(),
            InnerMinesHighUpChestLocation: InnerMinesHighUpChestLocation(),
            InnerMinesBossFight: InnerMinesBossFight(),
            InnerMinesStarPiece: InnerMinesStarPiece(),
            InnerMinesCharacter: InnerMinesCharacter(),
            BoosterPassBushLocation: BoosterPassBushLocation(),
            BoosterPassFirstRoomLeftChestLocation: BoosterPassFirstRoomLeftChestLocation(),
            BoosterPassFirstRoomRightChestLocation: BoosterPassFirstRoomRightChestLocation(),
            BoosterPassSecondRoomFlowerLocation: BoosterPassSecondRoomFlowerLocation(),
            BoosterPassSecretMiddleChestLocation: BoosterPassSecretMiddleChestLocation(),
            BoosterPassSecretRightChestLocation: BoosterPassSecretRightChestLocation(),
            BoosterPassSecretLeftChestLocation: BoosterPassSecretLeftChestLocation(),
            BoosterTowerSpookumStairsLocation: BoosterTowerSpookumStairsLocation(),
            BoosterTowerTrainRoomCreviceLocation: BoosterTowerTrainRoomCreviceLocation(),
            BoosterTowerChestNearThwompLocation: BoosterTowerChestNearThwompLocation(),
            BoosterTowerFallingChestLocation: BoosterTowerFallingChestLocation(),
            BoosterTowerKnifeGuyPrizeLocation: BoosterTowerKnifeGuyPrizeLocation(),
            BoosterTowerPortraitPrizeLocation: BoosterTowerPortraitPrizeLocation(),
            BoosterTowerElderKeyItemLocation: BoosterTowerElderKeyItemLocation(),
            BoosterTowerParachuteRoomChestLocation: BoosterTowerParachuteRoomChestLocation(),
            BoosterTowerParachuteRoomCreviceLocation: BoosterTowerParachuteRoomCreviceLocation(),
            BoosterTowerCheckerboardRightmostItemLocation: BoosterTowerCheckerboardRightmostItemLocation(),
            BoosterTowerCheckerboardTopItemLocation: BoosterTowerCheckerboardTopItemLocation(),
            BoosterTowerCheckerboardLeftmostItemLocation: BoosterTowerCheckerboardLeftmostItemLocation(),
            BoosterTowerCheckerboardUpperRightItemLocation: BoosterTowerCheckerboardUpperRightItemLocation(),
            BoosterTowerCheckerboardBottomItemLocation: BoosterTowerCheckerboardBottomItemLocation(),
            BoosterTowerCheckerboardCoin1Location: BoosterTowerCheckerboardCoin1Location(),
            BoosterTowerCheckerboardCoin2Location: BoosterTowerCheckerboardCoin2Location(),
            BoosterTowerCheckerboardCoin3Location: BoosterTowerCheckerboardCoin3Location(),
            BoosterTowerCheckerboardCoin4Location: BoosterTowerCheckerboardCoin4Location(),
            BoosterTowerCheckerboardCoin5Location: BoosterTowerCheckerboardCoin5Location(),
            BoosterTowerCheckerboardCoin6Location: BoosterTowerCheckerboardCoin6Location(),
            BoosterTowerCheckerboardCoin7Location: BoosterTowerCheckerboardCoin7Location(),
            BoosterTowerCheckerboardCoin8Location: BoosterTowerCheckerboardCoin8Location(),
            BoosterTowerCheckerboardCoin9Location: BoosterTowerCheckerboardCoin9Location(),
            BoosterTowerRoomKeyChestLocation: BoosterTowerRoomKeyChestLocation(),
            BoosterTowerTopFloorLowerChestLocation: BoosterTowerTopFloorLowerChestLocation(),
            BoosterTowerTopFloorUpperChestLocation: BoosterTowerTopFloorUpperChestLocation(),
            BoosterTowerTopFloorCornerChestLocation: BoosterTowerTopFloorCornerChestLocation(),
            BoosterTowerCurtainGamePrizeLocation: BoosterTowerCurtainGamePrizeLocation(),
            BoosterTowerIndoorBossFight: BoosterTowerIndoorBossFight(),
            BoosterTowerIndoorStarPiece: BoosterTowerIndoorStarPiece(),
            BoosterTowerBalconyBossFight: BoosterTowerBalconyBossFight(),
            BoosterTowerBalconyStarPiece: BoosterTowerBalconyStarPiece(),
            BoosterHillGuaranteedItem1: BoosterHillGuaranteedItem1(),
            BoosterHillGuaranteedItem2: BoosterHillGuaranteedItem2(),
            BoosterHillGuaranteedItem3: BoosterHillGuaranteedItem3(),
            BoosterHillGuaranteedItem4: BoosterHillGuaranteedItem4(),
            BoosterHillGuaranteedItem5: BoosterHillGuaranteedItem5(),
            BoosterHillGuaranteedItem6: BoosterHillGuaranteedItem6(),
            BoosterHillGuaranteedItem7: BoosterHillGuaranteedItem7(),
            BoosterHillGuaranteedItem8: BoosterHillGuaranteedItem8(),
            BoosterHillGuaranteedItem9: BoosterHillGuaranteedItem9(),
            BoosterHillGuaranteedItem10: BoosterHillGuaranteedItem10(),
            BoosterHillGuaranteedItem11: BoosterHillGuaranteedItem11(),
            BoosterHillGuaranteedItem12: BoosterHillGuaranteedItem12(),
            BoosterHillGuaranteedItem13: BoosterHillGuaranteedItem13(),
            BoosterHillGuaranteedItem14: BoosterHillGuaranteedItem14(),
            BoosterHillGuaranteedItem15: BoosterHillGuaranteedItem15(),
            BoosterHillGuaranteedItem16: BoosterHillGuaranteedItem16(),
            MarrymoreFirstSuitePrizeLocation: MarrymoreFirstSuitePrizeLocation(),
            MarrymoreSecondSuitePrizeLocation: MarrymoreSecondSuitePrizeLocation(),
            MarrymoreThirdSuitePrizeLocation: MarrymoreThirdSuitePrizeLocation(),
            MarrymoreFourthSuitePrizeLocation: MarrymoreFourthSuitePrizeLocation(),
            MarrymoreFifthSuitePrizeLocation: MarrymoreFifthSuitePrizeLocation(),
            MarrymoreSixthSuitePrizeLocation: MarrymoreSixthSuitePrizeLocation(),
            MarrymoreBigTipLocation: MarrymoreBigTipLocation(),
            MarrymoreHotelChestLocation: MarrymoreHotelChestLocation(),
            MarrymoreSnifit1Location: MarrymoreSnifit1Location(),
            MarrymoreSnifit2Location: MarrymoreSnifit2Location(),
            MarrymoreSnifit3Location: MarrymoreSnifit3Location(),
            MarrymoreAltarHeadLocation: MarrymoreAltarHeadLocation(),
            MarrymoreBossFight: MarrymoreBossFight(),
            MarrymoreBossFightStarPiece: MarrymoreBossFightStarPiece(),
            MarrymoreCharacter: MarrymoreCharacter(),
            StarHillStarPiece: StarHillStarPiece(),
            FrogDiscipleLocation1: FrogDiscipleLocation1(),
            FrogDiscipleLocation2: FrogDiscipleLocation2(),
            FrogDiscipleLocation3: FrogDiscipleLocation3(),
            FrogDiscipleLocation4: FrogDiscipleLocation4(),
            FrogDiscipleLocation5: FrogDiscipleLocation5(),
            SeasideBeachBossFight: SeasideBeachBossFight(),
            SeasideBeachStarPiece: SeasideBeachStarPiece(),
            SeasideTownBossPrizeLocation: SeasideTownBossPrizeLocation(),
            SeasideTownShedRescueLocation: SeasideTownShedRescueLocation(),
            SeaStarslapRoomChestLocation: SeaStarslapRoomChestLocation(),
            SeaSaveRoomBackChestLocation: SeaSaveRoomBackChestLocation(),
            SeaSaveRoomMiddleChestLocation: SeaSaveRoomMiddleChestLocation(),
            SeaSaveRoomFrontChestLocation: SeaSaveRoomFrontChestLocation(),
            SeaWhirlpoolChestLocation: SeaWhirlpoolChestLocation(),
            ShipRatStairsChestLocation: ShipRatStairsChestLocation(),
            ShipRatStairsBoxesLocation: ShipRatStairsBoxesLocation(),
            ShipTroopaPuzzleLocation: ShipTroopaPuzzleLocation(),
            ShipTrampolinePuzzle: ShipTrampolinePuzzle(),
            Ship3DMazePuzzle: Ship3DMazePuzzle(),
            ShipShopChestLocation: ShipShopChestLocation(),
            ShipCoinSnakePuzzleLocation: ShipCoinSnakePuzzleLocation(),
            ShipCannonballPuzzle: ShipCannonballPuzzle(),
            ShipBarrelPuzzle: ShipBarrelPuzzle(),
            ShipPasswordBossFight: ShipPasswordBossFight(),
            ShipPasswordStarPiece: ShipPasswordStarPiece(),
            EarlyInnerShipLeftChestLocation: EarlyInnerShipLeftChestLocation(),
            EarlyInnerShipRightChestLocation: EarlyInnerShipRightChestLocation(),
            InnerShipCloneRoomChestLocation: InnerShipCloneRoomChestLocation(),
            InnerShipBehindBoxesChestLocation: InnerShipBehindBoxesChestLocation(),
            InnerShipSaveRoomLeftChestLocation: InnerShipSaveRoomLeftChestLocation(),
            InnerShipSaveRoomRightChestLocation: InnerShipSaveRoomRightChestLocation(),
            Mimic2DropRewardLocation: Mimic2DropRewardLocation(),
            Mimic2BossFight: Mimic2BossFight(),
            Mimic2StarPiece: Mimic2StarPiece(),
            Mimic2ReloadRewardLocation: Mimic2ReloadRewardLocation(),
            InnerShipFirstUnderwaterRoomBottomItemLocation: InnerShipFirstUnderwaterRoomBottomItemLocation(),
            InnerShipFirstUnderwaterRoomTopItemLocation: InnerShipFirstUnderwaterRoomTopItemLocation(),
            InnerShipFirstUnderwaterRoomLeftItemLocation: InnerShipFirstUnderwaterRoomLeftItemLocation(),
            InnerShipFirstUnderwaterRoomMiddleItemLocation: InnerShipFirstUnderwaterRoomMiddleItemLocation(),
            InnerShipSecretRoomChestLocation: InnerShipSecretRoomChestLocation(),
            InnerShipPoolRoomLocation: InnerShipPoolRoomLocation(),
            InnerShipBeforeBossChestLocation: InnerShipBeforeBossChestLocation(),
            ShipFinalBossFight: ShipFinalBossFight(),
            ShipFinalStarPiece: ShipFinalStarPiece(),
            LandsEndRisingPlatformChestLocation: LandsEndRisingPlatformChestLocation(),
            LandsEndChowPitStaticChestLocation: LandsEndChowPitStaticChestLocation(),
            LandsEndChowPitMovingChestLocation: LandsEndChowPitMovingChestLocation(),
            LandsEndBeeTowerChestLocation: LandsEndBeeTowerChestLocation(),
            LandsEndGrottoEntranceChestLocation: LandsEndGrottoEntranceChestLocation(),
            LandsEndGrottoCornerChestLocation: LandsEndGrottoCornerChestLocation(),
            LandsEndGrottoEndChestLocation: LandsEndGrottoEndChestLocation(),
            LandsEndUndergroundSaveBoxChestLocation: LandsEndUndergroundSaveBoxChestLocation(),
            LandsEndFirstPurchasableChestLocation: LandsEndFirstPurchasableChestLocation(),
            LandsEndSecondPurchasableChestLocation: LandsEndSecondPurchasableChestLocation(),
            TroopaClimbSub12PrizeLocation: TroopaClimbSub12PrizeLocation(),
            LandsEndCloudBoss: LandsEndCloudBoss(),
            LandsEndCloudStarPiece: LandsEndCloudStarPiece(),
            BelomeTempleFortuneTellerLocation: BelomeTempleFortuneTellerLocation(),
            BelomeTempleLMRChestLocation: BelomeTempleLMRChestLocation(),
            BelomeTempleLRMChestLocation: BelomeTempleLRMChestLocation(),
            BelomeTempleRLMChestLocation: BelomeTempleRLMChestLocation(),
            BelomeTempleRMLChestLocation: BelomeTempleRMLChestLocation(),
            BelomeBeforeBossRightChestLocation: BelomeBeforeBossRightChestLocation(),
            BelomeBeforeBossLowerLeftChestLocation: BelomeBeforeBossLowerLeftChestLocation(),
            BelomeBeforeBossMiddleChestLocation: BelomeBeforeBossMiddleChestLocation(),
            BelomeBeforeBossUpperLeftChestLocation: BelomeBeforeBossUpperLeftChestLocation(),
            BelomeTempleTreasuryUpperCornerLeftItemLocation: BelomeTempleTreasuryUpperCornerLeftItemLocation(),
            BelomeTempleTreasuryUpperCornerLowerLeftItemLocation: BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(),
            BelomeTempleTreasuryUpperCornerTopItemLocation: BelomeTempleTreasuryUpperCornerTopItemLocation(),
            BelomeTempleTreasuryTopmostItemLocation: BelomeTempleTreasuryTopmostItemLocation(),
            BelomeTempleTreasuryMidLeftItemLocation: BelomeTempleTreasuryMidLeftItemLocation(),
            BelomeTempleTreasuryAlmostTopItemLocation: BelomeTempleTreasuryAlmostTopItemLocation(),
            BelomeTempleTreasuryAlmostLeftmostItemLocation: BelomeTempleTreasuryAlmostLeftmostItemLocation(),
            BelomeTempleTreasuryOuterUpperRightItemLocation: BelomeTempleTreasuryOuterUpperRightItemLocation(),
            BelomeTempleTreasuryInnerUpperRightItemLocation: BelomeTempleTreasuryInnerUpperRightItemLocation(),
            BelomeTempleTreasuryLowestItemsRightLocation: BelomeTempleTreasuryLowestItemsRightLocation(),
            BelomeTempleTreasuryLowerOuterBottomRightItemLocation: BelomeTempleTreasuryLowerOuterBottomRightItemLocation(),
            BelomeTempleTreasuryRightmostItemLocation: BelomeTempleTreasuryRightmostItemLocation(),
            BelomeTempleTreasuryBottomLeftCornerItemLocation: BelomeTempleTreasuryBottomLeftCornerItemLocation(),
            BelomeTempleTreasuryLowestItemsLeftLocation: BelomeTempleTreasuryLowestItemsLeftLocation(),
            BelomeTempleTreasuryUpperOuterBottomRightItemLocation: BelomeTempleTreasuryUpperOuterBottomRightItemLocation(),
            TempleBossFight: TempleBossFight(),
            TempleBossFightStarPiece: TempleBossFightStarPiece(),
            MonstroEntranceLocation: MonstroEntranceLocation(),
            MonstroThwompItemLocation: MonstroThwompItemLocation(),
            DojoFirstFight: DojoFirstFight(),
            DojoFirstFightStarPiece: DojoFirstFightStarPiece(),
            DojoSecondFight: DojoSecondFight(),
            DojoSecondFightStarPiece: DojoSecondFightStarPiece(),
            DojoThirdFight: DojoThirdFight(),
            DojoThirdFightStarPiece: DojoThirdFightStarPiece(),
            DojoFourthFight: DojoFourthFight(),
            DojoFourthFightStarPiece: DojoFourthFightStarPiece(),
            MonstroDojoClearRewardLocation: MonstroDojoClearRewardLocation(),
            MonstroSealedDoorBossFight: MonstroSealedDoorBossFight(),
            MonstroSealedDoorStarPiece: MonstroSealedDoorStarPiece(),
            MonstroSealedDoorClearRewardLocation: MonstroSealedDoorClearRewardLocation(),
            MonstroFlagExchangeLocation: MonstroFlagExchangeLocation(),
            BeanValleyFirstDeadEndLocation: BeanValleyFirstDeadEndLocation(),
            BeanValleyFirstProgressChestLocation: BeanValleyFirstProgressChestLocation(),
            BeanValleyLeftPiranhaPipeLocation: BeanValleyLeftPiranhaPipeLocation(),
            BeanValleyBottomLeftPiranhaPipeLocation: BeanValleyBottomLeftPiranhaPipeLocation(),
            BeanValleyBottomRightPiranhaPipeUpperLocation: BeanValleyBottomRightPiranhaPipeUpperLocation(),
            BeanValleyBottomRightPiranhaPipeLowerLocation: BeanValleyBottomRightPiranhaPipeLowerLocation(),
            BeanValleyRightPipeLeftChestLocation: BeanValleyRightPipeLeftChestLocation(),
            Mimic3BossFight: Mimic3BossFight(),
            Mimic3StarPiece: Mimic3StarPiece(),
            BeanValleyRightPipeRightChestLocation: BeanValleyRightPipeRightChestLocation(),
            BeanValleyRightPipeUnderStairsLocation: BeanValleyRightPipeUnderStairsLocation(),
            BeanValleyRightPipeAboveGroundLocation: BeanValleyRightPipeAboveGroundLocation(),
            BeanValleyPlanterBossFight: BeanValleyPlanterBossFight(),
            BeanValleyPlanterStarPiece: BeanValleyPlanterStarPiece(),
            BeanValleyBossNoteLocation: BeanValleyBossNoteLocation(),
            BeanstalkLowestChestLocation: BeanstalkLowestChestLocation(),
            BeanValley1stRoomFloatingItemLocation: BeanValley1stRoomFloatingItemLocation(),
            BeanValley1stRoomMiddleCoinLocation: BeanValley1stRoomMiddleCoinLocation(),
            BeanValley1stRoomUpperCoinLocation: BeanValley1stRoomUpperCoinLocation(),
            BeanValley1stRoomLowerCoinLocation: BeanValley1stRoomLowerCoinLocation(),
            Beanstalk2ndRoomFloatingItemLocation: Beanstalk2ndRoomFloatingItemLocation(),
            Beanstalk2ndRoomCoin1Location: Beanstalk2ndRoomCoin1Location(),
            Beanstalk2ndRoomCoin2Location: Beanstalk2ndRoomCoin2Location(),
            Beanstalk2ndRoomCoin3Location: Beanstalk2ndRoomCoin3Location(),
            BeanValleyEastBeanstalkCoin1Location: BeanValleyEastBeanstalkCoin1Location(),
            BeanValleyEastBeanstalkCoin2Location: BeanValleyEastBeanstalkCoin2Location(),
            BeanValleyEastBeanstalkCoin3Location: BeanValleyEastBeanstalkCoin3Location(),
            BeanValleyEastBeanstalkCoin4Location: BeanValleyEastBeanstalkCoin4Location(),
            BeanValleyEastBeanstalkCoin5Location: BeanValleyEastBeanstalkCoin5Location(),
            BeanValleyWestBeanstalkCoin1Location: BeanValleyWestBeanstalkCoin1Location(),
            BeanValleyWestBeanstalkCoin2Location: BeanValleyWestBeanstalkCoin2Location(),
            BeanValleyWestBeanstalkCoin3Location: BeanValleyWestBeanstalkCoin3Location(),
            BeanValleyWestBeanstalkFloatingItemLocation: BeanValleyWestBeanstalkFloatingItemLocation(),
            BeanstalkUpperCloudLeftChestLocation: BeanstalkUpperCloudLeftChestLocation(),
            BeanstalkUpperCloudRightChestLocation: BeanstalkUpperCloudRightChestLocation(),
            BeanstalkLowerCloudLeftChestLocation: BeanstalkLowerCloudLeftChestLocation(),
            BeanstalkLowerCloudRightChestLocation: BeanstalkLowerCloudRightChestLocation(),
            CasinoGrateGuyPrizeLocation: CasinoGrateGuyPrizeLocation(),
            NimbusShopChestLocation: NimbusShopChestLocation(),
            NimbusInnDreamPrize1Location: NimbusInnDreamPrize1Location(),
            NimbusInnDreamPrize2Location: NimbusInnDreamPrize2Location(),
            NimbusCastleStatueGamePrizeLocation: NimbusCastleStatueGamePrizeLocation(),
            StatueRoomBossFight: StatueRoomBossFight(),
            StatueRoomStarPiece: StatueRoomStarPiece(),
            NimbusCastleOuterPrisonCellarRightNPCLocation: NimbusCastleOuterPrisonCellarRightNPCLocation(),
            NimbusCastleOuterPrisonCellarLeftNPCLocation: NimbusCastleOuterPrisonCellarLeftNPCLocation(),
            NimbusCastleBusinessCentreOccupiedChestLocation: NimbusCastleBusinessCentreOccupiedChestLocation(),
            NimbusCastleCornerBridgeChestLocation: NimbusCastleCornerBridgeChestLocation(),
            NimbusCastleOutOfBoundsChestLocation: NimbusCastleOutOfBoundsChestLocation(),
            NimbusCastleAboveJawfulChestLocation: NimbusCastleAboveJawfulChestLocation(),
            NimbusCastleSingleGoldBirdChestLocation: NimbusCastleSingleGoldBirdChestLocation(),
            NimbusCastleTwoLevelLowerChestLocation: NimbusCastleTwoLevelLowerChestLocation(),
            GiantEggBossFight: GiantEggBossFight(),
            GiantEggStarPiece: GiantEggStarPiece(),
            NimbusCastleGiantEggRewardLocation: NimbusCastleGiantEggRewardLocation(),
            NimbusCastleTwoLevelUpperChestLocation: NimbusCastleTwoLevelUpperChestLocation(),
            NimbusCastleBackHallwayOccupiedChestLocation: NimbusCastleBackHallwayOccupiedChestLocation(),
            NimbusFinalBossFight: NimbusFinalBossFight(),
            NimbusFinalStarPiece: NimbusFinalStarPiece(),
            NimbusCastleBackHallwayLiberatedChestLocation: NimbusCastleBackHallwayLiberatedChestLocation(),
            NimbusCastleBusinessCentreLiberatedChestLocation: NimbusCastleBusinessCentreLiberatedChestLocation(),
            NimbusLandRightSideLocation: NimbusLandRightSideLocation(),
            NimbusLandCrocoItemLocation: NimbusLandCrocoItemLocation(),
            NimbusLandInnerCellarLocation: NimbusLandInnerCellarLocation(),
            VolcanoLavaCoveLeftChestLocation: VolcanoLavaCoveLeftChestLocation(),
            VolcanoLavaCoveRightChestLocation: VolcanoLavaCoveRightChestLocation(),
            VolcanoEarlyProgressChestLeftLocation: VolcanoEarlyProgressChestLeftLocation(),
            VolcanoEarlyProgressChestRightLocation: VolcanoEarlyProgressChestRightLocation(),
            VolcanoEarlyProgressThirdChestLocation: VolcanoEarlyProgressThirdChestLocation(),
            VolcanoLavaPoolLocation: VolcanoLavaPoolLocation(),
            VolcanoReverseRecoilItemLocation: VolcanoReverseRecoilItemLocation(),
            VolcanoRightDonutItemLocation: VolcanoRightDonutItemLocation(),
            VolcanoLeftDonutItemLocation: VolcanoLeftDonutItemLocation(),
            VolcanoSaveRoomLowerChestLocation: VolcanoSaveRoomLowerChestLocation(),
            VolcanoSaveRoomUpperChestLocation: VolcanoSaveRoomUpperChestLocation(),
            VolcanoShopEntranceChestLocation: VolcanoShopEntranceChestLocation(),
            VolcanoBridgeBossFight: VolcanoBridgeBossFight(),
            VolcanoBridgeStarPiece: VolcanoBridgeStarPiece(),
            VolcanoExitBossFight: VolcanoExitBossFight(),
            VolcanoExitStarPiece: VolcanoExitStarPiece(),
            KeepDarkRoomChestLocation: KeepDarkRoomChestLocation(),
            KeepFirstCrocoShopLeftChestLocation: KeepFirstCrocoShopLeftChestLocation(),
            KeepFirstCrocoShopRightChestLocation: KeepFirstCrocoShopRightChestLocation(),
            KeepInvisibleBridgeFrontChestLocation: KeepInvisibleBridgeFrontChestLocation(),
            KeepInvisibleBridgeRightChestLocation: KeepInvisibleBridgeRightChestLocation(),
            KeepInvisibleBridgeLeftChestLocation: KeepInvisibleBridgeLeftChestLocation(),
            KeepInvisibleBridgeBackChestLocation: KeepInvisibleBridgeBackChestLocation(),
            KeepInvisibleBridgeCoin1Location: KeepInvisibleBridgeCoin1Location(),
            KeepInvisibleBridgeCoin2Location: KeepInvisibleBridgeCoin2Location(),
            KeepInvisibleBridgeCoin3Location: KeepInvisibleBridgeCoin3Location(),
            KeepInvisibleBridgeCoin4Location: KeepInvisibleBridgeCoin4Location(),
            KeepXYPlatformsBackLeftChestLocation: KeepXYPlatformsBackLeftChestLocation(),
            KeepXYPlatformsFrontLeftChestLocation: KeepXYPlatformsFrontLeftChestLocation(),
            KeepXYPlatformsFrontRightChestLocation: KeepXYPlatformsFrontRightChestLocation(),
            KeepXYPlatformsBackRightChestLocation: KeepXYPlatformsBackRightChestLocation(),
            KeepElevatorRoomChestLocation: KeepElevatorRoomChestLocation(),
            KeepCannonballRoomFrontRightChestLocation: KeepCannonballRoomFrontRightChestLocation(),
            KeepCannonballRoomBackChestLocation: KeepCannonballRoomBackChestLocation(),
            KeepCannonballFrontLeftChestLocation: KeepCannonballFrontLeftChestLocation(),
            KeepCannonballMidRightChestLocation: KeepCannonballMidRightChestLocation(),
            KeepCannonballMidLeftChestLocation: KeepCannonballMidLeftChestLocation(),
            KeepCannonballCoin1Location: KeepCannonballCoin1Location(),
            KeepCannonballCoin2Location: KeepCannonballCoin2Location(),
            KeepCannonballCoin3Location: KeepCannonballCoin3Location(),
            KeepCannonballCoin4Location: KeepCannonballCoin4Location(),
            KeepCannonballCoin5Location: KeepCannonballCoin5Location(),
            KeepCannonballCoin6Location: KeepCannonballCoin6Location(),
            KeepCannonballCoin7Location: KeepCannonballCoin7Location(),
            KeepCannonballCoin8Location: KeepCannonballCoin8Location(),
            KeepRotatingPlatformsFrontChestLocation: KeepRotatingPlatformsFrontChestLocation(),
            KeepRotatingPlatformsFrontMidLeftChestLocation: KeepRotatingPlatformsFrontMidLeftChestLocation(),
            KeepRotatingPlatformsBackMidRightChestLocation: KeepRotatingPlatformsBackMidRightChestLocation(),
            KeepRotatingPlatformsFrontMidRightChestLocation: KeepRotatingPlatformsFrontMidRightChestLocation(),
            KeepRotatingPlatformsBackMidLeftChestLocation: KeepRotatingPlatformsBackMidLeftChestLocation(),
            KeepRotatingPlatformsBackChestLocation: KeepRotatingPlatformsBackChestLocation(),
            ObstacleCourseFinalFight: ObstacleCourseFinalFight(),
            ObstacleCourseFinalFightStarPiece: ObstacleCourseFinalFightStarPiece(),
            KeepDoorRewardChest1Location: KeepDoorRewardChest1Location(),
            KeepDoorRewardChest2Location: KeepDoorRewardChest2Location(),
            KeepDoorRewardChest3Location: KeepDoorRewardChest3Location(),
            KeepDoorRewardChest4Location: KeepDoorRewardChest4Location(),
            KeepDoorRewardChest5Location: KeepDoorRewardChest5Location(),
            KeepDoorRewardChest6Location: KeepDoorRewardChest6Location(),
            KeepAfterObstaclesBossFight: KeepAfterObstaclesBossFight(),
            KeepAfterObstaclesStarPiece: KeepAfterObstaclesStarPiece(),
            KeepAfterObstaclesBossChestLocation: KeepAfterObstaclesBossChestLocation(),
            KeepChandelierBossFight: KeepChandelierBossFight(),
            KeepChandelierStarPiece: KeepChandelierStarPiece(),
            KeepFinalBossFight: KeepFinalBossFight(),
            KeepFinalStarPiece: KeepFinalStarPiece(),
            OuterFactorySaveRoomChestLocation: OuterFactorySaveRoomChestLocation(),
            FactoryBoltPlatformsChestLocation: FactoryBoltPlatformsChestLocation(),
            FactoryEntranceBossFight: FactoryEntranceBossFight(),
            FactoryEntranceStarPiece: FactoryEntranceStarPiece(),
            FactoryAxemConveyorsChestLocation: FactoryAxemConveyorsChestLocation(),
            FactoryTreasurePitBackChestLocation: FactoryTreasurePitBackChestLocation(),
            FactoryTreasurePitFrontChestLocation: FactoryTreasurePitFrontChestLocation(),
            FactoryBigConveyorRoomFirstChestLocation: FactoryBigConveyorRoomFirstChestLocation(),
            FactoryBigConveyorRoomSecondChestLocation: FactoryBigConveyorRoomSecondChestLocation(),
            FactoryBehindNinjasRightChestLocation: FactoryBehindNinjasRightChestLocation(),
            FactoryBehindNinjasLeftChestLocation: FactoryBehindNinjasLeftChestLocation(),
            FactoryTransitionBossFight: FactoryTransitionBossFight(),
            FactoryTransitionStarPiece: FactoryTransitionStarPiece(),
            InnerFactoryFirstFight: InnerFactoryFirstFight(),
            InnerFactoryFirstFightStarPiece: InnerFactoryFirstFightStarPiece(),
            InnerFactoryToadGiftLocation: InnerFactoryToadGiftLocation(),
            InnerFactorySecondFight: InnerFactorySecondFight(),
            InnerFactorySecondFightStarPiece: InnerFactorySecondFightStarPiece(),
            InnerFactoryThirdFight: InnerFactoryThirdFight(),
            InnerFactoryThirdFightStarPiece: InnerFactoryThirdFightStarPiece(),
            InnerFactoryFourthFight: InnerFactoryFourthFight(),
            InnerFactoryFourthFightStarPiece: InnerFactoryFourthFightStarPiece(),
            FinalBossFight: FinalBossFight(),
        }

        # Only include FinalBossFightStarPiece if win condition is not FACTORY
        # (when FACTORY is the win condition, defeating the final boss ends the game
        # so there's no opportunity to collect the star piece)
        if not self.settings.is_flag_value(WinCondition, WinConditions.FACTORY):
            self.locations[FinalBossFightStarPiece] = FinalBossFightStarPiece()

        included_charaters = self.settings.get_flag(AvailableCharacters).enabled
        if MARIO_Ally in included_charaters:
            self.locations = {
                **self.locations,
                MarioSpell1: MarioSpell1(),
                MarioSpell2: MarioSpell2(),
                MarioSpell3: MarioSpell3(),
                MarioSpell4: MarioSpell4(),
                MarioSpell5: MarioSpell5(),
                MarioSpell6: MarioSpell6(),
            }
        if MALLOW_Ally in included_charaters:
            self.locations = {
                **self.locations,
                MallowSpell1: MallowSpell1(),
                MallowSpell2: MallowSpell2(),
                MallowSpell3: MallowSpell3(),
                MallowSpell4: MallowSpell4(),
                MallowSpell5: MallowSpell5(),
                MallowSpell6: MallowSpell6(),
            }
        if GENO_Ally in included_charaters:
            self.locations = {
                **self.locations,
                GenoSpell1: GenoSpell1(),
                GenoSpell2: GenoSpell2(),
                GenoSpell3: GenoSpell3(),
                GenoSpell4: GenoSpell4(),
                GenoSpell5: GenoSpell5(),
            }
        if BOWSER_Ally in included_charaters:
            self.locations = {
                **self.locations,
                BowserSpell1: BowserSpell1(),
                BowserSpell2: BowserSpell2(),
                BowserSpell3: BowserSpell3(),
                BowserSpell4: BowserSpell4(),
                BowserSpell5: BowserSpell5(),
                BowserSpell6: BowserSpell6(),
            }
        if TOADSTOOL_Ally in included_charaters:
            self.locations = {
                **self.locations,
                ToadstoolSpell1: ToadstoolSpell1(),
                ToadstoolSpell2: ToadstoolSpell2(),
                ToadstoolSpell3: ToadstoolSpell3(),
                ToadstoolSpell4: ToadstoolSpell4(),
                ToadstoolSpell5: ToadstoolSpell5(),
                ToadstoolSpell6: ToadstoolSpell6(),
            }

        

        # Only add Super Jump reward locations if Super Jump spell is enabled
        available_spells = self.settings.get_flag(AvailableSpells)
        super_jump_enabled = any(
            spell_opt.value == SuperJumpSpell for spell_opt in available_spells.enabled
        )
        if super_jump_enabled:
            self.locations = {
                **self.locations,
                MonstroFirstSuperJumpRewardLocation: MonstroFirstSuperJumpRewardLocation(),
                MonstroSecondSuperJumpRewardLocation: MonstroSecondSuperJumpRewardLocation(),
            }

        if self.settings.isflag_enabled(FixKnifeGuy):
            self.locations = {
                **self.locations,
                BoosterTowerKnifeGuy2PrizeLocation: BoosterTowerKnifeGuy2PrizeLocation(),
            }

        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            fwshop = FireworksShopItemLocation()
            fwshop._originally_held = ProgressiveFireworksPrize
            fwshop.set_prize(ProgressiveFireworksPrize())
            self.locations = {
                **self.locations,
                FireworksShopItemLocation: fwshop,
                PurtendStoreLocation: PurtendStoreLocation(),
                CookieTraderLocation: CookieTraderLocation(),
            }
            self.get_item(FireworksItem).set_price(0)
            self.get_item(ShinyStoneItem).set_price(0)
            self.get_item(CarboCookieItem).set_price(0)
        elif self.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            self.locations = {**self.locations, FireworksShopItemLocation: FireworksShopItemLocation()}
            self.get_item(FireworksItem).set_price(0)
            self.get_item(ShinyStoneItem).set_price(0)
            self.get_item(CarboCookieItem).set_price(0)

        strchars = self.settings.get_flag(StartingCharacters)
        startmax = len(strchars.enabled)
        if startmax >= 2:
            self.locations = {
                **self.locations,
                StartingCharacter2: StartingCharacter2(),
            }
        if startmax >= 3:
            self.locations = {
                **self.locations,
                StartingCharacter3: StartingCharacter3(),
            }
        if startmax >= 4:
            self.locations = {
                **self.locations,
                StartingCharacter4: StartingCharacter4(),
            }
        if startmax >= 5:
            self.locations = {
                **self.locations,
                StartingCharacter5: StartingCharacter5(),
            }
        # Resolve starting character selections (handles "Random_X" values)
        # and assign prizes to the starting character locations
        resolved_allies = (
            strchars.resolve_random_selections()
        )  # Uses seeded global random
        # Map allies by index to their prize classes (allies are all the same type)
        ally_to_prize: dict[int, type] = {
            MARIO_Ally.index: MarioRecruitmentPrize,
            MALLOW_Ally.index: MallowRecruitmentPrize,
            GENO_Ally.index: GenoRecruitmentPrize,
            BOWSER_Ally.index: BowserRecruitmentPrize,
            TOADSTOOL_Ally.index: ToadstoolRecruitmentPrize,
        }
        starting_char_locations = [
            StartingCharacter1,
            StartingCharacter2,
            StartingCharacter3,
            StartingCharacter4,
            StartingCharacter5,
        ]
        for i, ally in enumerate(resolved_allies):
            if i < len(starting_char_locations):
                loc_type = starting_char_locations[i]
                if loc_type in self.locations:
                    prize_cls = ally_to_prize.get(ally.index)
                    if prize_cls:
                        self.locations[loc_type].set_prize(prize_cls())

        if self.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
            self.locations = {
                **self.locations,
                GarroFreeItem: GarroFreeItem(),
            }


        # Optionally include remake content.
        if self.settings.get_flag(Remake).enabled:
            self.locations = {
                **self.locations,
                PostgameVoucherLocation: PostgameVoucherLocation(),
                MushroomWayLeftItemRemake: MushroomWayLeftItemRemake(),
                MushroomWayRightItemRemake: MushroomWayRightItemRemake(),
                InnerMinesPostgameBossFight: InnerMinesPostgameBossFight(),
                InnerMinesPostgameStarPiece: InnerMinesPostgameStarPiece(),
                InnerMinesPostgameDrop: InnerMinesPostgameDrop(),
                BoosterTowerIndoorBossFightRemake: BoosterTowerIndoorBossFightRemake(),
                BoosterTowerIndoorStarPieceRemake: BoosterTowerIndoorStarPieceRemake(),
                BoosterTowerRemakeBossFightPrizeLocation: BoosterTowerRemakeBossFightPrizeLocation(),
                MarrymoreBossFightRemake: MarrymoreBossFightRemake(),
                MarrymoreBossFightStarPieceRemake: MarrymoreBossFightStarPieceRemake(),
                MarrymoreBossFightRemakeItemDrop: MarrymoreBossFightRemakeItemDrop(),
                ShipPostgameBossFight: ShipPostgameBossFight(),
                ShipPostgameFightItemDrop: ShipPostgameFightItemDrop(),
                ShipPostgameStarPiece: ShipPostgameStarPiece(),
                TempleBossFightPostgame: TempleBossFightPostgame(),
                TempleBossFightStarPiecePostgame: TempleBossFightStarPiecePostgame(),
                TemplePostgameFightItemDrop: TemplePostgameFightItemDrop(),
                DojoFifthFight: DojoFifthFight(),
                DojoFifthFightStarPiece: DojoFifthFightStarPiece(),
                MonstroDojoPostgameClearRewardLocation: MonstroDojoPostgameClearRewardLocation(),
                LandsEndCaveSideRemake: LandsEndCaveSideRemake(),
            }
            # Only include Monstro sealed door postgame locations if win condition is not SEALED
            # (when SEALED is the win condition, defeating the sealed door boss ends the game
            # so there's no opportunity to collect postgame rewards)
            if not self.settings.is_flag_value(WinCondition, WinConditions.SEALED):
                self.locations[MonstroSealedDoorBossFightPostgame] = MonstroSealedDoorBossFightPostgame()
                self.locations[MonstroSealedDoorStarPiecePostgame] = MonstroSealedDoorStarPiecePostgame()
                self.locations[MonstroSealedDoorClearRewardLocationPostgame] = MonstroSealedDoorClearRewardLocationPostgame()
            # Checks for postgame-unlocking bosses by default expect an impossible value.
            # Enabling the remake flag sets it to the correct value, 7.
            cast(
                CompareVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "postgame_progress_checker_1"
                ),
            ).set_value(7)
            cast(
                CompareVarToConst,
                self.event_scripts.get_command_by_identifier(
                    "postgame_progress_checker_2"
                ),
            ).set_value(7)

        invisible_item_pool = [
            MariosPadBedFlag,
            RoseTownSignFlag,
            YosterIsleGoalFlag,
            MariosPadSteamwhistleFlag,
            MariosPadLanternFlag,
            MariosPadHatFlag,
            MushroomWayTreeFlag,
            MushroomKingdomSignFlag,
            MushroomKingdomEmptyHouseFlag,
            ChancellorThroneFlag,
            BanditsWayFlowerFlag,
            KeroStairsFlag,
            KeroGateFlag,
            MidasTreesFlag,
            TadpoleCabinetFlag,
            RoseWayDirtPatchFlag,
            RoseTownHydrantFlag,
            RoseTownSinkFlag,
            RoseTownBowserFlag,
            RoseTownGardenerHydrantFlag,
            RoseTownGardenerBucketFlag,
            RoseTownGardenerLeafFlag,
            ForestMazeSecretStumpFlag,
            ForestMazeSecretMushroomsFlag,
            ForestMazeSecretWigglerFlag,
            PipeVaultExteriorFlag,
            PipeVaultRedPipeFlag,
            YosterIsleHutFlag,
            MolevilleHydrantFlag,
            MolevilleMountainBushFlag,
            MolevilleBedFlag,
            MolevilleMinesArrowsFlag,
            MolevilleMinesCeilingFlag,
            MolevilleMinesEntryFlag,
            BoosterPassCornerBushFlag,
            BoosterTowerExteriorSignFlag,
            BoosterTowerDeskFlag,
            BoosterTowerMasherRoomFlag,
            BoosterTowerCurtainFlag,
            BoosterTowerThwompInvisibleFlag,
            BoosterTowerBrokenFrameFlag,
            BoosterTowerBeetleCageFlag,
            BoosterTowerToyBoxFlag,
            MarrymoreOutsideCrateFlag,
            MarrymoreHallwayFlag,
            MarrymoreSuiteBedFlag,
            MarrymoreKitchenFlag,
            MarrymoreFireplaceFlag,
            MarrymoreOrganFlag,
            MarrymoreAltarFlag,
            StarHillNorthStarFlag,
            SeasideTownAnchorFlag,
            SeasideTownHydrantFlag,
            SeasideTownBucketFlag,
            SeasideTownFlowersFlag,
            SeasideTownShedBoxFlag,
            SeaArrowFlag,
            SeaBoxesFlag,
            SeaStalagnateFlag,
            SeaUnderwaterSailFlag,
            ShipBarrelPileFlag,
            ShipDoorMarkerFlag,
            ShipButtonFlag,
            ShipSwitchFlag,
            LandsEndPlatformFlag,
            LandsEndCannonFlag,
            LandsEndArrowFlag,
            LandsEndHillFlag,
            LandsEndTwoHillFlag,
            LandsEndStalagmiteFlag,
            LandsEndCliffBushFlag,
            LandsEndSignFlag,
            DojoBonsaiFlag,
            MonstroEntranceSignFlag,
            MonstroBatFlag,
            MonstroFanFlag,
            MonstroShellFlag,
            BeanValleyPipeFlag,
            BeanValleyBeanstalkBlockFlag,
            CasinoBellFlag,
            NimbusGoldGoombaFlag,
            NimbusInnLobbyFlag,
            NimbusPlantFlag,
            NimbusBirdFlag,
            NimbusHotSpringsFlag,
            VolcanoShipsFlag,
            KeepPostObstacleBossRoomFlag,
            KeepThwompFlag,
            FactoryCanopyFlag,
            FactoryLugnutFlag,
            FactoryTrampolineFlag,
            FactoryButtonFlag,
        ]

        invisible_flag_locations: dict[type[PrizeLocation], PrizeLocation] = {}
        for i in range(0, 3):
            # choose the three invisible item locations
            if not self.settings.isflag_enabled(InvisibleFlagsSetting):
                location_cls = invisible_item_pool[i]
            else:
                location_cls = random.choice(invisible_item_pool)
            location = cast(InvisibleFlagLocation, location_cls(i))
            for r in location._rooms:
                # place them in rooms and set visibility triggers
                room = self.rooms._rooms[r]
                assert room is not None
                n = location.npc
                n_id = AreaObject(len(room.objects) + 0x14)
                n.set_visible(False)
                self.event_scripts.get_script_by_id(
                    E0091_INVISIBLE_ITEM_SUMMONER
                ).insert_before_nth_command(0, SummonObjectToSpecificLevel(n_id, r))
                room.add_object(location.npc)
            # set hint text
            if i == 0:
                self.update_dialog(
                    DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
                    "DRY BONES:\n" + location.clue_text,
                )
            elif i == 1:
                self.update_dialog(
                    DI1109_RESERVED_FOR_GREAPERFLAG_HINT,
                    "GREAPER:\n" + location.clue_text,
                )
            elif i == 2:
                self.update_dialog(
                    DI1107_RESERVED_FOR_BIGBOOFLAG_HINT,
                    "THE BIG BOO:\n" + location.clue_text,
                )
        self.locations = {**self.locations, **invisible_flag_locations}





    def _randomize_enemy_attacks_and_spells(self) -> None:
        """Randomize enemy spell and attack stats and effects."""
        from randomizer.types.spell import EnemySpell

        # Status effects that can be randomly assigned (excluding berserk for safety)
        # Indices: 0=Mute, 1=Sleep, 2=Poison, 3=Fear, 5=Mushroom, 6=Scarecrow
        safe_statuses = [
            Status.MUTE,
            Status.SLEEP,
            Status.POISON,
            Status.FEAR,
            Status.MUSHROOM,
            Status.SCARECROW,
        ]

        # Randomize enemy spells
        for spell in self.spells.spells:
            if not isinstance(spell, EnemySpell):
                continue

            # Mutate FP cost
            new_fp = self._mutate_normal(int(spell.fp), minimum=1, maximum=99)
            spell.set_fp(new_fp)

            # Shuffle status effects if the spell has any
            if spell.status_effects:
                num_effects = len(spell.status_effects)
                new_effects = random.sample(
                    safe_statuses, min(num_effects, len(safe_statuses))
                )
                spell.set_status_effects(new_effects)

            # Mutate power
            new_power = self._mutate_normal(int(spell.power), minimum=0, maximum=255)
            spell.set_power(int(max(0, min(255, new_power))))

            # Mutate hit rate (cap at 99 if it's an instant KO spell to allow protection items to work)
            max_hit = 99 if spell.check_ohko else 100
            new_hit_rate = self._mutate_normal(
                int(spell.hit_rate), minimum=1, maximum=max_hit
            )
            spell.set_hit_rate(new_hit_rate)

        # Randomize enemy attacks
        for attack in self.enemy_attacks.attacks:
            # Mutate attack level (0-7 range)
            new_level = self._mutate_normal(
                int(attack.attack_level), minimum=0, maximum=7
            )
            attack.set_attack_level(new_level)

            # Shuffle status effects if the attack has any
            if attack.status_effects:
                num_effects = len(attack.status_effects)
                new_effects = random.sample(
                    safe_statuses, min(num_effects, len(safe_statuses))
                )
                attack.set_status_effects(new_effects)

            # Mutate hit rate (cap at 99 if OHKO to allow protection to work)
            max_hit = 99 if attack.ohko else 255
            new_hit_rate = self._mutate_normal(
                int(attack.hit_rate), minimum=1, maximum=max_hit
            )
            attack.set_hit_rate(new_hit_rate)

    def _randomize_enemy_stats(self) -> None:
        """Randomize enemy stats based on EnemyStats flag setting."""
        from smrpgpatchbuilder.datatypes.spells.enums import Element, Status
        from smrpgpatchbuilder.datatypes.enemies.enums import FlowerBonusType
        from randomizer.data.enemies.enemies import (
            SMITHY2Enemy,
            SMITHYTankEnemy,
            SMITHYSafeEnemy2,
            SMITHYMageEnemy,
            SMITHYChestEnemy,
        )

        full_random = (
            self.settings.get_flag(EnemyStats).selected
            == EnemyStatsShuffleOptions.FULL_RANDOM
        )

        # Get list of non-boss enemies for inter-shuffling
        # Use ohko_immune as indicator of boss status
        non_boss_enemies = [e for e in self.enemies.enemies if not e.ohko_immune]
        all_enemies = list(self.enemies.enemies)

        # NUMBERS_ONLY and FULL_RANDOM: Inter-shuffle stats between similar-ranked enemies
        # Since we don't have a ranking system, shuffle among all non-boss enemies
        if full_random:
            # Inter-shuffle these attributes among non-boss enemies
            shuffle_attrs = [
                "hp",
                "speed",
                "defense",
                "magic_defense",
                "evade",
                "magic_evade",
                "resistances",
                "weaknesses",
                "status_immunities",
            ]
        else:
            # NUMBERS_ONLY: only shuffle numeric stats
            shuffle_attrs = [
                "hp",
                "speed",
                "defense",
                "magic_defense",
                "evade",
                "magic_evade",
            ]

        for attr in shuffle_attrs:
            # Create a shuffled version with probabilistic swapping
            shuffled = list(non_boss_enemies)
            max_index = len(non_boss_enemies) - 1
            done: set = set()

            for i in range(len(non_boss_enemies)):
                if shuffled[i] in done:
                    continue
                new_index = i
                # 50/50 chance to swap with next enemy
                while random.randint(0, 1) == 1:
                    new_index += 1
                new_index = min(new_index, max_index)
                a, b = shuffled[i], shuffled[new_index]
                done.add(a)
                shuffled[i] = b
                shuffled[new_index] = a

            # Swap attribute values
            swaps = [getattr(s, attr) for s in shuffled]
            for enemy, swapped_val in zip(non_boss_enemies, swaps):
                # Get the setter method
                setter_name = f"set_{attr}"
                if hasattr(enemy, setter_name):
                    setter = getattr(enemy, setter_name)
                    if isinstance(swapped_val, list):
                        setter(list(swapped_val))
                    else:
                        setter(int(swapped_val))

        # Inter-shuffle morph chances randomly (for non-boss enemies)
        if full_random:
            morph_chances = [e.morph_chance for e in non_boss_enemies]
            random.shuffle(morph_chances)
            for chance, enemy in zip(morph_chances, non_boss_enemies):
                enemy.set_morph_chance(chance)

        # Now mutate individual enemy stats
        for enemy in all_enemies:
            # Store old stats for bosses
            old_stats = {
                "hp": int(enemy.hp),
                "speed": int(enemy.speed),
                "attack": int(enemy.attack),
                "defense": int(enemy.defense),
                "magic_attack": int(enemy.magic_attack),
                "magic_defense": int(enemy.magic_defense),
                "fp": int(enemy.fp),
                "evade": int(enemy.evade),
                "magic_evade": int(enemy.magic_evade),
            }

            # Mutate numeric stats
            enemy.set_hp(self._mutate_normal(int(enemy.hp), minimum=1, maximum=32000))
            enemy.set_speed(
                self._mutate_normal(int(enemy.speed), minimum=0, maximum=255)
            )
            enemy.set_attack(
                self._mutate_normal(int(enemy.attack), minimum=1, maximum=255)
            )
            enemy.set_defense(
                self._mutate_normal(int(enemy.defense), minimum=1, maximum=255)
            )
            enemy.set_magic_attack(
                self._mutate_normal(int(enemy.magic_attack), minimum=1, maximum=255)
            )
            enemy.set_magic_defense(
                self._mutate_normal(int(enemy.magic_defense), minimum=1, maximum=255)
            )
            enemy.set_fp(self._mutate_normal(int(enemy.fp), minimum=1, maximum=255))
            enemy.set_evade(
                self._mutate_normal(int(enemy.evade), minimum=0, maximum=100)
            )
            enemy.set_magic_evade(
                self._mutate_normal(int(enemy.magic_evade), minimum=0, maximum=100)
            )

            # For bosses (identified by ohko_immune), don't let stats go below vanilla values
            if enemy.ohko_immune:
                for attr, old_val in old_stats.items():
                    current_val = int(getattr(enemy, attr))
                    if current_val < old_val:
                        setter = getattr(enemy, f"set_{attr}")
                        setter(old_val)

                # Small 1/255 chance for boss to be vulnerable to Geno Whirl
                if random.randint(1, 255) == 1:
                    enemy.set_ohko_immune(False)
            else:
                # For non-bosses: 1/3 chance to reverse OHKO immunity
                if random.randint(1, 3) == 3:
                    enemy.set_ohko_immune(not enemy.ohko_immune)

                # Randomize morph chance (only in FULL_RANDOM mode)
                if full_random:
                    morph_options = [0, 25, 75, 100]
                    enemy.set_morph_chance(random.choice(morph_options))

            # FULL_RANDOM: also shuffle elemental resistances/weaknesses and status immunities
            if full_random:
                # Mix status immunities and resistances together
                total_immunities = len(enemy.status_immunities) + len(enemy.resistances)
                new_status_immunities = random.randint(
                    max(0, total_immunities - 4), min(total_immunities, 4)
                )
                new_resistances = total_immunities - new_status_immunities

                # Limit to valid ranges
                new_status_immunities = max(0, min(4, new_status_immunities))
                new_resistances = max(0, min(4, new_resistances))

                # Available status effects for immunity (excluding Berserk and Invincible for balance)
                available_statuses = [
                    Status.MUTE,
                    Status.SLEEP,
                    Status.POISON,
                    Status.FEAR,
                ]
                enemy.set_status_immunities(
                    random.sample(
                        available_statuses,
                        min(new_status_immunities, len(available_statuses)),
                    )
                )

                # Available elements for resistance/weakness
                available_elements = [
                    Element.ICE,
                    Element.THUNDER,
                    Element.FIRE,
                    Element.JUMP,
                ]

                # 50/50 chance to prioritize immunities over weaknesses or vice versa
                if random.randint(0, 1) == 0:
                    # Prioritize resistances
                    new_res = random.sample(
                        available_elements,
                        min(new_resistances, len(available_elements)),
                    )
                    enemy.set_resistances(new_res)
                    # Weaknesses from remaining elements (allow JUMP to be both)
                    potential_weak = list(set(available_elements) - set(new_res))
                    potential_weak.append(Element.JUMP)  # Jump can be both
                    potential_weak = list(set(potential_weak))
                    current_weak_count = len(enemy.weaknesses)
                    enemy.set_weaknesses(
                        random.sample(
                            potential_weak, min(current_weak_count, len(potential_weak))
                        )
                    )
                else:
                    # Prioritize weaknesses
                    current_weak_count = len(enemy.weaknesses)
                    new_weak = random.sample(
                        available_elements,
                        min(current_weak_count, len(available_elements)),
                    )
                    enemy.set_weaknesses(new_weak)
                    # Resistances from remaining (allow JUMP to be both)
                    potential_res = list(set(available_elements) - set(new_weak))
                    potential_res.append(Element.JUMP)
                    potential_res = list(set(potential_res))
                    enemy.set_resistances(
                        random.sample(
                            potential_res, min(new_resistances, len(potential_res))
                        )
                    )

                # Randomize flower bonus type and chance
                flower_types = [
                    FlowerBonusType.ATTACK_UP,
                    FlowerBonusType.DEFENSE_UP,
                    FlowerBonusType.HP_MAX,
                    FlowerBonusType.ONCE_AGAIN,
                    FlowerBonusType.LUCKY,
                ]
                enemy.set_flower_bonus_type(random.choice(flower_types))
                # Chance is 0-100 in increments of 10
                chance = (random.randint(0, 5) + random.randint(0, 5)) * 10
                enemy.set_flower_bonus_chance(chance)

        # Special logic for Smithy 2: All heads must have the same HP
        try:
            main_head = self.enemies.get_by_type(SMITHY2Enemy)
            for head_type in [
                SMITHYTankEnemy,
                SMITHYSafeEnemy2,
                SMITHYMageEnemy,
                SMITHYChestEnemy,
            ]:
                head = self.enemies.get_by_type(head_type)
                head.set_hp(int(main_head.hp))
        except (KeyError, StopIteration):
            pass  # Enemy types not found, skip

    def _randomize_enemy_drops(
        self,
        consumables_group_1: list[type[RegularItem]],
        consumables_group_2: list[type[RegularItem]],
    ) -> None:
        """Randomize enemy drops (coins, XP, items)."""
        for enemy in self.enemies.enemies:
            # Mutate coins
            enemy.set_coins(
                self._mutate_normal(int(enemy.coins), minimum=0, maximum=255)
            )

            # Mutate XP
            old_xp = int(enemy.xp)
            new_xp = self._mutate_normal(old_xp, minimum=1, maximum=0xFFFF)

            # For bosses (ohko_immune), don't let XP go above vanilla
            # For normal enemies, don't let XP go below vanilla
            if enemy.ohko_immune:
                enemy.set_xp(min(old_xp, new_xp))
            else:
                enemy.set_xp(max(old_xp, new_xp))

            # Shuffle reward items with consumable items
            # Check if normal and rare items are linked (same item)
            linked = enemy.common_item_drop == enemy.rare_item_drop

            # Shuffle common item drop using group 1 (more common items)
            if enemy.common_item_drop is not None:
                enemy.set_common_item_drop(random.choice(consumables_group_1))

            # If linked, set rare to match common. Otherwise shuffle rare from group 2
            if linked:
                enemy.set_rare_item_drop(enemy.common_item_drop)
            elif enemy.rare_item_drop is not None:
                enemy.set_rare_item_drop(random.choice(consumables_group_2))

            # Randomize Yoshi Cookie item if enemy has morph chance
            if enemy.morph_chance > 0:
                # Use group 2 for Yoshi Cookie items (better rewards)
                enemy.set_yoshi_cookie_item(random.choice(consumables_group_2))

    def _randomize_enemy_formations(self) -> None:
        """Randomize enemy formations."""
        from functools import reduce

        # Valid coordinates for enemy placement in formations
        VALID_COORDINATES = [
            (119, 103),
            (135, 111),
            (151, 119),
            (167, 127),
            (103, 111),
            (119, 119),
            (135, 127),
            (151, 135),
            (87, 119),
            (103, 127),
            (119, 135),
            (135, 143),
            (71, 127),
            (87, 135),
            (103, 143),
            (119, 151),
            (55, 135),
            (71, 143),
            (87, 151),
            (103, 159),
            (39, 143),
            (55, 151),
            (71, 159),
            (87, 167),
        ]

        def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        def get_collective_distance(
            x1: int, y1: int, points: list[tuple[int, int]]
        ) -> float:
            if not points:
                return 1.0
            distances = [get_distance(x1, y1, x2, y2) for x2, y2 in points]
            return reduce(lambda a, b: a * b, distances, 1.0)

        def select_most_distance(
            possible_points: list[tuple[int, int]], used_points: list[tuple[int, int]]
        ) -> tuple[int, int]:
            # Filter out already-used coordinates to ensure no duplicates
            available = [p for p in possible_points if p not in used_points]
            if not available:
                # Fallback: use all coordinates if somehow all are used
                available = possible_points
            return max(
                available,
                key=lambda c: get_collective_distance(c[0], c[1], used_points),
            )

        # Max enemies for a formation
        max_enemies = 6

        for pack in self.battle_packs.packs:
            for formation in pack.formations:
                # Get current members (filter out None)
                current_members = [m for m in formation.members if m is not None]

                # Skip empty formations
                if not current_members:
                    continue

                # Skip formations with hidden enemies (special battle events)
                if any(m.hidden_at_start for m in current_members):
                    continue

                # Skip formations where we can't run away (usually boss fights)
                if not formation.can_run_away:
                    continue

                # Get unique enemy types from current formation
                current_enemy_types = list(set(m.enemy for m in current_members))

                # Build candidates list - start with current enemy types
                candidates = list(current_enemy_types)

                # Expand candidates to at least 3 by getting random enemies
                all_enemy_types = [
                    type(e) for e in self.enemies.enemies if not e.ohko_immune
                ]
                while len(candidates) < 3 and all_enemy_types:
                    new_enemy = random.choice(all_enemy_types)
                    if new_enemy not in candidates:
                        candidates.append(new_enemy)

                # Pick random number of enemies, weighted slightly lower
                num_enemies = random.randint(1, random.randint(3, max_enemies))
                num_enemies = max(num_enemies, len(current_enemy_types))

                # Start with at least one of each original enemy type
                chosen_enemies: list[type] = list(current_enemy_types)

                # Fill out the rest
                while len(chosen_enemies) < num_enemies:
                    sub_candidates = candidates + chosen_enemies
                    if not sub_candidates:
                        break
                    chosen_enemies.append(random.choice(sub_candidates))

                random.shuffle(chosen_enemies)

                # Assign coordinates - ensure no duplicates
                new_members: list[FormationMember | None] = []
                done_coordinates: list[tuple[int, int]] = []

                for enemy_type in chosen_enemies:
                    if not done_coordinates:
                        # First enemy: pick random coordinate
                        x, y = random.choice(VALID_COORDINATES)
                    else:
                        # Subsequent enemies: pick coordinate with most distance from others
                        # Also ensuring it's not already used
                        sample_size = min(
                            len(VALID_COORDINATES), len(chosen_enemies) * 2
                        )
                        candidates_coords = random.sample(
                            VALID_COORDINATES, sample_size
                        )
                        x, y = select_most_distance(candidates_coords, done_coordinates)

                    done_coordinates.append((x, y))
                    new_members.append(
                        FormationMember(
                            enemy=enemy_type,
                            x_pos=x,
                            y_pos=y,
                            hidden_at_start=False,
                        )
                    )

                # Update formation with new members
                formation.set_members(new_members)

    def _apply_exp_multiplier(self) -> None:
        """Apply EXP multiplier to all enemies based on settings."""
        exp_setting = self.settings.get_flag(EXPMultiplier).selected

        if exp_setting == EXPMultiplierOptions.VANILLA:
            return

        multiplier = 1
        if exp_setting == EXPMultiplierOptions.DOUBLE:
            multiplier = 2
        elif exp_setting == EXPMultiplierOptions.TRIPLE:
            multiplier = 3

        for enemy in self.enemies.enemies:
            current_xp = enemy.xp
            new_xp = min(9999, current_xp * multiplier)
            enemy.set_xp(new_xp)

    def _randomize_character_stats(self) -> None:
        """Randomize character stats, level-up bonuses, and stat growths."""
        from smrpgpatchbuilder.datatypes.allies.ally import LevelUp

        LEVEL_STATS = [
            "hp_plus",
            "attack_plus",
            "defense_plus",
            "mg_attack_plus",
            "mg_defense_plus",
        ]
        BONUS_STATS = [
            "hp_plus_bonus",
            "attack_plus_bonus",
            "defense_plus_bonus",
            "mg_attack_plus_bonus",
            "mg_defense_plus_bonus",
        ]

        # Randomize XP requirements for each level
        self._randomize_levelup_xps()

        # Collect all bonuses from all allies for inter-shuffling (first 19 levels)
        all_bonuses: list[LevelUp] = []
        for ally in self.allies._allies:
            all_bonuses.extend(ally.levels[:19])

        # Inter-shuffle level up stat bonuses between all characters
        for attrs in (
            ("hp_plus_bonus",),
            ("attack_plus_bonus", "defense_plus_bonus"),
            ("mg_attack_plus_bonus", "mg_defense_plus_bonus"),
        ):
            shuffled = all_bonuses[:]
            random.shuffle(shuffled)

            for attr in attrs:
                swaps = [getattr(s, attr) for s in shuffled]
                for bonus, bval in zip(all_bonuses, swaps):
                    setattr(bonus, attr, bval)

            # For any bonuses that are zero, pick a random non-zero one
            non_zeros = [
                b for b in all_bonuses if all(getattr(b, attr) for attr in attrs)
            ]
            for bonus in all_bonuses:
                for attr in attrs:
                    while getattr(bonus, attr) == 0 and non_zeros:
                        setattr(bonus, attr, getattr(random.choice(non_zeros), attr))

        # Randomize each ally's stats
        for ally in self.allies._allies:
            # Mutate starting level and speed
            ally.starting_level = self._mutate_normal(
                ally.starting_level, minimum=1, maximum=30
            )
            ally.starting_speed = self._mutate_normal(
                ally.starting_speed, minimum=1, maximum=255
            )

            # Randomize level up stat bonuses
            for level_up in ally.levels:
                for attr in BONUS_STATS:
                    value = getattr(level_up, attr)
                    # Make each bonus at least 1
                    new_value = max(self._mutate_normal(value, maximum=15), 1)
                    setattr(level_up, attr, new_value)

            # Randomize level up stat growths for each stat
            for attr in LEVEL_STATS:
                # Get current values at level 1 and level 20
                value_lvl1 = getattr(
                    ally,
                    (
                        f'starting_{attr.replace("_plus", "")}'
                        if attr == "hp_plus"
                        else f'starting_{attr.replace("_plus", "").replace("mg_", "mg_")}'
                    ),
                    1,
                )

                # For growths, work with levels 2-20 (first 19 entries)
                growths = [getattr(level_up, attr) for level_up in ally.levels[:19]]

                # Mutate each growth value
                for i, level_up in enumerate(ally.levels[:19]):
                    value = getattr(level_up, attr)
                    new_value = max(self._mutate_normal(value, maximum=15), 1)
                    setattr(level_up, attr, new_value)

                # Beyond level 20, give smaller increases (1-2)
                for level_up in ally.levels[19:]:
                    setattr(level_up, attr, random.choices([1, 2], weights=[2, 1])[0])

            # Set starting stats based on starting level and optimal bonuses
            self._finalize_character_stats(ally)

    def _randomize_levelup_xps(self) -> None:
        """Randomize the XP requirements for each level by shuffling the gaps."""
        # Get current XP values from first ally (they share the same XP table)
        if not self.allies._allies:
            return

        ally = self.allies._allies[0]
        if not ally.levels:
            return

        # Build gaps between levels
        gaps = []
        prev_xp = 0
        for level_up in ally.levels:
            gap = level_up.exp_needed - prev_xp
            gaps.append(self._mutate_normal(gap, minimum=1, maximum=9999))
            prev_xp = level_up.exp_needed

        gaps.sort()

        # Make sure we total 9999 at level 30
        total = sum(gaps)
        if total != 9999:
            diff = 9999 - total
            piece = diff / sum(range(1, len(gaps) + 1))
            for i in range(len(gaps)):
                gaps[i] += round(piece * (i + 1))

        # Check total again for rounding
        total = sum(gaps)
        if total != 9999:
            diff = 9999 - total
            gaps[-1] += diff
            gaps.sort()

        # Apply new XP values to all allies
        for ally in self.allies._allies:
            prev = 0
            for i, level_up in enumerate(ally.levels):
                if i < len(gaps):
                    new_val = prev + gaps[i]
                    level_up.exp_needed = new_val
                    prev = new_val

    def _finalize_character_stats(self, ally) -> None:
        """Finalize character starting stats based on starting level and optimal choices."""
        STAT_MAP = {
            "starting_max_hp": ("hp_plus", "hp_plus_bonus", 999),
            "starting_attack": ("attack_plus", "attack_plus_bonus", 255),
            "starting_defense": ("defense_plus", "defense_plus_bonus", 255),
            "starting_mg_attack": ("mg_attack_plus", "mg_attack_plus_bonus", 255),
            "starting_mg_defense": ("mg_defense_plus", "mg_defense_plus_bonus", 255),
        }

        for starting_attr, (growth_attr, bonus_attr, max_val) in STAT_MAP.items():
            base_value = getattr(ally, starting_attr)

            # Calculate stat at starting level with optimal bonus choices
            total = base_value
            for i, level_up in enumerate(ally.levels[: ally.starting_level - 1]):
                growth = getattr(level_up, growth_attr)
                bonus = getattr(level_up, bonus_attr)
                total += growth + bonus

            # Ensure we don't exceed maximum
            total = min(total, max_val)
            setattr(ally, starting_attr, total)

        # Set starting current HP to max HP
        ally.starting_current_hp = ally.starting_max_hp

        # Set starting experience based on starting level
        if ally.starting_level > 1 and ally.levels:
            ally.starting_experience = ally.levels[ally.starting_level - 2].exp_needed
        else:
            ally.starting_experience = 0

    def _randomize_character_spell_stats(self) -> None:
        """Randomize character spell stats (FP cost, power, hit rate)."""
        from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
        from ..data.spells.spells import (
            GenoBoostSpell,
            TherapySpell,
            GroupHugSpell,
            HPRainSpell,
            PsychopathSpell,
            SleepyTimeSpell,
            MuteSpell,
        )

        # Spells that should not have their power randomized
        NO_POWER_SHUFFLE = (GenoBoostSpell, SleepyTimeSpell, MuteSpell, PsychopathSpell)

        # Spells that should not have their hit rate randomized
        NO_HIT_RATE_SHUFFLE = (
            GenoBoostSpell,
            TherapySpell,
            GroupHugSpell,
            HPRainSpell,
            PsychopathSpell,
        )

        for spell in self.spells.spells:
            if not isinstance(spell, CharacterSpell):
                continue

            # Randomize FP cost (1-31, capped by set_fp assertion)
            new_fp = self._mutate_normal(int(spell.fp), minimum=1, maximum=31)
            spell.set_fp(new_fp)

            # Randomize power (except for certain spells)
            if not isinstance(spell, NO_POWER_SHUFFLE):
                new_power = self._mutate_normal(
                    int(spell.power), minimum=0, maximum=255
                )
                spell.set_power(int(max(0, min(255, new_power))))

            # Randomize hit rate (except for certain spells)
            if not isinstance(spell, NO_HIT_RATE_SHUFFLE):
                # Cap hit rate at 99 for instant KO spells so protection items work
                max_hit_rate = 99 if spell.check_ohko else 100
                new_hit_rate = self._mutate_normal(
                    int(spell.hit_rate), minimum=1, maximum=max_hit_rate
                )
                spell.set_hit_rate(new_hit_rate)

    def _randomize_equipment_properties(self) -> None:
        """Randomize equipment stats and buffs (excluding character allowances)."""
        from smrpgpatchbuilder.datatypes.spells.enums import TempStatBuff

        EQUIP_STATS = ["speed", "attack", "defense", "magic_attack", "magic_defense"]
        PRIMARY_STATS_BY_TYPE = {
            Weapon: ["attack"],
            Armor: ["defense", "magic_defense"],
            Accessory: ["speed"],
        }

        for item in self.items.items:
            if not isinstance(item, (Weapon, Armor, Accessory)):
                continue

            # Get primary stats for this item type
            primary_stats = []
            for item_type, stats in PRIMARY_STATS_BY_TYPE.items():
                if isinstance(item, item_type):
                    primary_stats = stats
                    break

            # Calculate stat point value (similar to old logic)
            stat_point_value = 0
            for attr in EQUIP_STATS:
                val = getattr(item, attr, 0)
                if val > 0:
                    if attr in primary_stats:
                        stat_point_value += val
                    else:
                        stat_point_value += val * 2

            # Randomize number of attributes to go up or down
            # 1/3 chance all non-zero stats go up
            ups: list[str] = []
            if random.randint(1, 3) == 1:
                ups = [attr for attr in EQUIP_STATS if getattr(item, attr, 0) > 0]

            if not ups:
                num_up = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 10, 5, 1])[0]
                while True:
                    ups = random.sample(EQUIP_STATS, num_up)
                    if set(ups) & set(primary_stats):
                        break

            # Attributes going down (1/3 chance all negative stats go down)
            if random.randint(1, 3) == 1:
                downs = [attr for attr in EQUIP_STATS if getattr(item, attr, 0) < 0]
            else:
                num_down = random.choices(
                    [0, 1, 2, 3, 4, 5], weights=[1, 5, 10, 10, 5, 1]
                )[0]
                downs = random.sample(EQUIP_STATS, num_down)

            # Priority to going up
            downs = [d for d in downs if d not in ups]

            # Track increases and decreases
            score = stat_point_value
            up_vals = {u: 0 for u in ups}
            down_vals = {d: 0 for d in downs}

            # Distribute down points
            if downs:
                if score != 0:
                    down_points = random.randint(0, random.randint(0, score))
                else:
                    down_points = random.randint(
                        0, random.randint(0, random.randint(0, 100))
                    )
                score += down_points
                for _ in range(down_points):
                    attr = random.choice(downs)
                    down_vals[attr] += 1

            # Distribute up points
            while score > 0:
                attr = random.choice(ups)
                up_vals[attr] += 1
                if attr in primary_stats:
                    score -= 1
                else:
                    score -= 2

            # Zero all stats
            for attr in EQUIP_STATS:
                setter = getattr(item, f"set_{attr}")
                setter(0)

            # Set new positive stats with mutation
            for attr in up_vals:
                val = self._mutate_normal(up_vals[attr], minimum=1, maximum=127)
                setter = getattr(item, f"set_{attr}")
                setter(val)

            # Set new negative stats with mutation
            for attr in down_vals:
                val = self._mutate_normal(down_vals[attr], minimum=1, maximum=127)
                setter = getattr(item, f"set_{attr}")
                setter(-val)

            # If weapon with variance, shuffle that too
            if isinstance(item, Weapon) and item.variance > 0:
                new_variance = self._mutate_normal(
                    int(item.variance), minimum=1, maximum=127
                )
                item.set_variance(new_variance)

            # Randomize special properties based on tier
            # Determine tier based on item price (rough approximation)
            price = item.price
            if price <= 50:
                tier = 1
            elif price <= 150:
                tier = 2
            elif price <= 400:
                tier = 3
            elif price <= 1000:
                tier = 4
            else:
                tier = 5

            odds_map = {1: 2 / 3, 2: 1 / 2, 3: 1 / 4, 4: 1 / 8, 5: 3 / 32}
            odds = odds_map.get(tier, 0) / 2  # Halved as per 7.1.3 update

            if odds > 0:
                # Instant KO protection
                ko_odds = odds
                if isinstance(item, Weapon):
                    ko_odds /= 2
                item.set_prevent_ko(random.random() < ko_odds)

                # Elemental immunities/resistances
                item.set_elemental_immunities([])
                item.set_elemental_resistances([])
                elements = [Element.ICE, Element.FIRE, Element.THUNDER]
                if random.randint(1, 2) == 1:
                    for elem in elements:
                        if random.random() < odds:
                            item.append_elemental_immunity(elem)
                        elif random.random() < odds:
                            item.append_elemental_resistance(elem)
                else:
                    for elem in elements:
                        if random.random() < odds:
                            item.append_elemental_resistance(elem)
                        elif random.random() < odds:
                            item.append_elemental_immunity(elem)

                # Status immunities
                item.set_status_immunities([])
                status_list = [
                    Status.MUTE,
                    Status.SLEEP,
                    Status.POISON,
                    Status.FEAR,
                    Status.MUSHROOM,
                    Status.SCARECROW,
                ]
                for status in status_list:
                    if random.random() < odds:
                        item.append_status_immunity(status)

                # Temp buffs (weighted toward accessories/armor)
                buff_odds = odds
                if isinstance(item, Weapon):
                    buff_odds /= 2
                elif isinstance(item, Armor):
                    buff_odds /= 5
                item.set_temp_buffs([])
                buffs = [
                    TempStatBuff.ATTACK,
                    TempStatBuff.DEFENSE,
                    TempStatBuff.MAGIC_ATTACK,
                    TempStatBuff.MAGIC_DEFENSE,
                ]
                for buff in buffs:
                    if random.random() < buff_odds:
                        item.append_temp_buff(buff)

    def _randomize_equipment_characters(
        self, setting: EquipmentCharactersOptions
    ) -> None:
        """Randomize which characters can equip each piece of equipment."""
        ALL_CHARS = [
            PartyCharacter(i) for i in range(5)
        ]  # Mario=0, Mallow=1, Geno=2, Bowser=3, Peach=4

        for item in self.items.items:
            if not isinstance(item, (Weapon, Armor, Accessory)):
                continue

            if setting == EquipmentCharactersOptions.EQUIP_ALL:
                # Anyone can equip anything
                item.set_equip_chars(list(ALL_CHARS))

            elif setting == EquipmentCharactersOptions.VANILLA_ACCESSORIES_ALL:
                # Only accessories get all chars
                if isinstance(item, Accessory):
                    item.set_equip_chars(list(ALL_CHARS))
                # Weapons and armor keep vanilla (no change needed)

            elif setting == EquipmentCharactersOptions.RANDOM_ACCESSORIES_ALL:
                if isinstance(item, Accessory):
                    # All accessories can be equipped by anyone
                    item.set_equip_chars(list(ALL_CHARS))
                else:
                    # Weapons and armor get randomized
                    self._randomize_single_equip_chars(item, ALL_CHARS)

            elif setting == EquipmentCharactersOptions.RANDOM:
                # Everything gets randomized
                self._randomize_single_equip_chars(item, ALL_CHARS)

    def _randomize_single_equip_chars(
        self, item: Equipment, all_chars: list[PartyCharacter]
    ) -> None:
        """Randomize equippable characters for a single item."""
        # Pick random number of characters with lower numbers weighted heavier
        num_equippable = random.randint(1, random.randint(1, 5))
        new_chars: set[PartyCharacter] = set()

        for _ in range(num_equippable):
            char_choices = set(all_chars) - new_chars
            if not char_choices:
                break
            new_chars.add(random.choice(list(char_choices)))

        item.set_equip_chars(list(new_chars))

    def _shuffle_shops(self) -> None:
        """Shuffle the contents of all shops based on settings."""
        from smrpgpatchbuilder.datatypes.spells.enums import TempStatBuff
        from randomizer.data.items.items import GoodieBagItem, PickMeUpItem

        quality = self.settings.get_flag(ShopQuality).selected
        bias_enabled = self.settings.isflag_enabled(BiasShopShuffle)
        no_pickmeups = self.settings.isflag_enabled(NoPickMeUps)
        free_shops = self.settings.isflag_enabled(FreeShops)

        # Define shop indices for special handling
        FROG_DISCIPLE_SHOP = SH03_FROG_DISCIPLE
        FROG_COIN_EMPORIUM = SH06_FROG_COIN_EMPORIUM
        JUICE_BAR_BASE = SH09_JUICE_BAR_BASE
        JUICE_BAR_ALTO = SH10_JUICE_BAR_ALTO
        JUICE_BAR_TENOR = SH11_JUICE_BAR_TENOR
        JUICE_BAR_SOPRANO = SH12_JUICE_BAR_SOPRANO

        # Get the items from Frog Disciple prize locations (already shuffled)
        frog_disciple_items: list[type[BaseItem] | None] = []
        frog_disciple_locations = [
            FrogDiscipleLocation1,
            FrogDiscipleLocation2,
            FrogDiscipleLocation3,
            FrogDiscipleLocation4,
            FrogDiscipleLocation5,
        ]
        for loc_type in frog_disciple_locations:
            loc = self.locations.get(loc_type)
            if loc and loc.prize:
                # Get the item type from the prize
                from .prize import ItemPrize

                if isinstance(loc.prize, ItemPrize):
                    prize_item = loc.prize.item
                    if prize_item:
                        frog_disciple_items.append(prize_item)

        # Set Frog Disciple shop contents (don't shuffle into it)
        self.shops.shops[FROG_DISCIPLE_SHOP].set_items(frog_disciple_items)

        # Define should_get_better_items shops
        should_get_better_items = [
            SH06_FROG_COIN_EMPORIUM,
            SH08_SEASIDE_TOWN_MINION,
            SH11_JUICE_BAR_TENOR,
            SH12_JUICE_BAR_SOPRANO,
            SH13_SEASIDE_WEAPON,
            SH14_SEASIDE_ARMOR,
            SH15_SEASIDE_ACCESSORY,
            SH16_SEASIDE_HEALTH_FOOD,
            SH23_KEEP_2,
            SH24_FACTORY_TOAD,
        ]
        if not self.settings.is_flag_value(SeaGate, SeaGating.OPEN):
            should_get_better_items.append(SH07_SEA_AND_SHIP_SHAMAN)
        if not self.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
            should_get_better_items.extend([SH17_MONSTRO, SH20_GOOMBETTE])
        if not self.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
            should_get_better_items.extend([SH18_VOLCANO_ITEM, SH19_VOLCANO_ARMOR])
        if self.settings.is_flag_value(NimbusGate, NimbusGating.MEGASMILAX):
            should_get_better_items.append(SH21_NIMBUS_LAND)
        if not self.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
            should_get_better_items.extend([SH22_KEEP_1])

        # Define consumable item pools
        low_impact_items: list[type[RegularItem]] = [
            MushroomItem,
            HoneySyrupItem,
            AbleJuiceItem,
            BracerItem,
            EnergizerItem,
            YoshiCookieItem,
            PureWaterItem,
            SleepyBombItem,
            BadMushroomItem,
            FlowerTabItem,
            FroggieDrinkItem,
            MukuCookieItem,
            FreshenUpItem,
            FrightBombItem,
            WiltShroomItem,
            RottenMushItem,
            MoldyMushItem,
            MushroomItem2,
        ]
        if not no_pickmeups:
            low_impact_items.append(PickMeUpItem)

        high_impact_items: list[type[RegularItem]] = [
            MidMushroomItem,
            MaxMushroomItem,
            MapleSyrupItem,
            RoyalSyrupItem,
            YoshiAdeItem,
            FireBombItem,
            IceBombItem,
            YoshiCandyItem,
            ElixirItem,
            MegalixirItem,
            CrystallineItem,
            PowerBlastItem,
        ]

        highest_impact_items: list[type[RegularItem]] = [
            RedEssenceItem,
            KerokeroColaItem,
            RockCandyItem,
        ]

        # Calculate equipment rank values and categorize them
        def calc_equip_rank(item: Equipment) -> float:
            variance = int(item.variance) if isinstance(item, Weapon) else 0
            attack = item.attack
            attack_base = attack - variance if attack - variance != 0 else 1
            attack_variance_factor = (
                min(2, (attack + variance) / attack_base) if attack > 0 else 0
            )

            rank = (
                attack * max(0, attack_variance_factor)
                + max(
                    0,
                    (item.magic_attack / (2 if item.magic_attack < 0 else 1))
                    + (item.magic_defense / (2 if item.magic_defense < 0 else 1))
                    + (item.defense / (2 if item.defense < 0 else 1))
                    + min(20, item.speed / 2),
                )
                + 10 * len(item.status_immunities)
                + 15 * len(item.elemental_immunities)
                + 7.5 * len(item.elemental_resistances)
                + 50 * (1 if item.prevent_ko else 0)
                + 30 * len(item.temp_buffs)
            )
            return rank

        # Get all equipment and sort by rank
        all_equipment = [
            i for i in self.items.items if isinstance(i, (Weapon, Armor, Accessory))
        ]
        equipment_ranks = [(type(e), calc_equip_rank(e)) for e in all_equipment]
        equipment_ranks.sort(key=lambda x: x[1], reverse=True)

        # Categorize equipment: top 20% = highest, next 30% = high, bottom 50% = low
        total_equip = len(equipment_ranks)
        highest_cutoff = int(total_equip * 0.2)
        high_cutoff = int(total_equip * 0.5)

        highest_impact_equip = [e[0] for e in equipment_ranks[:highest_cutoff]]
        high_impact_equip = [e[0] for e in equipment_ranks[highest_cutoff:high_cutoff]]
        low_impact_equip = [e[0] for e in equipment_ranks[high_cutoff:]]

        # Get original shop item types for each shop (for type restrictions)
        original_shop_data: dict[int, dict] = {}
        for shop in self.shops.shops:
            if shop is None:
                continue
            orig_items = [i for i in shop.items if i is not None]
            original_shop_data[shop.index] = {
                "has_weapon": any(issubclass(i, Weapon) for i in orig_items),
                "has_armor": any(issubclass(i, Armor) for i in orig_items),
                "has_accessory": any(issubclass(i, Accessory) for i in orig_items),
                "has_consumable": any(
                    not issubclass(i, (Weapon, Armor, Accessory)) for i in orig_items
                ),
                "original_items": orig_items,
                "original_count": len(orig_items),
            }

        # Handle EMPTY mode: only GoodieBag in every shop
        if quality == ShopQualities.EMPTY:
            for shop in self.shops.shops:
                if shop is None:
                    continue
                shop.set_items([GoodieBagItem])
            return

        # Build item pools based on quality setting
        def get_item_pool(
            quality: ShopQualities, is_equipment: bool = False
        ) -> tuple[list, list, list]:
            """Returns (low, high, highest) pools based on quality."""
            if is_equipment:
                if quality == ShopQualities.ORIGINAL:
                    # Only equipment that was originally in shops
                    orig_equip_in_shops: set = set()
                    for shop in self.shops.shops:
                        if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                            continue
                        for item in shop.items:
                            if item and issubclass(item, (Weapon, Armor, Accessory)):
                                orig_equip_in_shops.add(item)
                    return (
                        [e for e in low_impact_equip if e in orig_equip_in_shops],
                        [e for e in high_impact_equip if e in orig_equip_in_shops],
                        [e for e in highest_impact_equip if e in orig_equip_in_shops],
                    )
                elif quality == ShopQualities.MOSTLY_RANDOM:
                    return (low_impact_equip, high_impact_equip, [])
                else:  # COMPLETELY_RANDOM
                    return (low_impact_equip, high_impact_equip, highest_impact_equip)
            else:
                if quality == ShopQualities.ORIGINAL:
                    # Only consumables that were originally in shops
                    orig_in_shops: set = set()
                    for shop in self.shops.shops:
                        if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                            continue
                        for item in shop.items:
                            if item and not issubclass(
                                item, (Weapon, Armor, Accessory)
                            ):
                                orig_in_shops.add(item)
                    return (
                        [i for i in low_impact_items if i in orig_in_shops],
                        [i for i in high_impact_items if i in orig_in_shops],
                        [i for i in highest_impact_items if i in orig_in_shops],
                    )
                elif quality == ShopQualities.MOSTLY_RANDOM:
                    return (low_impact_items, high_impact_items, [])
                else:  # COMPLETELY_RANDOM
                    return (low_impact_items, high_impact_items, highest_impact_items)

        low_consumables, high_consumables, highest_consumables = get_item_pool(
            quality, is_equipment=False
        )
        low_equip, high_equip, highest_equip = get_item_pool(quality, is_equipment=True)

        # Remove Pick Me Ups if setting enabled
        if no_pickmeups:
            low_consumables = [i for i in low_consumables if i != PickMeUpItem]
            high_consumables = [i for i in high_consumables if i != PickMeUpItem]
            highest_consumables = [i for i in highest_consumables if i != PickMeUpItem]

        # Track items placed in Frog Coin Emporium (cannot appear elsewhere)
        frog_emporium_items: set = set()
        # Track items placed in Frog Disciple (can only also appear in Frog Coin Emporium)
        frog_disciple_set = set(frog_disciple_items)

        def can_place_item(
            item_type: type[BaseItem] | None, shop_idx: int, current_items: list
        ) -> bool:
            """Check if an item can be placed in a shop."""
            if item_type is None:
                return False
            # No duplicates in same shop
            if item_type in current_items:
                return False
            # Items in Frog Coin Emporium can't appear elsewhere
            if item_type in frog_emporium_items and shop_idx != FROG_COIN_EMPORIUM:
                return False
            # Items in Frog Disciple can only also appear in Frog Coin Emporium
            if item_type in frog_disciple_set and shop_idx not in [
                FROG_DISCIPLE_SHOP,
                FROG_COIN_EMPORIUM,
            ]:
                return False
            # Check type restrictions
            shop_data = original_shop_data.get(shop_idx, {})
            if issubclass(item_type, Weapon) and not shop_data.get("has_weapon", False):
                return False
            if issubclass(item_type, Armor) and not shop_data.get("has_armor", False):
                return False
            if issubclass(item_type, Accessory) and not shop_data.get(
                "has_accessory", False
            ):
                return False
            if not issubclass(
                item_type, (Weapon, Armor, Accessory)
            ) and not shop_data.get("has_consumable", False):
                return False
            return True

        def select_item(
            shop_idx: int, current_items: list, prefer_high: bool = False
        ) -> type[BaseItem] | None:
            """Select an item for a shop based on bias and availability."""
            is_better_shop = shop_idx in should_get_better_items

            # Build weighted pool
            candidates = []
            weights = []

            # Combine consumables and equipment pools
            all_low = low_consumables + low_equip
            all_high = high_consumables + high_equip
            all_highest = highest_consumables + highest_equip

            if bias_enabled:
                if is_better_shop:
                    # Better shops: favor high/highest impact
                    for item in all_highest:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(5)
                    for item in all_high:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(3)
                    for item in all_low:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(1)
                else:
                    # Other shops: favor low impact
                    for item in all_low:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(5)
                    for item in all_high:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(1)
                    # Significantly less likely for highest
                    for item in all_highest:
                        if can_place_item(item, shop_idx, current_items):
                            candidates.append(item)
                            weights.append(0.2)
            else:
                # No bias: equal weights
                for item in all_low + all_high + all_highest:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(1)

            if not candidates:
                return None

            return random.choices(candidates, weights=weights, k=1)[0]

        # Process each shop (except Frog Disciple which is already set)
        shops_to_process = [
            s
            for s in self.shops.shops
            if s is not None and s.index != FROG_DISCIPLE_SHOP
        ]

        # Process Frog Coin Emporium first (its items are exclusive)
        frog_emporium_shop = self.shops.shops[FROG_COIN_EMPORIUM]
        if frog_emporium_shop:
            shop_data = original_shop_data.get(FROG_COIN_EMPORIUM, {})
            target_count = min(15, max(1, shop_data.get("original_count", 5)))
            emporium_new_items: list[type[BaseItem] | None] = []

            for _ in range(target_count):
                item = select_item(
                    FROG_COIN_EMPORIUM, emporium_new_items, prefer_high=True
                )
                if item:
                    emporium_new_items.append(item)
                    frog_emporium_items.add(item)

            frog_emporium_shop.set_items(emporium_new_items)

        # Handle Juice Bar hierarchy (BASE < ALTO < TENOR < SOPRANO)
        juice_bars = [
            JUICE_BAR_BASE,
            JUICE_BAR_ALTO,
            JUICE_BAR_TENOR,
            JUICE_BAR_SOPRANO,
        ]
        juice_bar_items: dict[int, list[type[BaseItem] | None]] = {}

        for i, bar_idx in enumerate(juice_bars):
            shop = self.shops.shops[bar_idx]
            if shop is None:
                continue

            shop_data = original_shop_data.get(bar_idx, {})

            if i == 0:
                # BASE: start fresh
                target_count = max(1, shop_data.get("original_count", 1))
                bar_new_items: list[type[BaseItem] | None] = []
                for _ in range(target_count):
                    item = select_item(bar_idx, bar_new_items)
                    if item:
                        bar_new_items.append(item)
                juice_bar_items[bar_idx] = bar_new_items
            else:
                # Must be superset of previous (but not same)
                prev_items = list(juice_bar_items.get(juice_bars[i - 1], []))
                bar_new_items = list(prev_items)  # Start with previous items
                # Add at least one more item
                added = 0
                attempts = 0
                while added < 1 and attempts < 50:
                    item = select_item(bar_idx, bar_new_items)
                    if item and item not in bar_new_items:
                        bar_new_items.append(item)
                        added += 1
                    attempts += 1
                # Try to add more up to original count or 15
                target_extra = min(
                    15 - len(bar_new_items),
                    shop_data.get("original_count", len(bar_new_items))
                    - len(prev_items),
                )
                for _ in range(max(0, target_extra - 1)):
                    item = select_item(bar_idx, bar_new_items)
                    if item and item not in bar_new_items:
                        bar_new_items.append(item)
                juice_bar_items[bar_idx] = bar_new_items

            shop.set_items(juice_bar_items[bar_idx])

        # Process remaining shops
        processed = {FROG_DISCIPLE_SHOP, FROG_COIN_EMPORIUM} | set(juice_bars)
        for shop in shops_to_process:
            if shop.index in processed:
                continue

            shop_data = original_shop_data.get(shop.index, {})
            target_count = min(15, max(1, shop_data.get("original_count", 5)))
            shop_new_items: list[type[BaseItem] | None] = []

            for _ in range(target_count):
                item = select_item(shop.index, shop_new_items)
                if item:
                    shop_new_items.append(item)

            if shop_new_items:
                shop.set_items(shop_new_items)
            elif quality == ShopQualities.ORIGINAL:
                # If no items could be placed in ORIGINAL mode, discard
                shop.set_items([])

        # Guarantee Pick Me Ups appear in at least one shop if not disabled
        if not no_pickmeups:
            # Check if any shop contains Pick Me Up
            has_pickmeup = False
            for shop in self.shops.shops:
                if shop is not None and PickMeUpItem in (shop.items or []):
                    has_pickmeup = True
                    break

            if not has_pickmeup:
                # Find shops that can have consumables and have room
                eligible_shops = []
                for shop in self.shops.shops:
                    if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                        continue
                    shop_data = original_shop_data.get(shop.index, {})
                    if shop_data.get("has_consumable", False):
                        current_items = shop.items or []
                        if (
                            len(current_items) < 15
                            and PickMeUpItem not in current_items
                        ):
                            eligible_shops.append(shop)

                if eligible_shops:
                    target_shop = random.choice(eligible_shops)
                    current_items: list[type[BaseItem] | None] = list(
                        target_shop.items or []
                    )
                    current_items.append(PickMeUpItem)
                    target_shop.set_items(current_items)

        # Apply FreeShops: set all non-zero prices to 1
        if free_shops:
            for item in self.items.items:
                if item.price > 0:
                    item.set_price(1)

        # Apply Frog Coin Emporium price reduction (divide by 5)
        for item_type in frog_emporium_items:
            item = self.items.get_by_type(item_type)
            if item and item.price > 0:
                item.set_price(max(1, item.price // 5))

    def _randomize_tadpole_pond(self) -> None:
        selection = random.sample(all_songs, 3)
        self.event_scripts.get_script_by_id(E1082_MELODY_BAY_SONG_1_INPUT).set_contents(
            selection[0].generate_input_script(0)
        )
        self.event_scripts.get_script_by_id(
            E1079_MELODY_BAY_SONG_1_VALIDATOR
        ).set_contents(selection[0].generate_playback_script(0))
        self.overworld_dialogs.replace_dialog(
            DI2718_SONG_1_SCROLL_HINT, selection[0].scroll_text
        )
        self.overworld_dialogs.replace_dialog(
            DI2664_TADPOLE_SONG_1_HINT, selection[0].apprentice_hint_1
        )

        self.event_scripts.get_script_by_id(E1083_MELODY_BAY_SONG_2_INPUT).set_contents(
            selection[1].generate_input_script(1)
        )
        self.event_scripts.get_script_by_id(
            E1080_MELODY_BAY_SONG_2_VALIDATOR
        ).set_contents(selection[1].generate_playback_script(1))
        self.overworld_dialogs.replace_dialog(
            DI2665_TADPOLE_SONG_2_HINT, selection[1].apprentice_hint_2
        )
        self.overworld_dialogs.replace_dialog(
            DI1615_MOLEVILLE_BLUES_8, selection[1].mole_hint
        )
        self.event_scripts.get_script_by_id(E3132_MOLEVILLE_MINERS_SONG).set_contents(
            [
                RunDialog(
                    DI1615_MOLEVILLE_BLUES_8,
                    NPC_0,
                    closable=True,
                    sync=False,
                    multiline=True,
                    use_background=True,
                ),
                Return(),
            ]
        )

        self.event_scripts.get_script_by_id(E1084_MELODY_BAY_SONG_3_INPUT).set_contents(
            selection[2].generate_input_script(2)
        )
        self.event_scripts.get_script_by_id(
            E1081_MELODY_BAY_SONG_3_VALIDATOR
        ).set_contents(selection[2].generate_playback_script(2))
        cast(
            ActionQueueAsync,
            self.event_scripts.get_command_by_identifier("starfish_dance_hint"),
        ).set_subscript(
            selection[2].generate_starfish_hint(
                cast(
                    ActionQueueAsync,
                    self.event_scripts.get_script_by_id(E2061_MONSTRO_TOWN_STAR),
                ).subscript.contents
            )
        )
        self.event_scripts.get_script_by_id(
            E1088_MELODY_BAY_THIRD_SONG_HINT
        ).set_contents(selection[2].generate_tadpole_hint())

        self.song_1 = selection[0].scroll_text
        self.song_2 = selection[1].scroll_text
        self.song_3 = selection[2].scroll_text

        self.song_authors = list(
            set(
                selection[0].submitter_credits
                + selection[1].submitter_credits
                + selection[2].submitter_credits
            )
        )

    def _randomize_password(self) -> None:
        password = random.choice(password_pool)
        self.password = password.word
        decoy_word = random.choice([p for p in password_pool if p != password])
        correct_positions = []

        # create password submission logic
        for index, letter in enumerate(list(password.word)):
            letters = suggest_letter_bank(password.word, index, decoy_word.word)
            correct_position = letters.index(password.word[index])
            correct_positions.append(correct_position)

            # generate the dialogs that display your letter selection when you stand under the boxes
            box_dialogs = []
            box_dialogs.append(
                """[page]\n Key letter%i  <%s> %s  %s  %s  %s[end]"""
                % (
                    index + 1,
                    letters[0],
                    letters[1],
                    letters[2],
                    letters[3],
                    letters[4],
                )
            )
            box_dialogs.append(
                """[page]\n Key letter%i   %s <%s> %s  %s  %s[end]"""
                % (
                    index + 1,
                    letters[0],
                    letters[1],
                    letters[2],
                    letters[3],
                    letters[4],
                )
            )
            box_dialogs.append(
                """[page]\n Key letter%i   %s  %s <%s> %s  %s[end]"""
                % (
                    index + 1,
                    letters[0],
                    letters[1],
                    letters[2],
                    letters[3],
                    letters[4],
                )
            )
            box_dialogs.append(
                """[page]\n Key letter%i   %s  %s  %s <%s> %s[end]"""
                % (
                    index + 1,
                    letters[0],
                    letters[1],
                    letters[2],
                    letters[3],
                    letters[4],
                )
            )
            box_dialogs.append(
                """[page]\n Key letter%i   %s  %s  %s  %s <%s>[end]"""
                % (
                    index + 1,
                    letters[0],
                    letters[1],
                    letters[2],
                    letters[3],
                    letters[4],
                )
            )
            box_dialog_pairs = zip(box_dialogs, box_dialog_ids[index])
            for dialog_content, dialog_id in box_dialog_pairs:
                self.overworld_dialogs.replace_dialog(dialog_id, dialog_content)
            recitation_pairs = zip(letters, recitation_ids[index])
            for letter, dialog_id in recitation_pairs:
                self.overworld_dialogs.replace_dialog(dialog_id, """%s[end]""" % letter)

        # calibrate correctness checker
        self.event_scripts.get_script_by_id(
            E3411_SHIP_PASSWORD_CORRECTNESS_CHECK
        ).set_contents(
            [
                JmpIfVarNotEqualsConst(
                    SECONDARY_TEMP_7024, correct_positions[0], ["ship_password_check_2"]
                ),
                Inc(TEMP_70AC),
                JmpIfVarNotEqualsConst(
                    TEMP_7026,
                    correct_positions[1],
                    ["ship_password_check_3"],
                    identifier="ship_password_check_2",
                ),
                Inc(TEMP_70AC),
                JmpIfVarNotEqualsConst(
                    TEMP_7028,
                    correct_positions[2],
                    ["ship_password_check_4"],
                    identifier="ship_password_check_3",
                ),
                Inc(TEMP_70AC),
                JmpIfVarNotEqualsConst(
                    TEMP_702A,
                    correct_positions[3],
                    ["ship_password_check_5"],
                    identifier="ship_password_check_4",
                ),
                Inc(TEMP_70AC),
                JmpIfVarNotEqualsConst(
                    TEMP_702C,
                    correct_positions[4],
                    ["ship_password_check_6"],
                    identifier="ship_password_check_5",
                ),
                Inc(TEMP_70AC),
                JmpIfVarNotEqualsConst(
                    TEMP_702E,
                    correct_positions[5],
                    ["ship_password_check_end"],
                    identifier="ship_password_check_6",
                ),
                Inc(TEMP_70AC),
                Return(identifier="ship_password_check_end"),
            ]
        )

        # populate hint dialogs
        random.shuffle(hint_authors)
        # guarantee that the hint submitter will get their name on one of the hints
        writers = [password.submitter_hint_prefix] + hint_authors
        RWRITER = "%RANDOM_WRITER%"
        number_of_writers = len(
            [
                h
                for h in [
                    password.troopa_hint,
                    password.trampoline_hint,
                    password.maze_hint,
                    password.snake_hint,
                    password.cannonball_hint,
                    password.barrel_hint,
                    password.entrance_hint,
                    password.saveroom_hint,
                    password.greaper_hint_2,
                    password.greaper_hint,
                    password.drybones_hint,
                ]
                if h is not None and RWRITER in h
            ]
        )
        writers = writers[:number_of_writers]
        random.shuffle(writers)
        for s in writers:
            if RWRITER in password.troopa_hint:
                password.troopa_hint = password.troopa_hint.replace(RWRITER, s)
                continue
            if RWRITER in password.trampoline_hint:
                password.trampoline_hint = password.trampoline_hint.replace(RWRITER, s)
                continue
            if RWRITER in password.maze_hint:
                password.maze_hint = password.maze_hint.replace(RWRITER, s)
                continue
            if RWRITER in password.snake_hint:
                password.snake_hint = password.snake_hint.replace(RWRITER, s)
                continue
            if RWRITER in password.cannonball_hint:
                password.cannonball_hint = password.cannonball_hint.replace(RWRITER, s)
                continue
            if RWRITER in password.barrel_hint:
                password.barrel_hint = password.barrel_hint.replace(RWRITER, s)
                continue
            if password.entrance_hint and RWRITER in password.entrance_hint:
                password.entrance_hint = password.entrance_hint.replace(RWRITER, s)
                continue
            if password.saveroom_hint and RWRITER in password.saveroom_hint:
                password.saveroom_hint = password.saveroom_hint.replace(RWRITER, s)
                continue
            if password.greaper_hint and RWRITER in password.greaper_hint:
                password.greaper_hint = password.greaper_hint.replace(RWRITER, s)
                continue
            if password.greaper_hint_2 and RWRITER in password.greaper_hint_2:
                password.greaper_hint_2 = password.greaper_hint_2.replace(RWRITER, s)
                continue
            if password.drybones_hint and RWRITER in password.drybones_hint:
                password.drybones_hint = password.drybones_hint.replace(RWRITER, s)
                continue
        self.overworld_dialogs.replace_dialog(
            DI1664_TROOPA_PUZZLE_HINT, password.troopa_hint
        )
        self.overworld_dialogs.replace_dialog(
            DI1665_TRAMPOLINE_PUZZLE_HINT, password.trampoline_hint
        )
        self.overworld_dialogs.replace_dialog(
            DI1666_MAZE_PUZZLE_HINT, password.maze_hint
        )
        self.overworld_dialogs.replace_dialog(
            DI1667_SNAKE_PUZZLE_HINT, password.snake_hint
        )
        self.overworld_dialogs.replace_dialog(
            DI1668_CANNONBALL_PUZZLE_HINT, password.cannonball_hint
        )
        self.overworld_dialogs.replace_dialog(
            DI1669_BARREL_PUZZLE_HINT, password.barrel_hint
        )
        if password.entrance_hint is not None:
            self.overworld_dialogs.replace_dialog(
                DI1673_SHIP_ENTRANCE_NOTE, password.entrance_hint
            )
        if password.saveroom_hint is not None:
            self.overworld_dialogs.replace_dialog(
                DI1674_SHIP_SAVEROOM_NOTE, password.saveroom_hint
            )
        if password.greaper_hint is not None:
            self.overworld_dialogs.replace_dialog(
                DI1675_SHIP_GREAPER_1_NOTE, password.greaper_hint
            )
        if password.greaper_hint_2 is not None:
            self.overworld_dialogs.replace_dialog(
                DI1676_SHIP_GREAPER_2_NOTE, password.greaper_hint_2
            )
        if password.drybones_hint is not None:
            self.overworld_dialogs.replace_dialog(
                DI1656_SLEEPING_DRY_BONES, password.drybones_hint
            )

        self.password_author = password.submitter_credits

    def get_patch(self) -> Patch:
        patch = Patch()

        # Battle animations patch
        for animation_bank in self.battle_animations.values():
            patches = animation_bank.render()
            for p in patches:
                patch.add_data(p[0], p[1])

        # Event scripts patch
        for event_script_bank in self.event_scripts.banks:
            patch.add_data(event_script_bank.start, event_script_bank.render())

        # Monster AI scripts patch
        monster_scripts = self.monster_scripts.render()
        patch.add_data(self.monster_scripts.pointer_table_start, monster_scripts[0])
        patch.add_data(self.monster_scripts.range_2_start, monster_scripts[1])

        # Sprite graphics patch
        for p in self.sprites.render():
            patch.add_data(p[0], p[1])

        # Dialogs, enemies, items, action scripts, packets, battle packs, rooms, shops, spells
        # Run all render() calls in parallel
        with ThreadPoolExecutor() as executor:
            futures = {
                "battle_dialogs": executor.submit(self.battle_dialogs.render),
                "overworld_dialogs": executor.submit(self.overworld_dialogs.render),
                "enemies": executor.submit(self.enemies.render),
                "enemy_attacks": executor.submit(self.enemy_attacks.render),
                "items": executor.submit(self.items.render),
                "action_scripts": executor.submit(self.action_scripts.render),
                "packets": executor.submit(self.packets.render),
                "battle_packs": executor.submit(self.battle_packs.render),
                "rooms": executor.submit(self.rooms.render),
                "shops": executor.submit(self.shops.render),
                "spells": executor.submit(self.spells.render),
                "allies": executor.submit(self.allies.render),
            }
            # Wait for all to complete and add results to patch
            patch.add_dict(futures["battle_dialogs"].result())
            patch.add_dict(futures["overworld_dialogs"].result())
            patch.add_dict(futures["enemies"].result())
            patch.add_dict(futures["enemy_attacks"].result())
            patch.add_dict(futures["items"].result())
            patch.add_data(
                self.action_scripts.start, futures["action_scripts"].result()
            )
            patch.add_dict(futures["packets"].result())
            patch.add_dict(futures["battle_packs"].result())
            patch.add_dict(futures["rooms"].result())
            patch.add_dict(futures["shops"].result())
            patch.add_dict(futures["spells"].result())
            patch.add_dict(futures["allies"].result())

        patch.add_dict(update_credits(self))

        # Misc

        # Expand key item inventory size
        patch.add_data(0xC305, 0x20)
        patch.add_data(0xC37F, 0x20)
        patch.add_data(
            0xC3B5, 0x20
        )  # TODO might need to be larger than 0x20, recount key items
        patch.add_data(0xC302, [0xF0, 0xF8])
        patch.add_data(0xC37C, [0xF0, 0xF8])
        patch.add_data(0xC3B2, [0xF0, 0xF8])
        patch.add_data(0x2BC80, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BC95, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCA1, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x2BCB6, [0xF0, 0xF8, 0x7F])
        patch.add_data(0x353080, [0xF0, 0xF8, 0x7F])

        if self.settings.isflag_enabled(ShowEquips):
            patch.add_data(0x033B6D, bytes([0x29, 0x1F, 0xEA]))

        # Battle music IDs - write 8 selected music IDs to the music pointer table
        if self.selected_music_ids:
            patch.add_data(0x029F51, bytes(self.selected_music_ids))

        # Postgame weapon palettes
        patch.add_data(
            0x25894C,
            bytes.fromhex(
                "7B 37 BD 33 39 33 F7 2E F7 2A F7 22 31 26 52 22 DE 53 10 1E 8C 15 4A 15 08 11 C6 0C 63 0C"
            ),
        )
        patch.add_data(
            0x25896A,
            bytes.fromhex(
                "BD 6B BD 6B 5B 47 39 3B 95 1A D7 1E 74 1A EF 15 6C 0D 09 09 A6 04 A6 04 84 04 FF 7B 63 0C"
            ),
        )
        patch.add_data(
            0x25DEE4,
            bytes.fromhex(
                "FF 7F F5 7F EA 7F E0 7F 40 7F 80 7E E0 7D 20 7D 00 69 C0 58 A0 44 60 30 40 20 00 0C 00 00"
            ),
        )

        if self.settings.isflag_enabled(HoldB):
            # hold B to advance
            patch.add_data(0x5D5E, [0x20, 0x54, 0xF1])
            patch.add_data(0x15627, [0x22, 0x90, 0xFE, 0xC2, 0x89, 0x80, 0x00])
            patch.add_data(0xF154, [0x22, 0x90, 0xFE, 0xC2, 0x60])
            patch.add_data(
                0x2FE90, [0xAF, 0x14, 0x30, 0x00, 0x0F, 0x11, 0x30, 0x00, 0x6B]
            )

        # Palettes

        if self.main_character == MARIO_Ally:
            for i, p in self.mario_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.mario_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == MALLOW_Ally:
            for i, p in self.mallow_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.mallow_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == GENO_Ally:
            for i, p in self.geno_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.geno_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == BOWSER_Ally:
            for i, p in self.bowser_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.bowser_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        if self.main_character == TOADSTOOL_Ally:
            for i, p in self.toadstool_palette.doll_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.minecart_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.classic_patch().items():
                patch.add_data(i, p)
            for i, p in self.toadstool_palette.overworld_map_patch().items():
                patch.add_data(i, p)
        patch.add_dict(self.mario_palette.standard_patch())
        patch.add_dict(self.mallow_palette.standard_patch())
        patch.add_dict(self.geno_palette.standard_patch())
        patch.add_dict(self.bowser_palette.standard_patch())
        patch.add_dict(self.toadstool_palette.standard_patch())

        if self.settings.isflag_enabled(JapaneseABXY):
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

        starter = cast(CharacterPrize, self.get_location(StartingCharacter1).prize).ally
        i = starter.index
        file_select_char_bytes = [
            SPR0000_MARIO_WALKING_DOWN_LEFT,
            SPR0007_TOADSTOOL_WALKING_DOWN_LEFT,
            SPR0013_BOWSER_WALKING_DOWN_LEFT,
            SPR0025_GENO_WALKING_DOWN_LEFT,
            SPR0019_MALLOW_WALKING_DOWN_LEFT,
        ]
        self.file_select_character = starter.name

        # Change file select character graphic, if not Mario.
        if i != 0:
            addresses = [0x34757, 0x3489A, 0x34EE7, 0x340AA, 0x3501E]
            for addr, value in zip(addresses, [0, 1, 0, 0, 1]):
                patch.add_data(addr, file_select_char_bytes[i] + value)

        for i, name in enumerate(self.file_select_names):
            addr = 0x3EF528 + (i * 7)
            val = name.encode().ljust(7, b"\x00")
            patch.add_data(addr, val)

        # Update ROM title and version.
        title = "SMRPG-R {}".format(self.seed).ljust(20)
        if len(title) > 20:
            title = title[:19] + "?"

        # Add version number on name entry screen.
        version_text = ("v" + self.version).ljust(10)
        if len(version_text) > 10:
            raise ValueError("Version text is too long: {!r}".format(version_text))
        patch.add_data(0x3EF140, version_text)

        # Add title and major version number to SNES header data.
        patch.add_data(0x7FC0, title)
        v = self.version.split(".")
        patch.add_data(0x7FDB, int(v[0]))

        return patch
