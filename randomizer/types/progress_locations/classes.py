"""Base classes for any location in the game that can grant you progression.
A location can be a boss fight initiator, a character's capacity to learn a spell,
a character recruitment opportunity, or an item granter."""

from copy import deepcopy
from random import choice, random
from typing import Optional, Tuple, Type, TypeVar, List, Union, TYPE_CHECKING

from randomizer.entities.bosses.bosses import MokuraBoss
from randomizer.entities.characters.characters import (
    Bowser,
    Geno,
    Mallow,
    Mario,
    Toadstool,
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
    can_access_invisible_flags,
    can_defeat_second_moleville_boss,
    progression_safety,
)
from randomizer.entities.spells.spells import SuperJump

from randomizer.types.bosses import (
    Boss,
    Henchman,
    BattleMusic,
    Battlefields,
    BossLocations,
    HenchmanType,
    SpriteSize,
)
from randomizer.types.characters import Character
from randomizer.types.items import (
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
from randomizer.types.npcs.objects.animations.types import SpriteAnimation
from randomizer.types.npcs.fills import (
    BossModelFill,
    RepeatableHenchmanFill,
    StatueFill,
    UniqueHenchmanFill,
)
from randomizer.types.npcs.objects import VramStore, Empty
from randomizer.data.npcs.npcs import RedSmallToad
from randomizer.types.numbers import Int8, UInt16, UInt8
from randomizer.types.overworld_scripts.action_scripts.commands import (
    SetSpriteSequence,
)
from randomizer.types.overworld_scripts.event_scripts.commands.types import (
    ActionSubcriptCommandPrototype,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    TOTAL_SCRIPTS as TOTAL_EVENTS,
)
from randomizer.types.overworld_scripts.ids import TOTAL_ROOMS
from randomizer.types.rooms import (
    BattlePackClone,
    BattlePackNPC,
    RoomObject,
)
from randomizer.types.spells import CharacterSpell, Element
from randomizer.types.spells.classes import CloneSpell
from randomizer.types.world.flags import (
    FireworksOptions,
    ShuffleLocationSelector,
    AvailableSpells,
    BossReplaceMinigameSprites,
    EXPStarsAnywhere,
    EnabledBossChecks,
    EnabledRegularChecks,
    ExperienceNoRegular,
    FireworksSetting,
    KeyItemsAnywhere,
    MimicsAnywhere,
    RestrictSpecialEquips,
    ShuffleMagikoopaChest,
    ShuffleWeddingGear,
    StarPieceAvailability,
)

from .enums import LocationWorldArea, PacketType
from .table import get_default_battlefield_from_room


if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class Inventory(List):
    """A list of items, boss fights, spells, and characters the player is assumed
    to have collected."""

    def has_item_count(self, item_type: Type[Item], value=1):
        """The amount of a given item class collected."""
        count = [item for item in self if isinstance(item, item_type)]
        return len(count) >= value

    def has_item(self, item_type: Type[Item]):
        """Returns true if at least one of the given class is collected."""
        presence = next((item for item in self if isinstance(item, item_type)), None)
        return presence is not None

    def has_one_of(self, item_types: List[Type[Item]]):
        """Returns true of at least one of any of the given classes is collected."""
        found = False
        for held_item in self:
            for item_type in item_types:
                if isinstance(held_item, item_type):
                    found = True
                    break
        return found


class ProgressLocation:
    """Anything that can grant you progression: a boss fight initiator,
    a character's capacity to learn a spell, a character recruitment opportunity,
    or an item granter."""

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
    _tier: int = 4

    world: "GameWorld"

    @property
    def room_ids(self) -> List[UInt16]:
        """A list of all rooms which this location is found in.\n
        For example, the treasure chest in the mushroom kingdom hallway can be opened
        in both the occupied and unoccupied states of the mushroom kingdom, which are
        separate rooms, but the chest can only be opened once regardless of which room
        it was in.\n
        It is recommended to use room ID constant names for this."""
        for room_id in self._room_ids:
            assert 0 <= room_id <= TOTAL_ROOMS
        return [UInt16(room_id) for room_id in self._room_ids]

    @property
    def identifier(self) -> Optional[UInt16]:
        """Indicates the room number or arbitrary value specific to this location.
        Used for decision scripts to build and grant the correct item."""
        if self._identifier is None:
            return self._identifier
        return UInt16(self._identifier)

    @property
    def event_builder_identifiers(self) -> List[UInt16]:
        """Most item grant and boss fight location granters will run one of a small handful of
        designated scripts, each of which gives you the intended item depending usually on
        what room you are currently in. There are some exceptions where a number has to be used
        that would be an illegal value for any room, like 514, 515, etc - these are typically used
        when the same NPC in the same room is responsible for granting you multiple things, and the
        game needs to determine which of those things you are getting.\n
        This returns the specific number that a granter script looks for when making sure it is
        giving you the right thing."""
        if self.identifier is not None:
            return [UInt16(self.identifier)]
        assert len(self.room_ids) > 0
        return self.room_ids

    @property
    def key_item_location(self) -> bool:
        """If true, this location originally held a key (special) item."""
        return self.original_item is not None and issubclass(
            self.original_item, KeyItem
        )

    @property
    def special_equip_location(self) -> bool:
        """If true, this location originally held a key (special) equipment.\n
        This includes Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost
        Medal, Lazy Shell (both kinds), Zoom Shoes, FroggieStick, and Chomp."""
        return self.original_item is not None and issubclass(
            self.original_item, SpecialEquip
        )

    @property
    def star_chest(self) -> bool:
        """If true, this chest originally housed an EXP star."""
        return self.original_item is not None and issubclass(
            self.original_item, InvincibilityStar
        )

    @property
    def mimic_chest(self) -> bool:
        """If true, this chest originally housed a mimic chest battle."""
        return self.original_item is not None and issubclass(
            self.original_item, MimicFightChestAssignment
        )

    @property
    def slots_chest(self) -> bool:
        """If true, this chest originally housed a slot machine."""
        return self.original_item is not None and issubclass(
            self.original_item, SlotMachineChest
        )

    @property
    def original_item(self) -> Optional[Type[Item]]:
        """The item originally held by this location before shuffling."""
        return self._original_item

    @property
    def missable(self) -> bool:
        """If true, it is possible for this location to become permanently missable.\n
        These locations are never granted things that are required for progression."""
        return self._missable

    def set_missable(self, missable: bool) -> None:
        """If true, it is possible for this location to become permanently missable.\n
        These locations are never granted things that are required for progression."""
        self._missable = missable

    @property
    def affected_dialog_ids(self) -> List[int]:
        """A list of dialog IDs that will need to undergo changes to reflect the contents
        of this grant location.\n
        It is recommended to use dialog ID constant names for this."""
        return self._affected_dialog_ids

    def set_affected_dialog_ids(self, affected_dialog_ids: List[int]) -> None:
        """Overwrite the list of dialog IDs that will need to undergo changes to reflect
        the contents of this grant location.\n
        It is recommended to use dialog ID constant names for this."""
        self._affected_dialog_ids = affected_dialog_ids

    @property
    def excluded(self) -> bool:
        """If true, this location is excluded as a candidate for logical progression,
        usually by request of the player."""
        return self._excluded

    def set_excluded(self, excluded: bool) -> None:
        """If true, this location cannot be a candidate for logical progression."""
        self._excluded = excluded

    @property
    def allow_empty_when_finished_shuffling(self) -> bool:
        """If false, this location cannot be empty, and should be filled if it is still
        empty after shuffling has finished."""
        return self._allow_empty_when_finished_shuffling

    def set_allow_empty_when_finished_shuffling(
        self, allow_empty_when_finished_shuffling: bool
    ) -> None:
        """If false, this location cannot be empty, and should be filled if it is still
        empty after shuffling has finished."""
        self._allow_empty_when_finished_shuffling = allow_empty_when_finished_shuffling

    @property
    def keep_original_item_if_excluded(self) -> bool:
        """If true, this location will keep its original item if it has been manually
        excluded as a progression candidate."""
        return self._keep_original_item_if_excluded

    @property
    def tier(self) -> int:
        return self._tier

    # pylint: disable=W0613
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        """Returns true if this location is allowed to house items of the given type.\n
        For example, a boss fight location needs to house a boss fight, and cannot take
        character grants, etc."""
        if (self.missable or self.excluded) and isinstance(item, (StarPiece, KeyItem)):
            return False
        for accepted_class in self._accepted_types:
            if isinstance(item, accepted_class):
                return True
        return False

    def is_vanilla(self) -> bool:
        """If true, the contents of this location after shuffling are the same as its
        original contents."""
        if self.contents is None and self.original_item is None:
            return True
        if self.original_item is not None:
            original_item: Type[Item] = self.original_item
            # pylint: disable=W1116
            if isinstance(self.contents, original_item):
                return True
            if isinstance(self.contents, Coins) and issubclass(original_item, Coins):
                # pylint: disable=E1102
                return original_item().amount == self.contents.amount
        return False

    def is_vanilla_model(self) -> bool:
        """If true, the contents of this location after shuffling are graphically identical
        to its original contents, but may not necessarily be the same. i.e. Croco1 vs Croco2
        """
        return self.is_vanilla()

    @property
    def contents(self) -> Optional[Item]:
        """The current contents of this location."""
        return self._contents

    def set_contents(self, contents: Optional[Item]) -> None:
        """Set the current contents of this location."""
        if contents is not None:
            assert self.can_accept(contents)
        self._contents = contents

    @property
    def container_event(self) -> UInt16:
        """The "entry" event for this location. The event that will run when you interact with
        whatever is supposed to grant you something.\n
        An "entry" event is the event that checks what room (in most cases) you're currently in,
        and then grants the intended item based on that check.\n
        For example, consider a room with two treasure chests: one is meant to grant you a
        mushroom, and the other is meant to grant you a honey syrup. The mushroom chest might
        have its container event set to 247, and the honey syrup chest might have its container
        event set to 246. Inside both 247 and 246, is a huge list of if-statements that perform a
        certain action based on what room you're in. When event 247 detects you're in this room, it
        gives you a mushroom. When event 246 detects you're in this room, it gives you a
        Honey Syrup. Another room with two chests would also use 247 and 246, but the items it
        grants you by the same logic would be different."""
        return UInt16(self._container_event)

    def set_container_event(self, container_event: int) -> None:
        """Set the "entry" event for this location. The event that will run when you interact with
        whatever is supposed to grant you something.\n
        An "entry" event is the event that checks what room (in most cases) you're currently in,
        and then grants the intended item based on that check.\n
        For example, consider a room with two treasure chests: one is meant to grant you a
        mushroom, and the other is meant to grant you a honey syrup. The mushroom chest might
        have its container event set to 247, and the honey syrup chest might have its container
        event set to 246. Inside both 247 and 246, is a huge list of if-statements that perform a
        certain action based on what room you're in. When event 247 detects you're in this room, it
        gives you a mushroom. When event 246 detects you're in this room, it gives you a
        Honey Syrup. Another room with two chests would also use 247 and 246, but the items it
        grants you by the same logic would be different."""
        assert 0 <= container_event < TOTAL_EVENTS
        self._container_event = container_event

    @property
    def world_area(self) -> LocationWorldArea:
        """The overarching world area containing this location."""
        return self._world_area

    def does_contain(self, item_type: Optional[Type[Item]]) -> bool:
        """Checks whether or not the location contains the given item type."""
        if self.contents is None and item_type is None:
            return True
        if self.contents is not None and item_type is not None:
            return isinstance(self.contents, item_type)
        return False

    # pylint: disable=W0613
    def can_access(self, inventory: Inventory) -> bool:
        """Based on the items in the Inventory list, return whether or not this
        location is accessible.\n
        For example, the final Moleville fight is not accessible if the inventory
        lacks the Bambino bomb."""
        return True

    def __init__(self, world: "GameWorld"):
        self.world = world

        if len(self._room_ids) == 0:
            self._room_ids = []
        if len(self._accepted_types) == 0:
            self._accepted_types = []
        if len(self._affected_dialog_ids) == 0:
            self._affected_dialog_ids = []


ProgressLocationT = TypeVar("ProgressLocationT", bound="ProgressLocation")


class BossFightLocation(ProgressLocation):
    """A location that houses a shuffled boss fight."""

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
        """Provides the battlefield that the enclosed battle should take place on.\n
        Respects battlefields that certain bosses MUST use, but otherwise, will simply
        load a battlefield based on what room the location is in."""
        if self._battlefield is None:
            assert self.identifier is not None
            return get_default_battlefield_from_room(self.identifier)
        return self._battlefield

    @property
    def name_enum(self) -> BossLocations:
        """A unique identifier for this location among all boss locations."""
        return self._name_enum

    @property
    def music(self) -> BattleMusic:
        """The music that should normally play in this location."""
        return self._music

    @property
    def original_item(self) -> Type[Boss]:
        """The boss fight that originally was at this location."""
        return self._original_item

    @property
    def overworld_boss_npc_fills(self) -> List[BossModelFill]:
        """A list of overworld NPCs which will be replaced with the incoming boss' model."""
        return self._overworld_boss_npc_fills

    def set_overworld_boss_npc_fills(
        self, overworld_boss_npc_fills: List[BossModelFill]
    ) -> None:
        """Overwrite the list of overworld NPCs which will be replaced with the incoming
        boss' model. (I don't remember why this is modifiable)"""
        self._overworld_boss_npc_fills = overworld_boss_npc_fills

    @property
    def overworld_unique_henchmen_npc_fills(self) -> List[list[UniqueHenchmanFill]]:
        """A list of overworld NPC collections which will be replaced with model and other
        information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for unique henchmen specifically (i.e. henchmen which were either
        distinct characters like the Axem Rangers, or belonged to a boss only up to a certain
        number of repetitions like Bandana Blues)."""
        return self._overworld_unique_henchmen_npc_fills

    def set_overworld_unique_henchmen_npc_fills(
        self, overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]]
    ) -> None:
        """Set the list of overworld NPC collections which will be replaced with model and other
        information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for unique henchmen specifically (i.e. henchmen which were either
        distinct characters like the Axem Rangers, or belonged to a boss only up to a certain
        number of repetitions like Bandana Blues)."""
        self._overworld_unique_henchmen_npc_fills = overworld_unique_henchmen_npc_fills

    @property
    def overworld_generic_henchmen_npc_fills(
        self,
    ) -> List[list[RepeatableHenchmanFill]]:
        """A list of overworld NPC collections which will be replaced with model and other
        information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for generic henchmen specifically (i.e. henchmen which either
        respawned infinitely, or existed in quantities large enough to be considered generic,
        i.e. Shysters or Birdys)."""
        return self._overworld_generic_henchmen_npc_fills

    def set_overworld_generic_henchmen_npc_fills(
        self, overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]]
    ) -> None:
        """Set a list of overworld NPC collections which will be replaced with model and other
        information from incoming boss henchmen.

        Each item in a list of NPC locations will be filled by the same henchman.

        This property is for generic henchmen specifically (i.e. henchmen which either
        respawned infinitely, or existed in quantities large enough to be considered generic,
        i.e. Shysters or Birdys)."""
        self._overworld_generic_henchmen_npc_fills = (
            overworld_generic_henchmen_npc_fills
        )

    @property
    def has_vanilla_henchmen(self) -> bool:
        """If true, no henchmen replacements will take place."""
        if not isinstance(self.contents, Boss):
            return False
        return (
            len(
                self.overworld_unique_henchmen_npc_fills
                + self.overworld_generic_henchmen_npc_fills
            )
            == 0
        ) or (
            len(self.contents.repeatable_henchmen + self.contents.unique_henchmen) == 0
        )

    def _fill_model(
        self,
        fill: Union[BossModelFill, UniqueHenchmanFill, RepeatableHenchmanFill],
        new_occupant: Optional[Union[Boss, Henchman]],
    ):
        if fill.minigames_only and not self.world.settings.is_boolean_flag_enabled(
            BossReplaceMinigameSprites
        ):
            return
        if fill.occupant is None:
            return
        should_replace = (
            isinstance(fill, BossModelFill)
            or new_occupant is not None
            or (new_occupant is None and fill.remove_if_empty)
        )
        if should_replace:
            original_model = fill.occupant().model()
            animation_props_to_replace = original_model.animations.animation_prop_names
            # get 1-1 pairs of animations being replaced
            min_vram = 0
            animation_replacements: List[
                Tuple[SpriteAnimation, Optional[SpriteAnimation]]
            ] = [
                (
                    getattr(original_model.animations, prop),
                    getattr(new_occupant.model().animations, prop)
                    if new_occupant is not None
                    else None,
                )
                for prop in animation_props_to_replace
                if getattr(original_model.animations, prop) is not None
            ]
            # update every script with new sequence IDs
            for old_animation, new_animation in animation_replacements:
                new_animation_id = 0
                if new_animation is not None:
                    new_animation_id = new_animation.sequence_id
                # replace animations in embedded queues
                affected_events = list(fill.affected_event_scripts)
                if (
                    fill.fill_type in [HenchmanType.EXTERNAL_EVENT, HenchmanType.EVENT]
                    and fill.event_id is not None
                ):
                    affected_events.append(fill.event_id)
                for script_id in affected_events:
                    script = self.world.event_scripts.get_script_by_id(script_id)
                    queues = [
                        command
                        for command in script.contents
                        if isinstance(command, ActionSubcriptCommandPrototype)
                        and command.target == fill.npc
                    ]
                    for queue in queues:
                        sequence_commands = [
                            cmd
                            for cmd in queue.subscript.contents
                            if isinstance(cmd, SetSpriteSequence)
                            and not cmd.is_mold
                            and cmd.index == old_animation.sequence_id
                        ]
                        for cmd in sequence_commands:
                            cmd.set_index(new_animation_id)
                    if new_occupant is not None:
                        min_vram = max(
                            min_vram,
                            new_occupant.model(self.world).min_vram_from_event_script(
                                fill.npc, script_id
                            ),
                        )
                # replace animations in action scripts
                for script_id in fill.affected_action_scripts:
                    script = self.world.action_scripts.scripts[script_id]
                    for cmd in script.contents:
                        if (
                            isinstance(cmd, SetSpriteSequence)
                            and not cmd.is_mold
                            and cmd.index == old_animation
                        ):
                            cmd.set_index(new_animation_id)
                    if new_occupant is not None:
                        min_vram = max(
                            min_vram,
                            new_occupant.model(self.world).min_vram_from_action_script(
                                script_id
                            ),
                        )
            # replace npc in room
            room = self.world.rooms[fill.room_id]
            room_npc = room.objects[fill.npc_id]
            assert isinstance(room_npc, RoomObject)
            # replace npc in room
            inserted_model = Empty
            if isinstance(fill, BossModelFill):
                assert isinstance(new_occupant, Boss)
                inserted_model = new_occupant.model
                if fill.preferred_size == SpriteSize.LARGE:
                    inserted_model = new_occupant.big_model
                elif fill.preferred_size == SpriteSize.ATTACK:
                    inserted_model = new_occupant.attack_model
            else:
                assert isinstance(new_occupant, Henchman) or new_occupant is None
                room_npc.set_visible(new_occupant is not None)
                if isinstance(new_occupant, Henchman):
                    inserted_model = new_occupant.model
            room_npc.model.set_occupant(inserted_model)
            # set npc-specific properties
            if fill.prefer_south_only:
                room_npc.model.set_directions(VramStore.DIR2_SWSE)
            else:
                room_npc.model.set_directions(None)
            if fill.prefer_uncloneable:
                room_npc.model.set_cannot_clone(True)
            else:
                room_npc.model.set_cannot_clone(False)
            room_npc.model.set_vram_size(min_vram)
            # battle properties for henchmen
            if (
                (fill.fill_type == HenchmanType.PACK)
                and isinstance(room_npc, (BattlePackNPC, BattlePackClone))
                and new_occupant is not None
                and new_occupant.pack_number is not None
            ):
                room_npc.set_battle_pack(new_occupant.pack_number)
                pack = self.world.packs[new_occupant.pack_number]
                assert pack is not None
                formations = pack.formation_ids
                for formation in formations:
                    form = self.world.formations[formation]
                    assert form is not None
                    form.set_can_run_away(fill.can_run_away)
                    if fill.battlefield is not None:
                        form.set_battlefield_override(fill.battlefield)
        # replace dialogs
        if not isinstance(self.contents, Boss):
            return
        for dialog_id in fill.affected_dialog_ids:
            if dialog_id in self.contents.dialog_replacements:
                self.world.dialogs.replace_dialog(
                    dialog_id, self.contents.dialog_replacements[dialog_id]
                )
            if (
                dialog_id
                in self.contents.dialog_replacements_if_mandatory_fights_changed
                and self.world.settings.is_boolean_flag_enabled(
                    BossReplaceMinigameSprites
                )
            ):
                self.world.dialogs.replace_dialog(
                    dialog_id,
                    self.contents.dialog_replacements_if_mandatory_fights_changed[
                        dialog_id
                    ],
                )

    def _sanitize_room_data(self) -> None:
        """Modify all related scripts to be appropriate for this location's boss."""
        if self.is_vanilla() or self.original_item is None or self.contents is None:
            return
        assert isinstance(self.contents, Boss)

        # Do boss model replacements
        for fill in self.overworld_boss_npc_fills:
            self._fill_model(
                fill,
                self.contents,
            )
        if self.has_vanilla_henchmen:
            return

        # Do unique henchman replacements
        unique_fills = []
        for index, fills in enumerate(self.overworld_unique_henchmen_npc_fills):
            if index < len(self.contents.unique_henchmen):
                unique_fills.append((fills, self.contents.unique_henchmen[index]))
            else:
                new_contents = None
                if (
                    fills[0].repeatable_allowed
                    and len(self.contents.repeatable_henchmen) > 0
                ):
                    new_contents = choice(self.contents.repeatable_henchmen)
                unique_fills.append((fills, new_contents))
        for fills, new in unique_fills:
            for fill in fills:
                self._fill_model(fill, new)

        # Do repeatable henchman replacements
        generic_fills = []
        for index, fills in enumerate(self.overworld_generic_henchmen_npc_fills):
            new_contents = None
            if len(self.contents.repeatable_henchmen) > 0:
                new_contents = choice(self.contents.repeatable_henchmen)
            generic_fills.append((fills, new_contents))
        for fills, new in generic_fills:
            for fill in fills:
                self._fill_model(fill, new)

        # do statue fills on valentina spot

    def set_contents(self, contents: Optional[Boss]) -> None:
        super().set_contents(contents)

        # this should only be used when unsetting boss occupation on seed re-roll
        if contents is None:
            return

        # replace overworld models and rewrite behaviour to match new models
        self._sanitize_room_data()

        original_item: Type[Boss] = self.original_item

        # don't do any stat calc when vanilla
        # pylint: disable=W1116
        if isinstance(contents, original_item):
            return

        # get formation of boss being placed in this spot
        if contents.pack_number is None:
            raise ValueError(f"{contents} needs pack")
        incoming_pack_instance = self.world.packs[contents.pack_number]
        assert incoming_pack_instance is not None
        incoming_formation_id = incoming_pack_instance.formation_id
        incoming_formation = self.world.formations[incoming_formation_id]
        assert incoming_formation is not None

        # get donor stats based on original stats
        # not world instance, since it might have already been modified
        # pylint: disable=E1102
        original_contents = original_item()
        if original_contents.pack_number is None:
            raise ValueError(f"{original_contents} needs pack")
        original_pack_instance = self.world.packs[original_contents.pack_number]
        assert original_pack_instance is not None
        original_formation_id = original_pack_instance.formation_id
        original_formation = self.world.formations[original_formation_id]
        assert original_formation is not None

        # get_summed_stats is based on original unmodded stats of formation enemies
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
        ) = original_formation.get_summed_stats()

        # this already accounts for formations with special stat summing rules
        # like exor, valentina, etc
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

        # apply new stats to every incoming formation member's class instance
        truthy_members = [m.enemy for m in incoming_formation.members if m is not None]
        member_classes = set(
            truthy_members + incoming_formation.additional_enemies_to_scale
        )
        for member in member_classes:
            enemy = self.world.get_enemy_instance(member)
            enemy.set_hp(round(enemy.ratio_hp * hp))
            enemy.set_attack(round(enemy.ratio_attack * attack))
            enemy.set_defense(round(enemy.ratio_defense * defense))
            enemy.set_magic_attack(round(enemy.ratio_magic_attack * magic_attack))
            enemy.set_magic_defense(round(enemy.ratio_magic_defense * magic_defense))
            enemy.set_evade(round(enemy.ratio_evade * evade))
            enemy.set_magic_evade(round(enemy.ratio_magic_evade * magic_evade))

            xp_ratio: float = (
                enemy.xp
                / incoming_xp
                / len([m for m in truthy_members if isinstance(m, type(member))])
            )
            enemy.set_xp(round(xp_ratio * xp))
            enemy.update_world_entities()

        self._sanitize_room_data()

    @property
    def can_run_away(self) -> bool:
        """If false, the player shouldn't be able to run away from this location."""
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        """If false, the player shouldn't be able to run away from this location."""
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
                    if spell.target_enemies and spell.element == Element.NONE
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

    def __init__(self, world: "GameWorld"):
        super().__init__(world)
        if self.name_enum in world.settings.get_flag(EnabledBossChecks).disabled:
            self.set_excluded(True)
            # pylint: disable=E1102
            self.set_contents(self.original_item(world))

            self._accepted_types = []
        else:
            self._accepted_types = [Boss]
        if self._overworld_boss_npc_fills:
            self._overworld_boss_npc_fills = []
        if self._overworld_unique_henchmen_npc_fills:
            self._overworld_unique_henchmen_npc_fills = []
        if self._overworld_generic_henchmen_npc_fills:
            self._overworld_generic_henchmen_npc_fills = []
        if self._statue_fills:
            self._statue_fills = []


