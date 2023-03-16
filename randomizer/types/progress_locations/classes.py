from copy import deepcopy
from random import random
from typing import Optional, Type, TypeVar, List
from randomizer.entities.bosses.bosses import MokuraBoss
from randomizer.entities.characters.characters import (
    Bowser,
    BowserSpotted,
    Geno,
    GenoSpotted,
    Mallow,
    MallowSpotted,
    Mario,
    MarioSpotted,
    Toadstool,
    ToadstoolSpotted,
)
from randomizer.entities.items.items import (
    AltoCard,
    Amulet,
    AttackScarf,
    Beetlemania,
    BigBooFlag,
    BrightCard,
    Brooch,
    CarboCookie,
    CastleKey1,
    CastleKey2,
    Chomp,
    CoinTrick,
    Coins1,
    Coins10,
    CricketJam,
    CricketPie,
    Crown,
    DrillClaw,
    DryBonesFlag,
    EarlierTimes,
    ElderKey,
    ExpBooster,
    Feather,
    Fertilizer,
    Fireworks,
    Flower,
    FrogCoin,
    FroggieStick,
    FryingPan,
    GhostMedal,
    GoodieBag,
    GreaperFlag,
    Hammer,
    InfiniteCoins,
    JinxBelt,
    LambsLure,
    LazyShellArmor,
    LazyShellWeapon,
    LuckyJewel,
    Masher,
    MimicFightInitiator2,
    MimicFightInitiator3,
    MultiFrogCoin,
    MysteryEgg,
    NokNokShell,
    PolkaDress,
    ProgressiveCard,
    ProgressiveEgg,
    ProgressiveFireworks,
    QuartzCharm,
    RareFrogCoin,
    RareScarf,
    RecoveryMushroom,
    Ring,
    RoomKey,
    SafetyBadge,
    SafetyRing,
    ScroogeRing,
    SeeYa,
    Seed,
    ShedKey,
    SheepAttack,
    ShinyStone,
    Shoes,
    SignalRing,
    SlapGlove,
    SlotMachineChest,
    SonicCymbal,
    SopranoCard,
    StarEgg,
    StarGun,
    SuperSlap,
    SuperSuit,
    TempleKey,
    TenorCard,
    TroopaPin,
    UltraHammer,
    Wallet,
    YouMissed,
    ZoomShoes,
)
from randomizer.entities.progress_locations.helpers.area_access import (
    can_access_forest,
    can_access_invisible_flags,
    can_defeat_seaside_boss,
    can_defeat_second_moleville_boss,
    progression_safety,
)
from randomizer.entities.spells.spells import SuperJump
from randomizer.types.bosses.classes import Boss
from randomizer.types.characters.classes import Character
from randomizer.types.items.classes import (
    Coins,
    InvincibilityStar,
    Item,
    KeyItem,
    MarrymoreGear,
    MimicFightChestAssignment,
    RegularEquip,
    RegularItem,
    SpecialEquip,
    SpottedCharacter,
    StarPiece,
)
from randomizer.types.npcs.fills.classes import (
    BossModelFill,
    RepeatableHenchmanFill,
    StatueFill,
    UniqueHenchmanFill,
)
from randomizer.types.numbers.classes import Int8, UInt16, UInt8
from randomizer.types.bosses.enums import BattleMusic, Battlefields, BossLocations
from randomizer.types.progress_locations.enums import LocationWorldArea, PacketType
from randomizer.types.progress_locations.utils import get_default_battlefield_from_room
from randomizer.types.overworld_scripts.constants.misc import TOTAL_ROOMS
from randomizer.types.spells.classes import CharacterSpell
from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.enums import (
    BossScaleOptions,
    FireworksOptions,
    ShopQualities,
    ShuffleLocationSelector,
)
from randomizer.types.world.flags.flags import (
    AvailableSpells,
    BossReplaceMinigameSprites,
    BossShuffleScaleStats,
    EXPStarsAnywhere,
    EnabledBossChecks,
    EnabledRegularChecks,
    ExperienceNoRegular,
    FireworksSetting,
    KeyItemsAnywhere,
    MimicsAnywhere,
    RestrictSpecialEquips,
    ShopQuality,
    ShuffleMagikoopaChest,
    ShuffleWeddingGear,
    StarPieceAvailability,
)
from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_EVENTS,
)


