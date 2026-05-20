# pyright: reportWildcardImportFromLibrary=false
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Type, TypeVar, cast
import json
import random
import hashlib
import re
from copy import copy, deepcopy
from concurrent.futures import ThreadPoolExecutor

from randomizer.data.nmi_hook import (
    NMI_HOOK_CODE,
    NMI_VECTOR_ROM_OFFSET,
    NMI_VECTOR_NEW,
    EMU_NMI_VECTOR_ROM_OFFSET,
    EMU_NMI_VECTOR_NEW,
    TRAMPOLINE_ROM_OFFSET,
    TRAMPOLINE_CODE,
    HOOK_ROM_OFFSET,
    NMITIMEN_PATCHES,
)
from randomizer.patches import asm
from randomizer.data.variables.sprite_palette_names import (
    SPAL293_ABXY_ACTION_BUTTON_SELECTION_IN_BATTLE,
    SPAL379_ABXY_BUTTONS_FROM_BOWYER_S_BUTTON_LOCK,
)
from randomizer.utils.tower_access_scripts import AddToInventory
from randomizer.logic.credits_palette_fix import (
    shift_palette_row_masks_for_ally_buffer_growth as _shift_palette_row_masks_for_ally_buffer_growth,
)

from .flags import *
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
)
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *
from smrpgpatchbuilder.datatypes.monster_scripts.types import (
    MonsterScriptBank,
    MonsterScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptController,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import (
    PacketCollection,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    PackCollection,
)
from smrpgpatchbuilder.datatypes.levels.room_collection import RoomCollection
from smrpgpatchbuilder.datatypes.shops.classes import ShopCollection
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection, AnimationBank
from smrpgpatchbuilder.datatypes.sprites.palette import (
    EventPaletteCollection,
    SpritePaletteCollection,
)
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    RunEventAsSubroutine,
    PaletteSet,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
    Formation,
)
from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection
from smrpgpatchbuilder.datatypes.world_map_locations.classes import (
    WorldMapLocationCollection,
)
from ..data.items.items import *
from .item import Item
from .patch import Patch
from .spell import Spell
from .prize import (
    ItemPrize,
    SpellPrize,
)
from .ally import Ally

# TypeVar for spell types to allow CharacterSpell and other Spell subclasses
SpellT = TypeVar("SpellT", bound=Spell)
from .prizelocation import (
    BoosterHillLocation,
    CharacterRecruitmentLocation,
    InvisibleFlagLocation,
    NPCLocationRow,
    PrizeLocation,
    SpellSlotLocation,
    StandingLocation,
    StarPieceLocation,
    TreasureChestLocation,
)
# ThreeMustyFears proxy classes come from prizelocations via the wildcard import below
from .room import Room
from ..progression.prizelocations import *
from ..data.variables.dialog_names import *
from ..data.variables.battle_variable_names import *
from ..data.variables.battle_effect_names import *
from ..data.variables.shop_names import *
from ..data.variables.sprite_names import *
from ..data.spells.spells import *
from ..data.credits.credits import update_credits
from ..logic.setup.pre_shuffler_settings import apply_shuffler_independent_settings
from ..logic.setup.thresholds import apply_threshold_settings
from ..logic.setup.enemy_tweaks import (
    apply_enemy_tweaks,
    apply_experience_zero_settings,
)
from ..logic.setup.equipment_setup import apply_equipment_settings
from ..logic.setup.minigames_setup import apply_minigame_settings
from ..logic.setup.cosmetics import apply_cosmetic_settings
from ..logic.setup.prize_locations import set_locations
from ..logic.shufflers.items import shuffle_prizes, post_shuffle_cleanup
from ..logic.validation import validate_settings
from ..logic.shufflers.shops import shuffle_shops, exclude_seeya_from_frog_disciple
from ..logic.shufflers.equipment import (
    build_item_to_prize_mapping,
    build_item_impact_categories,
)
from ..logic.shufflers.enemies import (
    randomize_enemy_attacks_and_spells,
    randomize_enemy_stats,
    randomize_enemy_drops,
    randomize_enemy_formations,
    apply_exp_multiplier,
)
from ..logic.shufflers.characters import (
    randomize_character_stats,
    randomize_levelup_xps,
    randomize_character_spell_stats,
)
from ..logic.apply import apply_shuffler_results_to_game_data

from ..data.allies.palettes.types import (
    MarioPalette,
    MallowPalette,
    GenoPalette,
    BowserPalette,
    ToadstoolPalette,
)
from ..data.allies.palettes.mario import MarioDefault
from ..data.allies.palettes.mallow import MallowDefault
from ..data.allies.palettes.geno import GenoDefault
from ..data.allies.palettes.bowser import BowserDefault
from ..data.allies.palettes.toadstool import ToadstoolDefault
from .enemy import Enemy
from ..data.enemies.enemies import DODOEnemy, SHELLYEnemy, RIGHTEYEEnemy

PrizeLocationT = TypeVar("PrizeLocationT", bound=PrizeLocation)
from .settings import Settings

