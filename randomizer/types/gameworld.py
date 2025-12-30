from __future__ import annotations
from typing import Any, Callable, TypeVar, cast
import random
import hashlib
import re
from copy import copy
from concurrent.futures import ThreadPoolExecutor

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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
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
from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection
from smrpgpatchbuilder.datatypes.scripts_common.classes import IdentifierException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    RunEventAsSubroutine,
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
)
from .ally import Ally
from .prizelocation import (
    PrizeLocation,
)
from ..progression.prizelocations import *
from ..data.variables.dialog_names import *
from ..data.variables.battle_variable_names import *
from ..data.variables.battle_effect_names import *
from ..data.variables.shop_names import *
from ..data.variables.sprite_names import *
from ..data.spells.spells import *
from ..data.credits.credits import update_credits
from ..logic.setup.gating import apply_gating_settings
from ..logic.setup.thresholds import apply_threshold_settings
from ..logic.setup.enemy_tweaks import apply_enemy_tweaks
from ..logic.setup.equipment_setup import apply_equipment_settings
from ..logic.setup.minigames_setup import apply_minigame_settings
from ..logic.setup.cosmetics import apply_cosmetic_settings
from ..logic.setup.prize_locations import set_locations
from ..logic.shufflers.items import shuffle_prizes, post_shuffle_cleanup
from ..logic.validation import validate_settings
from ..logic.shufflers.shops import shuffle_shops
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
from ..logic.apply import apply_shuffler_results

from ..data.allies.palettes.types import (
    MarioPalette,
    MallowPalette,
    GenoPalette,
    BowserPalette,
    ToadstoolPalette,
)
from .enemy import Enemy