class Inventory(List):
    def has_item_count(self, item_type: Type[Item], value=1):
        count = [item for item in self if isinstance(item, item_type)]
        return len(count) >= value

    def has_item(self, item_type: Type[Item]):
        presence = next((item for item in self if isinstance(item, item_type)), None)
        return presence is not None

    def has_one_of(self, item_types: List[Type[Item]]):
        found = False
        for held_item in self:
            for item_type in item_types:
                if isinstance(held_item, item_type):
                    found = True
                    break
        return found


class ProgressLocation:
    _identifier: Optional[int] = None
    _room_ids: List[int] = []
    _accepted_types: List[Type[Item]] = []
    _original_item: Optional[Type[Item]] = None
    _contents: Optional[Item] = None
    _container_event: int = 0
    _missable: bool = False
    _world_area: LocationWorldArea
    _affected_dialog_ids: List[int] = []
    _excluded: bool = False
    _keep_original_item_if_excluded: bool = False
    _allow_empty_when_finished_shuffling: bool = False

    world: GameWorld

    @property
    def room_ids(self) -> List[UInt16]:
        for room_id in self._room_ids:
            assert 0 <= room_id <= TOTAL_ROOMS
        return [UInt16(room_id) for room_id in self._room_ids]

    @property
    def identifier(self) -> Optional[UInt16]:
        """Indicates the room number or arbitrary value specific to this location. Used for decision scripts to build and grant the correct item."""
        if self._identifier is None:
            return self._identifier
        return UInt16(self._identifier)

    def event_builder_identifiers(self) -> List[UInt16]:
        if self.identifier is not None:
            return [UInt16(self.identifier)]
        assert len(self.room_ids) > 0
        return self.room_ids

    @property
    def key_item_location(self) -> bool:
        return self.original_item is not None and issubclass(
            self.original_item, KeyItem
        )

    @property
    def special_equip_location(self) -> bool:
        return self.original_item is not None and issubclass(
            self.original_item, SpecialEquip
        )

    @property
    def star_chest(self) -> bool:
        return self.original_item is not None and issubclass(
            self.original_item, InvincibilityStar
        )

    @property
    def mimic_chest(self) -> bool:
        return self.original_item is not None and issubclass(
            self.original_item, MimicFightChestAssignment
        )

    @property
    def slots_chest(self) -> bool:
        return self.original_item is not None and issubclass(
            self.original_item, SlotMachineChest
        )

    @property
    def original_item(self) -> Optional[Type[Item]]:
        return self._original_item

    @property
    def missable(self) -> bool:
        return self._missable

    def set_missable(self, missable: bool) -> None:
        self._missable = missable

    def set_affected_dialog_ids(self, affected_dialog_ids: List[int]) -> None:
        self._affected_dialog_ids = affected_dialog_ids

    @property
    def affected_dialog_ids(self) -> List[int]:
        return self._affected_dialog_ids

    @property
    def excluded(self) -> bool:
        return self._excluded

    def set_excluded(self, excluded: bool) -> None:
        self._excluded = excluded

    @property
    def allow_empty_when_finished_shuffling(self) -> bool:
        return self._allow_empty_when_finished_shuffling

    def set_allow_empty_when_finished_shuffling(
        self, allow_empty_when_finished_shuffling: bool
    ) -> None:
        self._allow_empty_when_finished_shuffling = allow_empty_when_finished_shuffling

    @property
    def keep_original_item_if_excluded(self) -> bool:
        return self._keep_original_item_if_excluded

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if (self.missable or self.excluded) and (
            isinstance(item, KeyItem) or isinstance(item, StarPiece)
        ):
            return False
        accept: bool = False
        for accepted_class in self._accepted_types:
            if isinstance(item, accepted_class):
                accept = True
                break
        return accept

    def is_vanilla(self) -> bool:
        if self.contents is None and self.original_item is None:
            return True
        elif self.original_item is not None and isinstance(
            self.contents, self.original_item
        ):
            return True
        elif isinstance(self.contents, Coins) and (
            self.original_item is not None and issubclass(self.original_item, Coins)
        ):
            return self.original_item().amount == self.contents.amount
        return False

    @property
    def contents(self) -> Optional[Item]:
        return self._contents

    def set_contents(self, contents: Optional[Item]) -> None:
        if contents is not None:
            assert self.can_accept(contents)
        self._contents = contents

    @property
    def container_event(self) -> UInt16:
        return UInt16(self._container_event)

    def set_container_event(self, container_event: int) -> None:
        assert 0 <= container_event < TOTAL_EVENTS
        self._container_event = container_event

    @property
    def world_area(self) -> LocationWorldArea:
        return self._world_area

    def does_contain(self, item_type: Optional[Type[Item]]) -> bool:
        if self.contents is None and item_type is None:
            return True
        elif self.contents is not None and item_type is not None:
            return isinstance(self.contents, item_type)
        else:
            return False

    def can_access(self, inventory: Inventory) -> bool:
        return True

    def __init__(self, world: GameWorld):
        self.world = world

        if len(self._room_ids) == 0:
            self._room_ids = []
        if len(self._accepted_types) == 0:
            self._accepted_types = []
        if len(self._affected_dialog_ids) == 0:
            self._affected_dialog_ids = []