class BossStarPiecePrize(ProgressLocation):
    """A location that can grant a star piece as a potential prize after
    a boss battle."""

    _allow_empty_when_finished_shuffling: bool = True
    _name_enum: ShuffleLocationSelector

    @property
    def name_enum(self) -> ShuffleLocationSelector:
        """A unique identifier for this star piece granter."""
        return self._name_enum

    def __init__(self, world: "GameWorld"):
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
    """A location that can grant items."""

    _name_enum: Optional[ShuffleLocationSelector]

    @property
    def name_enum(self) -> Optional[ShuffleLocationSelector]:
        """A unique identifier for this item granter."""
        return self._name_enum

    def initiate_vanilla(self) -> None:
        """Populates the location with an instance of the item class it
        holds in the originalg game."""
        if self.original_item is not None:
            self.set_contents(self.world.get_item_instance(self.original_item))

    def __init__(self, world: "GameWorld"):
        super().__init__(world)
        if self.name_enum in world.settings.get_flag(EnabledRegularChecks).disabled:
            self.set_excluded(True)


class FrogDiscipleShopItem(ItemLocation):
    """A special kind of location specifically for the seaside frog coin shop."""

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

    def set_contents(self, contents: Item | None) -> None:
        if contents is not None:
            contents.become_frog_coin_item()
        return super().set_contents(contents)