if TYPE_CHECKING:
    from randomizer.logic.partition_calculator import VanillaRoomState


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
    spells: SpellCollection[Spell]
    sprites: SpriteCollection
    event_palettes: EventPaletteCollection
    sprite_palettes: SpritePaletteCollection
    mario_palette: MarioPalette = MarioDefault()
    mallow_palette: MallowPalette = MallowDefault()
    geno_palette: GenoPalette = GenoDefault()
    bowser_palette: BowserPalette = BowserDefault()
    toadstool_palette: ToadstoolPalette = ToadstoolDefault()
    main_character: Ally = MARIO_Ally
    file_select_character: str = "MARIO"
    world_map_locations: WorldMapLocationCollection
    password: str = "pearls"
    poison_mushroom_status: str | None = None
    song_1: str = "So La Mi Re Do Re Do Re"
    song_2: str = "Mi Do So Do Re La Ti Do"
    song_3: str = "La Ti Do Re So Do Re Mi"
    password_author: str = "ANONYMOUS"
    song_authors: list[str] = ["ANONYMOUS"]

    # Text-based shop items (set by shuffle_shops)
    room_service_items: list[type] = [PickMeUpItem, KerokeroColaItem]
    room_service_prices: list[int] = []  # Compensated prices (set by shuffle_shops)
    bomb_shop_items: list[type] = [FrightBombItem, FireBombItem, IceBombItem]

    locations: dict[type[PrizeLocation], PrizeLocation]
    chest_locations: list[PrizeLocation]
    standard_locations: list[PrizeLocation]
    coin_locations: list[PrizeLocation]
    spell_locations: list[PrizeLocation]
    boss_fight_locations: list[PrizeLocation]
    star_piece_locations: list[PrizeLocation]
    extra_star_piece_locations: list[PrizeLocation]
    key_item_locations: list[PrizeLocation]
    extra_key_item_locations: list[PrizeLocation]
    character_recruitment_locations: list[PrizeLocation]

    # Prize lookup cache: maps prize type -> location holding that prize
    # Updated via notify_prize_placed() when prizes are assigned
    _prize_type_to_location: dict[type, PrizeLocation]
    # Cache version - incremented when any prize is placed, used to invalidate caches
    _placement_version: int

    # Item impact categories (built by _build_item_impact_categories)
    low_impact_items: list[type[RegularItem]]
    high_impact_items: list[type[RegularItem]]
    highest_impact_items: list[type[RegularItem]]
    low_impact_equip: list[type[Equipment]]
    high_impact_equip: list[type[Equipment]]
    highest_impact_equip: list[type[Equipment]]
    equipment_ranks: list[tuple[type[Equipment], float]]

    # Mapping from item class to prize class (built by _build_item_to_prize_mapping)
    item_to_prize: dict[type[Item], type[ItemPrize]]

    # Music IDs for boss shuffle (built by apply_cosmetic_settings)
    selected_music_ids: list[int]

    # Progress callback for SSE streaming (set by __init__)
    _progress_callback: Callable[[str, int], None] | None

    # Invisible item locations - stored separately to allow reuse across shuffle retries
    # These are initialized once during the first call to set_locations, then reused
    _invisible_item_locations: dict[type[PrizeLocation], PrizeLocation] | None = None

    # Dummy NPC index tracking for deterministic object presence table
    # Pre-allocated once by _pre_allocate_dummy_npcs, then reused across shuffle retries
    _slot_dummy_indices: dict[int, int] | None = None   # room_id → starting object index of 5 slot dummies
    _flag_dummy_index: dict[int, int] | None = None     # room_id → object index of 1 flag dummy

    # Vanilla room NPC states for change detection during partition recalculation
    # Populated by snapshot_vanilla_room_states() before NPC shuffling begins
    _vanilla_room_states: dict[int, "VanillaRoomState"] | None = None

    # Spell assignment tracking for SpellsAnywhere mode
    # Maps character prize type -> count of spells assigned to that character
    _spell_assignments: dict[type, int] | None = None

    @property
    def overworld_character(self) -> CharacterPrize:
        if not self.settings.isflag_enabled(PlayAsStarter):
            return MarioRecruitmentPrize()
        s = self.get_location(StartingCharacter1)
        assert s is not None
        assert isinstance(s.prize, CharacterPrize)
        return s.prize

    def _report_progress(self, message: str, percent: int) -> None:
        """Report progress to the callback if one is set."""
        if self._progress_callback:
            self._progress_callback(message, percent)

    @classmethod
    def is_monstro_item(cls, item_type: type) -> bool:
        """Check if an item type is a special Monstro Town item."""
        return item_type in (
            ChompItem,
            ZoomShoesItem,
            FroggieStickItem,
            LazyShellItem,
            LazyShellItem2,
            GhostMedalItem,
            JinxBeltItem,
            QuartzCharmItem,
            AttackScarfItem,
            SuperSuitItem,
            WonderChompItem,
            Stella023Item,
            SageStickItem,
            EnduringBroochItem,
            TeamworkBandItem,
        )

    @classmethod
    def is_remake_item(cls, item_type: type) -> bool:
        """Check if an item type is a special Monstro Town item."""
        return item_type in (
            WonderChompItem,
            Stella023Item,
            SageStickItem,
            EnduringBroochItem,
            TeamworkBandItem,
            ExtraShinyStoneItem,
            CrystalShardItem,
        )

    def get_item(self, item: int | type):
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

    def get_spell(self, spell_id: int | Type[SpellT]) -> Spell:
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

    def is_location_enabled(self, location_type: type[PrizeLocation]) -> bool:
        """Check if a location type is enabled based on its category flag.

        Returns True if the location is enabled in the relevant flag based on its type:
        - BossFightLocation subclasses check ShuffledBosses
        - StarPieceLocation subclasses check EnabledBossChecks
        - SpellSlotLocation subclasses are always enabled (controlled by CharacterLearnedSpells/SpellsAnywhere)
        - CharacterRecruitmentLocation subclasses are always enabled (controlled by ShuffleCharacters)
        - Other PrizeLocation subclasses check EnabledRegularChecks
        """
        if issubclass(location_type, BossFightLocation):
            # BossFightLocations check ShuffledBosses (which bosses are in the shuffle pool)
            # .enabled contains enum members, so we compare against .value
            shuffled_bosses_flag = self.settings.get_flag(ShuffledBosses)
            return any(m.value == location_type for m in shuffled_bosses_flag.enabled)
        elif issubclass(location_type, SpellSlotLocation):
            # SpellSlotLocations are always considered "enabled" here - their actual
            # shuffle status is controlled by CharacterLearnedSpells/SpellsAnywhere flags
            return True
        elif issubclass(location_type, StarPieceLocation):
            # StarPieceLocations check EnabledBossChecks (star pieces are tied to boss fights)
            boss_checks_flag = self.settings.get_flag(EnabledBossChecks)
            return any(m.value == location_type for m in boss_checks_flag.enabled)
        elif issubclass(location_type, CharacterRecruitmentLocation):
            # CharacterRecruitmentLocations are always considered "enabled" here - their actual
            # shuffle status is controlled by ShuffleCharacters flag
            return True
        elif issubclass(location_type, InvisibleFlagLocation):
            # InvisibleFlagLocations are randomly assigned to one of 3 slots at runtime.
            # Look up this class in the world's invisible item locations to find its _which value,
            # then check if the corresponding proxy is enabled.
            if self._invisible_item_locations is None:
                return False
            location_instance = self._invisible_item_locations.get(location_type)
            if not isinstance(location_instance, InvisibleFlagLocation):
                return False
            which = location_instance._which
            proxy_classes = {
                0: ThreeMustyFearsBonesProxy,
                1: ThreeMustyFearsGreaperProxy,
                2: ThreeMustyFearsBooProxy,
            }
            proxy_class = proxy_classes.get(which)
            if proxy_class is None:
                return False
            regular_checks_flag = self.settings.get_flag(EnabledRegularChecks)
            return any(m.value == proxy_class for m in regular_checks_flag.enabled)
        else:
            # Check EnabledRegularChecks for non-boss locations
            regular_checks_flag = self.settings.get_flag(EnabledRegularChecks)
            return any(m.value == location_type for m in regular_checks_flag.enabled)

    def notify_prize_placed(self, location: PrizeLocation, prize) -> None:
        """Notify that a prize was placed - updates caches.

        Call this after setting a prize on a location to keep caches in sync.
        """
        if prize is not None:
            # Index by prize's exact type (not parent classes) for precise lookup
            self._prize_type_to_location[type(prize)] = location
        self._placement_version += 1

    def get_location_by_prize_type(self, prize_type: type) -> PrizeLocation | None:
        """Get the location containing a prize of the exact given type (O(1) lookup).

        Returns None if no location has a prize of that exact type.
        """
        return self._prize_type_to_location.get(prize_type)

    @property
    def placement_version(self) -> int:
        """Current placement version - changes whenever a prize is placed.

        Use this to invalidate caches that depend on prize placements.
        """
        return self._placement_version

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

    _next_formation_id: int | None = None

    def allocate_formation_id(self) -> int:
        """Allocate a unique formation ID for a new Formation object.

        Raises:
            ValueError: If all 512 formation IDs have been exhausted.
        """
        from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
            TOTAL_FORMATIONS,
        )

        if self._next_formation_id is None:
            max_id = 0
            for pack in self.battle_packs.packs:
                for f in pack.formations:
                    if f.formation_id is not None and f.formation_id > max_id:
                        max_id = f.formation_id
            self._next_formation_id = max_id + 1
        if self._next_formation_id >= TOTAL_FORMATIONS:
            raise ValueError(
                f"Cannot allocate formation ID: all {TOTAL_FORMATIONS} slots exhausted"
            )
        fid = self._next_formation_id
        self._next_formation_id += 1
        return fid

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
        For SpellPrize items, includes the character name in the format: "SpellName (CharacterName)"
        """
        result: dict[str, str] = dict()
        for loc_type, loc in self.locations.items():
            location_name = loc_type.__name__
            if loc.prize is None:
                prize_name = "None"
            else:
                prize_name = type(loc.prize).__name__
                # If it's a spell, include the character it's assigned to
                if isinstance(loc.prize, SpellPrize):
                    character = loc.prize.character
                    if character is not None:
                        character_name = character.__name__.replace(
                            "RecruitmentPrize", ""
                        )
                        prize_name = f"{prize_name} ({character_name})"
                    else:
                        prize_name = f"{prize_name} (No Character)"
            result[location_name] = prize_name
        return result

    def _get_spell_character_assignments_json(self) -> dict[str, str]:
        """Get JSON representation of all spell-to-character assignments.

        Returns a dictionary mapping spell names to their assigned character names.
        This works whether spells are in the general item pool or learned by level-up.
        """
        result: dict[str, str] = {}

        # Get all spell prizes from locations
        for loc in self.locations.values():
            if loc.prize and isinstance(loc.prize, SpellPrize):
                spell_name = type(loc.prize).__name__
                character = loc.prize.character
                if character is not None:
                    character_name = character.__name__.replace("RecruitmentPrize", "")
                    result[spell_name] = character_name
                else:
                    result[spell_name] = "No Character"

        return result

    event_2496_startup = []

    def _compute_check_bit_mapping(self) -> tuple[
        dict[str, tuple[int, int, bool]],
        dict[int, int],
        dict[int, int],
    ]:
        """Compute chest state table bit positions for chest check locations.

        The chest state table at BW-RAM $3D80 (FxPak $E03D80) uses cumulative
        bit packing by room ID: room 0 gets its bits first, then room 1, etc.
        Only chest-type objects (ChestNPC and ChestClone) get bits — other object
        types are skipped. Within a room, chests are numbered sequentially.

        Returns:
            (check_mapping, room_bit_offsets, room_chest_counts) where:
            - check_mapping: {location_class_name: (fxpak_addr, bit_index, set_when_checked)}
            - room_bit_offsets: {room_id: cumulative_bit_offset}
            - room_chest_counts: {room_id: chest_object_count}
        """
        from smrpgpatchbuilder.datatypes.levels.classes import ChestNPC, ChestClone
        from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject

        FXPAK_BASE = 0xE03D80
        NPC_AREA_OBJECT_START = 0x14  # AreaObject(0x14) = object index 0

        # Cumulative bit offset per room (rooms ordered by ID 0-511).
        # Only ChestNPC and ChestClone objects get bits in this table.
        cumulative = 0
        room_bit_offsets: dict[int, int] = {}
        room_chest_counts: dict[int, int] = {}
        for room_id in range(len(self.rooms._rooms)):
            room_bit_offsets[room_id] = cumulative
            room = self.rooms._rooms[room_id]
            count = (
                sum(1 for obj in room.objects if isinstance(obj, (ChestNPC, ChestClone)))
                if room is not None
                else 0
            )
            room_chest_counts[room_id] = count
            cumulative += count

        # Map TreasureChestLocation checks to bit positions.
        # The bit index within a room is the chest's position among chest-type
        # objects in the room (not its general area object index).
        mapping: dict[str, tuple[int, int, bool]] = {}
        for loc_cls, loc in self.locations.items():
            if not isinstance(loc, TreasureChestLocation):
                continue
            class_name = loc_cls.__name__
            for npc_ao, room_id in zip(loc._npc_ids, loc._rooms):
                ao = npc_ao if isinstance(npc_ao, AreaObject) else AreaObject(npc_ao + NPC_AREA_OBJECT_START)
                obj_idx = int(ao) - NPC_AREA_OBJECT_START
                # Count chest objects before this area object index
                room = self.rooms._rooms[room_id]
                chest_idx = 0
                if room is not None:
                    for i, obj in enumerate(room.objects):
                        if i >= obj_idx:
                            break
                        if isinstance(obj, (ChestNPC, ChestClone)):
                            chest_idx += 1
                bit_pos = room_bit_offsets[room_id] + chest_idx
                addr = FXPAK_BASE + (bit_pos // 8)
                bit = bit_pos % 8
                mapping[class_name] = (addr, bit, False)  # cleared = opened
                break  # first room is the primary

        return mapping, room_bit_offsets, room_chest_counts

    def _compute_npc_presence_mapping(self) -> dict[str, tuple[int, int, bool]]:
        """Compute NPC presence bit positions for NPC-despawn-based check locations.

        The NPC presence table at BW-RAM $6D20 (FxPak $E02D20) uses cumulative
        bit packing by room ID: room 0 gets bits for ALL its objects first,
        then room 1, etc. A cleared bit (1->0) means the NPC was removed.

        Only maps StandingLocation and NPCLocationRow subclasses that define
        _npc_ids. TreasureChestLocations are skipped (already detected by
        chest bit mapping).

        Returns:
            {location_class_name: (fxpak_addr, bit_index, set_when_checked)}
            where set_when_checked=False (bit CLEAR = check done).
        """
        from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import (
            AreaObject,
        )

        FXPAK_BASE = 0xE02D20
        NPC_AREA_OBJECT_START = 0x14

        # Cumulative bit offset: count ALL objects per room (not just chests)
        cumulative = 0
        room_bit_offsets: dict[int, int] = {}
        for room_id in range(len(self.rooms._rooms)):
            room_bit_offsets[room_id] = cumulative
            room = self.rooms._rooms[room_id]
            count = len(room.objects) if room is not None else 0
            cumulative += count

        # Map locations that use NPC presence for check detection.
        # Skip TreasureChestLocation (already handled by chest bit mapping).
        # StandingLocation uses _npc_ids; NPCLocationRow uses _check_npc_ids
        # (_npc_ids on NPCLocationRow controls model replacement, not tracking).
        mapping: dict[str, tuple[int, int, bool]] = {}
        for loc_cls, loc in self.locations.items():
            if isinstance(loc, StandingLocation):
                npc_ids = loc._npc_ids
            elif isinstance(loc, NPCLocationRow):
                npc_ids = loc._check_npc_ids
            else:
                continue
            if not npc_ids:
                continue

            class_name = loc_cls.__name__
            for npc_ao, room_id in zip(npc_ids, loc._rooms):
                ao = (
                    npc_ao
                    if isinstance(npc_ao, AreaObject)
                    else AreaObject(npc_ao + NPC_AREA_OBJECT_START)
                )
                obj_idx = int(ao) - NPC_AREA_OBJECT_START
                bit_pos = room_bit_offsets[room_id] + obj_idx
                addr = FXPAK_BASE + (bit_pos // 8)
                bit = bit_pos % 8
                mapping[class_name] = (addr, bit, False)  # bit CLEAR = done
                break  # first room is the primary
        return mapping

    def _compute_booster_hill_mapping(self) -> dict[str, int]:
        """Compute Booster Hill flower counter thresholds for check locations.

        BoosterHillLocation checks use the byte counter at BW-RAM $70B1
        (FxPak $E030B1). A check with _70B1_id=N is complete when the
        counter value >= N+1.

        Returns:
            {location_class_name: threshold} where threshold = _70B1_id + 1.
        """
        mapping: dict[str, int] = {}
        for loc_cls, loc in self.locations.items():
            if not isinstance(loc, BoosterHillLocation):
                continue
            mapping[loc_cls.__name__] = loc._70B1_id + 1
        return mapping

    @property
    def spoiler(self) -> dict[str, Any]:
        check_mapping, room_bit_offsets, room_chest_counts = (
            self._compute_check_bit_mapping()
        )
        npc_presence_mapping = self._compute_npc_presence_mapping()
        booster_hill_mapping = self._compute_booster_hill_mapping()
        result = {
            "settings": self._get_settings_json(),
            "locations": self._get_locations_json(),
            "shops": self._get_shops_json(),
            "palettes": self._get_palettes_json(),
            "spell_learning_levels": self._get_spell_learning_levels_json(),
            "spell_character_assignments": self._get_spell_character_assignments_json(),
            "password": self.password,
            "songs": [self.song_1, self.song_2, self.song_3],
            "check_bit_mapping": {
                name: {"addr": f"0x{addr:06X}", "bit": bit, "set_when_checked": swc}
                for name, (addr, bit, swc) in check_mapping.items()
            },
            "npc_presence_mapping": {
                name: {"addr": f"0x{addr:06X}", "bit": bit, "set_when_checked": swc}
                for name, (addr, bit, swc) in npc_presence_mapping.items()
            },
            "booster_hill_mapping": {
                name: {"threshold": threshold}
                for name, threshold in booster_hill_mapping.items()
            },
            "room_bit_offsets": {
                str(rid): off
                for rid, off in room_bit_offsets.items()
                if off > 0 or rid == 0
            },
            "room_chest_counts": {
                str(rid): cnt
                for rid, cnt in room_chest_counts.items()
                if cnt > 0
            },
        }
        if self.poison_mushroom_status:
            result["poison_mushroom_status"] = self.poison_mushroom_status
        return result

    def _get_palettes_json(self) -> dict[str, str]:
        """Get JSON representation of character palette names.

        Uses the palette's custom name if set, otherwise falls back to the class name.
        """

        def get_palette_name(palette: Any, original_name: str) -> str:
            # If palette has a custom name different from original, use it
            if hasattr(palette, "name") and palette.name != original_name:
                return palette.name
            # Otherwise use the class name
            return type(palette).__name__

        return {
            "Mario": get_palette_name(self.mario_palette, "Mario"),
            "Mallow": get_palette_name(self.mallow_palette, "Mallow"),
            "Geno": get_palette_name(self.geno_palette, "Geno"),
            "Bowser": get_palette_name(self.bowser_palette, "Bowser"),
            "Toadstool": get_palette_name(self.toadstool_palette, "Toadstool"),
        }

    def _get_shops_json(self) -> dict[str, list[str]]:
        """Get JSON representation of all shops with their item names."""
        from ..data.variables.shop_names import (
            SH00_MUSHROOM_KINGDOM,
            SH01_ROSE_TOWN_ITEM,
            SH02_ROSE_TOWN_ARMOR,
            SH03_FROG_DISCIPLE,
            SH04_MOLEVILLE,
            SH05_MARRYMORE,
            SH06_FROG_COIN_EMPORIUM,
            SH07_SEA_AND_SHIP_SHAMAN,
            SH08_SEASIDE_TOWN_MINION,
            SH09_JUICE_BAR_BASE,
            SH10_JUICE_BAR_ALTO,
            SH11_JUICE_BAR_TENOR,
            SH12_JUICE_BAR_SOPRANO,
            SH13_SEASIDE_WEAPON,
            SH14_SEASIDE_ARMOR,
            SH15_SEASIDE_ACCESSORY,
            SH16_SEASIDE_HEALTH_FOOD,
            SH17_MONSTRO,
            SH18_VOLCANO_ITEM,
            SH19_VOLCANO_ARMOR,
            SH20_GOOMBETTE,
            SH21_NIMBUS_LAND,
            SH22_KEEP_1,
            SH23_KEEP_2,
            SH24_FACTORY_TOAD,
        )

        shop_names = {
            SH00_MUSHROOM_KINGDOM: "Mushroom Kingdom",
            SH01_ROSE_TOWN_ITEM: "Rose Town Item",
            SH02_ROSE_TOWN_ARMOR: "Rose Town Armor",
            SH03_FROG_DISCIPLE: "Frog Disciple",
            SH04_MOLEVILLE: "Moleville",
            SH05_MARRYMORE: "Marrymore",
            SH06_FROG_COIN_EMPORIUM: "Frog Coin Emporium",
            SH07_SEA_AND_SHIP_SHAMAN: "Sea/Ship Shaman",
            SH08_SEASIDE_TOWN_MINION: "Seaside Town (Minion)",
            SH09_JUICE_BAR_BASE: "Juice Bar (Base)",
            SH10_JUICE_BAR_ALTO: "Juice Bar (Alto)",
            SH11_JUICE_BAR_TENOR: "Juice Bar (Tenor)",
            SH12_JUICE_BAR_SOPRANO: "Juice Bar (Soprano)",
            SH13_SEASIDE_WEAPON: "Seaside Weapon",
            SH14_SEASIDE_ARMOR: "Seaside Armor",
            SH15_SEASIDE_ACCESSORY: "Seaside Accessory",
            SH16_SEASIDE_HEALTH_FOOD: "Seaside Health Food",
            SH17_MONSTRO: "Monstro Town",
            SH18_VOLCANO_ITEM: "Barrel Volcano Item",
            SH19_VOLCANO_ARMOR: "Barrel Volcano Armor",
            SH20_GOOMBETTE: "Goombette",
            SH21_NIMBUS_LAND: "Nimbus Land",
            SH22_KEEP_1: "Bowser's Keep 1",
            SH23_KEEP_2: "Bowser's Keep 2",
            SH24_FACTORY_TOAD: "Factory Toad",
        }

        result: dict[str, list[str]] = dict()
        for shop in self.shops.shops:
            if shop is None:
                continue
            shop_name = shop_names.get(shop.index, f"Shop {shop.index}")
            item_names = []
            for item in shop.items:
                if item is None:
                    continue
                # item is a class type, get its _name attribute
                item_name = getattr(item, "_name", None)
                if item_name:
                    item_names.append(item_name)
                else:
                    item_names.append(item.__name__)
            result[shop_name] = item_names

        # Add text-based shops
        def get_item_name(item_type: type) -> str:
            name = getattr(item_type, "_name", None)
            if name:
                return name
            return item_type.__name__

        if self.room_service_items:
            result["Room Service (Marrymore)"] = [
                get_item_name(i) for i in self.room_service_items
            ]
        if self.bomb_shop_items:
            result["Swap Shop (Seaside)"] = [
                get_item_name(i) for i in self.bomb_shop_items
            ]

        return result

    def _get_spell_learning_levels_json(self) -> dict[str, dict[str, int]]:
        """Get JSON representation of which spells are learned at which levels for each character."""
        result: dict[str, dict[str, int]] = {}

        for ally in self.allies._allies:
            character_name = ally.name
            spells_by_level: dict[str, int] = {}

            # Check starting spells (learned at level 1)
            for spell_type in ally.starting_magic:
                spell_name = spell_type.__name__
                spells_by_level[spell_name] = 1

            # Check level-up spells
            for level_up in ally.levels:
                if level_up.spell_learned:
                    spell_name = level_up.spell_learned.__name__
                    spells_by_level[spell_name] = level_up.level

            if spells_by_level:
                result[character_name] = spells_by_level

        return result

    def _get_settings_json(self) -> dict[str, Any]:
        """Get JSON representation of all settings with their names and values."""
        from .flags import CategorizationFlagWithOrdinance

        def get_option_display_name(opt: Any) -> str:
            """Get a human-readable display name for an option."""
            if hasattr(opt, "value"):
                val = opt.value
                # Check if val is a string (e.g., "Random_1", "Random_2")
                if isinstance(val, str):
                    return val
                # Check if val is a class type (for ClassCategorizationOption)
                if isinstance(val, type):
                    # For class types, use _title (spell title) or __name__ (class name)
                    if hasattr(val, "_title") and val._title:
                        return val._title
                    elif hasattr(val, "_name") and val._name:
                        return val._name
                    else:
                        return val.__name__
                elif hasattr(val, "name") and isinstance(val.name, str):
                    return val.name
                elif hasattr(val, "_name") and isinstance(val._name, str):
                    return val._name
                else:
                    return str(val)
            elif hasattr(opt, "name"):
                return opt.name
            else:
                return str(opt)

        result: dict[str, Any] = dict()
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
            elif isinstance(flag, CategorizationFlagWithOrdinance):
                # Get list of selected options sorted by their order
                selected_with_order = [
                    (opt, order)
                    for opt, order in flag.options.items()
                    if order is not None
                ]
                # Sort by order value
                selected_with_order.sort(key=lambda x: x[1])
                # Get display names in order
                result[flag_name] = [
                    get_option_display_name(opt) for opt, _ in selected_with_order
                ]
            elif isinstance(flag, CategorizationFlag):
                # Get list of enabled options
                result[flag_name] = [
                    get_option_display_name(opt) for opt in flag.enabled
                ]
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
        spells: SpellCollection[Spell],
        sprites: SpriteCollection,
        world_map_locations: WorldMapLocationCollection,
        event_palettes: EventPaletteCollection,
        sprite_palettes: SpritePaletteCollection,
        progress_callback: Callable[[str, int], None] | None = None,
        debug_bps_patches: bool = False,
    ):
        self._progress_callback = progress_callback
        self._report_progress("Parsing settings...", 0)
        self.allies = allies
        self.seed = seed
        self.version = version
        self.settings = settings
        self._prize_type_to_location = dict()
        self._placement_version = 0
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
        self.rooms = deepcopy(rooms)
        self.shops = shops
        self.spells = spells
        self.sprites = sprites
        self.world_map_locations = world_map_locations
        self._cached_patch: Patch | None = None
        self._debug_bps_patches = debug_bps_patches
        self.event_palettes = event_palettes
        self.sprite_palettes = sprite_palettes

        # Validate settings combinations before doing anything else
        # This catches invalid combinations early with clear error messages
        validate_settings(self.settings)

        random.seed(self.seed)
        print(self.seed)

        self.event_2496_startup: list[UsableEventScriptCommand] = []

        # prize locations HAVE to all be defined by this point
        # not shuffled, just determined if they exist in the seed or not

        if self.settings.isflag_enabled(SkipMustyFearsSequence):
            self.event_scripts.get_script_by_id(E2496_START_GAME).insert_after_identifier("EVENT_2496_flag_setup", RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER))

        if self.settings.isflag_enabled(SkipMinecart):
            self.event_2496_startup += [
                SetBit(SKIP_MANDATORY_MINECART),
            ]
        if self.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            self.event_2496_startup += [
                SetBit(PROGRESSIVE_FIREWORKS_ENABLED),
            ]
        if self.settings.isflag_enabled(SeeYa):
            self.event_2496_startup += [
                AddToInventory(SeeYaItem),
            ]
            if not self.settings.isflag_enabled(ShuffleShops):
                self.event_2496_startup += [
                    SetBit(FROG_DISCIPLE_ITEM_5_PURCHASED),
                ]
        if self.settings.isflag_enabled(SkipAnts):
            self.event_2496_startup += [
                SetBit(SHOGUN_1_CLEARED),
                SetBit(SHOGUN_2_CLEARED),
                SetBit(SHOGUN_3_CLEARED),
                SetBit(SHOGUN_4_CLEARED),
                SetBit(SHOGUN_5_CLEARED),
            ]
        if self.settings.isflag_enabled(ShuffleMarioDoll):
            self.event_2496_startup += [
                SetBit(MARIO_DOLL_SHUFFLE_ENABLED),
            ]

        # Apply progression gating settings (win conditions, area gates, travel)
        apply_shuffler_independent_settings(self)

        # Apply threshold adjustments
        apply_threshold_settings(self)

        # Apply enemy and combat tweaks
        apply_enemy_tweaks(self)

        # Apply equipment and spell element settings
        apply_equipment_settings(self)

        # Build item impact categories (used for shop shuffling and other systems)
        self._build_item_impact_categories()

        # Build item to prize mapping (used for random prize substitution)
        self._build_item_to_prize_mapping()
        from ..logic.placement import PlacementException

        # Track failure counts to detect unsolvable settings
        # Key = number of unplaced items, Value = count of times this failure occurred
        failure_counts: dict[int, int] = dict()
        MAX_FAILURES_PER_COUNT = 5

        # Save a snapshot of rooms before shuffling so we can restore on retry
        # (shuffle adds invisible items to rooms which would accumulate on retries)
        rooms_snapshot = deepcopy(self.rooms)

        success = False
        while not success:
            try:
                self._shuffle_items()
                success = True
            except PlacementException as e:
                # Restore rooms to pre-shuffle state before retrying
                self.rooms = deepcopy(rooms_snapshot)
                # Reset dummy indices so _pre_allocate_dummy_npcs reruns with fresh rooms.
                # Also reset _invisible_item_locations so set_locations re-runs the
                # flag-NPC swap loop — otherwise the freshly re-added dummies stay at
                # (0, 0, 0) and the chosen flag NPCs never get written to room data.
                self._slot_dummy_indices = None
                self._flag_dummy_index = None
                self._invisible_item_locations = None
                if self.settings.debug_mode:
                    print(f"[DEBUG] Placement failed with {e.unplaced_count} unplaced items, retrying...")

                # Track this failure count
                count = e.unplaced_count
                failure_counts[count] = failure_counts.get(count, 0) + 1

                # Check if any failure count has reached the threshold
                if failure_counts and all(
                    v >= MAX_FAILURES_PER_COUNT for v in failure_counts.values()
                ):
                    raise WorldBuildingException(
                        f"Item placement appears unsolvable. "
                        f"Repeated failures with the same unplaced item counts: {failure_counts}. "
                        f"The chosen settings with excluded locations may be impossible to solve. "
                        f"Unplaced items on last attempt: {e.unplaced_items}"
                    )
            except Exception:
                # Re-raise unexpected exceptions
                raise

        # TODO: update sprite pointers for new ally IDs
        # TODO: make up some presets

        # Shop shuffling happens after equipment randomization so we can score equipment
        if self.settings.isflag_enabled(ShuffleShops):
            self._shuffle_shops()
        elif self.settings.isflag_enabled(SeeYa):
            exclude_seeya_from_frog_disciple(self)

        if self.settings.isflag_enabled(EnemyAttacks):
            self._randomize_enemy_attacks_and_spells()

        self._apply_shuffle_results()

        self._randomize_enemy_stats()

        # Update HP-based AI thresholds after all stat mutations are complete
        self._update_enemy_hp_thresholds()

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
            self._randomize_levelup_xps()

        # Randomize character spell stats
        if self.settings.isflag_enabled(CharacterSpellStats):
            self._randomize_character_spell_stats()

        # Apply debug mode max stats again after all character randomization
        # (ensures debug stats override everything)
        from ..logic.setup.debug import apply_debug_max_stats

        apply_debug_max_stats(self)

        # Apply EXP multiplier
        self._apply_exp_multiplier()

        # Apply experience zero settings AFTER all XP manipulation
        # This ensures 0 XP flags take precedence over randomization
        apply_experience_zero_settings(self)

        # Apply minigame settings
        apply_minigame_settings(self)

        self._rebuild_hash()
        self._report_progress("Applying cosmetics...", 40)

        # Apply cosmetic settings (re-seeded for variation between generations)
        apply_cosmetic_settings(self)

        with open("spoiler_after_replacements.json", "w") as f:
            json.dump(self.spoiler, f, indent=2, default=str)

    def _shuffle_items(self):
        self._report_progress("Shuffling checks...", 10)

        # determine which checks exist in this seed
        # this doesn't mean which ones are shuffled, it means which ones can be accessed at all
        # exclusions would be things like remake checks, surplus invisible item checks, super jump prizes when super jump not usable
        set_locations(self)

        # shuffle according to settings
        shuffle_prizes(self)

        # replace bad items with coins, supplant YouMissed, fill empty locations, etc

        # Write spoiler to JSON file
        with open("spoiler.json", "w") as f:
            json.dump(self.spoiler, f, indent=2, default=str)

        post_shuffle_cleanup(self)

    def _apply_shuffle_results(self):
        """Apply shuffle results to game data. Called after successful shuffle."""
        apply_shuffler_results_to_game_data(self)

        # Apply debug mode overrides (must be after apply_shuffler_results_to_game_data)
        from ..logic.setup.debug import apply_debug_max_stats

        apply_debug_max_stats(self)

        # Note:
        # apply_shuffler_results_to_game_data is meant to look at the shuffler results and materialize them
        # by changing the NPC models in rooms, updating event scripts with boss animation replacements,
        # build the events that control which chest grants you which item, etc.
        # Most logic for an individual check should go in that check's render(world) method.
        # Business logic in apply_shuffler_results_to_game_data is meant for materializing things that
        # need to either loop through a list of checks or do something with a set of locations, i.e. building the item granter events.
        # If you are going to modify these, follow this pattern.

    def _randomize_enemy_attacks_and_spells(self) -> None:
        """Randomize enemy spell and attack stats and effects."""
        randomize_enemy_attacks_and_spells(self)

    def _randomize_enemy_stats(self) -> None:
        """Randomize enemy stats based on EnemyStats flag setting."""
        randomize_enemy_stats(self)

    def _randomize_enemy_drops(
        self,
        consumables_group_1: list[type[RegularItem]],
        consumables_group_2: list[type[RegularItem]],
    ) -> None:
        """Randomize enemy drops (coins, XP, items)."""
        randomize_enemy_drops(self, consumables_group_1, consumables_group_2)

    def _randomize_enemy_formations(self) -> None:
        """Randomize enemy formations."""
        randomize_enemy_formations(self)

    def _apply_exp_multiplier(self) -> None:
        """Apply EXP multiplier to all enemies based on settings."""
        apply_exp_multiplier(self)

    def _randomize_character_stats(self) -> None:
        """Randomize character stats, level-up bonuses, and stat growths."""
        randomize_character_stats(self)

    def _randomize_levelup_xps(self) -> None:
        """Randomize the XP requirements for each level by shuffling the gaps."""
        randomize_levelup_xps(self)

    def _finalize_character_stats(self, ally) -> None:
        """Finalize character starting stats based on starting level and optimal choices."""
        pass

    def _randomize_character_spell_stats(self) -> None:
        """Randomize character spell stats (FP cost, power, hit rate)."""
        randomize_character_spell_stats(self)

    def _build_item_impact_categories(self) -> None:
        """Build item impact categories for use in shop shuffling and other systems."""
        build_item_impact_categories(self)

    def _build_item_to_prize_mapping(self) -> None:
        build_item_to_prize_mapping(self)

    def _shuffle_shops(self) -> None:
        """Shuffle the contents of all shops based on settings."""
        shuffle_shops(self)

    def _update_enemy_hp_thresholds(self) -> None:
        """Update HP-based AI script thresholds for specific enemies.

        This must be called AFTER both boss stat scaling and enemy stat mutations
        are complete, so the thresholds reflect the final HP values.
        """
        # Update Dodo's AI script HP threshold (60% of HP triggers phase 2)
        dodo = self.get_enemy(DODOEnemy)
        _, _, dodo_hp_check = self.monster_scripts.get_command_by_identifier(
            "dodo_low_hp_check"
        )
        cast(IfHPBelow, dodo_hp_check).set_threshold(round(dodo.hp * 0.6))
        # Update return condition
        valentina = self.get_enemy(VALENTINAEnemy)
        _, _, valentina_return_cmd = self.monster_scripts.get_command_by_identifier(
            "dodo_returns"
        )
        cast(IfHPBelow, valentina_return_cmd).set_threshold(
            round(valentina.hp * 1200 / 2000)
        )

        # Update Shelly's AI script HP thresholds (80%, 60%, 40%, 20% triggers phase changes)
        shelly = self.get_enemy(SHELLYEnemy)
        for identifier, percent in [
            ("shelly_low_hp_check_80_percent", 0.8),
            ("shelly_low_hp_check_60_percent", 0.6),
            ("shelly_low_hp_check_40_percent", 0.4),
            ("shelly_low_hp_check_20_percent", 0.2),
        ]:
            _, _, shelly_hp_check = self.monster_scripts.get_command_by_identifier(
                identifier
            )
            cast(IfHPBelow, shelly_hp_check).set_threshold(round(shelly.hp * percent))

        # Update Right Eye's revival HP in battle animation scripts (120% of HP)
        right_eye = self.get_enemy(RIGHTEYEEnemy)
        right_eye_revival_cmd = self.get_battle_animation_command_by_name(
            "right_eye_revival_hp"
        )
        cast(SetAMEM16BitToConst, right_eye_revival_cmd).set_value(
            round(right_eye.hp * 1.2)
        )

        # Update Punchinello's bomb-summoning thresholds
        punchinello = self.get_enemy(PUNCHINELLOEnemy)
        threshold_1 = round(punchinello.hp * 800 / 1200)
        _, _, bobomb_cmd_1 = self.monster_scripts.get_command_by_identifier(
            "punchinello_800_hp_1"
        )
        cast(IfHPBelow, bobomb_cmd_1).set_threshold(threshold_1)
        _, _, bobomb_cmd_2 = self.monster_scripts.get_command_by_identifier(
            "punchinello_800_hp_2"
        )
        cast(IfHPBelow, bobomb_cmd_2).set_threshold(threshold_1)
        threshold_2 = round(punchinello.hp * 400 / 1200)
        _, _, bobomb_cmd_3 = self.monster_scripts.get_command_by_identifier(
            "punchinello_400_hp_1"
        )
        cast(IfHPBelow, bobomb_cmd_3).set_threshold(threshold_2)
        _, _, bobomb_cmd_4 = self.monster_scripts.get_command_by_identifier(
            "punchinello_400_hp_2"
        )
        cast(IfHPBelow, bobomb_cmd_4).set_threshold(threshold_2)

        # Update Johnny's Get Tough threshold
        johnny = self.get_enemy(JOHNNYEnemy)
        _, _, get_tough_cmd = self.monster_scripts.get_command_by_identifier(
            "johnny_400_hp"
        )
        cast(IfHPBelow, get_tough_cmd).set_threshold(round(johnny.hp * 400 / 820))

        # Update Johnny 2's battle thresholds
        johnny_2 = self.get_enemy(JOHNNYEnemy2)
        _, _, johnny_cmd_1 = self.monster_scripts.get_command_by_identifier(
            "johnny_1000_hp"
        )
        cast(IfHPBelow, johnny_cmd_1).set_threshold(round(johnny_2.hp * 1000 / 2000))
        _, _, johnny_cmd_2 = self.monster_scripts.get_command_by_identifier(
            "johnny_500_hp"
        )
        cast(IfHPBelow, johnny_cmd_2).set_threshold(round(johnny_2.hp * 500 / 2000))

        # Update Bundt's warning phase
        bundt = self.get_enemy(BUNDTEnemy)
        _, _, bundt_warning_cmd = self.monster_scripts.get_command_by_identifier(
            "bundt_hp_threshold"
        )
        cast(IfHPBelow, bundt_warning_cmd).set_threshold(round(bundt.hp * 200 / 900))

        # Update Jinx 1's buff threshold
        jinx1 = self.get_enemy(JINX1Enemy)
        _, _, jinx1_buff_cmd = self.monster_scripts.get_command_by_identifier(
            "jinx1_phase2"
        )
        cast(IfHPBelow, jinx1_buff_cmd).set_threshold(round(jinx1.hp * 300 / 600))

        # Update Jinx 2's buff threshold
        jinx2 = self.get_enemy(JINX2Enemy)
        _, _, jinx2_buff_cmd = self.monster_scripts.get_command_by_identifier(
            "jinx2_phase2"
        )
        cast(IfHPBelow, jinx2_buff_cmd).set_threshold(round(jinx2.hp * 400 / 800))

        # Update Jinx 3's buff threshold
        jinx3 = self.get_enemy(JINX3Enemy)
        _, _, jinx3_buff_cmd = self.monster_scripts.get_command_by_identifier(
            "jinx3_phase2"
        )
        cast(IfHPBelow, jinx3_buff_cmd).set_threshold(round(jinx3.hp * 600 / 1000))
        _, _, jinx3_buff_cmd_2 = self.monster_scripts.get_command_by_identifier(
            "jinx3_phase3"
        )
        cast(IfHPBelow, jinx3_buff_cmd_2).set_threshold(round(jinx3.hp * 300 / 1000))

        # Update Croco 1's heal threshold
        croco1 = self.get_enemy(CROCO1Enemy)
        _, _, croco1_heal_cmd = self.monster_scripts.get_command_by_identifier(
            "croco1_heal"
        )
        cast(IfHPBelow, croco1_heal_cmd).set_threshold(round(croco1.hp * 100 / 320))

        # Update Croco 2's item steal threshold
        croco2 = self.get_enemy(CROCO2Enemy)
        _, _, croco2_steal_cmd = self.monster_scripts.get_command_by_identifier(
            "croco2_steal"
        )
        cast(IfHPBelow, croco2_steal_cmd).set_threshold(round(croco2.hp * 400 / 750))

        # Update Belome 1's phase change threshold
        belome1 = self.get_enemy(BELOME1Enemy)
        _, _, belome1_phase_change_cmd = self.monster_scripts.get_command_by_identifier(
            "belome1_phase2"
        )
        cast(IfHPBelow, belome1_phase_change_cmd).set_threshold(
            round(belome1.hp * 300 / 500)
        )

        # Update Booster 1's thresholds for stronger attacks
        booster1 = self.get_enemy(BOOSTEREnemy)
        _, _, booster1_strong_attack_1_cmd = (
            self.monster_scripts.get_command_by_identifier("booster_powers_up")
        )
        cast(IfHPBelow, booster1_strong_attack_1_cmd).set_threshold(
            round(booster1.hp * 500 / 800)
        )

        # Update Smithy's pattern thresholds
        smithy_2 = self.get_enemy(SMITHY2Enemy)
        _, _, smithy_phase_2 = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_2"
        )
        _, _, smithy_phase_3 = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_3"
        )
        _, _, smithy_phase_4 = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_4"
        )
        cast(IfHPBelow, smithy_phase_2).set_threshold(round(smithy_2.hp * 6000 / 8000))
        cast(IfHPBelow, smithy_phase_3).set_threshold(round(smithy_2.hp * 4000 / 8000))
        cast(IfHPBelow, smithy_phase_4).set_threshold(round(smithy_2.hp * 2000 / 8000))
        smithy_2 = self.get_enemy(SMITHYMageEnemy)
        _, _, smithy_phase_2_m = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_2_m"
        )
        _, _, smithy_phase_3_m = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_3_m"
        )
        _, _, smithy_phase_4_m = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_4_m"
        )
        cast(IfHPBelow, smithy_phase_2_m).set_threshold(
            round(smithy_2.hp * 6000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_3_m).set_threshold(
            round(smithy_2.hp * 4000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_4_m).set_threshold(
            round(smithy_2.hp * 2000 / 8000)
        )
        smithy_2 = self.get_enemy(SMITHYTankEnemy)
        _, _, smithy_phase_2_t = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_2_t"
        )
        _, _, smithy_phase_3_t = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_3_t"
        )
        _, _, smithy_phase_4_t = self.monster_scripts.get_command_by_identifier(
            "smithy2_phase_4_t"
        )
        cast(IfHPBelow, smithy_phase_2_t).set_threshold(
            round(smithy_2.hp * 6000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_3_t).set_threshold(
            round(smithy_2.hp * 4000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_4_t).set_threshold(
            round(smithy_2.hp * 2000 / 8000)
        )
        smithy_2 = self.get_enemy(SMITHYChestEnemy)
        _, _, smithy_phase_2_c = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_2_c"
        )
        _, _, smithy_phase_3_c = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_3_c"
        )
        _, _, smithy_phase_4_c = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_4_c"
        )
        cast(IfHPBelow, smithy_phase_2_c).set_threshold(
            round(smithy_2.hp * 6000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_3_c).set_threshold(
            round(smithy_2.hp * 4000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_4_c).set_threshold(
            round(smithy_2.hp * 2000 / 8000)
        )
        smithy_2 = self.get_enemy(SMITHYSafeEnemy2)
        _, _, smithy_phase_2_s = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_2_s"
        )
        _, _, smithy_phase_3_s = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_3_s"
        )
        _, _, smithy_phase_4_s = self.monster_scripts.get_command_by_identifier(
            "smithy_phase_4_s"
        )
        cast(IfHPBelow, smithy_phase_2_s).set_threshold(
            round(smithy_2.hp * 6000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_3_s).set_threshold(
            round(smithy_2.hp * 4000 / 8000)
        )
        cast(IfHPBelow, smithy_phase_4_s).set_threshold(
            round(smithy_2.hp * 2000 / 8000)
        )

    def get_patch(self) -> Patch:
        # Return cached patch if already generated
        if self._cached_patch is not None:
            return self._cached_patch

        patch = Patch(debug_mode=self._debug_bps_patches)
        progress = 45

        # Battle animations patch
        self._report_progress("Assembling battle animations...", progress)
        for animation_bank in self.battle_animations.values():
            patches = animation_bank.render()
            for p in patches:
                patch.add_data(p[0], p[1], source="battle_animations")
        progress += 3

        # Render character palettes when any non-default palette is selected
        palette_flags = [
            MarioPaletteChoice,
            MallowPaletteChoice,
            GenoPaletteChoice,
            BowserPaletteChoice,
            ToadstoolPaletteChoice,
        ]
        if any(
            self.settings.get_flag(f).selected.name != "DEFAULT" for f in palette_flags
        ) or self.overworld_character.ally.index != 0:
            patch.add_dict(self.mario_palette.render(self))
            patch.add_dict(self.mallow_palette.render(self))
            patch.add_dict(self.geno_palette.render(self))
            patch.add_dict(self.bowser_palette.render(self))
            patch.add_dict(self.toadstool_palette.render(self))

        # Finalize startup script
        self.event_2496_startup += [Return()]
        self.event_scripts.get_script_by_id(
            E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START
        ).set_contents(self.event_2496_startup)

        # ========================================================================
        # Render scripts and dialogs FIRST to reclaim unused space for animations
        # ========================================================================

        # Partition + palette-row fixups must run BEFORE event scripts render —
        # the fixup mutates DarkenLayersExceptPaletteRows commands in event scripts,
        # so any post-render mutation would be lost.
        # Ending cutscene rooms keep a static ally_buffer regardless of
        # protagonist. R088/R375/R496 use the Mario-NPC-at-front pattern where
        # the protagonist is rendered through a fixed NPC slot rather than the
        # ally buffer, so growing ally_buffer (e.g. to 2 for Bowser) would
        # only shift palette rows the cutscene scripts hardcoded references to.
        # R269/R432/R435/R441/R486/R506/R595 are other ending credits rooms
        # whose palette/layout assumptions also break under ally_buffer growth.
        _STATIC_PARTITION_ROOM_IDS = frozenset({
            88,   # R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION
            269,  # R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW
            375,  # R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY
            432,
            435,  # R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR
            441,
            486,
            292,  # R292 — split second-half of the R496 ending cutscene
            496,  # R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE
            505,
            506,
        })
        for room_id, r in enumerate(self.rooms._rooms):
            if r is not None and isinstance(r, Room) and room_id not in _STATIC_PARTITION_ROOM_IDS:
                r.update_partition_by_protagonist(self)

        _shift_palette_row_masks_for_ally_buffer_growth(self)

        # Event scripts patch
        # NOTE: render() returns pointer_table + script_content combined,
        # so we must write to pointer_table_start, not start
        for event_script_bank in self.event_scripts.banks:
            self._report_progress("Assembling event scripts...", progress)
            rendered = event_script_bank.render()
            patch.add_data(
                event_script_bank.pointer_table_start, rendered, source="event_scripts"
            )
            progress += 3

        # Overworld dialogs (rendered before sprites to reclaim unused space)
        self._report_progress("Assembling dialogs...", progress)
        dialog_data = self.overworld_dialogs.render()
        for addr, data in dialog_data.items():
            patch.add_data(addr, data, source="overworld_dialogs")
        progress += 3

        # Action scripts (rendered before sprites to reclaim unused space)
        # NOTE: render() returns pointer_table + script_content combined,
        # so we must write to pointer_table_start, not start
        self._report_progress("Assembling action scripts...", progress)
        action_data = self.action_scripts.render()
        patch.add_data(
            self.action_scripts.pointer_table_start,
            action_data,
            source="action_scripts",
        )
        progress += 3

        # Monster AI scripts (rendered before sprites to reclaim unused space)
        self._report_progress("Assembling monster AI scripts...", progress)
        monster_scripts = self.monster_scripts.render()
        patch.add_data(
            self.monster_scripts.pointer_table_start,
            monster_scripts[0],
            source="monster_scripts",
        )
        patch.add_data(
            self.monster_scripts.range_2_start,
            monster_scripts[1],
            source="monster_scripts",
        )
        progress += 3

        # Collect unused ranges and add as AnimationBanks
        # From overworld dialogs
        for start, end in self.overworld_dialogs.get_unused_ranges():
            self.sprites.animation_data_banks.append(AnimationBank(start, end))

        # From event scripts
        # for bank in self.event_scripts.banks:
        #     unused = bank.get_unused_range()
        #     if unused:
        #         self.sprites.animation_data_banks.append(
        #             AnimationBank(unused[0], unused[1])
        #         )

        # From action scripts
        unused = self.action_scripts.get_unused_range()
        if unused:
            self.sprites.animation_data_banks.append(
                AnimationBank(unused[0], unused[1])
            )

        # From battle animation scripts (0x3A bank)
        # Reserve 0x3AFA00-0x3B0000 for item descriptions by limiting battle animations
        self.battle_animations[0x3A].set_bank_end(0x3AFA00)
        unused_ranges = self.battle_animations[0x3A].get_unused_ranges()
        # Add the reserved range for item descriptions (1536 bytes)
        self.items.add_additional_desc_range(0x3AFA00, 0x3B0000)
        # Add unused ranges as animation banks for sprites
        for start, end in unused_ranges:
            self.sprites.animation_data_banks.append(AnimationBank(start, end))

        # From monster AI scripts
        for start, end in self.monster_scripts.get_unused_ranges():
            self.sprites.animation_data_banks.append(AnimationBank(start, end))

        # Sprite graphics patch (now has access to reclaimed animation banks)
        self._report_progress("Assembling graphics...", progress)

        # Sprites 490 (Smithy) and 491 (Smithy extended/"Shyper") must share
        # the same tile group so their subtile ordering matches — battle
        # animation events 82/86 use sprite 491's sequences interchangeably
        # with sprite 490's during the Smithy fight.
        for p in self.sprites.render(shared_image_groups=[[490, 491]]):
            patch.add_data(p[0], p[1], source="sprites")
        progress += 3

        # World map / file-select / overworld walker character overrides
        # are applied below in the non_mario_character block once we've
        # computed `starter` and `i`.

        # fuck you
        if random.randint(0, 100) < 10:
            self.battle_dialogs.battle_messages[38] = "Wanna double you're coins?"

        # Dialogs, enemies, items, packets, battle packs, rooms, shops, spells
        # (Note: overworld_dialogs and action_scripts are rendered earlier for space reclamation)

        # UncapMaxFP: Royal Syrup's vanilla _inflict=99 caps the heal at 99 FP
        # even though the item description reads "Recovers all Flower Pts." Bump
        # to 255 so the heal saturates at whatever max FP the player has (the
        # battle engine clamps at max FP, like Max Mushroom's _inflict=255 does
        # for HP). Must run before self.items.render() below.
        if self.settings.isflag_enabled(UncapMaxFP):
            self.get_item(RoyalSyrupItem).set_inflict(255)

        # Run all render() calls in parallel
        with ThreadPoolExecutor() as executor:
            futures = {
                "battle_dialogs": executor.submit(self.battle_dialogs.render),
                "enemies": executor.submit(self.enemies.render),
                "enemy_attacks": executor.submit(self.enemy_attacks.render),
                "items": executor.submit(self.items.render),
                "packets": executor.submit(self.packets.render),
                "battle_packs": executor.submit(self.battle_packs.render),
                "rooms": executor.submit(self.rooms.render),
                "shops": executor.submit(self.shops.render),
                "spells": executor.submit(self.spells.render),
                "allies": executor.submit(self.allies.render),
                "world_map_locations": executor.submit(self.world_map_locations.render),
            }
            # Wait for all to complete and add results to patch
            for key in [
                "battle_dialogs",
                "enemies",
                "enemy_attacks",
                "items",
                "packets",
                "battle_packs",
                "rooms",
                "shops",
                "spells",
                "allies",
                "world_map_locations",
            ]:
                result = futures[key].result()
                patch.add_dict(result, source=key)
                progress += 2
                self._report_progress("Assembling object data...", progress)

        self._report_progress("Writing patch...", 95)
        credits_data = update_credits(self)
        patch.add_dict(credits_data)

        # Always-on byte patches.
        patch.add_dict(asm.key_item_inventory.get_patch(), source="key_item_inventory")

        # Flag-gated byte patches.
        if (self.settings.is_flag_value(EXPChallenge, EXPChallengeOptions.NONE)
                or self.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE)
                or self.settings.debug_mode):
            patch.add_dict(asm.no_exp.get_patch(), source="no_exp")

        if self.settings.isflag_enabled(ShowEquips):
            patch.add_dict(asm.show_equips.get_patch(), source="show_equips")

        if self.settings.isflag_enabled(UncapMaxFP):
            patch.add_dict(asm.uncap_max_fp.get_patch(), source="uncap_max_fp")

        if self.selected_music_ids:
            patch.add_dict(
                asm.selected_music.get_patch(self.selected_music_ids),
                source="selected_music",
            )

        if self.settings.isflag_enabled(HoldB):
            patch.add_dict(asm.hold_b.get_patch(), source="hold_b")

        if self.settings.isflag_enabled(JapaneseABXY):
            self.sprite_palettes.get_palette(
                SPAL293_ABXY_ACTION_BUTTON_SELECTION_IN_BATTLE
            ).set_colors(
                [
                    0xFFFFFF,
                    0x630000,
                    0xB58C29,
                    0xD6CE4A,
                    0x42944A,
                    0x187B21,
                    0x394294,
                    0x18188C,
                    0x000042,
                    0xFF4A52,
                    0xDE3139,
                    0x312908,
                    0x083110,
                    0x000000,
                    0x000000,
                ]
            )
            self.sprite_palettes.get_palette(
                SPAL379_ABXY_BUTTONS_FROM_BOWYER_S_BUTTON_LOCK
            ).set_colors(
                [
                    0xFFFFFF,
                    0x630000,
                    0x949494,
                    0x4A4A4A,
                    0x42944A,
                    0x187B21,
                    0x394294,
                    0x18188C,
                    0x000042,
                    0xFF4A52,
                    0xDE3139,
                    0x8C3100,
                    0x083110,
                    0x000000,
                    0x000000,
                ]
            )

        starter = cast(CharacterPrize, self.get_location(StartingCharacter1).prize).ally
        self.file_select_character = starter.name

        # World map sprite + file-select graphic + overworld walker hooks
        # + file-select name strings — all character-display patches in
        # one place.
        patch.add_dict(
            asm.non_mario_character.get_patch(
                starter_index=starter.index,
                overworld_index=self.overworld_character.ally.index,
                file_select_names=self.file_select_names,
            ),
            source="non_mario_character",
        )

        if self.settings.isflag_enabled(FixInvincibility):
            patch.add_dict(asm.invincibility_fix.get_patch(), source="invincibility_fix")

        if self.settings.debug_mode:
            patch.add_dict(asm.debug_fp.get_patch(), source="debug_fp")

        # Palettes
        patch.add_dict(self.sprite_palettes.render())
        patch.add_dict(self.event_palettes.render())
        for s in self.spells.spells:
            if isinstance(s, CharacterSpell):
                patch.add_dict(s.palette_patch)

        patch.add_dict(asm.room_174_battlefield.get_patch(), source="room_174_battlefield")
        patch.add_dict(asm.room_325_solidity.get_patch(), source="room_325_solidity")
        patch.add_dict(asm.star_piece_sprite_fix.get_patch(), source="star_piece_sprite_fix")
        patch.add_dict(asm.sprite_group_whitelist.get_patch(), source="sprite_group_whitelist")
        patch.add_dict(asm.battle_init.get_patch(), source="battle_init")
        patch.add_dict(asm.battle_intro_hdma_fix.get_patch(), source="battle_intro_hdma_fix")
        patch.add_dict(asm.exp_star_music_sticky.get_patch(), source="exp_star_music_sticky")

        # Packet allocation patch — allow low-VRAM packets (those with
        # ``goes_to_npc_slot_buffer = True``) to use the NPC slot path
        # instead of the bitmap allocator.
        from ..data.packets.packets import Packet
        npc_slot_packet_ids: set[int] = {
            packet.packet_id
            for packet in self.packets.packets
            if isinstance(packet, Packet) and packet.goes_to_npc_slot_buffer
        }
        patch.add_dict(
            asm.packet_allocation.get_patch(npc_slot_packet_ids),
            source="packet_allocation",
        )

        patch.add_dict(asm.room_layouts.get_patch(), source="room_layouts")

        # Belome 3 spell-block + Enduring Brooch ASM hook (always-on).
        # The blocked-spell list inside the apply-damage helper changes
        # when InfuseSpellElements is on (those infused spells become
        # elemental, and Belome 3's rule is to nullify only
        # NON-elemental spells).
        patch.add_dict(
            asm.belome3_brooch.get_patch(
                infuse_spell_elements=self.settings.isflag_enabled(InfuseSpellElements)
            ),
            source="belome3_brooch",
        )

        # Battlefield underwater-palette whitelist (always-on). Without
        # this, BF14/BF34/BF38 force every actor onto a "+4 palette"
        # path (palette pointer +$78 = 4 × 30-byte monster palettes)
        # and any monster without a real underwater variant reads
        # garbage from a neighbor's palette. The hook gates the path
        # to the curated whitelist in
        # asm/battlefield_underwater_palette.py.
        patch.add_dict(
            asm.battlefield_underwater_palette.get_patch(),
            source="battlefield_underwater_palette",
        )

        # FxPakPro Archipelago NMI hook — DISABLED (proof of concept only).
        # Enabling NMI ($4200 bit 7) during gameplay causes the vanilla NMI handler
        # ($C0:0283) to fire every VBlank. That handler is NOT a no-op — it calls the
        # SA-1 message dispatcher ($0691) which corrupts battle state including
        # $7E0926 (party size). All FxPak/NMI patching is commented out.
        # patch.add_data(NMI_VECTOR_ROM_OFFSET, NMI_VECTOR_NEW)
        # patch.add_data(EMU_NMI_VECTOR_ROM_OFFSET, EMU_NMI_VECTOR_NEW)
        # patch.add_data(TRAMPOLINE_ROM_OFFSET, TRAMPOLINE_CODE)
        # patch.add_data(HOOK_ROM_OFFSET, NMI_HOOK_CODE)
        # for rom_offset, _old, new in NMITIMEN_PATCHES:
        #     patch.add_data(rom_offset, bytes([new]))

        # ROM title + version metadata (SNES header + name-entry screen).
        patch.add_dict(
            asm.rom_metadata.get_patch(seed=self.seed, version=self.version),
            source="rom_metadata",
        )

        # Cache the patch for subsequent calls
        self._cached_patch = patch

        return patch