TProgressLocation = TypeVar("TProgressLocation", bound="ProgressLocation")


class BossFightLocation(ProgressLocation):
    _original_item: Type[Boss]
    _battlefield: Optional[Battlefields] = None
    _name_enum: BossLocations = BossLocations.MUSHROOM_WAY
    _music: BattleMusic = BattleMusic.NORMAL
    _overworld_boss_npc_fills: List[BossModelFill] = []
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = []
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = []
    _statue_fills: List[StatueFill] = []
    _can_run_away: bool = False
    _stat_inheritor: Optional["Type[Boss]"] = None

    # Have a class method here that scales stats

    @property
    def battlefield(self) -> Battlefields:
        if self._battlefield is None:
            assert self.identifier is not None
            return get_default_battlefield_from_room(self.identifier)
        return self._battlefield

    @property
    def name_enum(self) -> BossLocations:
        return self._name_enum

    @property
    def music(self) -> BattleMusic:
        return self._music

    @property
    def original_item(self) -> Type[Boss]:
        return self._original_item

    @property
    def overworld_boss_npc_fills(self) -> List[BossModelFill]:
        """A list of overworld NPCs which will be replaced with the incoming boss' model."""
        return self._overworld_boss_npc_fills

    def set_overworld_boss_npc_fills(
        self, overworld_boss_npc_fills: List[BossModelFill]
    ) -> None:
        self._overworld_boss_npc_fills = overworld_boss_npc_fills

    @property
    def overworld_unique_henchmen_npc_fills(self) -> List[list[UniqueHenchmanFill]]:
        """A list of overworld NPC collections which will be replaced with model and other information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for unique henchmen specifically (i.e. henchmen which were either distinct characters like the Axem Rangers, or belonged to a boss only up to a certain number of repetitions like Bandana Blues)."""
        return self._overworld_unique_henchmen_npc_fills

    def set_overworld_unique_henchmen_npc_fills(
        self, overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]]
    ) -> None:
        self._overworld_unique_henchmen_npc_fills = overworld_unique_henchmen_npc_fills

    @property
    def overworld_generic_henchmen_npc_fills(
        self,
    ) -> List[list[RepeatableHenchmanFill]]:
        """A list of overworld NPC collections which will be replaced with model and other information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for generic henchmen specifically (i.e. henchmen which either respawned infinitely, or existed in quantities large enough to be considered generic, i.e. Shysters or Birdys)."""
        return self._overworld_generic_henchmen_npc_fills

    def set_overworld_generic_henchmen_npc_fills(
        self, overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]]
    ) -> None:
        self._overworld_generic_henchmen_npc_fills = (
            overworld_generic_henchmen_npc_fills
        )

    def set_contents(self, contents: Boss) -> None:
        super().set_contents(contents)

        for loc in self.overworld_boss_npc_fills:
            loc.set_occupant(type(contents))
            for dialog_id in loc.affected_dialog_ids:
                if dialog_id in contents.dialog_replacements:
                    self.world.dialogs.replace_dialog(
                        dialog_id, contents.dialog_replacements[dialog_id]
                    )
                if (
                    dialog_id
                    in contents.dialog_replacements_if_mandatory_fights_changed
                    and self.world.settings.is_boolean_flag_enabled(
                        BossReplaceMinigameSprites
                    )
                ):
                    self.world.dialogs.replace_dialog(
                        dialog_id,
                        contents.dialog_replacements_if_mandatory_fights_changed[
                            dialog_id
                        ],
                    )

        for henchman in self.overworld_unique_henchmen_npc_fills:
            for loc in henchman:
                for dialog_id in loc.affected_dialog_ids:
                    if dialog_id in contents.dialog_replacements:
                        self.world.dialogs.replace_dialog(
                            dialog_id, contents.dialog_replacements[dialog_id]
                        )
                    if (
                        dialog_id
                        in contents.dialog_replacements_if_mandatory_fights_changed
                        and self.world.settings.is_boolean_flag_enabled(
                            BossReplaceMinigameSprites
                        )
                    ):
                        self.world.dialogs.replace_dialog(
                            dialog_id,
                            contents.dialog_replacements_if_mandatory_fights_changed[
                                dialog_id
                            ],
                        )

        for henchman in self.overworld_generic_henchmen_npc_fills:
            for loc in henchman:
                for dialog_id in loc.affected_dialog_ids:
                    if dialog_id in contents.dialog_replacements:
                        self.world.dialogs.replace_dialog(
                            dialog_id, contents.dialog_replacements[dialog_id]
                        )
                    if (
                        dialog_id
                        in contents.dialog_replacements_if_mandatory_fights_changed
                        and self.world.settings.is_boolean_flag_enabled(
                            BossReplaceMinigameSprites
                        )
                    ):
                        self.world.dialogs.replace_dialog(
                            dialog_id,
                            contents.dialog_replacements_if_mandatory_fights_changed[
                                dialog_id
                            ],
                        )

        # don't do any stat calc when vanilla
        if (
            self.original_item == self.stat_inheritor
            and type(contents) == self.original_item
        ):
            return

        if contents.pack_number is None:
            raise Exception("%r needs pack" % contents)
        incoming_pack = self.world.packs[contents.pack_number]
        assert incoming_pack is not None
        incoming_formation_id = incoming_pack.formation_id
        incoming_formation = self.world.formations[incoming_formation_id]
        assert incoming_formation is not None

        original_contents = self.stat_inheritor()
        if original_contents.pack_number is None:
            raise Exception("%r needs pack" % original_contents)
        original_pack = self.world.packs[original_contents.pack_number]
        assert original_pack is not None
        original_formation_id = original_pack.formation_id
        original_formation = self.world.formations[original_formation_id]
        assert original_formation is not None

        (
            hp,
            xp,
            _,
            attack,
            defense,
            magic_attack,
            magic_defense,
            evade,
            magic_evade,
        ) = (
            original_formation.get_summed_stats()
        )  # this already accounts for formations with special stat summing rules like exor, valentina, etc
        (
            _,
            incoming_xp,
            _,
            _,
            _,
            _,
            _,
            _,
            _,
        ) = incoming_formation.get_summed_stats()
        extant_members = [m.enemy for m in incoming_formation.members if m is not None]
        member_classes = extant_members + incoming_formation.additional_enemies_to_scale
        for member in member_classes:
            enemy = self.world.get_enemy_instance(member)
            enemy.set_hp(round(enemy.ratio_hp * hp))
            enemy.set_attack(round(enemy.ratio_attack * attack))
            enemy.set_defense(round(enemy.ratio_defense * defense))
            enemy.set_magic_attack(round(enemy.ratio_magic_attack * magic_attack))
            enemy.set_magic_defense(round(enemy.ratio_magic_defense * magic_defense))
            enemy.set_evade(round(enemy.ratio_evade * evade))
            enemy.set_magic_evade(round(enemy.ratio_magic_evade * magic_evade))

            xp_ratio: float = enemy.xp / incoming_xp
            enemy.set_xp(round(xp_ratio * xp))
            enemy.update_world_entities()

    @property
    def can_run_away(self) -> bool:
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        self._can_run_away = can_run_away

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if not isinstance(item, Boss):
            return False
        if isinstance(item, MokuraBoss):
            assert inventory is not None
            if not inventory.has_one_of(
                [
                    type(spell)
                    for spell in self.world.character_spells
                    if spell.targetEnemies and spell.element == Element.NONE
                ]
            ):
                return False
        return super().can_accept(item)

    @property
    def affected_dialog_ids(self) -> List[int]:
        own_ids = deepcopy(self._affected_dialog_ids)
        fill_ids = [f.affected_dialog_ids for f in self.overworld_boss_npc_fills]
        flattened = [dialog_id for sublist in fill_ids for dialog_id in sublist]
        own_ids.extend(flattened)
        return list(set(own_ids))

    @property
    def stat_inheritor(self) -> "Type[Boss]":
        if self._stat_inheritor is None:
            return self.original_item
        return self._stat_inheritor

    def set_stat_inheritor(self, stat_inheritor: "Type[Boss]") -> None:
        self._stat_inheritor = stat_inheritor

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if self.name_enum in world.settings.get_flag(EnabledBossChecks).disabled:

            self.set_excluded(True)
            self.set_contents(self.original_item(world))

            self._accepted_types = []
        else:

            self._accepted_types = [Boss]
        if len(self._overworld_boss_npc_fills):
            self._overworld_boss_npc_fills = []
        if len(self._overworld_unique_henchmen_npc_fills):
            self._overworld_unique_henchmen_npc_fills = []
        if len(self._overworld_generic_henchmen_npc_fills):
            self._overworld_generic_henchmen_npc_fills = []
        if len(self._statue_fills):
            self._statue_fills = []