class ChestLocation(ItemLocation):
    """A location that can grant items, specifically as a treasure chest."""

    _set_70a7_manually_in_event_script: bool = False
    _npc_ids: List[int] = []

    @property
    def set_70a7_manually_in_event_script(self) -> bool:
        """If true, the 70A7 value to be used in the item grant event will be determined
        by the script this chest runs, instead of as an innate chest property."""
        return self._set_70a7_manually_in_event_script

    @property
    def npc_ids(self) -> List[UInt8]:
        """The NPC IDs that this chest possesses in the rooms it belongs to.\n
        Indexes must match the indexes of this location's room ids.\n
        For example, if the same chest is NPC 2 in room 100, and NPC 1 in room 200,
        then room_ids should be [100, 200] and npc_ids should be [2, 1]."""
        for npc_id in self._npc_ids:
            assert npc_id <= 27
        return [UInt8(id) for id in self._npc_ids]

    def __init__(self, world: "GameWorld"):
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
                FireworksSetting, FireworksOptions.SHUFFLE_ONE
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.PROGRESSIVE
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
            LocationWorldArea.MUSHROOM_WAY,
            LocationWorldArea.BANDITS_WAY,
            LocationWorldArea.KERO_SEWERS,
            LocationWorldArea.ROSE_WAY,
            LocationWorldArea.FOREST_MAZE,
            LocationWorldArea.MOLEVILLE_MINES,
            LocationWorldArea.BOOSTER_TOWER,
            LocationWorldArea.BOOSTER_PASS,
            LocationWorldArea.SEA,
            LocationWorldArea.SUNKEN_SHIP,
            LocationWorldArea.LANDS_END,
            LocationWorldArea.NIMBUS_CASTLE,
            LocationWorldArea.BARREL_VOLCANO,
        ]:
            return False
        return super().can_accept(item, inventory)