PrizeLocationT = TypeVar("PrizeLocationT", bound=PrizeLocation)
from .settings import Settings


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
    poison_mushroom_status: str | None = None
    song_1: str = "So La Mi Re Do Re Do Re"
    song_2: str = "Mi Do So Do Re La Ti Do"
    song_3: str = "La Ti Do Re So Do Re Mi"
    password_author: str = "ANONYMOUS"
    song_authors: list[str] = ["ANONYMOUS"]

    # Text-based shop items (set by shuffle_shops)
    room_service_items: list[type] = [PickMeUpItem, KerokeroColaItem]
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

    event_2496_startup = []

    @property
    def spoiler(self) -> dict[str, Any]:
        result = {
            "settings": self._get_settings_json(),
            "locations": self._get_locations_json(),
            "shops": self._get_shops_json(),
            "password": self.password,
            "songs": [self.song_1, self.song_2, self.song_3],
        }
        if self.poison_mushroom_status:
            result["poison_mushroom_status"] = self.poison_mushroom_status
        return result

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

        result: dict[str, list[str]] = {}
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
        progress_callback: Callable[[str, int], None] | None = None,
    ):
        print(seed)
        print(settings.flag_string)
        self._progress_callback = progress_callback
        self._report_progress("Importing game data", 1)
        self.allies = allies
        self.seed = seed
        self.version = version
        self.settings = settings
        self._prize_type_to_location = {}
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
        self.rooms = rooms
        self.shops = shops
        self.spells = spells
        self.sprites = sprites
        self.world_map_locations = world_map_locations

        random.seed(self.seed)

        self.event_2496_startup: list[UsableEventScriptCommand] = []

        self._report_progress("Applying settings to game data", 3)

        # prize locations HAVE to all be defined by this point
        # not shuffled, just determined if they exist in the seed or not

        if self.settings.isflag_enabled(SkipMustyFearsSequence):
            self.event_2496_startup += [
                RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER)
            ]

        # Apply progression gating settings (win conditions, area gates, travel)
        apply_gating_settings(self)

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

        # Validate settings combinations before shuffling
        # This catches invalid combinations early with clear error messages
        validate_settings(self.settings)

        from ..logic.placement import PlacementException

        # Track failure counts to detect unsolvable settings
        # Key = number of unplaced items, Value = count of times this failure occurred
        failure_counts: dict[int, int] = {}
        MAX_FAILURES_PER_COUNT = 5

        success = False
        while not success:
            try:
                print("retrying...")
                self._shuffle_items()
                print("success!")
                success = True
            except PlacementException as e:
                # Track this failure count
                count = e.unplaced_count
                failure_counts[count] = failure_counts.get(count, 0) + 1
                print(
                    f"Placement failed with {count} unplaced items (attempt #{failure_counts[count]} for this count)"
                )

                # Check if all failure counts have reached the threshold
                if failure_counts and all(
                    v >= MAX_FAILURES_PER_COUNT for v in failure_counts.values()
                ):
                    raise WorldBuildingException(
                        f"Item placement appears unsolvable. "
                        f"Repeated failures with the same unplaced item counts: {failure_counts}. "
                        f"The chosen settings with excluded locations may be impossible to solve. "
                        f"Unplaced items on last attempt: {e.unplaced_items}"
                    )
            except Exception as e:
                # Re-raise unexpected exceptions
                raise

        # TODO Stat scaling for boss shuffle
        # TODO: Henchmen vs no henchmen, hill/statue or not
        # TODO: NPCs, dialogs for bosses and henchmen
        # TODO: Do search-and-replace for all pronouns, names, etc related to main characters, positioned bosses, etc
        # TODO: slot machines
        # TODO: booster tower animations
        # TODO: copy sprites over and update menu pointers and set to 8-d in vram
        # TODO: look at 0x35xxxx report and free up data
        # TODO: message tonic

        self._report_progress("Randomizing shops", 45)

        # Shop shuffling happens after equipment randomization so we can score equipment
        if self.settings.isflag_enabled(ShuffleShops):
            self._shuffle_shops()

        self._report_progress("Randomizing enemies", 50)
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
        self._report_progress("Randomizing characters", 55)

        # Randomize character stats
        if self.settings.isflag_enabled(CharacterStats):
            self._randomize_character_stats()
            self._randomize_levelup_xps()

        # Randomize character spell stats
        if self.settings.isflag_enabled(CharacterSpellStats):
            self._randomize_character_spell_stats()

        # Apply EXP multiplier
        self._apply_exp_multiplier()
        self._report_progress("Applying minigame settings", 60)

        # Apply minigame settings
        apply_minigame_settings(self)

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
        self._report_progress("Applying cosmetics", 70)

        # Apply cosmetic settings (re-seeded for variation between generations)
        apply_cosmetic_settings(self)

        import json

        with open("spoiler_after_replacements.json", "w") as f:
            json.dump(self.spoiler, f, indent=2, default=str)

    def _shuffle_items(self):

        # determine which checks exist in this seed

        self._report_progress("Building check list", 5)
        # this doesn't mean which ones are shuffled, it means which ones can be accessed at all
        # exclusions would be things like remake checks, surplus invisible item checks, super jump prizes when super jump not usable
        set_locations(self)

        # shuffle according to settings
        shuffle_prizes(self)

        self._report_progress("Applying cleanup settings", 39)
        # replace bad items with coins, supplant YouMissed, etc

        # Write spoiler to JSON file
        import json

        with open("spoiler.json", "w") as f:
            json.dump(self.spoiler, f, indent=2, default=str)

        post_shuffle_cleanup(self)
        apply_shuffler_results(self)

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

    def get_patch(self) -> Patch:
        self._report_progress("Rendering game data", 75)
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
        self._report_progress("Rendering (parallel)", 85)
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
        self._report_progress("Rendering palettes", 95)

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
            SPR0014_BOWSER_WALKING_DOWN_LEFT,
            SPR0028_GENO_WALKING_DOWN_LEFT,
            SPR0021_MALLOW_WALKING_DOWN_LEFT,
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

        self._report_progress("Complete", 100)
        return patch