class BossStarPiecePrize(ProgressLocation):
    _allow_empty_when_finished_shuffling: bool = True
    _name_enum: ShuffleLocationSelector

    @property
    def name_enum(self) -> ShuffleLocationSelector:
        return self._name_enum

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if self.name_enum in world.settings.get_flag(EnabledBossChecks).disabled:

            self.set_excluded(True)
            self.set_contents(None)

            self._accepted_types = []
        else:
            self._accepted_types = [StarPiece]

    # can_access will require inventory to contain a specific boss. (not boss _location_)
    # how to exclude locations, in that case?
    # check if any boss locations have accepted the corresponding boss yet. if not, skip


class ItemLocation(ProgressLocation):
    _name_enum: Optional[ShuffleLocationSelector]

    @property
    def name_enum(self) -> Optional[ShuffleLocationSelector]:
        return self._name_enum

    def initiate_vanilla(self) -> None:
        if self.original_item is not None:
            self.set_contents(self.world.get_item_instance(self.original_item))

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if self.name_enum in world.settings.get_flag(EnabledRegularChecks).disabled:
            self.set_excluded(True)


class FrogDiscipleShopItem(ItemLocation):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if type(item) not in [
            Hammer,
            FroggieStick,
            NokNokShell,
            Chomp,
            Masher,
            SlapGlove,
            UltraHammer,
            SuperSlap,
            DrillClaw,
            StarGun,
            SonicCymbal,
            LazyShellWeapon,
            FryingPan,
            PolkaDress,
            SuperSuit,
            LazyShellArmor,
            ZoomShoes,
            SafetyBadge,
            SafetyRing,
            Amulet,
            ScroogeRing,
            ExpBooster,
            AttackScarf,
            RareScarf,
            CoinTrick,
            GhostMedal,
            JinxBelt,
            Feather,
            TroopaPin,
            SignalRing,
            QuartzCharm,
            SeeYa,
            GoodieBag,
            EarlierTimes,
            Wallet,
            SheepAttack,
            LambsLure,
            MysteryEgg,
            LuckyJewel,
            StarEgg,
            ProgressiveEgg,
        ]:
            return False

        return super().can_accept(item)