class EarlygameChestLocation(ChestLocation):
    """A subtype of chest locations that cannot accept the two strongest mimic fights
    when balanced boss scaling is turned on."""

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if progression_safety(self.world) and isinstance(
            item, (MimicFightInitiator2, MimicFightInitiator3)
        ):
            return False
        return super().can_accept(item)


class MidgameChestLocation(ChestLocation):
    """A subtype of chest locations that cannot accept the strongest mimic fight
    when balanced boss scaling is turned on."""

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if progression_safety(self.world) and isinstance(item, MimicFightInitiator3):
            return False
        return super().can_accept(item)


class ChestLocationAllowCoins(ChestLocation):
    """A subtype of chest that is allowed to contain coins.\n
    This sometimes has to be restricted for graphical reasons."""

    def __init__(self, world: "GameWorld"):
        super().__init__(world)

        allowed_items = deepcopy(self._accepted_types)
        allowed_items.append(Coins)
        self._accepted_types = allowed_items


class ChestLocationAllowSlots(ChestLocationAllowCoins):
    """A subtype of chest that is allowed to contain slot machines.\n
    This sometimes has to be restricted for graphical reasons."""

    def __init__(self, world: "GameWorld"):
        super().__init__(world)

        allowed_items = deepcopy(self._accepted_types)
        allowed_items.append(SlotMachineChest)
        self._accepted_types = allowed_items