class ChestLocation(ItemLocation):
    _set_70A7_manually_in_event_script: bool = False
    _npc_ids: List[int] = []

    @property
    def set_70A7_manually_in_event_script(self) -> bool:
        return self._set_70A7_manually_in_event_script

    @property
    def npc_ids(self) -> List[UInt8]:
        for id in self._npc_ids:
            assert id <= 27
        return [UInt8(id) for id in self._npc_ids]

    def __init__(self, world: GameWorld):
        super().__init__(world)

        if len(self._npc_ids) == 0:
            self._npc_ids = []

        self._accepted_types = []
        if self.key_item_location and not world.settings.is_boolean_flag_enabled(
            KeyItemsAnywhere
        ):
            self._accepted_types.append(KeyItem)
        elif self.special_equip_location and world.settings.is_boolean_flag_enabled(
            RestrictSpecialEquips
        ):
            self._accepted_types.append(SpecialEquip)
        elif self.star_chest and not world.settings.is_boolean_flag_enabled(
            EXPStarsAnywhere
        ):
            self._accepted_types.append(InvincibilityStar)
        else:
            self._accepted_types.append(RegularItem)
            self._accepted_types.append(RegularEquip)
            self._accepted_types.append(ProgressiveEgg)
            self._accepted_types.append(Beetlemania)
            self._accepted_types.append(YouMissed)
            self._accepted_types.append(Flower)
            self._accepted_types.append(RecoveryMushroom)
            self._accepted_types.append(FrogCoin)
            self._accepted_types.append(MultiFrogCoin)
            if world.settings.is_boolean_flag_enabled(MimicsAnywhere):
                self._accepted_types.append(MimicFightChestAssignment)
            if world.settings.is_boolean_flag_enabled(KeyItemsAnywhere):
                self._accepted_types.append(KeyItem)
            if not world.settings.is_boolean_flag_enabled(RestrictSpecialEquips):
                self._accepted_types.append(SpecialEquip)
            if (
                world.settings.is_boolean_flag_enabled(StarPieceAvailability)
                and random() > 0.7
            ):
                self._accepted_types.append(StarPiece)
            if world.settings.is_boolean_flag_enabled(ShuffleMagikoopaChest):
                self._accepted_types.append(InfiniteCoins)
            if world.settings.is_boolean_flag_enabled(EXPStarsAnywhere):
                self._accepted_types.append(InvincibilityStar)
            if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
                self._accepted_types.append(MarrymoreGear)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.shuffle1
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.progressive
            ):
                self._accepted_types.append(ProgressiveFireworks)

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if isinstance(item, InvincibilityStar):
            chest_locations = [
                location
                for location in self.world.item_locations
                if self.world_area == location.world_area
                and location.does_contain(InvincibilityStar)
            ]
            return len(chest_locations) == 0
        if isinstance(item, InvincibilityStar) and self.world_area not in [
            LocationWorldArea.MushroomWay,
            LocationWorldArea.BanditsWay,
            LocationWorldArea.KeroSewers,
            LocationWorldArea.RoseWay,
            LocationWorldArea.ForestMaze,
            LocationWorldArea.MolevilleMines,
            LocationWorldArea.BoosterTower,
            LocationWorldArea.BoosterPass,
            LocationWorldArea.Sea,
            LocationWorldArea.SunkenShip,
            LocationWorldArea.LandsEnd,
            LocationWorldArea.NimbusCastle,
            LocationWorldArea.BarrelVolcano,
        ]:
            return False
        return super().can_accept(item, inventory)


class EarlygameChestLocation(ChestLocation):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if progression_safety(self.world) and (
            isinstance(item, MimicFightInitiator2)
            or isinstance(item, MimicFightInitiator3)
        ):
            return False
        return super().can_accept(item)


class MidgameChestLocation(ChestLocation):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if progression_safety(self.world) and isinstance(item, MimicFightInitiator3):
            return False
        return super().can_accept(item)


class ChestLocationAllowCoins(ChestLocation):
    def __init__(self, world: GameWorld):
        super().__init__(world)

        allowed_items = deepcopy(self._accepted_types)
        allowed_items.append(Coins)
        self._accepted_types = allowed_items


class ChestLocationAllowSlots(ChestLocationAllowCoins):
    def __init__(self, world: GameWorld):
        super().__init__(world)

        allowed_items = deepcopy(self._accepted_types)
        allowed_items.append(SlotMachineChest)
        self._accepted_types = allowed_items


class MimicReloadRewardChest(ChestLocation):
    def set_room_ids(self, room_ids: List[UInt16]) -> None:
        self._room_ids = [int(room) for room in room_ids]


class GrantLocation(ItemLocation):
    def __init__(self, world: GameWorld):
        super().__init__(world)

        self._accepted_types = []
        if self.key_item_location and not world.settings.is_boolean_flag_enabled(
            KeyItemsAnywhere
        ):
            self._accepted_types.append(KeyItem)
        elif self.special_equip_location and world.settings.is_boolean_flag_enabled(
            RestrictSpecialEquips
        ):
            self._accepted_types.append(SpecialEquip)
        else:
            self._accepted_types.append(RegularItem)
            self._accepted_types.append(RegularEquip)
            self._accepted_types.append(Coins)
            self._accepted_types.append(ProgressiveEgg)
            self._accepted_types.append(Beetlemania)
            self._accepted_types.append(FrogCoin)
            self._accepted_types.append(MultiFrogCoin)
            if world.settings.is_boolean_flag_enabled(KeyItemsAnywhere):
                self._accepted_types.append(KeyItem)
            if not world.settings.is_boolean_flag_enabled(RestrictSpecialEquips):
                self._accepted_types.append(SpecialEquip)
            if (
                world.settings.is_boolean_flag_enabled(StarPieceAvailability)
                and random() > 0.7
            ):
                self._accepted_types.append(StarPiece)
            if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
                self._accepted_types.append(MarrymoreGear)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.shuffle1
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.progressive
            ):
                self._accepted_types.append(ProgressiveFireworks)


class InvisibleItemCandidate(GrantLocation):
    _x_coord: int = 0
    _y_coord: int = 0
    _z_coord: int = 0
    _x_shift: int = 0
    _y_shift: int = 0
    _clue_text: str = ""

    @property
    def key_item_location(self) -> bool:
        return True

    # needs a container event

    @property
    def clue_text(self) -> str:
        return self._clue_text

    @property
    def x_coord(self) -> UInt8:
        return UInt8(self._x_coord)

    @property
    def y_coord(self) -> UInt8:
        return UInt8(self._y_coord)

    @property
    def z_coord(self) -> UInt8:
        return UInt8(self._z_coord)

    @property
    def x_shift(self) -> Int8:
        return Int8(self._x_shift)

    @property
    def y_shift(self) -> Int8:
        return Int8(self._y_shift)

    def can_access(self, parent_class: Type[TProgressLocation], inventory: Inventory):
        return parent_class.can_access(self, inventory) and can_access_invisible_flags(
            self.world, inventory
        )