class MimicReloadRewardChest(ChestLocation):
    """A subtype of chest that contains a reward upon reloading the room
    after defeating one of the two weaker mimic fights. It will always occupy
    the same chest as its corresponding mimic fight."""

    def set_room_ids(self, room_ids: List[UInt16]) -> None:
        """Use this to set the room IDs of this chest to match the room IDs of the
        mimic chest it follows."""
        self._room_ids = [int(room) for room in room_ids]


class GrantLocation(ItemLocation):
    """A subtype of item location that grants an item to you explicitly in
    an event script, rather than via a chest or touching a freestanding item."""

    def __init__(self, world: "GameWorld"):
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
                FireworksSetting, FireworksOptions.SHUFFLE_ONE
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.PROGRESSIVE
            ):
                self._accepted_types.append(ProgressiveFireworks)


class InvisibleItemCandidate(GrantLocation):
    """An invisible item location used in the Three Musty Fears sidequest.\n
    Three such locations can be randomly selected and given an item.\n
    This location type comes with certain properties that place its trigger
    in the world correctly."""

    _x_coord: int = 0
    _y_coord: int = 0
    _z_coord: int = 0
    _x_shift: int = 0
    _y_shift: int = 0
    _clue_text: str = ""
    _tier: int = 4

    @property
    def key_item_location(self) -> bool:
        return True

    # needs a container event

    @property
    def clue_text(self) -> str:
        """The text that one of the Three Musty Fears should say to give a clue
        about where this is located."""
        return self._clue_text

    @property
    def x_coord(self) -> UInt8:
        """The X coordinate at which to place this trigger in the room."""
        return UInt8(self._x_coord)

    @property
    def y_coord(self) -> UInt8:
        """The Y coordinate at which to place this trigger in the room."""
        return UInt8(self._y_coord)

    @property
    def z_coord(self) -> UInt8:
        """The Z coordinate at which to place this trigger in the room."""
        return UInt8(self._z_coord)

    @property
    def x_shift(self) -> Int8:
        """Any additional pixels by which this should be shifted on the X axis."""
        return Int8(self._x_shift)

    @property
    def y_shift(self) -> Int8:
        """Any additional pixels by which this should be shifted on the Y axis."""
        return Int8(self._y_shift)

    def set_original_item(self, item: Type[Item]) -> None:
        """Only flag candidates have this method.
        the three selected locations need to be able to donate each flag to the shuffler.
        """
        self._original_item = item

    def can_access(self, parent_class: Type[ProgressLocationT], inventory: Inventory):
        return parent_class.can_access(self, inventory) and can_access_invisible_flags(
            self.world, inventory
        )


class TreasureShopItem(ItemLocation):
    """A special item location subtype for the three items that are sold to you by the
    treasure hunting toad in Moleville."""

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
    """A special location subtype for the four items that the player starts the game with."""

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item) and item.consumable

    def __init__(self, world: "GameWorld"):
        super().__init__(world)
        self.initiate_vanilla()


class FreestandingLocation(ItemLocation):
    """Item locations that grant specifically by picking up a physical item in the overworld."""

    _npc_ids: List[int] = []
    _keep_original_item_if_excluded: bool = True

    @property
    def npc_ids(self) -> List[UInt8]:
        """The NPC IDs that this object possesses in the rooms it belongs to.\n
        Indexes must match the indexes of this location's room ids.\n
        For example, if the same object is NPC 2 in room 100, and NPC 1 in room 200,
        then room_ids should be [100, 200] and npc_ids should be [2, 1]."""
        for npc_id in self._npc_ids:
            assert npc_id <= 27
        return [UInt8(id) for id in self._npc_ids]

    def __init__(self, world: "GameWorld"):
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
                FireworksSetting, FireworksOptions.SHUFFLE_ONE
            ):
                self._accepted_types.append(Fireworks)
            if world.settings.is_flag_value(
                FireworksSetting, FireworksOptions.PROGRESSIVE
            ):
                self._accepted_types.append(ProgressiveFireworks)

        if (
            self.name_enum in world.settings.get_flag(EnabledRegularChecks).disabled
            and self.original_item is not None
        ):
            self.set_contents(world.get_item_instance(self.original_item))