class TreasureShopItem(ItemLocation):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if type(item) not in [
            Hammer,
            FroggieStick,
            NokNokShell,
            Chomp,
            Masher,
            SlapGlove,
            UltraHammer,
            SuperSlap,
            DrillClaw,
            StarGun,
            SonicCymbal,
            LazyShellWeapon,
            FryingPan,
            PolkaDress,
            SuperSuit,
            LazyShellArmor,
            ZoomShoes,
            SafetyBadge,
            SafetyRing,
            Amulet,
            ScroogeRing,
            ExpBooster,
            AttackScarf,
            RareScarf,
            CoinTrick,
            GhostMedal,
            JinxBelt,
            Feather,
            TroopaPin,
            SignalRing,
            QuartzCharm,
            SeeYa,
            TempleKey,
            GoodieBag,
            EarlierTimes,
            RareFrogCoin,
            Wallet,
            CricketPie,
            CastleKey1,
            CastleKey2,
            SheepAttack,
            CarboCookie,
            ShinyStone,
            RoomKey,
            ElderKey,
            ShedKey,
            LambsLure,
            MysteryEgg,
            LuckyJewel,
            SopranoCard,
            AltoCard,
            TenorCard,
            Seed,
            Fertilizer,
            BigBooFlag,
            DryBonesFlag,
            GreaperFlag,
            CricketJam,
            Fireworks,
            BrightCard,
            StarEgg,
            ProgressiveCard,
            ProgressiveEgg,
            ProgressiveFireworks,
            Beetlemania,
            Shoes,
            Brooch,
            Ring,
            Crown,
        ]:
            return False

        return super().can_accept(item)

    def can_access(self, inventory: Inventory):
        return can_defeat_second_moleville_boss(self.world, inventory)


class StartingItemGrant(GrantLocation):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item) and item.consumable

    def __init__(self, world: GameWorld):
        super().__init__(world)
        self.initiate_vanilla()


class FreestandingLocation(ItemLocation):
    _npc_ids: List[int] = []
    _keep_original_item_if_excluded: bool = True

    @property
    def npc_ids(self) -> List[UInt8]:
        for id in self._npc_ids:
            assert id <= 27
        return [UInt8(id) for id in self._npc_ids]

    def __init__(self, world: GameWorld):
        super().__init__(world)

        if len(self._npc_ids) == 0:
            self._npc_ids = []

        self._accepted_types = []
        if self.key_item_location and not world.settings.is_boolean_flag_enabled(
            KeyItemsAnywhere
        ):
            self._accepted_types.append(KeyItem)
        else:
            self._accepted_types.append(RegularItem)
            self._accepted_types.append(RegularEquip)
            self._accepted_types.append(Coins1)
            self._accepted_types.append(Coins10)
            self._accepted_types.append(ProgressiveEgg)
            self._accepted_types.append(Beetlemania)
            self._accepted_types.append(FrogCoin)
            self._accepted_types.append(Flower)
            self._accepted_types.append(RecoveryMushroom)
            if world.settings.is_boolean_flag_enabled(KeyItemsAnywhere):
                self._accepted_types.append(KeyItem)
            if not world.settings.is_boolean_flag_enabled(RestrictSpecialEquips):
                self._accepted_types.append(SpecialEquip)
            if (
                world.settings.is_boolean_flag_enabled(StarPieceAvailability)
                and random() > 0.7
            ):
                self._accepted_types.append(StarPiece)
            if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
                self._accepted_types.append(MarrymoreGear)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.shuffle1
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.progressive
            ):
                self._accepted_types.append(ProgressiveFireworks)


class MidasRiverTunnelItem(FreestandingLocation):
    _midas_action_script: int = 0

    @property
    def midas_action_script(self) -> UInt16:
        return UInt16(self._midas_action_script)


class PacketItem(FreestandingLocation):
    _creation_script: int = 0
    _packet_type: PacketType = PacketType.Static

    @property
    def creation_script(self) -> UInt16:
        return UInt16(self._creation_script)

    @property
    def packet_type(self) -> PacketType:
        return self._packet_type


class CharacterSpottedLocation(ProgressLocation):
    _original_item: Optional[Type[SpottedCharacter]]

    def __init__(self, world: GameWorld):
        super().__init__(world)

        self._accepted_types = [SpottedCharacter]