class MidasRiverTunnelItem(FreestandingLocation):
    """A subclass of freestanding item grant that specifically defines items given to you
    in the tunnel cutscenes of the Midas River waterfall. These have special requirements
    for how they are animated."""

    _midas_action_script: int = 0

    @property
    def midas_action_script(self) -> UInt16:
        """The action script to animate this item within the tunnel."""
        return UInt16(self._midas_action_script)


class PacketItem(FreestandingLocation):
    """A subclass of freestanding item grant where the item object to be interacted with
    is a packet, and not a NPC as defined in the room's NPC table."""

    _creation_script: int = 0
    _packet_type: PacketType = PacketType.STATIC

    @property
    def creation_script(self) -> UInt16:
        """The script that inserts the packet into the room."""
        return UInt16(self._creation_script)

    @property
    def packet_type(self) -> PacketType:
        """The specific animation behaviour of the packet."""
        return self._packet_type


class CharacterSpottedLocation(ProgressLocation):
    """A special placeholder class that represents your first time seeing a recruitable character,
    whether or not you recruit them.\n
    An example use case would be if Forest Maze is locked behind seeing Geno for the first time
    (like in the original game), but Geno is actually recruited at Marrymore. The Marrymore
    character can be seen on Booster Hill without being recruited. Therefore, if you visit
    Booster Hill and see Geno being carried up the hill, it would open Forest Maze."""

    _original_item: Optional[Type[SpottedCharacter]]

    def __init__(self, world: "GameWorld"):
        super().__init__(world)

        self._accepted_types = [SpottedCharacter]


class CharacterReplacementFill:

    """A container class representing one of a collection of NPCs across rooms that belong to one
    recruitable character. A shuffled recruitable character will fill these locations
    with its own model data.\n
    It is recommended to use event and action script ID constant names for this."""

    _room_id: int
    _npc_id: int
    _event_scripts: List[int]
    _action_scripts: List[int]

    @property
    def room_id(self) -> int:
        """A room that the shuffled character appears in."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Designate the room that the shuffled character appears in."""
        self._room_id = room_id

    @property
    def npc_id(self) -> int:
        """The NPC ID within the room that the character will replace."""
        return self._npc_id

    def set_npc_id(self, npc_id: int) -> None:
        """Set the NPC ID within the room that the character will replace."""
        self._npc_id = npc_id

    @property
    def event_scripts(self) -> List[int]:
        """The list of event scripts which may need to be changed to accommodate
        the character filling this location, usually due to those event
        scripts containing action queues animating this NPC."""
        return self._event_scripts

    def set_event_scripts(self, event_scripts: List[int]) -> None:
        """Overwrite the list of event scripts which may need to be changed to accommodate
        the character filling this location, usually due to those event
        scripts containing action queues animating this NPC.\n
        It is recommended to use event script ID constant names for this."""
        self._event_scripts = event_scripts

    @property
    def action_scripts(self) -> List[int]:
        """The list of action scripts which may need to be changed to accommodate
        the character filling this location."""
        return self._action_scripts

    def set_action_scripts(self, action_scripts: List[int]) -> None:
        """Overwrite the list of action scripts which may need to be changed to accommodate
        the character filling this location.\n
        It is recommended to use action script ID constant names for this."""
        self._action_scripts = action_scripts

    def __init__(
        self,
        room_id: int,
        npc_id: int,
        event_scripts: Optional[List[int]] = None,
        action_scripts: Optional[List[int]] = None,
    ) -> None:
        if event_scripts is None:
            event_scripts = []
        if action_scripts is None:
            action_scripts = []
        self.set_room_id(room_id)
        self.set_npc_id(npc_id)
        self.set_event_scripts(event_scripts)
        self.set_action_scripts(action_scripts)


class CharacterRecruitLocation(ProgressLocation):
    """A collection of instances where a certain recruitable character appears,
    which need to be filled with the model of a shuffled character."""

    _original_item: Optional[Type[Character]]
    _fills: List[CharacterReplacementFill] = []
    _credits_fills: List[CharacterReplacementFill] = []
    _doll_fills: List[CharacterReplacementFill] = []

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = CharacterSpottedLocation

    @property
    def original_item(self) -> Optional[Type[Character]]:
        """The item originally held by this location before shuffling."""
        return self._original_item

    @property
    def associated_spotted_location(self) -> Type[CharacterSpottedLocation]:
        """The associated location class representing this same character being simply seen
        without necessarily being recruited."""
        return self._associated_spotted_location

    @property
    def fills(self) -> List[CharacterReplacementFill]:
        """The list of instances where this character appears in playable levels
        to be populated by this character's model info."""
        return self._fills

    @property
    def credits_fills(self) -> List[CharacterReplacementFill]:
        """The list of instances where this character appears in the ending credits
        to be populated by this character's model info."""
        return self._credits_fills

    @property
    def doll_fills(self) -> List[CharacterReplacementFill]:
        """The list of instances where this character's doll appears
        to be populated by appropriate model info."""
        return self._doll_fills

    def _fill_model(self, fill: CharacterReplacementFill):
        model = RedSmallToad
        if self.contents is not None:
            model = self.contents.model
        room = self.world.rooms[fill.room_id]
        room_npc = room.objects[fill.npc_id]
        assert isinstance(room_npc, RoomObject)
        room_npc.model.set_occupant(model)

        # TODO: finish this method, rewrite stuff like "sprites_primary" prop on characters

    def set_contents(self, contents: Item | None) -> None:
        super().set_contents(contents)

        for fill in self.fills:
            self._fill_model(fill)

    def __init__(self, world: "GameWorld"):
        super().__init__(world)

        if len(self._fills) == 0:
            self._fills = []
        if len(self._credits_fills) == 0:
            self._credits_fills = []
        if len(self._doll_fills) == 0:
            self._doll_fills = []

        self._accepted_types = [Character]


class CharacterSpellSlot(ProgressLocation):
    """A granter specifically for spells that a playable character can learn.\n
    This is included in the shuffler because progression may require you to have
    an offense spell to transform Mokura, for instance."""

    def __init__(self, world: "GameWorld"):
        super().__init__(world)

        self._accepted_types = [CharacterSpell]


class LaterSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that the character does not start with."""

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if self.world.settings.is_boolean_flag_enabled(ExperienceNoRegular):
            assert inventory is not None
            # Do not place Super Jump in a late spell slot if character
            # may not be able to earn EXP to get it.
            if SuperJump in self.world.settings.get_flag(AvailableSpells).enabled:
                if not inventory.has_item(SuperJump):
                    return False
            # Do not start placing spells in later slots until at least one enemy-targeting spell
            # has been placed as the starting spell for a character we have access to.
            else:
                if not inventory.has_one_of(
                    [
                        type(spell)
                        for spell in self.world.character_spells
                        if spell.target_enemies
                    ]
                ):
                    return False
        return super().can_accept(item)


class MarioSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that Mario learns."""

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Mario)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        spell_slots = [
            s for s in self.world.character_spell_slots if isinstance(s, MarioSpellSlot)
        ]
        if isinstance(item, CloneSpell):
            for spell_slot in spell_slots:
                if spell_slot.does_contain(type(item.parent_spell)):
                    return False
        elif isinstance(item, CharacterSpell):
            for spell_slot in spell_slots:
                if (
                    isinstance(spell_slot.contents, CloneSpell)
                    and item == spell_slot.contents.parent_spell
                ):
                    return False
        return super().can_accept(item, inventory)


class MallowSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that Mallow learns."""

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Mallow)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        spell_slots = [
            s
            for s in self.world.character_spell_slots
            if isinstance(s, MallowSpellSlot)
        ]
        if isinstance(item, CloneSpell):
            for spell_slot in spell_slots:
                if spell_slot.does_contain(type(item.parent_spell)):
                    return False
        elif isinstance(item, CharacterSpell):
            for spell_slot in spell_slots:
                if (
                    isinstance(spell_slot.contents, CloneSpell)
                    and item == spell_slot.contents.parent_spell
                ):
                    return False
        return super().can_accept(item, inventory)


class GenoSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that Geno learns."""

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Geno)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        spell_slots = [
            s for s in self.world.character_spell_slots if isinstance(s, GenoSpellSlot)
        ]
        if isinstance(item, CloneSpell):
            for spell_slot in spell_slots:
                if spell_slot.does_contain(type(item.parent_spell)):
                    return False
        elif isinstance(item, CharacterSpell):
            for spell_slot in spell_slots:
                if (
                    isinstance(spell_slot.contents, CloneSpell)
                    and item == spell_slot.contents.parent_spell
                ):
                    return False
        return super().can_accept(item, inventory)


class BowserSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that Bowser learns."""

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Bowser)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        spell_slots = [
            s
            for s in self.world.character_spell_slots
            if isinstance(s, BowserSpellSlot)
        ]
        if isinstance(item, CloneSpell):
            for spell_slot in spell_slots:
                if spell_slot.does_contain(type(item.parent_spell)):
                    return False
        elif isinstance(item, CharacterSpell):
            for spell_slot in spell_slots:
                if (
                    isinstance(spell_slot.contents, CloneSpell)
                    and item == spell_slot.contents.parent_spell
                ):
                    return False
        return super().can_accept(item, inventory)


class ToadstoolSpellSlot(CharacterSpellSlot):
    """A spell slot granter specifically for spells that Toadstool learns."""

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(Toadstool)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        spell_slots = [
            s
            for s in self.world.character_spell_slots
            if isinstance(s, ToadstoolSpellSlot)
        ]
        if isinstance(item, CloneSpell):
            for spell_slot in spell_slots:
                if spell_slot.does_contain(type(item.parent_spell)):
                    return False
        elif isinstance(item, CharacterSpell):
            for spell_slot in spell_slots:
                if (
                    isinstance(spell_slot.contents, CloneSpell)
                    and item == spell_slot.contents.parent_spell
                ):
                    return False
        return super().can_accept(item, inventory)