def _equivalent_spotted_character(char_class: Character) -> Type[SpottedCharacter]:
    if isinstance(char_class, Mario):
        return MarioSpotted
    elif isinstance(char_class, Mallow):
        return MallowSpotted
    elif isinstance(char_class, Geno):
        return GenoSpotted
    elif isinstance(char_class, Bowser):
        return BowserSpotted
    elif isinstance(char_class, Toadstool):
        return ToadstoolSpotted
    else:
        raise Exception("what did you try to put in this location?")


class CharacterReplacementFill:

    _room_id: int
    _npc_id: int
    _event_scripts: List[int]
    _action_scripts: List[int]

    @property
    def room_id(self) -> int:
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        self._room_id = room_id

    @property
    def npc_id(self) -> int:
        return self._npc_id

    def set_npc_id(self, npc_id: int) -> None:
        self._npc_id = npc_id

    @property
    def event_scripts(self) -> List[int]:
        return self._event_scripts

    def set_event_scripts(self, event_scripts: List[int]) -> None:
        self._event_scripts = event_scripts

    @property
    def action_scripts(self) -> List[int]:
        return self._action_scripts

    def set_action_scripts(self, action_scripts: List[int]) -> None:
        self._action_scripts = action_scripts

    def __init__(
        self,
        room_id: int,
        npc_id: int,
        event_scripts: List[int] = [],
        action_scripts: List[int] = [],
    ) -> None:
        self.set_room_id(room_id)
        self.set_npc_id(npc_id)
        self.set_event_scripts(event_scripts)
        self.set_action_scripts(action_scripts)


class CharacterRecruitLocation(ProgressLocation):
    _original_item: Optional[Type[Character]]
    _fills: List[CharacterReplacementFill] = []
    _credits_fills: List[CharacterReplacementFill] = []
    _doll_fills: List[CharacterReplacementFill] = []

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = CharacterSpottedLocation

    @property
    def associated_spotted_location(self) -> Type[CharacterSpottedLocation]:
        return self._associated_spotted_location

    @property
    def fills(self) -> List[CharacterReplacementFill]:
        return self._fills

    @property
    def credits_fills(self) -> List[CharacterReplacementFill]:
        return self._credits_fills

    @property
    def doll_fills(self) -> List[CharacterReplacementFill]:
        return self._doll_fills

    # when setting contents, set associated spotted to world instance of character
    def set_contents(
        self, contents: Optional[Character], related: Type[CharacterSpottedLocation]
    ) -> None:
        super().set_contents(contents)
        equivalent_spotted_location = self.world.get_location_instance(related)
        if contents is not None:
            spotted_char = _equivalent_spotted_character(contents)
            spotted_char_instance = self.world.get_spotted_character_instance(
                spotted_char
            )
        else:
            spotted_char = None
            spotted_char_instance = None
        equivalent_spotted_location.set_contents(spotted_char_instance)

    def __init__(self, world: GameWorld):
        super().__init__(world)

        if len(self._fills) == 0:
            self._fills = []
        if len(self._credits_fills) == 0:
            self._credits_fills = []
        if len(self._doll_fills) == 0:
            self._doll_fills = []

        self._accepted_types = [Character]


class CharacterSpellSlot(ProgressLocation):
    def __init__(self, world: GameWorld):
        super().__init__(world)

        self._accepted_types = [CharacterSpell]


class LaterSpellSlot(CharacterSpellSlot):
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if self.world.settings.is_boolean_flag_enabled(ExperienceNoRegular):
            assert inventory is not None
            # Do not place Super Jump in a late spell slot if character may not be able to earn EXP to get it.
            if SuperJump in self.world.settings.get_flag(AvailableSpells).enabled:
                if not inventory.has_item(SuperJump):
                    return False
            # Do not start placing spells in later slots until at least one enemy-targeting spell has been placed as the starting spell for a character we have access to.
            else:
                if not inventory.has_one_of(
                    [
                        type(spell)
                        for spell in self.world.character_spells
                        if spell.targetEnemies
                    ]
                ):
                    return False
        return super().can_accept(item)


class MarioSpellSlot(CharacterSpellSlot):
    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Mario)


class MallowSpellSlot(CharacterSpellSlot):
    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Mallow)


class GenoSpellSlot(CharacterSpellSlot):
    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Geno)


class BowserSpellSlot(CharacterSpellSlot):
    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Bowser)


class ToadstoolSpellSlot(CharacterSpellSlot):
    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Toadstool)
