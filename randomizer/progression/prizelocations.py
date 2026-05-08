from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import uuid4

from randomizer.data.variables.overworld_area_names import OW50_BARREL_VOLCANO

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MEM_70A8,
    BOWSER,
)

from ..types.logic import Inventory
from ..types.prize import Prize
from ..types.prizelocation import (
    AllyNPCSub,
    BossFightLocationHenchmanNPC,
    BossFightLocationNPC,
    PrizeLocation,
    RemoveIfNotFilled,
    StandingLocation,
    TreasureChestLocationRow1,
    TreasureChestLocationRow2,
    TreasureChestLocationRow3,
    TreasureChestLocationRow4,
    TreasureChestLocationRow5,
    TreasureChestLocationRow6,
    NPCLocationRow1,
    NPCLocationRow2,
    NPCLocationRow3,
    NPCLocationRow4,
    NPCLocationRow5,
    NPCLocationRow6,
    NPCLocationRow7,
    StandingLocationRow1,
    StandingLocationRow2,
    StandingLocationRow3,
    StandingLocationRow4,
    StandingLocationRow5,
    StandingLocationRow6,
    StandingLocationRow7,
    StandingLocationRow8,
    StandingLocationRow9,
    StandingLocationRow10,
    StandingLocationRow11,
    StandingLocationRow12,
    StandingLocationRow13,
    StandingLocationRow14,
    StandingLocationRow15,
    RiverLocationRow2,
    BossFightLocation,
    CharacterRecruitmentLocation,
    StartingCharacterLocation,
    StarPieceLocation,
    SpellSlotLocation,
    ShuffleLocationSelector,
    TreasureShopLocation,
    BoosterHillLocation,
    FrogDiscipleLocation,
    PacketLocationRow1,
    InvisibleFlagLocation,
    WorldAreaEnum,
    KeyItemLocation,
    MimicFightLocation,
)
from ..types.packet_type import PacketType
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from ..data.variables.action_script_names import *
from ..data.variables.pack_names import *
from ..data.variables.variable_names import YOSHI_ITEM_GRANTED, PRIMARY_TEMP_7000
from ..data.variables.dialog_names import DI2010_DEBUG_7000
from ..data.variables.event_palette_names import (
    EPAL0024_KEEP_BOSS_1_EVIL,
    EPAL0025_KEEP_BOSS_1_REFORMED,
)
from .prizes import *
from ..types.prize import (
    FPFlowerPrize,
    SlotsPrize,
    EmptyPrize,
    CoinPrize,
    FrogCoinPrize,
)
from ..types.flags import *
from ..utils.npcs import (
    set_npc_direction_if_swse_only,
    set_mines_punch_command,
)
from ..utils.snippets.es_mimic_rise import get_mimic_rise_kamek
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_5,
    NPC_6,
    NPC_7,
    NPC_8,
    NPC_9,
    NPC_10,
    NPC_11,
    NPC_12,
    NPC_13,
    NPC_14,
    NPC_15,
    NPC_16,
    NPC_17,
    NPC_18,
    NPC_19,
    NPC_20,
    NPC_21,
    NPC_22,
    NPC_23,
    NPC_24,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import (
    SOUTHEAST,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_SetSpriteSequence,
    A_FaceSoutheast,
    A_FaceSouthwest,
    A_Pause,
    A_VisibilityOn,
    A_PlaySound,
)
from typing import TYPE_CHECKING, cast

from ..data.physical_objects.items import (
    BigCoinObject,
    DefaultItem,
    FlowerObject,
    FrogCoinObject,
    KeyObject,
    RecoveryMushroomObject,
    SmallCoinObject,
    SmallFrogCoinObject,
)

from ..logic.renders import (
    render_bandits_way_boss,
    render_booster_tower_indoor_boss_postgame,
    render_forest_maze_character_empty,
    render_forest_maze_character,
    render_booster_tower_indoor_boss,
    render_booster_tower_henchman_scripts,
    render_marrymore_boss_henchmen,
    render_marrymore_character_empty,
    render_marrymore_character,
    render_seaside_beach_boss,
    render_ship_password_boss,
    render_ship_final_boss,
    render_dojo_first_fight,
    render_dojo_fight,
    render_bean_valley_planter_boss,
    render_ship_postgame_boss,
    render_statue_room_boss,
    render_volcano_exit_boss,
    render_inner_factory_second_fight,
    render_inner_factory_third_fight_slot,
    render_inner_factory_fourth_fight,
    render_final_boss_fight,
)

if TYPE_CHECKING:
    from ..types.logic import Inventory
    from ..types.gameworld import GameWorld


# Lazy imports for flags defined after the circular import point in flags.py
# These flags are defined after flags.py imports prizelocations, so they're not
# available via "from ..types.flags import *" at module load time.
def _get_late_flags():
    """Lazy import for flags defined after the circular import in flags.py."""
    from ..types.flags import (
        BowserDoorShuffle,
        BucketWarp,
        CasinoWarp,
        FixKnifeGuy,
        SkipBossFights,
        StarPiecesRequired,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
    )

    return {
        "BowserDoorShuffle": BowserDoorShuffle,
        "BucketWarp": BucketWarp,
        "CasinoWarp": CasinoWarp,
        "FixKnifeGuy": FixKnifeGuy,
        "SkipBossFights": SkipBossFights,
        "StarPiecesRequired": StarPiecesRequired,
        "SuitePrize1Threshold": SuitePrize1Threshold,
        "SuitePrize2Threshold": SuitePrize2Threshold,
        "SuitePrize3Threshold": SuitePrize3Threshold,
        "SuitePrize4Threshold": SuitePrize4Threshold,
        "SuitePrize5Threshold": SuitePrize5Threshold,
        "SuitePrize6Threshold": SuitePrize6Threshold,
    }


_late_flags_cache = None


def _get_flag(name: str):
    """Get a late-defined flag by name."""
    global _late_flags_cache
    if _late_flags_cache is None:
        _late_flags_cache = _get_late_flags()
    return _late_flags_cache[name]


# Comments are included here to document what condition is met for a location to be considered checked.
# Anything that takes a flag has a variable name listed, ie TOAD_IN_MUSHROOM_WAY_1.
# The actual memory address this corresponds to can be found in data/variables/variable_names.py
# ie TOAD_IN_MUSHROOM_WAY_1 = Flag(0x7052, 4) = $7052 bit 4

# There are no longer any missable checks. All missable checks have become permanent in one way or another

# note: hidon + pandorite mimics work weird. they do three things
# they can appear in any chest
# say for example the fight is in the MushroomKingdomMainHall chest...
# 1: the mimic fight begins - this is the MushroomKingdomMainHall check. the mimic fight is not an AP item but it is considered an "item" for internal shuffling purposes
# 2: upon defeat, the mimic drops an item - this is the Mimic1DropRewardLocation check. this is considered checked when MIMIC_1_CLEARED is set (or MIMIC_2_CLEARED). this can in theory be an AP item
# at this point, the chest looks and acts empty from the player's POV, but it is NOT disabled!
# when the player reloads the room, the chest is hittable again for an extra check. this is the Mimic1ReloadRewardLocation and can also in theory be an AP item. this DOES disable the chest
# in memory, this third check is considered done when the host chest (MushroomKingdomMainHall for ex.) has its object trigger disabled
# so it's kind of like a chest checked condition gets deferred when a mimic is found
# the actual chest that does this is random every seed
# i am not sure what that implies for AP but we can work it out

# not sure what to do about InfiniteCoinsPrize
# normally an easy way to tell a chest is checked is if its object trigger is disabled
# but the chest that holds infinite coins never disables its object trigger
# can be in a random chest
# is it possible for tracker to know ahead of time which chest it is in and flag it as checked when first opened?
# when the player first hits the chest that contains infinite coins it will set the INFINITE_COINS_FOUND bit regardless of what chest it's been shuffled into


########## mario's house


class StartingItem1Location(NPCLocationRow2):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_1
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem2Location(NPCLocationRow3):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_2
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem3Location(NPCLocationRow4):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_3
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem4Location(NPCLocationRow5):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingCharacter1(StartingCharacterLocation):
    _originally_held = MarioRecruitmentPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_1
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1220_STARTING_CHARACTER_1
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class MarioSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = JumpSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = FireOrbSpellPrize
    _level = 3

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = SuperJumpSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = SuperFlameSpellPrize
    _level = 10

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class MarioSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = UltraJumpSpellPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class MarioSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = UltraFlameSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class StartingCharacter2(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_2
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1221_STARTING_CHARACTER_2
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter3(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_3
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1222_STARTING_CHARACTER_3
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter4(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_4
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1223_STARTING_CHARACTER_4
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter5(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_5
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1224_STARTING_CHARACTER_5
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class PostgameVoucherLocation(NPCLocationRow6, KeyItemLocation):
    _bias = True
    _originally_held = StayVoucherPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.POSTGAME_VOUCHER
    _world_area = WorldAreaEnum.MARIOS_PAD
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_inner_mines(world, inventory)
            and can_access_tower(world, inventory)
            and can_clear_chapel(world, inventory)
            and can_clear_ship(world, inventory)
            and can_access_temple_boss(world, inventory)
            and can_access_sealed_door_boss(world, inventory)
            and can_access_fifth_dojo_boss(world, inventory)
        )

    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(VOUCHER_CHECK_DONE, ["next"]),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(SHIP_LIBERATED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["next"]),
        JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["next"]),
        Jmp(["marios_pad_hint_text"]),
    ]

    # Flag as checked: VOUCHER_CHECK_DONE


########## mushroom way


class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = Coins5Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R203_MUSHROOM_WAY_AREA_01, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 203 has its object trigger disabled.


class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = Coins8Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 2),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R203_MUSHROOM_WAY_AREA_01, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 203 has its object trigger disabled.


class MushroomWay1ToadRescue(NPCLocationRow2):
    _originally_held = HoneySyrupPrize
    _rooms = [R203_MUSHROOM_WAY_AREA_01, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 3),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_1, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_1


class MushroomWay2LedgeChest(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_3
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        EXPStarPrize,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 4),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R204_MUSHROOM_WAY_AREA_02, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 204 has its object trigger disabled.


class MushroomWay2ToadRescue(NPCLocationRow3):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 5),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_2


class MushroomWayRightGoomba(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
        FrogCoinPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 6),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R204_MUSHROOM_WAY_AREA_02, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 204 has its object trigger disabled.


class MushroomWayLeftItemRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.REMAKE_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 7),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_10, R204_MUSHROOM_WAY_AREA_02, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]

    # Flag as checked: npc 10 in room 204 has been removed from the room.


class MushroomWayRightItemRemake(StandingLocationRow2):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.REMAKE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 8),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_11, R204_MUSHROOM_WAY_AREA_02, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]

    # Flag as checked: npc 11 in room 204 has been removed from the room.


class MushrooomWayBossFight(BossFightLocation):
    _originally_held = HammerBrosFight
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _pack_id = PACK183_MUSHROOM_WAY_BOSS
    _post_unlocks_event_id = E1194_MUSHROOM_WAY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R205_MUSHROOM_WAY_AREA_03,
            NPC_7,
            sequence_setter_event_id=E0755_MUSHROOM_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MUSHROOM_WAY):
            content.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_STAR_PIECE
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _parent = MushrooomWayBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 9),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayBossFightRewardItem(NPCLocationRow1):
    _bias = True
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = MallowRecruitmentPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_CHARACTER
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _container_event = E1225_MUSHROOM_WAY_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(R203_MUSHROOM_WAY_AREA_01, NPC_8),
        AllyNPCSub(R204_MUSHROOM_WAY_AREA_02, NPC_7),
        AllyNPCSub(R205_MUSHROOM_WAY_AREA_03, NPC_5),
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 11),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return is_all_starting_chars_set(world, inventory)

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(2)
        return super().set_prize(prize)

    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MallowSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = ThunderboltSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = HPRainSpellPrize
    _level = 3

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = PsychopathSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = ShockerSpellPrize
    _level = 10

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


class MallowSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = SnowyPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


class MallowSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = StarRainSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


########## mushroom kingdom - available before and during invasion


class MushroomKingdomMainHall(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
        R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
    ]
    _npc_ids = [NPC_2, NPC_6]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_HALLWAY
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 12),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: either npc 2 in room 17 or npc 6 in room 325 has its object trigger disabled.


class MushroomKingdomLiberatedVaultLeft(TreasureChestLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_0, NPC_2]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 13),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultRight(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_1, NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 14),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultMiddle(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_2, NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_3
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 15),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: npc 2 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomChair(NPCLocationRow1):
    _originally_held = MushroomPrize
    _rooms = [
        R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _check_npc_ids = [NPC_0, NPC_7]
    _id = ShuffleLocationSelector.PEACH_SURPRISE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 16),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # flag as checked: npc 0 is missing/despawned from room 20 or npc 7 is missing/despawned from room 328


class MushroomKingdomFreeShopItem(NPCLocationRow1):
    _originally_held = PickMeUpPrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 17),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # flag as checked: MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED


class MushroomKingdomShopBasementLeft(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 18),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 492 has its object trigger disabled.


class MushroomKingdomShopBasementRight(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 19),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 492 has its object trigger disabled.


class MushroomKingdomWalletGuyFirstRewardLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 20),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(RETURNED_WALLET, ["next"]),
        StoreItemAmountTo7000(WalletItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(WalletPrize)

    # Flag as checked: RETURNED_WALLET


class MushroomKingdomWalletGuySecondRewardLocation(NPCLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 21),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SECOND_WALLET_PRIZE_RECEIVED, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(RETURNED_WALLET, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory) and inventory.has_item(WalletPrize)

    # Flag as checked: SECOND_WALLET_PRIZE_RECEIVED


########## mushroom kingdom = available only during occupation or later


class MushroomKingdomOccupiedOutdoorGuardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE]
    _check_npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.INVASION_EASTERN_GUARD
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 22),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: NPC 5 removed from room 190
    # Remember you need to define an additional henchman slot for the liberated room


class MushroomKingdomOccupiedCastleToadRescueLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _id = ShuffleLocationSelector.INVASION_TOAD_RESCUE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 23),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Remember you need to define an additional henchman slot for the liberated room
    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED


class MushroomKingdomOccupiedFamilyRescueLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [
        R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
        R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
    ]
    _id = ShuffleLocationSelector.INVASION_FAMILY
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 24),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitClear(
            OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED,
            ["mushroom_kingdom_hint_text"],
        ),
        JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED and OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED must BOTH be set


class MushroomKingdomOccupiedGuestRoomLocation(NPCLocationRow1):
    _bias = True
    _originally_held = WakeUpPinPrize
    _rooms = [R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM]
    _id = ShuffleLocationSelector.INVASION_GUEST_ROOM
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 25),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED


class MushroomKingdomBossFight(BossFightLocation):
    _bias = True
    _originally_held = MackBossFight
    _rooms = [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _pack_id = PACK179_MUSHROOM_KINGDOM_BOSS
    _post_unlocks_event_id = E1195_BANDITS_WAY_BOSS_UNLOCKS
    _henchman_can_run_away = False

    _npc_slots = [
        BossFightLocationNPC(
            R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            NPC_3,
            sequence_setter_event_id=E0761_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_4],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_5],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_6],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_7],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_8],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_9],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R191_MUSHROOM_KINGDOM_OUTSIDE,
            ],
            [
                NPC_3,
                NPC_5,
                NPC_0,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_4,
                NPC_10,
            ],
            pack_id=PACK010_KINGDOM_HENCHMEN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0051_HENCHMAN_CONTAINER_1,
        ),
        BossFightLocationHenchmanNPC(
            [
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ],
            [
                NPC_3,
            ],
        ),
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ],
            [
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_4,
                NPC_6,
                NPC_1,
                NPC_1,
                NPC_0,
                NPC_0,
                NPC_1,
                NPC_3,
                NPC_1,
            ],
            pack_id=PACK011_KINGDOM_HENCHMEN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0052_HENCHMAN_CONTAINER_2,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        for slot, henchman in henchmen_assignments:
            model = henchman.model
            if model is not None:
                npc_base = model().base
                for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                    set_npc_direction_if_swse_only(world, room_id, npc_id, npc_base)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
            content.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                    RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE),
                    RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


class MushroomKingdomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece1
    _rooms = [R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_STAR_PIECE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _parent = MushroomKingdomBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 26),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )

    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


########## mushroom kingdom: only available AFTER liberation


class MushroomKingdomStoreExchangeLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = CricketPiePrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 27),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(RARE_FROG_COIN_EXCHANGED, ["next"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        StoreItemAmountTo7000(RareFrogCoinItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory) and inventory.has_item(
            RareFrogCoinPrize
        )

    # Flag as checked: RARE_FROG_COIN_EXCHANGED


class MushroomKingdomInnPurchaseLocation(NPCLocationRow1):
    _bias = True
    _originally_held = BeetlemaniaPrize
    _rooms = [
        R493_MUSHROOM_KINGDOM_INN_1F,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 28),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(GAMEBOY_KID_PURCHASE_COMPLETE, ["next"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: GAMEBOY_KID_PURCHASE_COMPLETE


########## bandit's way


class BanditsWayFlowerJumpLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BANDITS_WAY_1
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]  # slots can work here graphically but this is a stupid place for it
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 29),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R207_BANDITS_WAY_AREA_02, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 9 in room 207 has its object trigger disabled.


class BanditsWayCoin1Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_1
    _world_area = WorldAreaEnum.BANDITS_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 30),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        #    JmpIfObjectNotInSpecificLevel(NPC_3, R207_BANDITS_WAY_AREA_02, ["next"]),
        #    JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        #    Jmp(["bandits_way_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 3 in room 207 has been removed from the room.


class BanditsWayCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_2
    _world_area = WorldAreaEnum.BANDITS_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 31),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        #    JmpIfObjectNotInSpecificLevel(NPC_4, R207_BANDITS_WAY_AREA_02, ["next"]),
        #    JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        #    Jmp(["bandits_way_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 4 in room 207 has been removed from the room.


class BanditsWayCoin3Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_3
    _world_area = WorldAreaEnum.BANDITS_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 32),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        #    JmpIfObjectNotInSpecificLevel(NPC_5, R207_BANDITS_WAY_AREA_02, ["next"]),
        #    JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        #    Jmp(["bandits_way_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 5 in room 207 has been removed from the room.


class BanditsWayDogChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R077_BANDITS_WAY_AREA_03]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_2
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 33),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R077_BANDITS_WAY_AREA_03, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 0 in room 77 has its object trigger disabled.


class BanditsWayPlatformsLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = BanditsWayStarPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_CHEST
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 34),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R078_BANDITS_WAY_AREA_04, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if not isinstance(self.prize, EXPStarPrize):
            world.event_scripts.get_script_by_id(
                E1538_BANDITS_WAY_STAR_CHEST_CAMERA_AND_DOGS
            ).insert_before_nth_command(0, Jmp(["EVENT_1538_jmp_to_event_2"]))
        return super().render(world)

    # Flag as checked: npc 0 in room 78 has its object trigger disabled.


class BanditsWayPlatformsRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BANDITS_WAY_DOG_JUMP
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 35),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R078_BANDITS_WAY_AREA_04, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if not isinstance(self.prize, EXPStarPrize):
            world.event_scripts.get_script_by_id(
                E1587_BANDITS_WAY_4_RIGHT_CHEST
            ).insert_before_nth_command(0, Jmp(["EVENT_1587_jmp_to_event_2"]))
        return super().render(world)

    # Flag as checked: npc 1 in room 78 has its object trigger disabled.


class BanditsWayDeadEndChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_CROCO
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [
        EXPStarPrize,
        SlotsPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 36),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R206_BANDITS_WAY_AREA_05, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 0 in room 206 has its object trigger disabled.


class BanditsWayBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco1BossFight
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BANDITS_WAY
    _pack_id = PACK163_BANDITS_WAY_BOSS
    _post_unlocks_event_id = E1196_MUSHROOM_KINGDOM_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R076_BANDITS_WAY_AREA_01,
            NPC_5,
            sequence_setter_event_id=E0757_BANDITS_WAY_AREA_01_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R207_BANDITS_WAY_AREA_02,
            NPC_8,
            sequence_setter_event_id=E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R077_BANDITS_WAY_AREA_03,
            NPC_8,
            sequence_setter_event_id=E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R078_BANDITS_WAY_AREA_04,
            NPC_12,
            sequence_setter_event_id=E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R206_BANDITS_WAY_AREA_05,
            NPC_8,
            sequence_setter_event_id=E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
            NPC_10,
            sequence_setter_event_id=E1193_ENDING_CREDITS_YOSTER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def render(self, world: GameWorld):
        """Set animation scripts for this boss to be more specific for the character"""
        assert isinstance(self.prize, BossFightPrize)
        w = super().render(world)
        render_bandits_way_boss(world, self.prize)
        return w

    # Flag as checked: BANDITS_WAY_LIBERATED


class BanditsWayStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_PIECE
    _world_area = WorldAreaEnum.BANDITS_WAY
    _parent = BanditsWayBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 37),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )

    # Flag as checked: BANDITS_WAY_LIBERATED


class BanditsWayBossFirstItemDropLocation(NPCLocationRow1, KeyItemLocation):
    _bias = True
    _originally_held = RareFrogCoinPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 38),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: BANDITS_WAY_LIBERATED set


class BanditsWayBossSecondItemDropLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = WalletPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD_2
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 39),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: BANDITS_WAY_LIBERATED set (checked at same time as BanditsWayBossSecondItemDropLocation)


########## kero sewers


class KeroSewersStairRoomLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_PANDORITE_ROOM
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 40),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_1"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            ["next"],
            identifier="sewers_closed_check_1",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 60 has its object trigger disabled.


class KeroSewersStairRoomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FirstMimicFightLauncher
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PANDORITE_CHEST
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 41),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_2"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            ["next"],
            identifier="sewers_closed_check_2",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 1 in room 60 has its object trigger disabled.


class Mimic1BossFight(MimicFightLocation):
    _bias = True
    _originally_held = PandoriteBossFight
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS_FIGHT
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK156_SEWER_CHEST_FIGHT
    _post_unlocks_event_id = E1249_MIMIC_1_BOSS_UNLOCKS

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    # Flag as checked: MIMIC_1_CLEARED


class Mimic1DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TrueformPinPrize
    _rooms = [512]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.PANDORITE_REWARD_1
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    # flag as checked: MIMIC_1_CLEARED


class Mimic1StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS
    _world_area = WorldAreaEnum.KERO_SEWERS
    _parent = Mimic1BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and inventory.has_item(
            FirstMimicFightLauncher
        )

    # Flag as checked: MIMIC_1_CLEARED


class Mimic1ReloadRewardLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = Coins50Prize
    _rooms: list[int] = []  # Dynamic room, handled by mimic system
    _npc_ids: list[AreaObject] = []  # No specific NPC
    _id = ShuffleLocationSelector.PANDORITE_REWARD_2
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512
    # FirstMimicFightLauncher must be blacklisted to prevent circular dependency:
    # This location's can_access requires defeating first mimic, which requires
    # accessing the FirstMimicFightLauncher location - can't be the same location.
    _blacklist = [EXPStarPrize, SlotsPrize, MimicFightInitiatorPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def grant(self) -> EventScript:
        # Mimic rewards don't need room-specific chest disable commands
        if self.prize is None:
            return EventScript([Return()])
        return EventScript(
            [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        )

    # flag as checked: the host chest for FirstMimicFightLauncher has its object trigger disabled


class KeroSewersFourRatRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KeroSewersStarPrize
    _rooms = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 42),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_3"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
            ["next"],
            identifier="sewers_closed_check_3",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 59 has its object trigger disabled.


class KeroSewersBeforeBelomeLowerLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_LOWER
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 43),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_4"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            ["next"],
            identifier="sewers_closed_check_4",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 301 has its object trigger disabled.


class KeroSewersBeforeBelomeUpperBeforeFlipLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_1
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [
        EXPStarPrize,
        FirstMimicFightLauncher,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 44),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_5"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(
            SEWER_CHEST_FIRST_PRIZE_OBTAINED,
            ["next"],
            identifier="sewers_closed_check_5",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: SEWER_CHEST_FIRST_PRIZE_OBTAINED


class KeroSewersBeforeBelomeUpperAfterFlipLocation(
    KeyItemLocation, TreasureChestLocationRow3
):
    _originally_held = CricketJamPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_2
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [
        EXPStarPrize,
        SlotsPrize,
        FirstMimicFightLauncher,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 45),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SEWERS_FLIPPED_CHEST_OPENED, ["next"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(LANDS_END_GROTTO_BARREL_FLIPPED, ["lands_end_grotto_hint_text"]),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: SEWERS_FLIPPED_CHEST_OPENED


class KeroSewersBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome1BossFight
    _rooms = [R302_KERO_SEWERS_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.KERO_SEWERS_BOSS
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK168_SEWER_BOSS
    _post_unlocks_event_id = E1197_KERO_SEWER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            NPC_1,
            sequence_setter_event_id=E0772_KERO_SEWERS_BELOME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
            content.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: SEWER_BOSS_DEFEATED


class KeroSewersStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_PIECE
    _world_area = WorldAreaEnum.KERO_SEWERS
    _parent = KeroSewersBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 46),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_6"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(SEWER_BOSS_DEFEATED, ["next"], identifier="sewers_closed_check_6"),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sewer(
            world, inventory
        )

    # Flag as checked: SEWER_BOSS_DEFEATED


########## Midas River


class MidasRiverFirstCompletionRewardLocation(NPCLocationRow1):
    _originally_held = NokNokShellPrize
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _id = ShuffleLocationSelector.MIDAS_RIVER_FIRST_TIME
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 47),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED, ["next"]),
        Jmp(["midas_river_hint_text"]),
    ]
    # Flag as checked: MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED


class MidasRiverLeftCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.MIDAS_RIVER_LEFT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 48),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_1, ["next"]),
        Jmp(["midas_river_hint_text"]),
    ]
    # Flag as checked: MIDAS_RIVER_TUNNEL_2_BIT_1


class MidasRiverBottomLeftCaveLocation(RiverLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_LEFT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 49),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_3_PRIZE, ["next"]),
        Jmp(["midas_river_hint_text"]),
    ]
    # Flag as checked: MIDAS_RIVER_TUNNEL_3_PRIZE


class MidasRiverBottomRightCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_RIGHT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 50),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["next"]),
        Jmp(["midas_river_hint_text"]),
    ]
    # Flag as checked: MIDAS_RIVER_TUNNEL_4_PRIZE


########## tadpole pond


class TadpolePondCricketPieExchangeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FroggiestickPrize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_PIE_REWARD
    _world_area = WorldAreaEnum.TADPOLE_POND
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 51),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(CRICKET_PIE_EXCHANGED, ["next"]),
        StoreItemAmountTo7000(CricketPieItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(CricketPiePrize)

    # Flag as checked: CRICKET_PIE_EXCHANGED


class TadpolePondCricketJamExchangeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FrogCoin10Prize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_JAM_REWARD
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 52),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(CRICKET_PIE_EXCHANGED, ["next"]),
        JmpIfBitSet(CRICKET_JAM_EXCHANGED, ["next"]),
        StoreItemAmountTo7000(CricketJamItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(CricketPiePrize) and inventory.has_item(
            CricketJamPrize
        )

    # Flag as checked: CRICKET_JAM_EXCHANGED


class MelodyBayFirstRewardLocation(NPCLocationRow1, KeyItemLocation):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_1
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 53),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]
    # Flag as checked: MELODY_BAY_ITEM_1_GRANTED


class MelodyBaySecondRewardLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_2
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 54),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["next"]),
        JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["next"]),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    # Flag as checked: MELODY_BAY_ITEM_2_GRANTED


class MelodyBayThirdRewardLocation(NPCLocationRow3, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_3
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 55),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["next"]),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_clear_mines(world, inventory)
            and can_access_temple_boss(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: MELODY_BAY_ITEM_3_GRANTED


########## rose way


class RoseWaySwingingPlatformRoomLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_PLATFORM
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]  # SlotsPrize can go here graphically, it's just too annoying to hit 4 times
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 56),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 80 has its object trigger disabled.


class RoseWayLeftIslandLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.ROSE_WAY_FLOWER
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 57),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_7, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 7 in room 79 has been removed from the room.


class RoseWayMiddleIslandLocation(StandingLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.ROSE_WAY_MUSHROOM
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 58),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_8, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 8 in room 79 has been removed from the room.


class RoseWayCoin1Location(StandingLocationRow7):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_1
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 59),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_18, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]
    # Flag as checked: npc 17 in room 79 has been removed from the room.


class RoseWayCoin2Location(StandingLocationRow6):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_2
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 60),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_19, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]
    # Flag as checked: npc 18 in room 79 has been removed from the room.


class RoseWayCoin3Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_20]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_3
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 61),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_20, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]
    # Flag as checked: npc 19 in room 79 has been removed from the room


class RoseWayCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_21]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_4
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 62),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_21, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]
    # Flag as checked: npc 20 in room 79 has been removed from the room


class RoseWayCoin5Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_22]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_5
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 63),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_22, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]
    # Flag as checked: npc 21 in room 79 has been removed from the room


class RoseWayFiveChestRoomTopLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_1
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 64),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomLeftLocation(TreasureChestLocationRow2):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 65),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomRightLocation(TreasureChestLocationRow3):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 66),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 2 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomLeftLocation(TreasureChestLocationRow4):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_4
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 67),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 3 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomRightLocation(TreasureChestLocationRow5):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_5
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 68),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]
    # Flag as checked: npc 4 in room 81 has its object trigger disabled.


########### rose town


class RoseTownShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 69),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R087_ROSE_TOWN_ITEM_SHOP, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: npc 4 in room 87 has its object trigger disabled.


class RoseTownShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 70),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: npc 5 in room 87 has its object trigger disabled.


class RoseTownCloudRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LazyShellArmorPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SlotsPrize]
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 71),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R419_LAZY_SHELL_CLOUD, ["next"]
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["rose_town_hint_text"]),
        JmpIfBitSet(GAVE_SEED, ["hint_check_fertilizer"]),
        StoreItemAmountTo7000(SeedItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            GAVE_FERTILIZER, ["rose_town_hint_text"], identifier="hint_check_fertilizer"
        ),
        StoreItemAmountTo7000(FertilizerItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_mines(world, inventory)
            and can_clear_forest(world, inventory)
        )

    # Flag as checked: npc 0 in room 419 has its object trigger disabled.


class RoseTownCloudLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LazyShellWeaponPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SlotsPrize]
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 72),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R419_LAZY_SHELL_CLOUD, ["next"]
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["rose_town_hint_text"]),
        JmpIfBitSet(GAVE_SEED, ["hint_check_fertilizer2"]),
        StoreItemAmountTo7000(SeedItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            GAVE_FERTILIZER,
            ["rose_town_hint_text"],
            identifier="hint_check_fertilizer2",
        ),
        StoreItemAmountTo7000(FertilizerItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_mines(world, inventory)
            and can_clear_forest(world, inventory)
        )

    # Flag as checked: npc 1 in room 419 has its object trigger disabled.


class RoseTownInnToadPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [
        R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
        R096_ROSE_TOWN_INN_2F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TOAD
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 73),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(ROSE_TOWN_INN_TOAD_ITEM_RECEIVED, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: ROSE_TOWN_INN_TOAD_ITEM_RECEIVED


class RoseTownInnGazPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FingerShotPrize
    _rooms = [R086_ROSE_TOWN_INN_1F]
    _id = ShuffleLocationSelector.GAZ
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 74),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(ROSE_TOWN_GAZ_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)

    # Flag as checked: ROSE_TOWN_GAZ_ITEM_GRANTED


class RoseTownTreasureHouseLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 75),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: npc 0 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 76),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseMazeRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 77),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TREASURE_HUNTER_HOUSE_PRIZE, ["next"]),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(FOREST_MAZE_SECRET_FOUND, ["forest_maze_hint_text"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: TREASURE_HUNTER_HOUSE_PRIZE


class RoseTownTreasureHouseUpperChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 78),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]
    # Flag as checked: npc 1 in room 97 or 98 has its object trigger disabled.


########## forest maze


class ForestMazeFirstRoomLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R224_FOREST_MAZE_AREA_01]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 79),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R224_FOREST_MAZE_AREA_01, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 224 has its object trigger disabled.


class ForestMazeFirstUndergroundExitLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R228_FOREST_MAZE_AREA_04]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 80),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R228_FOREST_MAZE_AREA_04, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 228 has its object trigger disabled.


class ForestMazeUndergroundWigglerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        CoinPrize,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 81),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 242 has its object trigger disabled.


class ForestMazeUndergroundBottomRightTrunkChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        CoinPrize,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 82),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 3 in room 242 has its object trigger disabled.


class ForestMazeUndergroundMiddleLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = EmptyPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_3
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        CoinPrize,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 83),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 242 has its object trigger disabled.


class ForestMazeInnerMazeEntranceLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_RED_ESSENCE
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 84),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 227 has its object trigger disabled.


class ForestMazeSecretTopRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 85),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 1 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 86),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 234 has its object trigger disabled.


class ForestMazeSecretTopMiddleChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_3
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 87),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 3 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomMiddleChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_4
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 88),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 234 has its object trigger disabled.


class ForestMazeSecretLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_5
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 89),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 5 in room 234 has its object trigger disabled.


class ForestMazeBossFight(BossFightLocation):
    _bias = True
    _originally_held = BowyerBossFight
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_BOSS
    _world_area = WorldAreaEnum.FOREST_MAZE
    _pack_id = PACK181_FOREST_BOSS
    _post_unlocks_event_id = E1198_FOREST_MAZE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_11,
            sequence_setter_event_id=E0775_FOREST_MAZE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_1]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_7]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_3]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_9]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_4]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_5]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_2]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_8]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_0]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_6]),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC([R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE], [NPC_7]),
        BossFightLocationHenchmanNPC([R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE], [NPC_8]),
        BossFightLocationHenchmanNPC([R228_FOREST_MAZE_AREA_04], [NPC_1]),
        BossFightLocationHenchmanNPC(
            [R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09], [NPC_13]
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
            content.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        result = super().render(world)
        # Fix directions for all character henchman NPCs in the boss room.
        # super().render() only runs _on_henchmen_assigned when the prize
        # differs from the original, but the vanilla Aero NPCs also face
        # NORTHEAST/SOUTHWEST despite being SWSE-only sprites.
        if self._character_henchman_slots is None:
            return result
        for slot in self._character_henchman_slots:
            for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                room = world.rooms._rooms[room_id]
                assert room is not None
                obj = room.get_npc_by_target_id(npc_id)
                if obj is not None:
                    npc_base = obj._npc
                    set_npc_direction_if_swse_only(
                        world, room_id, npc_id, npc_base, SOUTHEAST
                    )
        return result

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        if self._character_henchman_slots is None:
            return

        # Build a lookup of slot -> henchman for quick access
        assignment_map: dict[BossFightLocationHenchmanNPC, BossFightHenchman] = {
            slot: henchman for slot, henchman in henchmen_assignments
        }

        removed_ctr = 0

        # Loop through ALL character henchman slots, not just assigned ones
        for slot in self._character_henchman_slots:
            henchman = assignment_map.get(slot)
            for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                # Check if this slot was assigned
                if henchman is not None:
                    npc_base = henchman.model().base
                    set_npc_direction_if_swse_only(
                        world, room_id, npc_id, npc_base, SOUTHEAST
                    )
                else:
                    # Slot was not assigned - hide the NPC with default sprite
                    if not isinstance(
                        self.prize, self._originally_held  # pyright: ignore
                    ):
                        removed_ctr += 1
                        rm = world.rooms._rooms[room_id]
                        assert rm is not None
                        rm.get_npc_by_target_id(npc_id).set_visible(False)
                        world.event_scripts.delete_command_by_identifier(
                            f"forest_henchman_{npc_id}"
                        )
        if removed_ctr == 10:
            world.event_scripts.delete_command_by_identifier(
                "forest_henchmen_bounce_30"
            )

        # If any mook henchman slot received a new model, remove Aero's
        # bouncing animation mold commands (they reference Aero-specific
        # sprite sequences that won't exist for the replacement NPC).
        if self._mook_henchman_slots is not None:
            mook_slots_assigned = any(
                slot in assignment_map and assignment_map[slot].model is not None
                for slot in self._mook_henchman_slots
            )
            if mook_slots_assigned:
                for i in range(1, 8):
                    world.action_scripts.delete_command_by_identifier(f"aero_mold_{i}")

    # Flag as checked: FOREST_LIBERATED


class ForestMazeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece2
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_STAR_PIECE
    _world_area = WorldAreaEnum.FOREST_MAZE
    _parent = ForestMazeBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 90),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_forest(
            world, inventory
        )

    # Flag as checked: FOREST_LIBERATED


class ForestMazeCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = GenoRecruitmentPrize
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_CHARACTER
    _world_area = WorldAreaEnum.FOREST_MAZE
    _container_event = E1226_FOREST_MAZE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            NPC_11,
        ),
        AllyNPCSub(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_10,
        ),
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 91),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitSet(FOREST_LIBERATED, ["next"]),
        Jmp(["forest_maze_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(6)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_forest_maze_character_empty(world)
        else:
            assert isinstance(self.prize, CharacterPrize)
            self._apply_forest_maze_npc_overrides(world)
            render_forest_maze_character(world, self.prize)
        return op

    def _apply_forest_maze_npc_overrides(self, world: GameWorld) -> None:
        """Use the MARIO_ENDING_2 (sprite 0) NPC for Mario at every forest-maze fill.

        Forest-maze animations apply sprite_offset relative to sprite 0
        (because render_forest_maze_character passes use_primary=True for
        Mario). The default MarioCharacterNPC base is sprite 409, which makes
        those offsets resolve to unrelated sprites and corrupts animation.
        """
        assert isinstance(self.prize, CharacterPrize)
        if not isinstance(self.prize, MarioRecruitmentPrize):
            return
        from ..data.rooms.npcs import MARIO_ENDING_2

        for npc_sub in self._npc_fills:
            room = world.rooms._rooms[npc_sub.room_id]
            if room is None:
                continue
            obj = room.get_npc_by_target_id(npc_sub.npc_id)
            if obj is not None:
                obj._npc = MARIO_ENDING_2

    # Flag as checked: FOREST_LIBERATED


class GenoSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBeamSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBoostSpellPrize
    _level = 8

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = GenoWhirlSpellPrize
    _level = 11

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBlastSpellPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class GenoSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = GenoFlashSpellPrize
    _level = 17

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class GenoSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 19

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


########## pipe vault


class PipeVaultSlidingCoinRoomBackChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 92),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 8 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomMiddleChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 93),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 9 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_3
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 94),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 10 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomCoin1Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 95),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_0, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]),
        # Jmp(["pipe_vault_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1


class PipeVaultSlidingCoinRoomCoin2Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 96),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_1, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]),
        # Jmp(["pipe_vault_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 1 in room 125 has been removed from the room.


class PipeVaultSlidingCoinRoomCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_3
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 97),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_2, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]),
        # Jmp(["pipe_vault_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 2 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin4Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_4
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 98),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_3, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]),
        # Jmp(["pipe_vault_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 3 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin5Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_5
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 99),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_4, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]),
        # Jmp(["pipe_vault_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 4 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCrouchItemLocation(StandingLocationRow6):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_FROG_COIN
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 100),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 5 in room 125 has been removed from the room.


class PipeVaultGoombaThumpinFirstPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 101),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_1_GRANTED, ["next"]),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: GOOMBA_THUMPIN_PRIZE_1_GRANTED


class PipeVaultGoombaThumpinSecondPrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 102),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_2_GRANTED, ["next"]),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: GOOMBA_THUMPIN_PRIZE_2_GRANTED


class PipeVaultRisingPlatformChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 103),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 0 in room 128 has its object trigger disabled.


class PipeVaultChompweedChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins20Prize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 104),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 1 in room 128 has its object trigger disabled.


########### yoster isle


class YosterEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.YOSTER_ISLE_ENTRANCE
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 105),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, ["next"]
        ),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: npc 1 in room 33 has its object trigger disabled.


class YosterRaceCookieYoshiLocation(KeyItemLocation, NPCLocationRow5):
    _bias = True
    _originally_held = CookiesPrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_COOKIE
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 106),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitSet(YOSHI_ITEM_GRANTED, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: YOSHI_ITEM_GRANTED


class YosterRacePrize1Location(NPCLocationRow1):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_1
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 107),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["next"]),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(COOKIES_SHUFFLED, ["yoster_isle_hint_text"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["yoster_isle_hint_text"]),
        StoreItemAmountTo7000(CookiesItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize2Location(NPCLocationRow3):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 108),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["next"]),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(COOKIES_SHUFFLED, ["yoster_isle_hint_text"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["yoster_isle_hint_text"]),
        StoreItemAmountTo7000(CookiesItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize3Location(NPCLocationRow4):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_3
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 109),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["next"]),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(COOKIES_SHUFFLED, ["yoster_isle_hint_text"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["yoster_isle_hint_text"]),
        StoreItemAmountTo7000(CookiesItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


########## moleville


class TreasureShopItem1(TreasureShopLocation, NPCLocationRow1):
    _bias = True
    _originally_held = LuckyJewelPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 110),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    def render(self, world: GameWorld):
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2911_TREASURE_SELLER_ITEM_1, self.prize.nickname.get_slot_1_dialog()
            )
        return super().render(world)

    # Flag as checked: TREASURE_SHOP_ITEM_1_PURCHASED


class TreasureShopItem2(TreasureShopLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveEggPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 111),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(SEASIDE_LIBERATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_seaside_boss(
            world, inventory
        )

    def render(self, world: GameWorld):
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2908_TREASURE_SELLER_ITEM_2, self.prize.nickname.get_slot_2_dialog()
            )
        return super().render(world)

    # Flag as checked: TREASURE_SHOP_ITEM_2_PURCHASED


class TreasureShopItem3(TreasureShopLocation, NPCLocationRow3):
    _bias = True
    _originally_held = FryingPanPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 112),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(VOLCANO_LIBERATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_volcano(world, inventory)

    def render(self, world: GameWorld):
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2914_TREASURE_SELLER_ITEM_3, self.prize.nickname.get_slot_3_dialog()
            )
        return super().render(world)

    # Flag as checked: TREASURE_SHOP_ITEM_3_PURCHASED


class FireworksShopItemLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = RegularFireworksPrize
    _rooms = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _id = ShuffleLocationSelector.FIREWORKS_SHOP
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 113),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(FIREWORKS_HOUSE_ITEM_SOLD, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def key(self, world: GameWorld) -> bool:
        return not world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    # Flag as checked: FIREWORKS_HOUSE_ITEM_SOLD
    # not a check if progressive fireworks is turned off


class PurtendStoreLocation(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveFireworksPrize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.PURTEND_STORE
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 114),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(PURTEND_STORE_CHECK_DONE, ["next"]),
        JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and inventory.has_item_count(
            ProgressiveFireworksPrize, 1
        )

    # flag as checked: PURTEND_STORE_CHECK_DONE
    # not a check if progressive fireworks turned off


class CookieTraderLocation(KeyItemLocation, NPCLocationRow4):
    _bias = True
    _originally_held = ProgressiveFireworksPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.COOKIE_TRADER
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 115),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(COOKIE_TRADER_CHECKED, ["next"]),
        JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and inventory.has_item_count(
            ProgressiveFireworksPrize, 2
        )

    # flag as checked: COOKIE_TRADER_CHECKED
    # not a check if progressive fireworks turned off


class BucketGirlRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.BUCKET_GIRL
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 116),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["next"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        # If you don't have a carbo cookie and have progressive fireworks turned on, you still need to find a shuffled item. No hint.
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        # If you have vanilla fireworks turned on, you can just do the trade sequence.
        JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]),
        # Otherwise, if shuffle one is turned on, you can do the trade sequence if you have any of the three items.
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        if not can_clear_mines(world, inventory):
            return False
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            return inventory.has_item_count(ProgressiveFireworksPrize, 3)
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            return inventory.has_item(RegularFireworksPrize)
        else:
            return True

    # Flag as checked: CARBO_COOKIE_GIVEN


class OuterMinesTrampolineHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _check_npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 117),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, ["next"]
        ),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 273


class OuterMinesLeftHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    _check_npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 118),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, ["next"]
        ),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 277


class OuterMinesRightHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _check_npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 119),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            ["next"],
        ),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 283


class OuterMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco2BossFight
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _override_id = 518
    _default_battlefield = BF25_UNDERGROUND
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK164_MINES_FIRST_BOSS
    _post_unlocks_event_id = E1199_OUTER_MNES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            NPC_0,
            sequence_setter_event_id=E0777_MINES_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0779_MINES_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0781_MINES_TINY_ROOM_2_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0783_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0785_MINES_SMALL_NORTH_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0787_MINES_LONG_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE],
            [NPC_1],
            PACK142_MINES_HENCHMAN_MIDDLE,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            ],
            [NPC_1, NPC_2, NPC_3],
            PACK141_MINES_HENCHMAN_LEFT,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM],
            [NPC_1],
            PACK079_MINES_HENCHMAN_RIGHT,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [518]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = OuterMinesBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 120),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_moleville_entrance(
            world, inventory
        )

    # Flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesBossPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BambinoBombPrize
    _id = ShuffleLocationSelector.CROCO_2_ITEM
    _world_area = WorldAreaEnum.MOLEVILLE
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 121),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # flag as checked: MINES_BOSS_1_DEFEATED


class InnerMinesTracksChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MolevilleMinesStarPrize
    _rooms = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 122),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, ["next"]
        ),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 285 has its object trigger disabled.


class InnerMinesShyguyCartLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_SHY_GUY
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 123),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(RUNAWAY_MINECART_ITEM_OBTAINED, ["next"]),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: RUNAWAY_MINECART_ITEM_OBTAINED


class InnerMinesBoxesChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_COINS
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 124),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC,
            ["next"],
        ),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 280 has its object trigger disabled.


class InnerMinesSaveBlockChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 125),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            ["next"],
        ),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 288 has its object trigger disabled.


class InnerMinesHighUpChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 126),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            ["next"],
        ),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 1 in room 288 has its object trigger disabled.


class InnerMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = PunchinelloBossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK140_MINES_BOSS_2
    _post_unlocks_event_id = E1200_INNER_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            NPC_0,
            sequence_setter_event_id=E0788_MINES_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_4, NPC_5, NPC_6],
            PACK152_MINES_BOSS_ROOM_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [
                R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
            ],
            [NPC_1],
        ),
    ]
    _tiny_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_1, NPC_2, NPC_3],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
            content.extend(
                [
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
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        # Check if any tiny henchman slots were assigned
        if self._tiny_henchman_slots is not None:
            assigned_slots = {slot for slot, _ in henchmen_assignments}
            for slot in self._tiny_henchman_slots:
                if slot in assigned_slots:
                    world.action_scripts.delete_command_by_identifier("microbomb_spark")
                    break

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        assert self._npc_slots is not None
        # Read the NPC model placement chose (cached on the location).
        npc_model = self.resolve_npc_model_for_slot(world, self._npc_slots[0])
        set_mines_punch_command(world, npc_model())
        return op

    # Flag as checked: MINES_BOSS_2_DEFEATED


class InnerMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece3
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = InnerMinesBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 127),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]
    # Flag as checked: MINES_BOSS_2_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_mines(
            world, inventory
        )


class InnerMinesCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = BowserRecruitmentPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_CHARACTER
    _world_area = WorldAreaEnum.MOLEVILLE
    _container_event = E1227_MOLEVILLE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            NPC_1,
        ),
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 128),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(8)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        # starters need to be set first
        return can_clear_mines(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    # Flag as checked: MINES_BOSS_2_DEFEATED


class BowserSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = TerrorizeSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = PoisonGasSpellPrize
    _level = 12

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = CrusherSpellPrize
    _level = 15

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = BowserCrushSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class BowserSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 20

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class BowserSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 22

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class InnerMinesPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Punchinello2BossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _default_battlefield = BF25_UNDERGROUND
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _pack_id = PACK071_MINES_POSTGAME
    _post_unlocks_event_id = E1253_POSTGAME_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            NPC_0,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _parent = InnerMinesPostgameBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 129),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["_mines_boss_2_defeated_check"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            MINES_BOSS_2_DEFEATED, ["next"], identifier="_mines_boss_2_defeated_check"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["_mines_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            MINES_POSTGAME_COMPLETED,
            ["next"],
            identifier="_mines_postgame_completed_check",
        ),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(
            inventory, world
        ) and can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameDrop(NPCLocationRow1):
    _bias = True
    _originally_held = WonderChompPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_POSTGAME_DROP
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 130),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["__mines_boss_2_defeated_check"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            MINES_BOSS_2_DEFEATED, ["next"], identifier="__mines_boss_2_defeated_check"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["__mines_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            MINES_POSTGAME_COMPLETED,
            ["next"],
            identifier="__mines_postgame_completed_check",
        ),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


########## booster pass


class BoosterPassBushLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _id = ShuffleLocationSelector.BOOSTER_PASS_BUSH
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 131),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_PASS_BUSH_ITEM_FOUND, ["next"]),
        Jmp(["booster_pass_hint_text"]),
    ]
    # flag as checked: BOOSTER_PASS_BUSH_ITEM_FOUND


class BoosterPassFirstRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_PASS_1
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 132),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8, R100_BOOSTER_PASS_AREA_01, ["next"]
        ),
        Jmp(["booster_pass_hint_text"]),
    ]
    # flag as checked: npc 8 in room 100 has its object trigger disabled.


class BoosterPassFirstRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RockCandyPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_PASS_2
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 133),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R100_BOOSTER_PASS_AREA_01, ["next"]
        ),
        Jmp(["booster_pass_hint_text"]),
    ]
    # flag as checked: npc 9 in room 100 has its object trigger disabled.


class BoosterPassSecondRoomFlowerLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_PASS_FLOWER
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 134),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_6, R101_BOOSTER_PASS_AREA_02, ["next"]),
        Jmp(["booster_pass_hint_text"]),
    ]
    # flag as checked: npc 6 in room 101 has been removed from the room.


class BoosterPassSecretMiddleChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_1
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 135),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10, R405_BOOSTER_PASS_SECRET, ["next"]
        ),
        JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["booster_pass_hint_text"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 10 in room 405 has its object trigger disabled.


class BoosterPassSecretRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_2
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 136),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_11, R405_BOOSTER_PASS_SECRET, ["next"]
        ),
        JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["booster_pass_hint_text"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 11 in room 405 has its object trigger disabled.


class BoosterPassSecretLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_3
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 137),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_12, R405_BOOSTER_PASS_SECRET, ["next"]
        ),
        JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["booster_pass_hint_text"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 12 in room 405 has its object trigger disabled.


########## booster tower


class BoosterTowerSpookumStairsLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_SPOOKUM
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [ThirdMimicFightLauncher]
    _extra_sprite_buffer_rooms = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 138),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 6 in room 196 has its object trigger disabled.


class BoosterTowerTrainRoomCreviceLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    _check_npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_RAILWAY
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 139),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: NPC 1 removed from room 194


class BoosterTowerChestNearThwompLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_THWOMP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 140),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_SEESAW_CHEST_OPENED, ["next"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 2 in room 36 has its object trigger disabled.


class BoosterTowerFallingChestLocation(
    NPCLocationRow1
):  # this looks like a chest, requires an overworld item, but acts like a npc reward
    _originally_held = MasherPrize
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MASHER
    _container_event = E0253_NPC_QUEST_1_GRANT
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 141),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_SEESAW_CHEST_OPENED, ["next"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: TOWER_SEESAW_CHEST_OPENED


class BoosterTowerKnifeGuyPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BrightCardPrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 142),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check"],
            identifier="returned_mario_doll_check",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["next"], identifier="tower_boss_2_check"),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)

    # flag as checked: KNIFE_GUY_PRIZE_GRANTED


# this check does not exist if FixKnifeGuy is disabled
class BoosterTowerKnifeGuy2PrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 143),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check_"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check_"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check_"],
            identifier="returned_mario_doll_check_",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check_"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            KNIFE_GUY_SECOND_PRIZE_AWARDED, ["next"], identifier="tower_boss_2_check_"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(
            world, inventory
        ) and world.settings.isflag_enabled(_get_flag("FixKnifeGuy"))

    # flag as checked: KNIFE_GUY_SECOND_PRIZE_AWARDED


class BoosterTowerPortraitPrizeLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = ElderKeyPrize
    _rooms = [R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PORTRAITS
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 144),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_7, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 7 in room 195 has been removed from the room
    # AND
    # PORTRAIT_GAME_COMPLETED is set


class BoosterTowerElderKeyItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = ChompPrize
    _rooms = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 145),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP, ["next"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_14,
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            ["elder_key_door_opened"],
        ),
        StoreItemAmountTo7000(ElderKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_OPENED,
            ["booster_tower_hint_text"],
            identifier="elder_key_door_opened",
        ),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(ElderKeyPrize)

    # flag as checked: npc 0 in room 200 has been removed from the room.


class BoosterTowerParachuteRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 146),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 35 has its object trigger disabled.


class BoosterTowerParachuteRoomCreviceLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _check_npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE_CREVICE
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 147),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_8, R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: NPC 8 removed from room 35


class BoosterTowerCheckerboardRightmostItemLocation(
    KeyItemLocation, StandingLocationRow14
):
    _originally_held = RoomKeyPrize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 148),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 5 in room 41 has been removed from the room.


class BoosterTowerCheckerboardTopItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 149),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 0 in room 41 has been removed from the room.


class BoosterTowerCheckerboardLeftmostItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 150),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 1 in room 41 has been removed from the room.


class BoosterTowerCheckerboardUpperRightItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 151),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 2 in room 41 has been removed from the room.


class BoosterTowerCheckerboardBottomItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_4
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 152),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 3 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin1Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 153),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_7, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 7 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin2Location(StandingLocationRow6):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 154),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_8, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 8 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin3Location(StandingLocationRow7):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 155),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_9, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin4Location(StandingLocationRow8):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_4
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 156),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_10, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 10 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin5Location(StandingLocationRow9):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_5
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 157),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_11, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 11 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin6Location(StandingLocationRow10):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_6
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 158),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_12, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 12 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin7Location(StandingLocationRow11):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_7
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 159),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_13, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 13 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin8Location(StandingLocationRow12):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_8
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 160),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_14, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 14 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin9Location(StandingLocationRow13):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_9
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 161),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_15, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["next"]),
        # JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        # JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 15 in room 41 has been removed from the room.


class BoosterTowerRoomKeyChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = ZoomShoesPrize
    _rooms = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 162),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM, ["next"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["room_key_door_opened"],
        ),
        StoreItemAmountTo7000(RoomKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_OPENED, ["booster_tower_hint_text"], identifier="room_key_door_opened"
        ),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(RoomKeyPrize)

    # flag as checked: npc 0 in room 48 has its object trigger disabled.


class BoosterTowerTopFloorLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 163),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 0 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = GoodieBagPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 164),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 1 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorCornerChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 165),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 199 has its object trigger disabled.


class BoosterTowerCurtainGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = AmuletPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CURTAIN_GAME
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 166),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check__"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check__"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check__"],
            identifier="returned_mario_doll_check__",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check__"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check__"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)

    # flag as checked: TOWER_BOSS_1_STAR_PIECE
    # will be granted regardless of whether they do curtain game or fight boss


class BoosterTowerMarioDollLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = MarioDollPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MARIO_DOLL
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 167),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check___"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check___"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check___"],
            identifier="returned_mario_doll_check___",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check___"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            ["next"],
            identifier="tower_boss_2_check___",
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)

    # Flag as checked: NPC 5 removed from room 192


class BoosterTowerIndoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoosterBossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK161_TOWER_FIRST_FIGHT
    _post_unlocks_event_id = E1201_TOWER_CURTAIN_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            NPC_0,
            sequence_setter_event_id=E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_9,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            NPC_6,
            sequence_setter_event_id=E0791_TOWER_ANCESTOR_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            NPC_6,
            sequence_setter_event_id=E0792_TOWER_FIRST_BOBOMB_STAIRCASE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R054_BOOSTER_HILL_DUMMY,
            NPC_7,
        ),
        BossFightLocationNPC(
            R202_BOOSTER_TOWER_ENTRANCE,
            NPC_1,
            sequence_setter_event_id=E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            NPC_3,
            sequence_setter_event_id=E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_3,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_10,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_4, NPC_1, NPC_0, NPC_3, NPC_0, NPC_2],
            PACK000_TOWER_HENCHMAN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0053_HENCHMAN_CONTAINER_3,
        ),
        BossFightLocationHenchmanNPC(
            [
                R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_0, NPC_2, NPC_1, NPC_4, NPC_1, NPC_1],
            PACK001_TOWER_HENCHMAN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0054_HENCHMAN_CONTAINER_4,
        ),
        BossFightLocationHenchmanNPC(
            [
                R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_8, NPC_3, NPC_2, NPC_5, NPC_2, NPC_3],
            PACK054_TOWER_HENCHMAN_3,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0055_HENCHMAN_CONTAINER_5,
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_4]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_5]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_6]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_7]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_8]
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R405_BOOSTER_PASS_SECRET],
            [NPC_9],
            PACK032_TOWER_PASS_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        )
    ]
    _dialogs_expecting_replacement = [
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
        DI2560_TOWER_HENCHMAN_1,
        DI2572_TOWER_HENCHMAN_2,
        DI3072_TOWER_HENCHMAN_3_WINDOW,
        DI3073_TOWER_HENCHMAN_3,
        DI4060_NEED_TO_DO_CHAPEL_CHECKS,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.npc_slots and self.prize and self.prize.model:
            assert isinstance(self.prize, BossFightPrize)
            is_vanilla = isinstance(
                self.prize, (self._originally_held, Booster2BossFight)
            )

            # Check if character henchman slots are assigned (KeepMinigameSpritesIntact not set)
            from ..types.flags import KeepMinigameSpritesIntact

            character_henchmen_assigned = not world.settings.isflag_enabled(
                KeepMinigameSpritesIntact
            ) and (
                (
                    self.prize.character_henchmen is not None
                    and len(self.prize.character_henchmen) >= 3
                )
                or (
                    self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
            )

            render_booster_tower_indoor_boss(
                world,
                self.prize,
                self.npc_slots,
                is_vanilla,
                character_henchmen_assigned,
            )
            if character_henchmen_assigned:
                char_count = (
                    len(self.prize.character_henchmen)
                    if self.prize.character_henchmen
                    else 0
                )
                has_mook_fallback = (
                    char_count < 3
                    and self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
                effective_count = 3 if has_mook_fallback else char_count
                render_booster_tower_henchman_scripts(
                    world,
                    self.prize,
                    effective_count,
                )

            # Only if mook henchman slot is assigned
            mook_henchmen_assigned = (
                not world.settings.isflag_enabled(KeepMinigameSpritesIntact)
                and self.prize.mook_henchmen is not None
                and len(self.prize.mook_henchmen) > 0
            )

        return op

    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerIndoorBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 168),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check____"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check____"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check____"],
            identifier="returned_mario_doll_check____",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check____"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check____"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Booster2BossFight
    _rooms = [R004_POSTGAME_TOWER]
    _override_id = 528
    _default_battlefield = BF12_BOOSTER_TOWER
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _pack_id = PACK070_TOWER_POSTGAME
    _post_unlocks_event_id = E1202_POSTGAME_TOWER_CURTAIN_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R004_POSTGAME_TOWER,
            NPC_0,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_3],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.npc_slots and self.prize and self.prize.model:
            render_booster_tower_indoor_boss_postgame(
                world,
                self.prize,
            )
        assert isinstance(self.prize, BossFightPrize)
        is_vanilla = isinstance(self.prize, (BoosterBossFight, Booster2BossFight))
        has_henchmen_substitutions = (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) > 0
        ) or (
            self.prize.mook_henchmen is not None and len(self.prize.mook_henchmen) > 0
        )
        if not is_vanilla and not has_henchmen_substitutions:
            room = world.rooms._rooms[R004_POSTGAME_TOWER]
            assert room is not None
            room.get_npc_by_target_id(NPC_1).set_visible(False)
            room.get_npc_by_target_id(NPC_2).set_visible(False)
            room.get_npc_by_target_id(NPC_3).set_visible(False)

        return op

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerIndoorStarPieceRemake(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _override_id = 528
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _parent = BoosterTowerIndoorBossFightRemake
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 169),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check_____"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check_____"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check_____"],
            identifier="returned_mario_doll_check_____",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check_____"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check_____"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["__tower_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            POSTGAME_TOWER_COMPLETED,
            ["next"],
            identifier="__tower_postgame_completed_check",
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerRemakeBossFightPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = Stella023Prize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_POSTGAME_DROP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 170),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check_______"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check_______"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check_______"],
            identifier="returned_mario_doll_check_______",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check_______"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check_______"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["___tower_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            POSTGAME_TOWER_COMPLETED,
            ["next"],
            identifier="___tower_postgame_completed_check",
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerBalconyBossFight(BossFightLocation):
    _bias = True
    _originally_held = KnifeGuyGrateGuyBossFight
    _rooms = [R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK177_TOWER_SECOND_BOSS
    _post_unlocks_event_id = E1203_TOWER_BALCONY_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
            content.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
            content.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: TOWER_BOSS_2_DEFEATED


class BoosterTowerBalconyStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerBalconyBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 171),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check______"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check______"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check______"],
            identifier="returned_mario_doll_check______",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check______"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_2_DEFEATED, ["next"], identifier="tower_boss_2_check______"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: TOWER_BOSS_2_DEFEATED


########## booster hill


class BoosterHillGuaranteedItem1(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 0
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_1
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P038_BOOSTER_HILL_PRIZE_0,
        P069_BOOSTER_HILL_PRIZE_STANDING_0,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 172),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 1),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 0 to 1


class BoosterHillGuaranteedItem2(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 1
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_2
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P039_BOOSTER_HILL_PRIZE_1,
        P071_BOOSTER_HILL_PRIZE_STANDING_1,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 173),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 2),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 1 to 2


class BoosterHillGuaranteedItem3(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 2
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_3
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P041_BOOSTER_HILL_PRIZE_2,
        P072_BOOSTER_HILL_PRIZE_STANDING_2,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 174),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 3),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 2 to 3


class BoosterHillGuaranteedItem4(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 3
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_4
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P042_BOOSTER_HILL_PRIZE_3,
        P074_BOOSTER_HILL_PRIZE_STANDING_3,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 175),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 4),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 3 to 4


class BoosterHillGuaranteedItem5(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 4
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_5
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P044_BOOSTER_HILL_PRIZE_4,
        P075_BOOSTER_HILL_PRIZE_STANDING_4,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 176),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 5),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 4 to 5


class BoosterHillGuaranteedItem6(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 5
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_6
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P046_BOOSTER_HILL_PRIZE_5,
        P077_BOOSTER_HILL_PRIZE_STANDING_5,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 177),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 6),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 5 to 6


class BoosterHillGuaranteedItem7(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 6
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_7
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P057_BOOSTER_HILL_PRIZE_6,
        P078_BOOSTER_HILL_PRIZE_STANDING_6,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 178),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 7),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 6 to 7


class BoosterHillGuaranteedItem8(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 7
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_8
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P058_BOOSTER_HILL_PRIZE_7,
        P080_BOOSTER_HILL_PRIZE_STANDING_7,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 179),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 8),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 7 to 8


class BoosterHillGuaranteedItem9(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 8
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_9
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P059_BOOSTER_HILL_PRIZE_8,
        P081_BOOSTER_HILL_PRIZE_STANDING_8,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 180),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 9),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 8 to 9


class BoosterHillGuaranteedItem10(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 9
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_10
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P060_BOOSTER_HILL_PRIZE_9,
        P082_BOOSTER_HILL_PRIZE_STANDING_9,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 181),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 9 to 10


class BoosterHillGuaranteedItem11(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 10
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_11
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P061_BOOSTER_HILL_PRIZE_10,
        P083_BOOSTER_HILL_PRIZE_STANDING_10,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 182),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 11),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 10 to 11


class BoosterHillGuaranteedItem12(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 11
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_12
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P100_BOOSTER_HILL_PRIZE_11,
        P084_BOOSTER_HILL_PRIZE_STANDING_11,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 183),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 12),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 11 to 12


class BoosterHillGuaranteedItem13(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 12
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_13
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P063_BOOSTER_HILL_PRIZE_12,
        P085_BOOSTER_HILL_PRIZE_STANDING_12,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 184),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 13),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 12 to 13


class BoosterHillGuaranteedItem14(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 13
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_14
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P065_BOOSTER_HILL_PRIZE_13,
        P086_BOOSTER_HILL_PRIZE_STANDING_13,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 185),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 14),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 13 to 14


class BoosterHillGuaranteedItem15(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 14
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_15
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P066_BOOSTER_HILL_PRIZE_14,
        P087_BOOSTER_HILL_PRIZE_STANDING_14,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 186),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 15),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 14 to 15


class BoosterHillGuaranteedItem16(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 15
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_16
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P068_BOOSTER_HILL_PRIZE_15,
        P088_BOOSTER_HILL_PRIZE_STANDING_15,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 187),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 16),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 15 to 16


########## marrymore


class MarrymoreFirstSuitePrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_1
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 188),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0709_SUITE_1_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize1Threshold setting


class MarrymoreSecondSuitePrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_2
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 189),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0710_SUITE_2_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize2Threshold setting


class MarrymoreThirdSuitePrizeLocation(NPCLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_3
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 190),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0711_SUITE_3_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize3Threshold setting


class MarrymoreFourthSuitePrizeLocation(NPCLocationRow4):
    _originally_held = FrogCoin2Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_4
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 191),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0712_SUITE_4_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize4Threshold setting


class MarrymoreFifthSuitePrizeLocation(NPCLocationRow5):
    _originally_held = FrogCoin3Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_5
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 192),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0713_SUITE_5_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize5Threshold setting


class MarrymoreSixthSuitePrizeLocation(NPCLocationRow6):
    _originally_held = FrogCoin20Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_6
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 193),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E0714_SUITE_6_HINT_SUBR),
    ]
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize6Threshold setting
    # LMK if these need dedicated bits or if AP is able to figure out the threshold on its own


class MarrymoreBigTipLocation(NPCLocationRow7):
    _originally_held = FlowerBoxPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_BIG_TIP
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 194),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MARRYMORE_MAJOR_TIP_GIVEN, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]
    # flag as checked: MARRYMORE_MAJOR_TIP_GIVEN


class MarrymoreHotelChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R009_MARRYMORE_INN_REGULAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MARRYMORE_INN
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 195),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM, ["next"]
        ),
        Jmp(["marrymore_hotel_hint_text"]),
    ]
    # flag as checked: npc 0 in room 9 has its object trigger disabled.


# These are really NPC grants but they need sprite replacements.
# Override container event
class MarrymoreSnifit1Location(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_1
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E0253_NPC_QUEST_1_GRANT
    _npc_ids = [NPC_8]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 196),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitSet(CHAPEL_ITEM_1_RETRIEVED, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_1_RETRIEVED


class MarrymoreSnifit2Location(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ShoesPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_2
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E0252_NPC_QUEST_2_GRANT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 197),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitSet(CHAPEL_ITEM_2_RETRIEVED, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_2_RETRIEVED


class MarrymoreSnifit3Location(KeyItemLocation, NPCLocationRow3):
    _bias = True
    _originally_held = RingPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_3
    _world_area = WorldAreaEnum.MARRYMORE
    _npc_ids = [NPC_5]
    _container_event = E0251_NPC_QUEST_3_GRANT
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 198),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitSet(CHAPEL_ITEM_3_RETRIEVED, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_3_RETRIEVED


class MarrymoreAltarHeadLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = CrownPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.MARRYMORE_ALTAR
    _world_area = WorldAreaEnum.MARRYMORE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 199),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_7, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, ["next"]
        ),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: npc 5 in room 154 has been removed from the room.


class MarrymoreBossFight(BossFightLocation):
    _bias = True
    _originally_held = BundtBossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _pack_id = PACK176_CHAPEL_BOSS
    _post_unlocks_event_id = E1204_CHAPEL_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R155_MARRYMORE_CHAPEL_KITCHEN,
            NPC_0,
            sequence_setter_event_id=E0796_MARRYMORE_KITCHEN_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_11,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_1, NPC_3],
        ),
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_2, NPC_4],
        ),
    ]
    _dialogs_expecting_replacement = [DI2061_HEAD_CHEF, DI2062_APPRENTICE_CHEF]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
            content.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) >= 1
        ):
            render_marrymore_boss_henchmen(world, self.prize.character_henchmen)
        return op

    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_STAR_PIECE
    _world_area = WorldAreaEnum.MARRYMORE
    _parent = MarrymoreBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 200),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)

    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = ToadstoolRecruitmentPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_CHARACTER
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E1228_MARRYMORE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_10,
        ),
        AllyNPCSub(
            R054_BOOSTER_HILL_DUMMY,
            NPC_8,
        ),
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 201),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(9)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_marrymore_character_empty(world)
        else:
            assert isinstance(
                self.prize, CharacterPrize
            ), f"MarrymoreCharacter prize must be CharacterPrize, got {type(self.prize)}"
            self._apply_marrymore_npc_overrides(world)
            render_marrymore_character(world, self.prize)
        return op

    def _apply_marrymore_npc_overrides(self, world: GameWorld) -> None:
        """Apply per-character NPC overrides for Marrymore chapel/Booster Hill.

        Mario: every fill (chapel NPC_10 and Booster Hill NPC_8) gets the
        MARIO_ENDING_2 (sprite 0) NPC. Chapel animations are driven by
        update_ally_animation with use_primary=True, so the sprite_offsets
        are relative to sprite 0; leaving any fill at the default sprite 409
        Mario clone makes those offsets resolve to wrong sprites and corrupts
        the chapel animation.

        Bowser is cannot_clone=True with vram_size=1 (dedicated VRAM).
        All others are cloneable (cannot_clone=False, vram_size=0).
        """
        from smrpgpatchbuilder.datatypes.levels.classes import BufferType

        assert isinstance(self.prize, CharacterPrize)

        if isinstance(self.prize, MarioRecruitmentPrize):
            from ..data.rooms.npcs import MARIO_ENDING_2

            for npc_sub in self._npc_fills:
                room = world.rooms._rooms[npc_sub.room_id]
                if room is None:
                    continue
                obj = room.get_npc_by_target_id(npc_sub.npc_id)
                if obj is not None:
                    obj._npc = MARIO_ENDING_2

        room_54 = world.rooms._rooms[R054_BOOSTER_HILL_DUMMY]
        if room_54 is None:
            return

        # Apply NPC 8 vram/clone tuning in room 54 (Booster Hill).
        obj = room_54.get_npc_by_target_id(NPC_8)
        if obj is None:
            return
        if isinstance(self.prize, BowserRecruitmentPrize):
            obj._min_vram_size = 1
        else:
            # Mario, Mallow, Geno, Peach — cloneable, use buffer system
            obj._min_vram_size = 0
        obj._cannot_clone = True

    # Flag as checked: MARRYMORE_LIBERATED


class ToadstoolSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = TherapySpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = GroupHugSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = SleepyTimeSpellPrize
    _level = 11

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = ComeBackSpellPrize
    _level = 13

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class ToadstoolSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = MuteSpellPrize
    _level = 15

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class ToadstoolSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = PsychBombSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class MarrymoreBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Bundt2BossFight
    _rooms = [R050_POSTGAME_CHAPEL]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _override_id = 529
    _default_battlefield = BF35_MARRYMORE_CHAPEL_SANCTUARY
    _remake_only = True
    _pack_id = PACK078_CHAPEL_POSTGAME
    _post_unlocks_event_id = E1204_CHAPEL_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R050_POSTGAME_CHAPEL,
            NPC_0,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R050_POSTGAME_CHAPEL],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R050_POSTGAME_CHAPEL],
            [NPC_2],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        is_vanilla = isinstance(self.prize, (BundtBossFight, Bundt2BossFight))
        has_henchmen_substitutions = (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) > 0
        ) or (
            self.prize.mook_henchmen is not None and len(self.prize.mook_henchmen) > 0
        )
        if not is_vanilla and not has_henchmen_substitutions:
            room = world.rooms._rooms[R050_POSTGAME_CHAPEL]
            assert room is not None
            room.get_npc_by_target_id(NPC_1).set_visible(False)
            room.get_npc_by_target_id(NPC_2).set_visible(False)
        return op

    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightStarPieceRemake(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_STAR_PIECE
    _world_area = WorldAreaEnum.MARRYMORE
    _override_id = 529
    _remake_only = True
    _parent = MarrymoreBossFightRemake
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 202),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(POSTGAME_CHAPEL_COMPLETE, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_chapel_postgame_boss(
            world, inventory
        )

    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightRemakeItemDrop(NPCLocationRow4):
    _bias = True
    _originally_held = EnduringBroochPrize
    _rooms = [R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_ITEM_DROP
    _world_area = WorldAreaEnum.MARRYMORE
    _remake_only = True
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 203),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(POSTGAME_CHAPEL_COMPLETE, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)

    # flag as checked: POSTGAME_CHAPEL_COMPLETE


########### star hill


class StarHillStarPiece(StarPieceLocation):
    _originally_held = StarPiece4
    _rooms = [R159_STAR_HILL_AREA_04]
    _id = ShuffleLocationSelector.STAR_HILL_STAR_PIECE_1
    _world_area = WorldAreaEnum.STAR_HILL
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 204),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectInSpecificLevel(
            NPC_9, R159_STAR_HILL_AREA_04, ["star_hill_hint_text"]
        ),
        JmpIfBitSet(STAR_HILL_CHECKED, ["next"]),
        Jmp(["star_hill_hint_text"]),
    ]
    # Flag as checked (send item, which i guess we can't do yet with SP checks):  NPC 9 removed from room and STAR_HILL_CHECKED
    # Flag as checked (tracker): STAR_HILL_CHECKED


########### seaside town pre-liberation


class FrogDiscipleLocation1(FrogDiscipleLocation):
    _originally_held = SeeYaPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_1
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 205),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_1_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]
    # flag as checked: FROG_DISCIPLE_ITEM_1_PURCHASED


class FrogDiscipleLocation2(FrogDiscipleLocation):
    _originally_held = EarlierTimesPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_2
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 206),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_2_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]
    # flag as checked: FROG_DISCIPLE_ITEM_2_PURCHASED
    # FROG_DISCIPLE_ITEM_1_PURCHASED if SeeYa flag is enabled and shop shuffle is turned off, in which case this isn't really a check


class FrogDiscipleLocation3(FrogDiscipleLocation):
    _originally_held = ExpBoosterPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_3
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 207),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_3_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]
    # flag as checked: FROG_DISCIPLE_ITEM_3_PURCHASED
    # FROG_DISCIPLE_ITEM_2_PURCHASED if SeeYa flag is enabled and shop shuffle is turned off, in which case this isn't really a check


class FrogDiscipleLocation4(FrogDiscipleLocation):
    _originally_held = CoinTrickPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_4
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 208),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_4_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]
    # flag as checked: FROG_DISCIPLE_ITEM_4_PURCHASED
    # FROG_DISCIPLE_ITEM_3_PURCHASED if SeeYa flag is enabled and shop shuffle is turned off, in which case this isn't really a check


class FrogDiscipleLocation5(FrogDiscipleLocation):
    _originally_held = ScroogeRingPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_5
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 209),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_5_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]
    # flag as checked: FROG_DISCIPLE_ITEM_5_PURCHASED
    # FROG_DISCIPLE_ITEM_4_PURCHASED if SeeYa flag is enabled and shop shuffle is turned off, in which case this isn't really a check


########### seaside town when boss fight available


class SeasideBeachBossFight(BossFightLocation):
    _bias = True
    _originally_held = YaridovichBossFight
    _rooms = [R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_FIGHT
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _pack_id = PACK180_SEASIDE_BOSS
    _post_unlocks_event_id = E1206_SEASIDE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            NPC_0,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            NPC_4,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_6,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_7,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_0, NPC_0],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
                R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_0, NPC_0, NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_3, NPC_0, NPC_3],
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST], [NPC_0]
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2830_SEASIDE_BOSS_WELCOMES_YOU,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2832_OCCUPIED_SEASIDE_INNKEEPER,
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
            content.extend([ClearBit(LANDS_END_GATED)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, YaridovichBossFight):
            render_seaside_beach_boss(world, self.prize)

            # Hide NPCs for unassigned character henchman slots
            if (
                self._character_henchman_slots is not None
                and self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) > 0
            ):
                assigned_count = len(self.prize.character_henchmen)
                for slot_index, slot in enumerate(self._character_henchman_slots):
                    if slot_index >= assigned_count:
                        for room_id, npc_id in zip(slot.room_ids, slot.npc_ids):
                            rm = world.rooms._rooms[room_id]
                            assert rm is not None
                            rm.get_npc_by_target_id(npc_id).set_visible(False)
                        if slot_index == 0:
                            deletions = [
                                "ship_henchman_1_beach_1",
                                "ship_henchman_1_beach_2",
                                "ship_henchman_1_beach_3",
                            ]
                            for d in deletions:
                                world.event_scripts.delete_command_by_identifier(d)
                        if slot_index == 1:
                            world.event_scripts.delete_command_by_identifier(
                                "ship_henchman_2_beach_1"
                            )

        return op

    # Flag as checked: SEASIDE_LIBERATED


class SeasideBeachStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece5
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _parent = SeasideBeachBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 210),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SEASIDE_LIBERATED, ["next"]),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        Jmp(["seaside_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_seaside_boss(
            world, inventory
        )

    # Flag as checked: SEASIDE_LIBERATED


class SeasideTownBossPrizeLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = ShedKeyPrize
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 211),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0, R316_SEASIDE_TOWN_BEACH, ["seaside_town_hint_text"]
        ),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        Jmp(["seaside_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)

    # flag as checked: npc 0 in room 316 has been removed from the room.
    # TODO probably need a bit for this, item is absent by default and only summoned when boss defeated


########### seaside town gated by shed key


class SeasideTownShedRescueLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerBoxPrize
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 212),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["next"]),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            ["seaside_town_hint_text"],
        ),
        StoreItemAmountTo7000(ShedKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["seaside_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_seaside_boss(world, inventory) and inventory.has_item(
            ShedKeyPrize
        )

    # flag as checked: SEASIDE_SHED_EMPTIED


########## sea


class SeaStarslapRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SeaStarPrize
    _rooms = [R134_SEA_AREA_03_SUPER_STAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_STAR_CHEST
    _world_area = WorldAreaEnum.SEA
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 213),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R134_SEA_AREA_03_SUPER_STAR_ROOM, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 134 has its object trigger disabled.


class SeaSaveRoomBackChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_1
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 214),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 132 has its object trigger disabled.


class SeaSaveRoomMiddleChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_2
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 215),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 1 in room 132 has its object trigger disabled.


class SeaSaveRoomFrontChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_3
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 216),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 2 in room 132 has its object trigger disabled.


class SeaWhirlpoolChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 217),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 133 has its object trigger disabled.


########## sunken ship


class ShipRatStairsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 218),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 167 has its object trigger disabled.


class ShipRatStairsBoxesLocation(PacketLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_box_item"
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.CHEST
    _packet_id = P037_SHIP_STAIRCASE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS_FLOWER
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 219),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED


class ShipTroopaPuzzleLocation(PacketLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_troopa_item"
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P027_SUNKEN_SHIP_TROOPA_PUZZLE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_TROOPA_PUZZLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 220),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_TROOPA_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_TROOPA_PRIZE


class ShipTrampolinePuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_trampoline_item"
    _rooms = [R163_SUNKEN_SHIP_PUZZLE_ROOM_2]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P026_SUNKEN_SHIP_TRAMPOLINE_PUZZLE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_TRAMPOLINE_PUZZLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 221),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(UNKNOWN_707D_1, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: UNKNOWN_707D_1


class Ship3DMazePuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _replace = "spawn_ship_3d_maze_item"
    _rooms = [R168_SUNKEN_SHIP_PUZZLE_ROOM_3]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P029_SUNKEN_SHIP_3D_MAZE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_3D_MAZE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 222),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_MAZE_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_MAZE_PRIZE


class ShipShopChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SHOP
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 223),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory) and can_damage_enemies_with_spells(
            world, inventory
        )

    # flag as checked: npc 0 in room 169 has its object trigger disabled.


class ShipCoinSnakePuzzleLocation(StandingLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
    ]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _npc_ids = [
        NPC_0,
        NPC_1,
        NPC_2,
        NPC_3,
        NPC_4,
        NPC_5,
        NPC_6,
        NPC_7,
        NPC_8,
        NPC_9,
        NPC_10,
        NPC_11,
        NPC_12,
        NPC_13,
        NPC_14,
        NPC_15,
        NPC_16,
    ]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COIN_SNAKE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 224),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_COIN_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_COIN_PRIZE


class ShipCannonballPuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = MushroomPrize
    _replace = "spawn_ship_cannonball_item"
    _rooms = [R172_SUNKEN_SHIP_PUZZLE_ROOM_5]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P035_SUNKEN_SHIP_CANNONBALL_PUZZLE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CANNONBALL_PUZZLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 225),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_CANNONBALL_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_CANNONBALL_PRIZE


class ShipBarrelPuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_barrel_item"
    _rooms = [R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P036_BARREL_PUZZLE_PRIZE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BARREL_PUZZLE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 226),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(UNKNOWN_707D_5, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: UNKNOWN_707D_5


class ShipPasswordBossFight(BossFightLocation):
    _bias = True
    _originally_held = KingCalamariBossFight
    _rooms = [R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK167_SHIP_FIRST_BOSS
    _post_unlocks_event_id = E1207_SHIP_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            NPC_7,
            sequence_setter_event_id=E0800_SHIP_PASSWORD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI1660_SHIP_PASSWORD_COMPLETE]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, KingCalamariBossFight):
            render_ship_password_boss(world, self.prize)
        return op

    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class ShipPasswordStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipPasswordBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 227),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)

    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class EarlyInnerShipLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 228),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 175 has its object trigger disabled.


class EarlyInnerShipRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_2
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 229),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 175 has its object trigger disabled.


class InnerShipCloneRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 230),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 179 has its object trigger disabled.


class InnerShipBehindBoxesChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_FROG_COIN_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 231),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 183 has its object trigger disabled.


class InnerShipSaveRoomLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_HIDON_MUSHROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 232),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 184 has its object trigger disabled.


class InnerShipSaveRoomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = SecondMimicFightLauncher
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.HIDON_CHEST
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 233),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 184 has its object trigger disabled.


class Mimic2DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = SafetyBadgePrize
    _rooms = [513]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.HIDON_REWARD_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 513
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 234),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIMIC_2_CLEARED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # flag as checked: MIMIC_2_CLEARED


class Mimic2BossFight(MimicFightLocation):
    _bias = True
    _originally_held = HidonBossFight
    _rooms = [513]  # can be in any room.
    _override_id = 513
    _id = ShuffleLocationSelector.HIDON_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK157_SHIP_CHEST_FIGHT
    _post_unlocks_event_id = E1250_MIMIC_2_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # Flag as checked: MIMIC_2_CLEARED


class Mimic2StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.HIDON_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _rooms = [513]
    _override_id = 513
    _parent = Mimic2BossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 235),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIMIC_2_CLEARED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # Flag as checked: MIMIC_2_CLEARED


class Mimic2ReloadRewardLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = Coins100Prize
    _rooms: list[int] = []  # Dynamic room, handled by mimic system
    _npc_ids: list[AreaObject] = []  # No specific NPC
    _id = ShuffleLocationSelector.HIDON_REWARD_2
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 513
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 236),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MIMIC_2_CLEARED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]
    # SecondMimicFightLauncher must be blacklisted to prevent circular dependency:
    # This location's can_access requires defeating second mimic, which requires
    # accessing the SecondMimicFightLauncher location - can't be the same location.
    _blacklist = [EXPStarPrize, SlotsPrize, MimicFightInitiatorPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    def grant(self) -> EventScript:
        # Mimic rewards don't need room-specific chest disable commands
        if self.prize is None:
            return EventScript([Return()])
        return EventScript(
            [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        )

    # flag as checked: the host chest for SecondMimicFightLauncher has its object trigger disabled


UNDERWATER_ALLOWED_MODELS = [
    BigCoinObject,
    SmallCoinObject,
    FrogCoinObject,
    SmallFrogCoinObject,
    FlowerObject,
    RecoveryMushroomObject,
    DefaultItem,
    KeyObject,
]


class InnerShipFirstUnderwaterRoomBottomItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _model_allowlist = UNDERWATER_ALLOWED_MODELS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 237),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomTopItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_2
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _model_allowlist = UNDERWATER_ALLOWED_MODELS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 238),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomLeftItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_3
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _model_allowlist = UNDERWATER_ALLOWED_MODELS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 239),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomMiddleItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_4
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _model_allowlist = UNDERWATER_ALLOWED_MODELS
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 240),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 3 in room 187 has been removed from the room.


class InnerShipSecretRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SafetyRingPrize
    _rooms = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 241),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 185 has its object trigger disabled.


class InnerShipPoolRoomLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BLOOBER_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 242),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 5 in room 27 has been removed from the room.


class InnerShipBeforeBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 243),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4,
            R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 4 in room 24 has its object trigger disabled.


class ShipFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = JohnnyBossFight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK166_SHIP_SECOND_BOSS
    _post_unlocks_event_id = E1208_SHIP_END_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_8,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
            NPC_0,
            sequence_setter_event_id=E1191_ENDING_CREDITS_CLIFF_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ],
            [NPC_0, NPC_1, NPC_2, NPC_3],
            PACK068_SHIP_HENCHMAN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
            ],
            [NPC_0, NPC_1],
            PACK069_SHIP_HENCHMAN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
        DI1781_SHIP_BOSS_JUMP_ON_HEAD,
        DI1782_SHIP_BOSS_DRINK,
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
        DI1786_LETTER_FROM_SHIP_BOSS,
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
            content.extend([SetBit(SEASIDE_BOSS_AVAILABLE)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (JohnnyBossFight, Johnny2Fight)):
            render_ship_final_boss(world, self.prize)

        return op

    # Flag as checked: SHIP_LIBERATED


class ShipFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipFinalBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 244),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_LIBERATED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)

    # Flag as checked: SHIP_LIBERATED


class ShipPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Johnny2Fight
    _rooms = [R003_POSTGAME_SHIP]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 526
    _default_battlefield = BF04_SUNKEN_SHIP
    _remake_only = True
    _pack_id = PACK118_SHIP_POSTGAME
    _post_unlocks_event_id = E1209_POSTGAME_SHIP_END_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R003_POSTGAME_SHIP,
            NPC_0,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_3],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_4],
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2023_SHIP_BOSS_2_DRINK,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        assert self.prize is not None
        op = super().render(world)
        render_ship_postgame_boss(world, self.prize)
        return op

    # Flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameFightItemDrop(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = ExtraShinyStonePrize
    _rooms = [R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_DROP
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _remake_only = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 245),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(POSTGAME_SHIP_COMPLETED, ["next"]),
        JmpIfBitClear(SHIP_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["sunken_ship_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    # flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 526
    _remake_only = True
    _parent = ShipPostgameBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 246),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(POSTGAME_SHIP_COMPLETED, ["next"]),
        JmpIfBitClear(SHIP_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["sunken_ship_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_SHIP_COMPLETED


########## lands end


class LandsEndRisingPlatformChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R137_LANDS_END_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.LANDS_END_RED_ESSENCE
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 247),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R137_LANDS_END_AREA_01, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 4 in room 137 has its object trigger disabled.


class LandsEndChowPitStaticChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_1
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = []
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 248),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R138_LANDS_END_AREA_02, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 138 has its object trigger disabled.


class LandsEndChowPitMovingChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [
        SlotsPrize
    ]  # SlotsPrize can go here graphically, it's just too annoying to hit 4 times
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 249),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R138_LANDS_END_AREA_02, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 138 has its object trigger disabled.


class LandsEndBeeTowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LNDS_END_BEE_ROOM
    _world_area = WorldAreaEnum.LANDS_END
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 250),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R141_LANDS_END_AREA_04_ROTATING_FLOWERS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 141 has its object trigger disabled.


class LandsEndCaveSideRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _world_area = WorldAreaEnum.LANDS_END
    _npc_ids = [NPC_19]
    _remake_only = True
    _id = ShuffleLocationSelector.LANDS_END_CAVE_SIDE_REMAKE
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 251),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_19, R142_LANDS_END_AREA_05_SKY_BRIDGE, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and world.settings.is_flag_value(
            Remake, True
        )

    # Flag as checked: npc 19 in room 142 is removed.


class LandsEndGrottoEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_1
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 252),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7,
            R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            ["next"],
        ),
        Jmp(["lands_end_grotto_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 270 has its object trigger disabled.


class LandsEndGrottoCornerChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 253),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            ["next"],
        ),
        Jmp(["lands_end_grotto_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 270 has its object trigger disabled.


class LandsEndGrottoEndChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SHY_AWAY
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 254),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(LANDS_END_GATED, ["lands_end_grotto_end_chest_sewers_closed"]),
        JmpIfBitSet(SEWERS_CLOSED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
            ["next"],
            identifier="lands_end_grotto_end_chest_sewers_closed",
        ),
        Jmp(["lands_end_grotto_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 401 has its object trigger disabled.


class LandsEndUndergroundSaveBoxChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 255),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R263_LANDS_END_UNDERGROUND_AREA_01, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 5 in room 263 has its object trigger disabled.


class LandsEndFirstPurchasableChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndStar2Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = []
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 256),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_18, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 18 in room 262 has its object trigger disabled.


class LandsEndSecondPurchasableChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LandsEndStar3Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = []
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 257),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_19, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 19 in room 262 has its object trigger disabled.


class TroopaClimbSub12PrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TroopaPinPrize
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _id = ShuffleLocationSelector.TROOPA_CLIMB
    _world_area = WorldAreaEnum.LANDS_END
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 258),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TROOPA_CLIMB_COMPLETED, ["next"]),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and can_access_monstro_town(
            world, inventory
        )

    # TODO need to modify lands end overworld marker to never take you to the back exit if you havent unlocked the area yet
    # flag as checked: TROOPA_CLIMB_COMPLETED


class LandsEndCloudBoss(BossFightLocation):
    _bias = True
    _originally_held = MokuraBossFight
    _id = ShuffleLocationSelector.LANDS_END_CLOUD_BOSS_FIGHT
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [
        R137_LANDS_END_AREA_01,
        R317_LANDS_END_DESERT_AREA_01,
        R318_LANDS_END_DESERT_AREA_02,
        R319_LANDS_END_DESERT_AREA_06,
        R402_LANDS_END_DESERT_AREA_03,
        R403_LANDS_END_DESERT_AREA_05,
        R404_LANDS_END_DESERT_AREA_04,
        R424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE,
        R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM,
        R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE,
    ]
    _override_id = 519
    _pack_id = PACK207_LANDS_END_CLOUD
    _post_unlocks_event_id = E1210_CLOUD_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE


class LandsEndCloudStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.LANDS_END_STAR_PIECE_1
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [519]
    _override_id = 519
    _parent = LandsEndCloudBoss
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 259),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # can appear in first room
        JmpIfBitSet(LANDS_END_CLOUD_STAR_PIECE, ["next"]),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)

    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE


class BelomeTempleFortuneTellerLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins50Prize
    _rooms = [R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_TELLER
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 260),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 5 in room 420 has its object trigger disabled.


class BelomeTempleLMRChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_1
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 261),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 421 has its object trigger disabled.


class BelomeTempleLRMChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_2
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 262),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 421 has its object trigger disabled.


class BelomeTempleRLMChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_3
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 263),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 8 in room 421 has its object trigger disabled.


class BelomeTempleRMLChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 264),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 9 in room 421 has its object trigger disabled.


class BelomeBeforeBossRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_1
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 265),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 0 in room 425 has its object trigger disabled.


class BelomeBeforeBossLowerLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 266),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 1 in room 425 has its object trigger disabled.


class BelomeBeforeBossMiddleChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 267),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 2 in room 425 has its object trigger disabled.


class BelomeBeforeBossUpperLeftChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_4
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 268),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 3 in room 425 has its object trigger disabled.


class BelomeTempleTreasuryUpperCornerLeftItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 269),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 0 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_2
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 270),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 1 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerTopItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_3
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 271),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 2 in room 422 has been removed from the room.


class BelomeTempleTreasuryTopmostItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_4
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 272),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 3 in room 422 has been removed from the room.


class BelomeTempleTreasuryMidLeftItemLocation(StandingLocationRow5):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_1
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 273),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_4, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 4 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostTopItemLocation(StandingLocationRow6):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_2
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 274),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 5 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostLeftmostItemLocation(StandingLocationRow7):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_3
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 275),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 6 in room 422 has been removed from the room.


class BelomeTempleTreasuryOuterUpperRightItemLocation(StandingLocationRow8):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_4
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 276),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_7, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 7 in room 422 has been removed from the room.


class BelomeTempleTreasuryInnerUpperRightItemLocation(StandingLocationRow9):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_5
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 277),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_8, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 8 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsRightLocation(StandingLocationRow10):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_6
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 278),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_9, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 9 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowerOuterBottomRightItemLocation(StandingLocationRow11):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_7
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 279),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 10 in room 422 has been removed from the room.


class BelomeTempleTreasuryRightmostItemLocation(StandingLocationRow12):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_8
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 280),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_11, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 11 in room 422 has been removed from the room.


class BelomeTempleTreasuryBottomLeftCornerItemLocation(StandingLocationRow13):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_2
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 281),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_13, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 13 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsLeftLocation(StandingLocationRow14):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_1
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 282),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_14, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 14 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperOuterBottomRightItemLocation(StandingLocationRow15):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        FlowerObject,
        RecoveryMushroomObject,
        FrogCoinObject,
        BigCoinObject,
        SmallCoinObject,
        SmallFrogCoinObject,
        SmallFrogCoinObjectNoMoney,
        KeyObject,
        DefaultItem,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 283),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_15, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 15 in room 422 has been removed from the room.


class TempleBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome2BossFight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_FIGHT
    _world_area = WorldAreaEnum.TEMPLE
    _pack_id = PACK169_TEMPLE_BOSS
    _post_unlocks_event_id = E1211_TEMPLE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            NPC_4,
            sequence_setter_event_id=E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
            content.extend(
                [
                    SetBit(MAP_MONSTRO_TOWN),
                    SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_temple_boss(world, inventory)

    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS
    _world_area = WorldAreaEnum.TEMPLE
    _parent = TempleBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 284),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TEMPLE_BOSS_DEFEATED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_GATED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_temple_boss(
            world, inventory
        )

    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightPostgame(BossFightLocation):
    _bias = True
    _originally_held = Belome3Fight
    _rooms = [R293_BELOME_3_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_FIGHT
    _world_area = WorldAreaEnum.TEMPLE
    _override_id = 523
    _default_battlefield = BF42_BELOME_TEMPLE
    _remake_only = True
    _pack_id = PACK033_POSTGAME_TEMPLE
    _post_unlocks_event_id = E1212_POSTGAME_TEMPLE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            NPC_1,
            sequence_setter_event_id=E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple_postgame_boss(world, inventory)

    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TempleBossFightStarPiecePostgame(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME
    _world_area = WorldAreaEnum.TEMPLE
    _override_id = 523
    _remake_only = True
    _parent = TempleBossFightPostgame
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 285),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TEMPLE_POSTGAME_BOSS_DEFEATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["belome3_voucher_used"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            TEMPLE_BOSS_DEFEATED,
            ["belome_temple_hint_text"],
            identifier="belome3_voucher_used",
        ),
        JmpIfBitClear(TEMPLE_BOSS_GATED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_temple_postgame_boss(
            world, inventory
        )

    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TemplePostgameFightItemDrop(NPCLocationRow1):
    _bias = True
    _originally_held = SageStickPrize
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_DROP
    _world_area = WorldAreaEnum.TEMPLE
    _remake_only = True
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 286),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TEMPLE_POSTGAME_BOSS_DEFEATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["belome3_voucher_used2"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            TEMPLE_BOSS_DEFEATED,
            ["belome_temple_hint_text"],
            identifier="belome3_voucher_used2",
        ),
        JmpIfBitClear(TEMPLE_BOSS_GATED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple_postgame_boss(world, inventory)

    # flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


########## monstro town


class MonstroEntranceLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 287),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R267_MONSTRO_TOWN_ENTRANCE, ["next"]
        ),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    # flag as checked: npc 1 in room 267 has its object trigger disabled.


class MonstroThwompItemLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = TempleKeyPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 288),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    # flag as checked: npc 0 in room 324 has been removed from the room.


class DojoFirstFight(BossFightLocation):
    _bias = True
    _originally_held = JaggerBossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK189_DOJO_PREFIGHT
    _post_unlocks_event_id = E1213_DOJO_1_BOSS_UNLOCKS
    _allow_run_away = True

    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_1,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 289),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, JaggerBossFight):
            render_dojo_first_fight(world, self.prize)
        return op

    # Flag as checked: DOJO_BOSS_1_DEFEATED


class DojoFirstFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = DojoFirstFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 290),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]
    # Flag as checked: DOJO_BOSS_1_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_monstro_town(
            world, inventory
        )


class DojoSecondFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx1BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 515
    _default_battlefield = BF46_JINXS_DOJO
    _pack_id = PACK178_DOJO_FIGHT_1
    _post_unlocks_event_id = E1214_DOJO_2_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_0,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_2_initiate_aq",
                "dojo_boss_2_initiate",
                "dojo_boss_2_pause",
            )
        # If the swapped-in NPC's sprite has a non-gridplane mold 0,
        # set cannot_clone on the room object to prevent VRAM conflicts.
        room = world.rooms._rooms[R255_MONSTRO_TOWN_JINXS_DOJO]
        assert room is not None
        npc_obj = room.get_npc_by_target_id(NPC_0)
        sprite = world.get_sprite(npc_obj._npc.sprite_id)
        if not sprite.animation.properties.molds[0].gridplane:
            npc_obj.set_cannot_clone(True)
        return op

    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoSecondFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_2
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 515
    _parent = DojoSecondFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 291),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_monstro_town(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoThirdFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx2BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 516
    _default_battlefield = BF46_JINXS_DOJO
    _pack_id = PACK187_DOJO_SECOND_BOSS
    _post_unlocks_event_id = E1215_DOJO_3_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_2,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_3_initiate_aq",
                "dojo_boss_3_initiate",
                "dojo_boss_3_pause",
                "dojo_boss_3_deescalate_aq",
                "dojo_boss_3_deescalate",
            )
        return op

    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoThirdFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_3
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 516
    _parent = DojoThirdFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 292),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoFourthFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx3BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 517
    _default_battlefield = BF46_JINXS_DOJO
    _pack_id = PACK188_DOJO_THIRD_BOSS
    _post_unlocks_event_id = E1216_DOJO_4_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_3,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI3353_DOJO_BOSS_2_FULLY_DEFEATED]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_4_initiate_aq",
                "dojo_boss_4_initiate",
                "dojo_boss_4_pause",
                "dojo_boss_4_deescalate_aq",
                "dojo_boss_4_deescalate",
            )
        return op

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_4
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 517
    _parent = DojoFourthFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 293),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class MonstroDojoClearRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = JinxBeltPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.JINX_DOJO_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 294),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFifthFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx4BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_POSTGAME
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 525
    _default_battlefield = BF46_JINXS_DOJO
    _remake_only = True
    _pack_id = PACK119_DOJO_POSTGAME
    _post_unlocks_event_id = E1217_DOJO_5_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_4,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_fifth_dojo_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_5_initiate_aq",
                "dojo_boss_5_initiate",
                "dojo_boss_5_pause",
                "dojo_boss_5_deescalate_aq",
                "dojo_boss_5_deescalate",
            )
        return op

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class DojoFifthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 525
    _remake_only = True
    _parent = DojoFifthFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 295),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["monstro_town_hint_text"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["monstro_town_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_fifth_dojo_boss(
            world, inventory
        )

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroDojoPostgameClearRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = TeamworkBandPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 296),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(DOJO_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["monstro_town_hint_text"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["monstro_town_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_fifth_dojo_boss(world, inventory)

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroSealedDoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = CulexBossFight
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK216_MONSTRO_DOOR_BOSS
    _post_unlocks_event_id = E1218_MONSTRO_SEALED_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3338_MONSTRO_SUPERBOSS_HINT,
        DI3057_MONSTRO_SUPERBOSS_PROMPT,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_door_boss(world, inventory)

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_BOSS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = MonstroSealedDoorBossFight
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 297),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        # door will be open if you have progressive fireworks or single fireworks enabled and have gotten to the carbo cookie
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["monstro_town_hint_text"]
        ),
        # door is always openable if you have a shiny stone
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["monstro_town_hint_text"]),
        # if none of the above are true, you need to turn in the fireworks if moleville is liberated and shuffle one is turned on
        # or just buy a fireworks if vanilla behaviour enabled
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(
            SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]
        ),  # should tell you to go to moleville since thats where the shiny stone is
        StoreItemAmountTo7000(
            FireworksItem
        ),  # final branch: shuffle 1 is turned on and moleville is cleared: if you have a fireworks you can exchange it now
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sealed_door_boss(
            world, inventory
        )

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorClearRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = QuartzCharmPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 298),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        # door will be open if you have progressive fireworks or single fireworks enabled and have gotten to the carbo cookie
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["monstro_town_hint_text"]
        ),
        # door is always openable if you have a shiny stone
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["monstro_town_hint_text"]),
        # if none of the above are true, you need to turn in the fireworks if moleville is liberated and shuffle one is turned on
        # or just buy a fireworks if vanilla behaviour enabled
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(
            SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]
        ),  # should tell you to go to moleville since thats where the shiny stone is
        StoreItemAmountTo7000(
            FireworksItem
        ),  # final branch: shuffle 1 is turned on and moleville is cleared: if you have a fireworks you can exchange it now
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_door_boss(world, inventory)

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorBossFightPostgame(BossFightLocation):
    _bias = True
    _originally_held = Culex3DBossFight
    _rooms = [R351_CULEXS_ROOM]
    _override_id = 524
    _default_battlefield = BF47_CULEX
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _pack_id = PACK055_MONSTRO_DOOR_POSTGAME
    _post_unlocks_event_id = E1219_POSTGAME_MONSTRO_SEALED_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)

    _dialogs_expecting_replacement = [DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT]

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorStarPiecePostgame(StarPieceLocation):
    _bias = True
    _originally_held = None
    _override_id = 524
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _parent = MonstroSealedDoorBossFightPostgame
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 299),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["culex_pg_prereq"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ExtraShinyStoneItem, identifier="culex_pg_prereq"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sealed_postgame_boss(
            world, inventory
        )

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorClearRewardLocationPostgame(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = CrystalShardPrize
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 300),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["culex_pg_prereq2"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ExtraShinyStoneItem, identifier="culex_pg_prereq2"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroFirstSuperJumpRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = AttackScarfPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_30
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 301),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SUPER_JUMP_PRIZE_1_GRANTED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["super_jump_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            SuperJumpSpellPrize
        )

    # Flag as checked: SUPER_JUMP_PRIZE_1_GRANTED


class MonstroSecondSuperJumpRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = SuperSuitPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_100
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 302),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SUPER_JUMP_PRIZE_2_GRANTED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["super_jump_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            SuperJumpSpellPrize
        )

    # Flag as checked: SUPER_JUMP_PRIZE_2_GRANTED


class MonstroFlagExchangeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = GhostMedalPrize
    _rooms = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 303),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(MUSTY_FEARS_QUEST_COMPLETE, ["next"]),
        StoreItemAmountTo7000(DryBonesFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(BigBooFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(GreaperFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(DryBonesFlagPrize)
            and inventory.has_item(GreaperFlagPrize)
            and inventory.has_item(BigBooFlagPrize)
        )

    # Flag as checked: DI2232_FLAGS_FOUND


########## bean valley


class BeanValleyFirstDeadEndLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 304),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R252_BEAN_VALLEY_MAIN_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 3 in room 252 has its object trigger disabled.


class BeanValleyFirstProgressChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 305),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R252_BEAN_VALLEY_MAIN_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 4 in room 252 has its object trigger disabled.


class BeanValleyLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize1
    _rooms = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 306),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 0 in room 334 has its object trigger disabled.


class BeanValleyBottomLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize2
    _rooms = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 307),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 0 in room 348 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeUpperLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize3
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 308),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 0 in room 349 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeLowerLocation(TreasureChestLocationRow2):
    _originally_held = KerokeroColaPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 309),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 2 in room 349 has its object trigger disabled.


class BeanValleyRightPipeLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = ThirdMimicFightLauncher
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 310),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 5 in room 335 has its object trigger disabled.


class Mimic3BossFight(MimicFightLocation):
    _bias = True
    _originally_held = BoxBoyBossFight
    _rooms = [514]  # can be in any room.
    _override_id = 514
    _id = ShuffleLocationSelector.BOX_BOY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK158_VALLEY_CHEST_FIGHT
    _slots_pack_id = PACK160_SLOTS_CHEST_FIGHT
    _post_unlocks_event_id = E1251_MIMIC_3_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ThirdMimicFightLauncher) and not_earlygame(
            world, inventory
        )

    # Flag as checked: MIMIC_3_CLEARED


class Mimic3StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOX_BOY_BOSS
    _rooms = [514]
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _override_id = 514
    _parent = Mimic3BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and inventory.has_item(ThirdMimicFightLauncher)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: MIMIC_3_CLEARED


class BeanValleyRightPipeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 311),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 7 in room 335 has its object trigger disabled.


class BeanValleyRightPipeUnderStairsLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _check_npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 312),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_9, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 9 in room 335 is removed.


class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 313),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_13, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    # flag as checked: npc 13 in room 251 has its object trigger disabled.


class BeanValleyPlanterBossFight(BossFightLocation):
    _bias = True
    _originally_held = MegasmilaxBossFight
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK173_VALLEY_BOSS
    _post_unlocks_event_id = E1229_BEAN_VALLEY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R254_BEAN_VALLEY_SMILAX_AREA,
            NPC_1,
            sequence_setter_event_id=E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
            content.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (MegasmilaxBossFight)):
            render_bean_valley_planter_boss(world, self.prize)
        return op

    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyPlanterStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _parent = BeanValleyPlanterBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 314),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BEAN_VALLEY_BOSS_DEFEATED, ["next"]),
        Jmp(["bean_valley_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)

    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyBossNoteLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = SeedPrize
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 315),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(BEAN_VALLEY_BOSS_DEFEATED, ["next"]),
        JmpIfBitSet(SEED_CHECKED, ["next"]),
        Jmp(["bean_valley_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    # flag as checked: SEED_CHECKED


class BeanstalkLowestChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 316),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 9 in room 379 has its object trigger disabled.


class BeanValley1stRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 317),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 3 in room 378 has been removed from the room.


class BeanValley1stRoomMiddleCoinLocation(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 318),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_4, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 4 in room 378 has been removed from the room.


class BeanValley1stRoomUpperCoinLocation(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 319),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_5, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 5 in room 378 has been removed from the room.


class BeanValley1stRoomLowerCoinLocation(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 320),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectNotInSpecificLevel(NPC_6, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 6 in room 378 has been removed from the room.


class Beanstalk2ndRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 321),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_6, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 6 in room 379 has been removed from the room.


class Beanstalk2ndRoomCoin1Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 322),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 3 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin2Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 323),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 4 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin3Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 324),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 5 in room 379 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 325),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 3 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 326),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 4 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 327),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 5 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_4
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 328),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_6, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 6 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin5Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_5
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 329),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_7, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 7 in room 380 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 330),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 4 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 331),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 5 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 332),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_6, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    # flag as checked: npc 6 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkFloatingItemLocation(StandingLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 333),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_7,
            R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
            ["next"],
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 7 in room 381 has been removed from the room.


class BeanstalkUpperCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 334),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 1 in room 372 has its object trigger disabled.


class BeanstalkUpperCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RareScarfPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 335),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 2 in room 372 has its object trigger disabled.


class BeanstalkLowerCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 336),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 1 in room 373 has its object trigger disabled.


class BeanstalkLowerCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 337),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    # flag as checked: npc 2 in room 373 has its object trigger disabled.


########## casino


class CasinoGrateGuyPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = StarEggPrize
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _id = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE
    _world_area = WorldAreaEnum.CASINO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 338),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(CASINO_PRIZE_WON, ["next"]),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(MAP_CASINO, ["bean_valley_hint_text"]),
        Jmp(["casino_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BrightCardPrize)

    # flag as checked: CASINO_PRIZE_WON


########## nimbus land


class NimbusShopChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SHOP
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 339),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R344_NIMBUS_LAND_ITEM_SHOP, ["next"]
        ),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: npc 0 in room 344 has its object trigger disabled.


class NimbusInnDreamPrize1Location(NPCLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 340),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(NIMBUS_INN_PRIZE_GRANTED, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


class NimbusInnDreamPrize2Location(NPCLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 341),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(NIMBUS_INN_PRIZE_GRANTED, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


# Only enabled with one specific setting
class GarroFreeItem(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = GoldPaintPrize
    _rooms = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_GARRO
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 342),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(GARRO_ITEM_GRANTED, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: GARRO_ITEM_GRANTED


class NimbusCastleStatueGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FeatherPrize
    _rooms = [
        R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
        R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
    ]
    _override_id = 520
    _id = ShuffleLocationSelector.DODO_REWARD
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 343),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["next"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory)

    # flag as checked: STATUE_GAME_DONE


class StatueRoomBossFight(BossFightLocation):
    _bias = True
    _originally_held = DodoBossFight
    _override_id = 520
    _default_battlefield = BF22_NIMBUS_CASTLE
    _id = ShuffleLocationSelector.NIMBUS_LAND_STATUE_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK208_NIMBUS_CASTLE_FIRST_BOSS
    _post_unlocks_event_id = E1230_STATUE_BOSS_UNLOCKS
    _rooms = [
        R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
        R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
    ]
    _npc_slots = [
        BossFightLocationNPC(
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            NPC_1,
            sequence_setter_event_id=E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_3,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI2180_CHAPEL_NPC]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        from ..types.flags import KeepMinigameSpritesIntact

        assert self._npc_slots is not None
        statue_slot = next(
            (
                s
                for s in self._npc_slots
                if s.room_id == R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM
            ),
            None,
        )
        chosen = (
            self.resolve_npc_model_for_slot(world, statue_slot)
            if statue_slot is not None
            else None
        )
        render_statue_room_boss(
            world,
            self.prize,
            world.settings.isflag_enabled(KeepMinigameSpritesIntact),
            chosen_npc_model=chosen,
        )
        return op

    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class StatueRoomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STAR_PIECE_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = StatueRoomBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 344),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = world.settings.isflag_enabled(
            _get_flag("SkipBossFights")
        ) or not_earlygame(world, inventory)
        return (
            super().can_access(inventory, world)
            and can_access_nimbus_castle(world, inventory)
            and boss_condition
        )

    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class NimbusCastleOuterPrisonCellarRightNPCLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 345),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(BLUE_CELLAR_GUARD_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: BLUE_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleOuterPrisonCellarLeftNPCLocation(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = CastleKey1Prize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 346),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(RED_CELLAR_GUARD_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: RED_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleBusinessCentreOccupiedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_BUSINESS_CENTRE
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [SlotsPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 347),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(NIMBUS_MISSABLE_CHECK_CLEARED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: NIMBUS_MISSABLE_CHECK_CLEARED
    # (not really missable anymore. the chest that replaces this in the liberated castle will simply give you its item first if you didn't already get it)


class NimbusCastleCornerBridgeChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
        R500_NIMBUS_CASTLE_AREA_04_DUMMY,
    ]
    _npc_ids = [NPC_2, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_BEFORE_BIRDETTA_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 348),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 2 in room 111 has its object trigger disabled.
    # or npc 0 in room 500 has its object trigger disabled


class NimbusCastleOutOfBoundsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 349),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 0 in room 410 has its object trigger disabled


class NimbusCastleAboveJawfulChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 350),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 1 in room 410 has its object trigger disabled


class NimbusCastleSingleGoldBirdChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_SINGLE_GOLD_BIRD
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = []
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 351),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 1 in room 113 has its object trigger disabled.


class NimbusCastleTwoLevelLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 352),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 0 in room 114 has its object trigger disabled.


### nimbus castle gated by ck1


class GiantEggBossFight(BossFightLocation):
    _bias = True
    _originally_held = BirdettaBossFight
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_EGG_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK175_NIMBUS_CASTLE_SECOND_BOSS
    _post_unlocks_event_id = E1231_EGG_BOSS_UNLOCKS
    _dialogs_expecting_replacement = [DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class GiantEggStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = GiantEggBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 353),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_1"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_1"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfBitSet(
            NIMBUS_MID_BOSS_COMPLETED, ["next"], identifier="nimbus_ck_dummy_1"
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_castle_hint_text"],
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_inner_nimbus(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class NimbusCastleGiantEggRewardLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = CastleKey2Prize
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_BIRDETTA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 354),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_2"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_2"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfBitSet(
            NIMBUS_MID_BOSS_COMPLETED, ["next"], identifier="nimbus_ck_dummy_2"
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_castle_hint_text"],
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory) and not_earlygame(
            world, inventory
        )

    # flag as checked: NIMBUS_MID_BOSS_COMPLETED


### nimbus land gated by ck2


class NimbusCastleTwoLevelUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 355),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["next"],
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_3"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_3"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_3"],
            identifier="nimbus_ck_dummy_3",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_3",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_late_nimbus(world, inventory)

    # flag as checked: npc 1 in room 114 has its object trigger disabled.


class NimbusCastleBackHallwayOccupiedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = NimbusLandStarPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 356),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_4"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_4"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_4"],
            identifier="nimbus_ck_dummy_4",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_4",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_late_nimbus(world, inventory)

    # flag as checked: npc 0 in room 121 has its object trigger disabled.


class NimbusFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ValentinaBossFight
    _rooms = [R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_FINAL_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK171_NIMBUS_CASTLE_THIRD_BOSS
    _post_unlocks_event_id = E1232_NIMBUS_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0822_NIMBUS_LAND_OCCUPIED_EXTERIOR_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_4,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_11],
        ),
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_12],
        ),
    ]
    _statue_slots = [
        # Garro's house
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_1,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_2,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_3,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Main hall
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_0,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_1,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_2,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_3,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_4,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_5,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied 4-way path
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Antechamber
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_1,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied throne room
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Polishing room
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_0,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_1,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_2,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Lone statue room
        BossFightLocationNPC(
            R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            NPC_3,
            sequence_setter_event_id=E0827_NIMBUS_CASTLE_SINGLE_BIRD_STATUE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Left shaman hall
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_6,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_7,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Right shaman hall
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_6,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_7,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated throne room
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Hot springs
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_1,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_2,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_3,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_4,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Cellar hallway
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_0,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_1,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Five-door hallway
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_2,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_3,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_4,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated 4-way path
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1120_NIMBUS_BIRD_GUARD,
        DI1945_NIMBUS_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
            content.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: NIMBUS_LAND_LIBERATED


class NimbusFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_3
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = NimbusFinalBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 357),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_40"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_40"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_40"],
            identifier="nimbus_ck_dummy_40",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_40",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_nimbus_boss(
            world, inventory
        )

    # Flag as checked: NIMBUS_LAND_LIBERATED


### nimbus land gated by liberation


class NimbusCastleBackHallwayLiberatedChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_AFTER_VALENTINA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 358),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_5"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_5"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_5"],
            identifier="nimbus_ck_dummy_5",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_5",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: npc 1 in room 121 has its object trigger disabled.


class NimbusCastleBusinessCentreLiberatedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 359),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_6"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_6"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_6"],
            identifier="nimbus_ck_dummy_6",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_6",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: room 499 npc 0 deactivated


class NimbusLandRightSideLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = FertilizerPrize
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _check_npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.NIMBUS_LAND_RIGHT_SIDE
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 360),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_7"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_7"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_7"],
            identifier="nimbus_ck_dummy_7",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_7",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: NPC 9 removed from room 438.


class NimbusLandCrocoItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = SignalRingPrize
    _rooms = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 361),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_8"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_8"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_8"],
            identifier="nimbus_ck_dummy_8",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_8",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: npc 5 in room 345 has been removed from the room.


class NimbusLandInnerCellarLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _id = ShuffleLocationSelector.NIMBUS_LAND_CELLAR
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 362),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_9"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_9"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_9"],
            identifier="nimbus_ck_dummy_9",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_9",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED


########## barrel volcano


class VolcanoLavaCoveLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 363),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 355 has its object trigger disabled.


class VolcanoLavaCoveRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 364),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 2 in room 355 has its object trigger disabled.


class VolcanoEarlyProgressChestLeftLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 365),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R384_VOLCANO_AREA_05, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressChestRightLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 366),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R384_VOLCANO_AREA_05, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressThirdChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R385_VOLCANO_AREA_06]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_STAR_ROOM
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 367),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R385_VOLCANO_AREA_06, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 385 has its object trigger disabled.


class VolcanoLavaPoolLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R361_VOLCANO_AREA_09]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_LAVA_POOL
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 368),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectNotInSpecificLevel(NPC_1, R361_VOLCANO_AREA_09, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 361 has been removed from the room.


class VolcanoReverseRecoilItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_REVERSE
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 369),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_4, R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 4 in room 383 has been removed from the room.


class VolcanoRightDonutItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 370),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectNotInSpecificLevel(NPC_1, R358_VOLCANO_AREA_11, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 358 has been removed from the room.


class VolcanoLeftDonutItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 371),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectNotInSpecificLevel(NPC_2, R358_VOLCANO_AREA_11, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 2 in room 358 has been removed from the room.


class VolcanoSaveRoomLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 372),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R366_VOLCANO_AREA_13_WSAVE_POINT, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 366 has its object trigger disabled.


class VolcanoSaveRoomUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 373),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R366_VOLCANO_AREA_13_WSAVE_POINT, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 366 has its object trigger disabled.


class VolcanoShopEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_HINOPIO
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 374),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 367 has its object trigger disabled.


class VolcanoBridgeBossFight(BossFightLocation):
    _bias = True
    _originally_held = CzarDragonBossFight
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK172_VOLCANO_FIRST_BOSS
    _post_unlocks_event_id = E1233_VOLCANO_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0840_VOLCANO_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            ],
            [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)

    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoBridgeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoBridgeBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 375),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )

    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoExitBossFight(BossFightLocation):
    _bias = True
    _originally_held = AxemRangersBossFight
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK182_VOLCANO_BOSS
    _post_unlocks_event_id = E1234_VOLCANO_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R392_VOLCANO_POSTCD_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0842_VOLCANO_FINAL_PRE_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R394_VOLCANO_POSTCD_AREA_05,
            NPC_2,
            sequence_setter_event_id=E0843_VOLCANO_POST_BOSS_ROOM_WITH_ENEMY_WARPS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            NPC_1,
            sequence_setter_event_id=E0844_VOLCANO_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R391_VOLCANO_POSTCD_AREA_04,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_1, NPC_0, NPC_2],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_2, NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                R394_VOLCANO_POSTCD_AREA_05,
            ],
            [NPC_3, NPC_4, NPC_1],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R394_VOLCANO_POSTCD_AREA_05,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_4, NPC_0, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
            content.extend(
                [
                    SetBit(MAP_VISTA_HILL),
                    ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
                ]
            )
            if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                content.extend(
                    [
                        SetBit(MAP_GATE),
                        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                    ]
                )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        # STAR_PIECE_TRIGGER_EVENT
        op = super().render(world)
        if self.prize is None:
            identifier = str(uuid4())
            first: list[list[UsableEventScriptCommand]] = [
                [
                    JmpIfVarEqualsConst(
                        PRIMARY_TEMP_7000,
                        R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                        [identifier],
                    )
                ]
            ]
            second: list[UsableEventScriptCommand] = [
                ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True),
                Return(),
            ]
            op = (first, second, op[2])
        if isinstance(self.prize, AxemRangersBossFight):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_volcano_exit_boss(world, self.prize)
        return op

    # Flag as checked: VOLCANO_LIBERATED


class VolcanoExitStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece6
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoExitBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 376),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitSet(VOLCANO_LIBERATED, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if self.prize is None:
            identifier = str(uuid4())
            return (
                [
                    [
                        JmpIfVarEqualsConst(
                            PRIMARY_TEMP_7000,
                            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                            [identifier],
                        )
                    ]
                ],
                [
                    ExitToWorldMap(
                        area=OW50_BARREL_VOLCANO,
                        bit_6=True,
                        bit_7=True,
                        identifier=identifier,
                    ),
                    Return(),
                ],
            )
        else:
            return super().render(world)

    # Flag as checked: VOLCANO_LIBERATED


########## bowser's keep


class KeepDarkRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DARK_ROOM
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 377),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM, ["next"]
        ),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 0 in room 453 has its object trigger disabled.


class KeepFirstCrocoShopLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 378),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM, ["next"]
        ),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 0 in room 451 has its object trigger disabled.


class KeepFirstCrocoShopRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 379),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM, ["next"]
        ),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 1 in room 451 has its object trigger disabled.


class KeepInvisibleBridgeFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrightBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 380),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 4 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 381),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 5 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = IceBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 382),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 6 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeBackChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 383),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 7 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeCoin1Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 384),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_8, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 8 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 385),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_9, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 9 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 386),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_10, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 10 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin4Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 387),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_11, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 11 in room 322 has been removed from the room.


class KeepXYPlatformsBackLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 388),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 10 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 389),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_11, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 11 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontRightChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 390),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_12, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 12 in room 458 has its object trigger disabled.


class KeepXYPlatformsBackRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 391),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_13, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 13 in room 458 has its object trigger disabled.


class KeepElevatorRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ELEVATOR_PLATFORMS
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 392),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8,
            R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 8 in room 321 has its object trigger disabled.


class KeepCannonballRoomFrontRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 393),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 3 in room 457 has its object trigger disabled.


class KeepCannonballRoomBackChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 394),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 4 in room 457 has its object trigger disabled.


class KeepCannonballFrontLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 395),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 5 in room 457 has its object trigger disabled.


class KeepCannonballMidRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 396),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 6 in room 457 has its object trigger disabled.


class KeepCannonballMidLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 397),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 7 in room 457 has its object trigger disabled.


class KeepCannonballCoin1Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 398),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_8, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 8 in room 457 has been removed from the room.


class KeepCannonballCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 399),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_9, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 9 in room 457 has been removed from the room.


class KeepCannonballCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 400),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_10, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 10 in room 457 has been removed from the room.


class KeepCannonballCoin4Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 401),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_11, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 11 in room 457 has been removed from the room.


class KeepCannonballCoin5Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 402),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_12, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 12 in room 457 has been removed from the room.


class KeepCannonballCoin6Location(StandingLocationRow6):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 403),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_13, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 13 in room 457 has been removed from the room.


class KeepCannonballCoin7Location(StandingLocationRow7):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 404),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_14, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 14 in room 457 has been removed from the room.


class KeepCannonballCoin8Location(StandingLocationRow8):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 405),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        # JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_15, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 15 in room 457 has been removed from the room.


class KeepRotatingPlatformsFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 406),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 1 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 407),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 2 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidRightChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 408),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 3 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 409),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 4 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 410),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 5 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackChestLocation(TreasureChestLocationRow6):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 411),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)

    # flag as checked: npc 6 in room 455 has its object trigger disabled.


class ObstacleCourseFinalFight(BossFightLocation):
    _bias = True
    _originally_held = ChesterBossFight
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_CHESTER
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK159_SIX_DOOR_RUSH_FIGHT
    _post_unlocks_event_id = E1235_OBSTACLE_COURSE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_4,
            sequence_setter_event_id=E0845_VOLCANO_BRIEF_HENCHMAN_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        )
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize,
            (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
        ):
            m = self.prize.smallest_npc()
            a = m.animations.dojo_challenge
            if a is not None and a.total_duration is not None:
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_obstacle_boss_intro",
                    ),
                ).set_subscript(
                    [
                        A_FaceSouthwest(),
                        A_VisibilityOn(),
                        A_Pause(40),
                        A_SetSpriteSequence(
                            index=a.sequence_id, looping=False, is_sequence=True
                        ),
                        A_Pause(a.total_duration),
                    ]
                )
            else:
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_obstacle_boss_intro",
                    ),
                ).set_subscript(
                    [
                        A_FaceSouthwest(),
                        A_VisibilityOn(),
                        A_Pause(40),
                        A_Pause(50),
                    ]
                )
        return op

    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class ObstacleCourseFinalFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_CHESTER
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = ObstacleCourseFinalFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 412),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BATTLE_DOOR_BOSS_BIT, ["next"]),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class KeepDoorRewardChest1Location(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SonicCymbalPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 413),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_1_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_1_PRIZE_RETRIEVED


class KeepDoorRewardChest2Location(TreasureChestLocationRow2):
    _bias = True
    _originally_held = SuperSlapPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 414),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_2_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_2_PRIZE_RETRIEVED


class KeepDoorRewardChest3Location(TreasureChestLocationRow3):
    _bias = True
    _originally_held = DrillClawPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 415),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_3_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_3_PRIZE_RETRIEVED


class KeepDoorRewardChest4Location(TreasureChestLocationRow4):
    _bias = True
    _originally_held = StarGunPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 416),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_4_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = not_earlygame(world, inventory)
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_4_PRIZE_RETRIEVED


class KeepDoorRewardChest5Location(TreasureChestLocationRow5):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 417),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_5_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_5_PRIZE_RETRIEVED


class KeepDoorRewardChest6Location(TreasureChestLocationRow6):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 418),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_6_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_6_PRIZE_RETRIEVED


class KeepAfterObstaclesBossFight(BossFightLocation):
    _bias = True
    _originally_held = KamekBossFight
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK209_KEEP_FIRST_BOSS
    _post_unlocks_event_id = E1236_KEEP_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            NPC_0,
            sequence_setter_event_id=E0848_KEEP_BATTLE_DOOR_2B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
            NPC_0,
            sequence_setter_event_id=E0849_KEEP_BATTLE_DOOR_2C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            NPC_0,
            sequence_setter_event_id=E0850_KEEP_BATTLE_DOOR_1A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            NPC_0,
            sequence_setter_event_id=E0851_KEEP_BATTLE_DOOR_1B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_0,
            sequence_setter_event_id=E0846_KEEP_BATTLE_DOOR_1C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            NPC_0,
            sequence_setter_event_id=E0852_KEEP_BATTLE_DOOR_2A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR,
            NPC_6,
            sequence_setter_event_id=E1192_ENDING_CREDITS_KEEP_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if isinstance(self.prize, KamekBossFight):
            # Vanilla Kamek: super().render skips npc_slots swapping, so apply
            # the R435 ending-credits base override manually here.
            from ..data.rooms.npcs import MAGIKOOPA_NPC_2

            credits_room = world.rooms._rooms[
                R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR
            ]
            assert credits_room is not None
            credits_obj = credits_room.get_npc_by_target_id(NPC_6)
            assert credits_obj is not None
            credits_obj._npc = MAGIKOOPA_NPC_2
        if not isinstance(self.prize, KamekBossFight):
            world.event_scripts.get_command_by_identifier(
                "kamek_palette", PaletteSetMorphs
            ).set_palette_set(EPAL0025_KEEP_BOSS_1_REFORMED)
            world.event_scripts.get_command_by_identifier(
                "kamek_palette_2", PaletteSet
            ).set_palette_set_starts_at(EPAL0025_KEEP_BOSS_1_REFORMED)
            m = self.prize.smallest_npc()
            if isinstance(
                self.prize,
                (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
            ):
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_aq"
                    ),
                ).set_subscript(get_mimic_rise_kamek())
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_pause"
                )

            elif m.animations.keep_challenge is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    "keep_boss_1_animation_aq",
                    "keep_boss_1_animation",
                    A_SetSpriteSequence,
                ).set_index(m.animations.keep_challenge.sequence_id)
                cast(
                    Pause,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_pause",
                    ),
                ).set_length(max(80, m.animations.keep_challenge.total_duration + 10))
            else:
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_aq"
                )

            # rise script not used for box summon or battle halls, so have a separate if block
            if m.animations.keep_summon is not None:
                world.action_scripts.get_command_by_identifier(
                    "keep_battle_room_summon", A_SetSpriteSequence
                ).set_index(m.animations.keep_summon.sequence_id)
                world.event_scripts.get_command_by_identifier(
                    "EVENT_941_pause_0", Pause
                ).set_length(
                    (
                        m.animations.keep_summon.contact_frame
                        or m.animations.keep_summon.total_duration
                    )
                    + 12
                )
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(
                            NPC_1,
                            [
                                A_FaceSoutheast(),
                                A_Pause(60),
                                A_SetSpriteSequence(
                                    index=m.animations.keep_summon.sequence_id,
                                    is_sequence=True,
                                    looping=False,
                                    mirror_sprite=True,
                                ),
                                A_Pause(
                                    m.animations.keep_summon.contact_frame
                                    or m.animations.keep_summon.total_duration
                                ),
                            ],
                        ),
                        Return(),
                    ]
                )
            else:
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(NPC_1, [A_FaceSoutheast(), A_Pause(60)]),
                        Return(),
                    ]
                )
                world.action_scripts.delete_command_by_identifier(
                    "keep_battle_room_summon"
                )
        else:
            world.event_scripts.delete_command_by_identifier("kamek_palette_3")

        # Substitute event palettes 24 (evil) and 25 (reformed) with the
        # chosen boss's sprite palette so the pre/post-reformation scene
        # shows the correct colors for the shuffled boss.
        selected_npc = self.prize.smallest_npc()
        selected_sprite = world.get_sprite(selected_npc.base.sprite_id)
        default_palette_index = (
            selected_sprite.palette_id + selected_sprite.palette_offset
        )
        default_colors = list(
            world.sprite_palettes.get_palette(default_palette_index).colors
        )
        world.event_palettes.get_palette(EPAL0025_KEEP_BOSS_1_REFORMED).set_colors(
            default_colors
        )

        evil_palette_colors = selected_npc.evil_palette
        if evil_palette_colors is None:
            evil_colors = default_colors
        else:
            evil_colors = list(evil_palette_colors)
        world.event_palettes.get_palette(EPAL0024_KEEP_BOSS_1_EVIL).set_colors(
            evil_colors
        )

        return op

    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = KeepAfterObstaclesBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 419),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = InfiniteCoinsPrize
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, RecoveryMushroomPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 420),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, ["next"]
        ),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)

        if not isinstance(self.prize, self._originally_held):
            # only colour the chest gold if it's vanilla
            world.event_scripts.delete_command_by_identifier(
                "infinite_coin_chest_palette"
            )
            world.event_scripts.delete_command_by_identifier(
                "infinite_coin_chest_palette_2"
            )
            # give it a random sound effect
            world.event_scripts.get_subscript_command_by_identifier(
                "infinite_coin_chest_aq", "infinite_coin_chest_sfx", A_PlaySound
            ).set_sound(random.randint(1, 162))
        return op

    # flag as checked: npc 0 in room 266 has its object trigger disabled.


class KeepChandelierBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoomerBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _default_battlefield = BF07_BOWSERS_KEEP
    _pack_id = PACK210_KEEP_SECOND_BOSS
    _post_unlocks_event_id = E1237_KEEP_CHANDELIER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0853_KEEP_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, BoomerBossFight):
            assert self._npc_slots is not None
            # Read the NPC model placement chose (cached on the location).
            npc_model = self.resolve_npc_model_for_slot(world, self._npc_slots[0])
            m = npc_model()
            if m.animations.chandelier_challenge is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                    A_SetSpriteSequence,
                ).set_index(m.animations.chandelier_challenge.sequence_id)
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge_pause_45",
                    A_Pause,
                ).set_length(m.animations.chandelier_challenge.total_duration)
            else:
                world.event_scripts.delete_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                )
        return op

    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepChandelierStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _parent = KeepChandelierBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 421),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_2_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if self.prize is None:
            identifier = str(uuid4())
            assert self.override_id is not None
            first: list[list[UsableEventScriptCommand]] = [
                [JmpIfVarEqualsConst(PRIMARY_TEMP_7000, self.override_id, [identifier])]
            ]
            second: list[UsableEventScriptCommand] = [
                ClearBit(
                    DO_SECOND_KEEP_BOSS_FIGHT_FROM_STAR_PIECE, identifier=identifier
                ),
                JmpToEvent(E2226_KEEP_3RD_BOSS),
            ]
            return (first, second)
        else:
            return super().render(world)

    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ExorBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _default_battlefield = BF07_BOWSERS_KEEP
    _pack_id = PACK186_KEEP_THIRD_BOSS
    _post_unlocks_event_id = E1238_KEEP_EXIT_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(FactoryGate, FactoryGating.KEEP):
            content.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: KEEP_BOSS_3_DEFEATED


class KeepFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _parent = KeepFinalBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 422),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if self.prize is None:
            identifier = str(uuid4())
            assert self.override_id is not None
            first: list[list[UsableEventScriptCommand]] = [
                [JmpIfVarEqualsConst(PRIMARY_TEMP_7000, self.override_id, [identifier])]
            ]
            second: list[UsableEventScriptCommand] = [
                ClearBit(
                    DO_SECOND_KEEP_BOSS_FIGHT_FROM_STAR_PIECE, identifier=identifier
                ),
                JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
            ]
            return (first, second)
        else:
            return super().render(world)

    # Flag as checked: KEEP_BOSS_3_DEFEATED


########## outer factory


class OuterFactorySaveRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FACTORY_SAVE_ROOM
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 423),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT, ["next"]
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory)

    # flag as checked: npc 0 in room 237 has its object trigger disabled.


class FactoryBoltPlatformsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = UltraHammerPrize
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.FACTORY_BOLT_PLATFORMS
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 424),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7, R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, ["next"]
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory)

    # flag as checked: npc 7 in room 239 has its object trigger disabled.


class FactoryEntranceBossFight(BossFightLocation):
    _bias = True
    _originally_held = CountdownBossFight
    _rooms = [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.FACTORY
    _pack_id = PACK174_FACTORY_FIRST_BOSS
    _post_unlocks_event_id = E1239_OUTER_FACTORY_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0854_ABYSS_1ST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM],
            [NPC_1],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM],
            [NPC_2],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryEntranceStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R433_SMITHY_FACTORY_AREA_01_DUMMY]
    _id = ShuffleLocationSelector.FACTORY_BOSS_1
    _world_area = WorldAreaEnum.FACTORY
    _parent = FactoryEntranceBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 425),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryAxemConveyorsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.FACTORY_FALLING_AXEMS
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 426),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 6 in room 434 has its object trigger disabled.


class FactoryTreasurePitBackChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 427),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 0 in room 443 has its object trigger disabled.


class FactoryTreasurePitFrontChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 428),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 2 in room 443 has its object trigger disabled.


class FactoryBigConveyorRoomFirstChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 429),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 8 in room 475 has its object trigger disabled.


class FactoryBigConveyorRoomSecondChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 430),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 9 in room 475 has its object trigger disabled.


class FactoryBehindNinjasRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 431),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 1 in room 443 has its object trigger disabled.


class FactoryBehindNinjasLeftChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 432),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 3 in room 443 has its object trigger disabled.


class FactoryTransitionBossFight(BossFightLocation):
    _bias = True
    _originally_held = CloakerDominoBossFight
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.FACTORY
    _pack_id = PACK184_FACTORY_SECOND_BOSS
    _post_unlocks_event_id = E1240_OUTER_FACTORY_2_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: ABYSS_BOSS_2_DEFEATED


class FactoryTransitionStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_2
    _world_area = WorldAreaEnum.FACTORY
    _parent = FactoryTransitionBossFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 433),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(ABYSS_BOSS_2_DEFEATED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: ABYSS_BOSS_2_DEFEATED


########## inner factory


class InnerFactoryFirstFight(BossFightLocation):
    _bias = True
    _originally_held = ClerkBossFight
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK146_FACTORY_BOSS_RUSH_1
    _post_unlocks_event_id = E1241_INNER_FACTORY_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R469_FACTORY_GROUNDS_AREA_01,
            NPC_8,
            sequence_setter_event_id=E0855_INNER_FACTORY_1ST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_7],
            PACK150_FACTORY_BOSS_RUSH_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_6],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryFirstFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_1
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryFirstFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 434),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(INNER_FACTORY_ROOM_1_COMPLETED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryToadGiftLocation(NPCLocationRow1):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _id = ShuffleLocationSelector.FACTORY_TOAD_GIFT
    _world_area = WorldAreaEnum.INNER_FACTORY
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 435),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(TOAD_SHOP_FREEBIE_RECEIVED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: TOAD_SHOP_FREEBIE_RECEIVED


class InnerFactorySecondFight(BossFightLocation):
    _bias = True
    _originally_held = ManagerBossFight
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK147_FACTORY_BOSS_RUSH_2
    _post_unlocks_event_id = E1242_INNER_FACTORY_2_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R471_FACTORY_GROUNDS_AREA_02,
            NPC_15,
            sequence_setter_event_id=E0856_INNER_FACTORY_2ND_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_12],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_13],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_14],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        if isinstance(self.prize, self._originally_held):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_inner_factory_second_fight(world, self.prize)
        return op

    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactorySecondFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactorySecondFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 436),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(INNER_FACTORY_ROOM_2_COMPLETED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactoryThirdFight(BossFightLocation):
    _bias = True
    _originally_held = DirectorBossFight
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK148_FACTORY_BOSS_RUSH_3
    _post_unlocks_event_id = E1243_INNER_FACTORY_3_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R472_FACTORY_GROUNDS_AREA_03,
            NPC_10,
            sequence_setter_event_id=E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_7]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_8]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_9]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)

        # Process each slot separately
        for slot_index in range(3):
            if (
                self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) > slot_index
            ):
                render_inner_factory_third_fight_slot(
                    world, self.prize.character_henchmen[slot_index], slot_index
                )

        return op

    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryThirdFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryThirdFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 437),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectNotInSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryFourthFight(BossFightLocation):
    _bias = True
    _originally_held = GunyolkBossFight
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK149_FACTORY_BOSS_RUSH_4
    _post_unlocks_event_id = E1244_INNER_FACTORY_4_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            NPC_12,
            sequence_setter_event_id=E0858_INNER_FACTORY_4TH_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            ],
            [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6],
        ),
    ]

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        # If the prize is not the original GunyolkBossFight, hide NPCs 0-6 in room 470
        if not isinstance(self.prize, GunyolkBossFight):
            render_inner_factory_fourth_fight(world)
        return op

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class InnerFactoryFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryFourthFight
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 438),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(INNER_FACTORY_ROOM_4_COMPLETED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class FinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = SmithyBossFight
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_FINAL
    _world_area = WorldAreaEnum.INNER_FACTORY
    _rooms = [R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE]
    _pack_id = PACK185_FINAL_BOSS
    _force_battlefield = BF44_FACTORY_GROUNDS_SMITHYS_PAD
    _post_unlocks_event_id = E1245_INNER_FACTORY_5_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R509_FACTORY_GROUNDS_SMITHYS_PAD,
            NPC_8,
            sequence_setter_event_id=E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
            ],
            [
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_15,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
            ],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_factory_final_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        # Replace event scripts for non-Smithy boss in Smithy's location
        if not isinstance(self.prize, SmithyBossFight):
            render_final_boss_fight(world, self.prize)
        return op

    # Flag as checked: FACTORY_BOSS_DEFEATED


class FinalBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece7
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = FinalBossFight
    _rooms = [
        R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
        R108_MOLEVILLE_OUTSIDE,
        R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
    ]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 439),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, ["next"]
        ),
        JmpIfBitSet(MAP_GATE, ["factory_hint_text"]),
        JmpIfBitClear(CASINO_WARP_ENABLED, ["check_bucket_warp"]),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["check_bucket_warp"]),
        JmpIfBitClear(MAP_CASINO, ["bean_valley_hint_text"]),
        Jmp(["casino_hint_text"]),
        JmpIfBitClear(BUCKET_WARP_ENABLED, ["next"], identifier="check_bucket_warp"),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["next"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]),
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_inner_factory_final_boss(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: FACTORY_BOSS_DEFEATED


########## invisible flag check pool

# Three of the following locations will be chosen at random and included in the seed. If the setting is disabled, then it will be the first three (defaults).
# In a tracker, their exact locations should not be known, but these will be considered checked when a certain bit is set.
# INVISIBLE_FLAG_1_FOUND, INVISIBLE_FLAG_2_FOUND, INVISIBLE_FLAG_3_FOUND


class MariosPadBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 11
    _world_area = WorldAreaEnum.MARIOS_PAD
    _clue_text = """\n[center]My item's underneath a green bed.[await]"""
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 440),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class RoseTownSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 10
    _y_coord = 47
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = """\n[center]My item's behind a wooden flower.[await]"""
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 441),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class YosterIsleGoalFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 21
    _y_coord = 62
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _y_shift = -4
    _clue_text = """\n[center]My item's between "O" and "A".[await]"""
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 442),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory) and (
            can_access_monstro_town(world, inventory)
            or world.settings.isflag_enabled(SkipMustyFearsSequence)
        )


class MariosPadSteamwhistleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 11
    _y_coord = 34
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = "[center]Mine is underneath a steamwhistle.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 443),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    # All other flag locations are in logic only after you can talk to the musty fears because otherwise how tf would you know where to look?
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadLanternFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 13
    _y_coord = 35
    _world_area = WorldAreaEnum.MARIOS_PAD
    _x_shift = 8
    _y_shift = -8
    _clue_text = "[center]Mine is under a white lantern.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 444),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadHatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 5
    _y_coord = 13
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = """\n[center]My item's under a red hat.[await]"""
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 445),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomWayTreeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _x_coord = 11
    _y_coord = 16
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _z_coord = 3
    _x_shift = -16
    _clue_text = " Mine's under a tree, up on a ledge\n by itself.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 446),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _x_coord = 22
    _y_coord = 116
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 2
    _y_shift = -8
    _clue_text = "[center]Mine's behind a wooden mushroom.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 447),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomEmptyHouseFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
        R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE,
    ]
    _x_coord = 14
    _y_coord = 61
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _y_shift = 8
    _clue_text = " Mine is under the bed in an empty\n house.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 448),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class ChancellorThroneFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
        R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    ]
    _x_coord = 19
    _y_coord = 24
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 3
    _clue_text = "[center]Mine's under a blue chair.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 449),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BanditsWayFlowerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _x_coord = 25
    _y_coord = 89
    _world_area = WorldAreaEnum.BANDITS_WAY
    _x_shift = 16
    _clue_text = "[center]Mine's on a landing flower.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 450),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_bandits_way(
            world, inventory
        )


class KeroStairsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _x_coord = 5
    _y_coord = 41
    _world_area = WorldAreaEnum.KERO_SEWERS
    _z_coord = 4
    _y_shift = 8
    _clue_text = " Mine's in a corner, nearby lots of\n dank stairs.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 451),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["ks_availability_check"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="ks_availability_check"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class KeroGateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE]
    _x_coord = 4
    _y_coord = 88
    _world_area = WorldAreaEnum.KERO_SEWERS
    _z_coord = 4
    _x_shift = -16
    _clue_text = "[center]Mine is by a lone metal spike fence.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 452),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(SEWERS_CLOSED, ["ks_availability_check_2"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="ks_availability_check_2"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class MidasTreesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _x_coord = 24
    _y_coord = 26
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _x_shift = -8
    _clue_text = " Mine's between a lone pair of\n palm trees, near the water.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 453),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class TadpoleCabinetFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _x_coord = 25
    _y_coord = 29
    _world_area = WorldAreaEnum.TADPOLE_POND
    _z_coord = 2
    _x_shift = 8
    _y_shift = 8
    _clue_text = "[center]Mine is in a frog cabinet.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 454),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseWayDirtPatchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    _x_coord = 25
    _y_coord = 88
    _world_area = WorldAreaEnum.ROSE_WAY
    _clue_text = " Mine is in the middle of a HUGE\n patch of dirt.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 455),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 15
    _y_coord = 63
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "[center]Mine is under a depressed hydrant.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 456),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownSinkFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R089_ROSE_TOWN_DURING_BOWYER_THREE_GRANDKIDS_HOUSE,
        R090_ROSE_TOWN_THREE_GRANDKIDS_HOUSE,
    ]
    _x_coord = 15
    _y_coord = 10
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = 1
    _clue_text = "[center]My item is in a kitchen sink under\n[center] some green curtains.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 457),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownBowserFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        R086_ROSE_TOWN_INN_1F,
    ]
    _x_coord = 7
    _y_coord = 21
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "[center]Mine's under a tiny turtle.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 458),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownGardenerHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 2
    _y_coord = 85
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "[center]Mine is under a private hydrant.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 459),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 5
    _y_coord = 87
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "[center]Mine is under a private bucket.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 460),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerLeafFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _x_coord = 4
    _y_coord = 111
    _world_area = WorldAreaEnum.ROSE_TOWN
    _z_coord = 10
    _clue_text = "[center]Mine's on a big leaf between\n[center] two chests.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 461),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["rose_town_cloud_invisible_hint_check"]),
        JmpIfBitSet(GAVE_SEED, ["hint_check_fertilizer3"]),
        StoreItemAmountTo7000(SeedItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            GAVE_FERTILIZER,
            ["rose_town_cloud_invisible_hint_check"],
            identifier="hint_check_fertilizer3",
        ),
        StoreItemAmountTo7000(FertilizerItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED,
            ["next"],
            identifier="rose_town_cloud_invisible_hint_check",
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class ForestMazeSecretStumpFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R231_FOREST_MAZE_SECRET_ENTRANCE]
    _x_coord = 18
    _y_coord = 72
    _world_area = WorldAreaEnum.FOREST_MAZE
    _x_shift = 16
    _clue_text = " Mine is behind a brightly\n illuminated tree stump.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 462),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretMushroomsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R235_FOREST_MAZE_AREA_08_UNDERGROUND]
    _x_coord = 25
    _y_coord = 93
    _world_area = WorldAreaEnum.FOREST_MAZE
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 463),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretWigglerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER]
    _x_coord = 2
    _y_coord = 39
    _world_area = WorldAreaEnum.FOREST_MAZE
    _clue_text = "[center]Mine is on a sleepy bug.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 464),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class PipeVaultExteriorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R055_PIPE_VAULT_ENTRANCE]
    _x_coord = 17
    _y_coord = 19
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is by a pipe in the middle of\n the road.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 465),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class PipeVaultRedPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R129_PIPE_VAULT_AREA_05]
    _x_coord = 21
    _y_coord = 107
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -8
    _y_shift = -8
    _clue_text = "[center]Mine is behind a low red pipe.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 466),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class YosterIsleHutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 11
    _y_coord = 70
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _clue_text = "[center]Mine's under a fruity gazebo.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 467),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class MolevilleHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 6
    _y_coord = 63
    _world_area = WorldAreaEnum.MOLEVILLE
    _y_shift = -8
    _clue_text = "[center]Mine's under a gold hydrant.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 468),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMountainBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 19
    _y_coord = 33
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 14
    _clue_text = " Mine's in a bush at the top of\n a mountain.[await]"
    _x_shift = -8
    _y_shift = -8
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 469),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMountainGoFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 21
    _y_coord = 39
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 12
    _clue_text = " Mine is on “GO”.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1009),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R337_MOLEVILLE_INN]
    _x_coord = 6
    _y_coord = 12
    _world_area = WorldAreaEnum.MOLEVILLE
    _x_shift = 16
    _clue_text = "[center]Mine's under a middle bed.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 470),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMinesArrowsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MOLEVILLE
    _clue_text = " Mine's between two arrows pointing away from each other.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 471),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesCeilingFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _x_coord = 8
    _y_coord = 13
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 4
    _clue_text = " Mine's in a zig-zag room, up\n on the ceiling.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 472),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesEntryFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING]
    _x_coord = 22
    _y_coord = 23
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 3
    _x_shift = 16
    _clue_text = "\n My item?[delay]\n ...[delay]It's on the word “IN”,\n [delay]above a big hole.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 473),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_mines(
            world, inventory
        )


class BoosterPassCornerBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _x_coord = 17
    _y_coord = 112
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _x_shift = -8
    _y_shift = 8
    _clue_text = "[center]Mine's in a corner bush.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 474),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerExteriorSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _x_coord = 4
    _y_coord = 110
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = " Mine's behind a sign with Japanese\n letters.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 475),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerDeskFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    _x_coord = 24
    _y_coord = 113
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = '\n      Mine\'s under "B" and "K".[await]'
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 476),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_1"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_1"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerMasherRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _x_coord = 19
    _y_coord = 122
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _y_shift = 8
    _clue_text = "[center]Mine's on a lightly-loaded see-saw.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 477),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_2"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_2"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerCurtainFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _x_coord = 7
    _y_coord = 64
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 9
    _y_shift = 8
    _clue_text = " Mine's in a corner, between a\n window and a red curtain.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 478),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_3"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_3"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerThwompInvisibleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _x_coord = 5
    _y_coord = 114
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 12
    _clue_text = "[center]Mine is near a lonely thwomp.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 479),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_4"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_4"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBrokenFrameFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    _x_coord = 15
    _y_coord = 83
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = -8
    _y_shift = -9
    _clue_text = "[center]Mine is in a broken frame.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 480),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_5"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_5"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBeetleCageFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 18
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _clue_text = "[center]Mine is on an insect cage.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 481),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_6"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_6"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerToyBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 24
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = "[center]Mine is behind a toy box.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 482),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_7"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_7"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class MarrymoreOutsideCrateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
        R064_MARRYMORE_OUTSIDE,
    ]
    _x_coord = 23
    _y_coord = 60
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = "[center]Mine is under a lone backyard box.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 483),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreHallwayFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R011_MARRYMORE_INN_3F]
    _x_coord = 18
    _y_coord = 76
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 3
    _clue_text = " My item is in a flower pot in a\n hallway.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 484),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreCurtains(InvisibleFlagLocation):
    _bias = True
    _rooms = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 7
    _y_coord = 52
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 0
    _clue_text = " Mine's beneath a clock that's beside red curtains.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1008),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreSuiteBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 7
    _y_coord = 13
    _world_area = WorldAreaEnum.MARRYMORE
    _x_shift = -16
    _clue_text = " Mine's beneath two adjoined\n red beds.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 485),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreKitchenFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R155_MARRYMORE_CHAPEL_KITCHEN]
    _x_coord = 2
    _y_coord = 20
    _world_area = WorldAreaEnum.MARRYMORE
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is in a big cabinet full of\n dishes.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 486),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreFireplaceFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R152_MARRYMORE_CHAPEL_MAIN_HALL]
    _x_coord = 9
    _y_coord = 33
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 2
    _y_shift = -8
    _clue_text = "[center]Mine is in an empty fireplace.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 487),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreWindowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
    ]
    _x_coord = 17
    _y_coord = 15
    _world_area = WorldAreaEnum.MARRYMORE
    _clue_text = " Mine is under a single stained glass window.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1007),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class MarrymoreOrganFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 65
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine is behind a big musical\n instrument.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 488),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class MarrymoreAltarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 70
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _clue_text = "[center]Mine's behind a podium.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 489),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class StarHillNorthStarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R158_STAR_HILL_AREA_02]
    _x_coord = 8
    _y_coord = 69
    _world_area = WorldAreaEnum.STAR_HILL
    _z_coord = 2
    _x_shift = -10
    _clue_text = "[center]Mine is atop the North Star.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 490),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownAnchorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 14
    _y_coord = 57
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _x_shift = 16
    _clue_text = "[center]Mine is behind an anchor.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 491),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 16
    _y_coord = 25
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _z_coord = 5
    _x_shift = 0
    _y_shift = -8
    _clue_text = "[center]Mine is under a high steel hydrant.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 492),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 20
    _y_coord = 31
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _z_coord = 3
    _clue_text = "[center]Mine is in a bucket between two\n[center]staircases.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 493),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownFlowersFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
        R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    ]
    _x_coord = 26
    _y_coord = 60
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _clue_text = " Mine's in the middle of three\n pink flowers.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 494),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownShedBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _x_coord = 5
    _y_coord = 23
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _clue_text = " Mine's under a lone crate in an\n empty house.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 495),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["seaside_town_invis_check"]),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            ["seaside_town_invis_check"],
        ),
        StoreItemAmountTo7000(ShedKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="seaside_town_invis_check"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_seaside_boss(world, inventory)
            and inventory.has_item(ShedKeyPrize)
        )


class SeaArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 8
    _y_coord = 21
    _world_area = WorldAreaEnum.SEA
    _x_shift = -8
    _y_shift = -8
    _clue_text = "[center]Mine is beside a mossy up-arrow.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 496),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaBoxesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 9
    _y_coord = 36
    _world_area = WorldAreaEnum.SEA
    _y_shift = -8
    _clue_text = "[center]Mine's in some V-shaped boxes.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 497),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaStalagnateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _x_coord = 18
    _y_coord = 43
    _world_area = WorldAreaEnum.SEA
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is behind a big gray\n stalagnate.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 498),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaUnderwaterSailFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP]
    _x_coord = 4
    _y_coord = 41
    _world_area = WorldAreaEnum.SEA
    _clue_text = "[center]Mine's behind a sail.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 499),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipBarrelPileFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES]
    _x_coord = 7
    _y_coord = 66
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 3
    _clue_text = "[center]Mine is atop a big pile of barrels.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 500),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipDoorMarkerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY]
    _x_coord = 18
    _y_coord = 82
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 1
    _y_shift = 8
    _clue_text = " Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number “4”.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 501),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _x_coord = 16
    _y_coord = 113
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = "[center]Mine is under a floating button.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 502),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipSwitchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _x_coord = 17
    _y_coord = 121
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = (
        'Mine is underneath a floating "J"\n[center]that is all on its lonesome.[await]'
    )
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 503),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_ship(
            world, inventory
        )


class LandsEndPlatformFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R137_LANDS_END_AREA_01]
    _x_coord = 6
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "[center]Mine is under a rising platform.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 504),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class LandsEndCannonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL]
    _x_coord = 11
    _y_coord = 115
    _world_area = WorldAreaEnum.LANDS_END
    _y_shift = -8
    _clue_text = " Mine's under a big, quiet cannon.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 505),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _x_coord = 28
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 16
    _clue_text = "[center]Mine is beside an orange up-arrow.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 506),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R404_LANDS_END_DESERT_AREA_04]
    _x_coord = 23
    _y_coord = 96
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 8
    _y_shift = 8
    _clue_text = " Mine is on a short, remote red hill.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 507),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndTwoHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R319_LANDS_END_DESERT_AREA_06]
    _x_coord = 8
    _y_coord = 121
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "   My item's between two red hills.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 508),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndStalagmiteFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R265_LANDS_END_UNDERGROUND_AREA_03]
    _x_coord = 22
    _y_coord = 88
    _z_coord = 4
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 8
    _y_shift = 8
    _clue_text = (
        " Mine's on a big stalagmite\n formation in an underground cave.[await]"
    )
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 509),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndCliffBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 23
    _y_coord = 103
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 22
    _clue_text = " Mine is on a bush, way up high on\n a cliff.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 510),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 24
    _y_coord = 118
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 0
    _y_shift = -4
    _x_shift = 8
    _clue_text = "[center]My item's on a yellow arrow.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 511),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class TempleShaftFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM]
    _x_coord = 22
    _y_coord = 56
    _world_area = WorldAreaEnum.TEMPLE
    _x_shift = 8
    _clue_text = " My item's in an elevator shaft.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1004),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class TempleShaftSwitchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM]
    _x_coord = 17
    _y_coord = 18
    _world_area = WorldAreaEnum.TEMPLE
    _z_coord = 2
    _x_shift = 8
    _clue_text = " My item's below one golden wall ornament.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1005),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class BelomeBeforeBossUpperLeftChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_4
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 268),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 3 in room 425 has its object trigger disabled.


class DojoBonsaiFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _x_coord = 6
    _y_coord = 9
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _y_shift = 8
    _clue_text = "[center]Mine's underneath a bonsai tree.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 512),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroEntranceSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _x_coord = 9
    _y_coord = 102
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _clue_text = "[center]Mine's in a lone flowery bush.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroBatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 4
    _y_shift = 8
    _clue_text = "[center]Mine's behind a wooden bat.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 514),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroFanFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F]
    _x_coord = 12
    _y_coord = 80
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _x_shift = -16
    _clue_text = "[center]Mine's beside a fan.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 515),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroShellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP]
    _x_coord = 16
    _y_coord = 15
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _y_shift = 8
    _clue_text = "[center]Mine's beneath a spinning shell.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 516),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _x_coord = 17
    _y_coord = 85
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine's on an isolated, dead-end\n pipe.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 517),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyBeanstalkBlockFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA]
    _x_coord = 27
    _y_coord = 27
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _clue_text = "[center]Mine's underneath a big beanstalk.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 518),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyCloudsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _x_coord = 18
    _y_coord = 70
    _z_coord = 1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _clue_text = "Mine is below a long red spiral.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1010),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class CasinoBellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _x_coord = 5
    _y_coord = 20
    _z_coord = 1
    _world_area = WorldAreaEnum.CASINO
    _x_shift = -4
    _y_shift = -4
    _clue_text = "[center]Mine is beside a tiny bell.[await][pause]\n[center]I don't think it does anything.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 519),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            BrightCardPrize
        )


class NimbusGoldGoombaFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _x_coord = 5
    _y_coord = 14
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = "[center]Mine is on a golden Goomba.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 520),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusOutdoorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
        R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
    ]
    _x_coord = 5
    _y_coord = 49
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 2
    _clue_text = "My item is under a tree star.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1011),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusInnLobbyFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R343_NIMBUS_LAND_INN]
    _x_coord = 6
    _y_coord = 84
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 2
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is under a stove with two\n pots.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 521),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusPlantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT
    ]
    _x_coord = 27
    _y_coord = 74
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = " Mine is behind a big potted plant\n in a corner.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 522),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_10"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_10"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy_10"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_nimbus_castle(
            world, inventory
        )


class NimbusBirdFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _x_coord = 28
    _y_coord = 48
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _y_shift = -8
    _clue_text = " Mine is under a birdcage, in a\n restricted dead-end area.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 523),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_11"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_11"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_11"],
            identifier="nimbus_ck_dummy_11",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_ck_dummy3_11"],
            identifier="nimbus_ck_dummy2_11",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy3_11"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class NimbusHotSpringsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R447_NIMBUS_LAND_HOT_SPRINGS]
    _x_coord = 19
    _y_coord = 114
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 5
    _clue_text = " Mine's on the right side of a\n hot pool.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 524),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy3_12"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class BarrelVolcanoInnSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _x_coord = 15
    _y_coord = 106
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 6
    _clue_text = (
        "\n My item?[await]\n It's on an “INN” that's missing its second “N”.[await]"
    )
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1000),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class BarrelVolcanoStumpetFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R390_VOLCANO_AREA_16_ERUPTING_STUMPET]
    _x_coord = 15
    _y_coord = 8
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 0
    _clue_text = (
        "\n Mine is behind a big tree. A BIIIIIG tree. It doesn't have leaves.[await]"
    )
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1002),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoShipsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 11
    _y_coord = 61
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 2
    _clue_text = "[center]Mine is between two vehicles.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 525),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 8
    _y_coord = 56
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 1
    _x_shift = 8
    _clue_text = "[center]Mine is on a firm mattress.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1001),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoLampFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 6
    _y_coord = 56
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 0
    _clue_text = (
        " Mine is under the only artificial light source in the volcano.[await]"
    )
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 1003),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class KeepPostObstacleBossRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _x_coord = 26
    _y_coord = 97
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _x_shift = 8
    _y_shift = 8
    _clue_text = "[center]Mine is between two red doors.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 526),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_pass_obstacle_courses(world, inventory)
            and not_earlygame(world, inventory)
        )


class KeepThwompFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM]
    _x_coord = 19
    _y_coord = 47
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _clue_text = "[center]Mine is under a big thwomp.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 527),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_pass_obstacle_courses(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryCanopyFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT]
    _x_coord = 16
    _y_coord = 15
    _world_area = WorldAreaEnum.FACTORY
    _z_coord = 10
    _y_shift = 8
    _clue_text = "  My item's under a bolted canopy.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 528),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_factory(
            world, inventory
        )


class FactoryLugnutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _x_coord = 23
    _y_coord = 52
    _world_area = WorldAreaEnum.FACTORY
    _z_coord = 7
    _clue_text = "    My item's underneath a lugnut.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 529),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_factory(
            world, inventory
        )


class FactoryTrampolineFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN]
    _x_coord = 14
    _y_coord = 9
    _world_area = WorldAreaEnum.FACTORY
    _y_shift = 16
    _clue_text = " My item is with the world's\n loneliest trampoline.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 530),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _x_coord = 4
    _y_coord = 36
    _world_area = WorldAreaEnum.INNER_FACTORY
    _z_coord = 5
    _clue_text = " Mine is on a jammed machine\n button.[await]"
    _hint = [
        SetVarToConst(PRIMARY_TEMP_7000, 531),
        RunDialog(
            dialog_id=DI2010_DEBUG_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


########## Three Musty Fears Proxy Classes
# These proxy classes represent the 3 Three Musty Fears slots in the UI
# rather than exposing all individual InvisibleFlagLocation subclasses


class ThreeMustyFearsBonesProxy(PrizeLocation):
    """Proxy class for Dry Bones' invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_BONES


class ThreeMustyFearsGreaperProxy(PrizeLocation):
    """Proxy class for Greaper's invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_GREAPER


class ThreeMustyFearsBooProxy(PrizeLocation):
    """Proxy class for Big Boo's invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_BOO


########## Mixins


def can_defeat_bosses(world: GameWorld, inventory: Inventory, count: int) -> bool:
    if world.settings.is_flag_value(
        ProgressionLogicDifficulty, ProgressionLogicDifficultyOptions.HARD
    ):
        return True
    return inventory.has_item_count(BossFightPrize, count)


def not_earlygame(world: GameWorld, inventory: Inventory) -> bool:
    return can_defeat_bosses(world, inventory, 5)


#    return can_defeat_bosses(world, inventory, 0)
# setting to 0 as a test
# having this restriction makes it difficult for seeds to succeed with highly restrictive logic
# at that point i think it's kinda on you if you want to make your own life that difficult


def all_starters_places(world: GameWorld, inventory: Inventory) -> bool:
    strchars = world.settings.get_flag(StartingCharacters)
    startmax = len(strchars.enabled)
    return inventory.has_item_count(CharacterPrize, startmax)


def can_access_bandits_way(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bandit's Way."""
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.HAMMER_BRO):
        return inventory.has_item(HammerBrosFight)
    # Mushroom Way: true
    return True


def can_access_sewer(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Kero Sewers."""
    if can_access_lands_end(world, inventory):
        return True
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MACK):
        return inventory.has_item(MackBossFight)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
        return can_access_bandits_way(world, inventory)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
        return can_access_bandits_way(world, inventory) and inventory.has_item(
            RareFrogCoinPrize
        )
    return True


def can_access_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Forest Maze."""
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        return inventory.has_item(CricketPiePrize)
    return True


def can_clear_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Forest Maze."""
    return can_access_forest(world, inventory)


def can_access_pipe_vault(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Pipe Vault."""
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
        return can_clear_forest(world, inventory)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    return True


def can_access_moleville_entrance(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the uper entrance to the mines."""
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
        return can_access_forest(world, inventory)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
        return can_access_pipe_vault(world, inventory)
    return True


def can_access_inner_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the inner half
    of Moleville Mines (beyond the exploding wall)."""
    return can_access_moleville_entrance(world, inventory) and inventory.has_item(
        BambinoBombPrize
    )


def can_clear_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Moleville Mines."""
    return can_access_inner_mines(world, inventory)


def can_access_moleville_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Moleville."""
    return (
        can_access_inner_mines(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_tower(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter Booster Tower."""
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
        return inventory.has_item(MarioRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER):
        return inventory.has_item(BowserRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        return inventory.has_item(ToadstoolRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
        return can_access_inner_mines(world, inventory)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        return inventory.has_item(PunchinelloBossFight)
    return True


def can_do_tower_curtain_game(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to do the curtain game in Booster Tower."""
    if world.settings.isflag_enabled(ShuffleMarioDoll) and not inventory.has_item(
        MarioDollPrize
    ):
        return False
    return can_access_tower(world, inventory)


def can_access_tower_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Booster Tower."""
    return (
        can_do_tower_curtain_game(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_hill(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Booster Hill."""
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
        return can_do_tower_curtain_game(world, inventory)
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    return True


def can_access_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter the Marrymore chapel."""
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
        return can_do_tower_curtain_game(world, inventory)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
        return can_access_hill(world, inventory)
    return True


def can_clear_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss of Marrymore."""
    return (
        inventory.has_item(ShoesPrize)
        and inventory.has_item(RingPrize)
        and inventory.has_item(BroochPrize)
        and inventory.has_item(CrownPrize)
        and can_access_chapel(world, inventory)
        and not_earlygame(world, inventory)
    )


def can_access_chapel_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Marrymore."""
    return (
        can_clear_chapel(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_sea(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Sea."""
    if world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
        return inventory.has_item(ToadstoolRecruitmentPrize)
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        return inventory.has_item_count(StarPiecePrize, 4)
    if world.settings.is_flag_value(SeaGate, SeaGating.BUNDT):
        return inventory.has_item(BundtBossFight)
    if world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
        return can_access_chapel(world, inventory) and not_earlygame(world, inventory)
    return True


def can_clear_ship(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Sunken Ship."""
    return can_access_sea(world, inventory) and not_earlygame(world, inventory)


def can_access_ship_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Sunken Ship."""
    return (
        can_clear_ship(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Seaside Town boss."""
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
        return can_clear_ship(world, inventory)
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.JOHNNY):
        return inventory.has_item(JohnnyBossFight)
    return True


def can_clear_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    return can_access_seaside_boss(world, inventory) and not_earlygame(world, inventory)


def can_access_lands_end(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Land's End."""
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        return inventory.has_item_count(StarPiecePrize, 5)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
        return can_access_seaside_boss(world, inventory) and inventory.has_item(
            ShedKeyPrize
        )
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.YARIDOVICH):
        return inventory.has_item(YaridovichBossFight)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
        return can_clear_seaside_boss(world, inventory)
    return True


def can_access_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Belome Temple."""
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
        return inventory.has_item(TempleKeyPrize) and can_access_lands_end(
            world, inventory
        )
    return can_access_lands_end(world, inventory)


def can_clear_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Belome Temple."""
    return can_access_temple_boss(world, inventory) and not_earlygame(world, inventory)


def can_access_temple_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Belome Temple."""
    return (
        can_clear_temple_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_monstro_town(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Monstro Town."""
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
        return can_access_temple_boss(world, inventory) and not_earlygame(
            world, inventory
        )
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
        return inventory.has_item(Belome2BossFight)
    return True


def can_access_fifth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 5th Monstro dojo boss."""
    return (
        can_access_monstro_town(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_outer_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get to Nimbus Land."""
    if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
        return not_earlygame(world, inventory)
    if world.settings.is_flag_value(NimbusGate, NimbusGating.MEGASMILAX):
        return inventory.has_item(MegasmilaxBossFight)
    return True


def can_access_nimbus_castle(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Nimbus Castle."""
    outer_access = can_access_outer_nimbus(world, inventory)
    if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        return outer_access and inventory.has_item(GoldPaintPrize)
    return outer_access


def can_access_inner_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 1 door."""
    return can_access_nimbus_castle(world, inventory) and inventory.has_item(
        CastleKey1Prize
    )


def can_access_late_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 2 door."""
    return can_access_inner_nimbus(world, inventory) and inventory.has_item(
        CastleKey2Prize
    )


def can_clear_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear the Nimbus Land boss."""
    return can_access_late_nimbus(world, inventory) and not_earlygame(world, inventory)


def can_access_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Barrel Volcano."""
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
        return can_clear_nimbus_boss(world, inventory)
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA):
        return inventory.has_item(ValentinaBossFight)
    return True


def can_clear_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Barrel Volcano."""
    return can_access_volcano(world, inventory) and not_earlygame(world, inventory)


def can_access_keep(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bowser's Keep."""
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
        return can_clear_volcano(world, inventory)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        return inventory.has_item_count(StarPiecePrize, 6)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.AXEM):
        return inventory.has_item(AxemRangersBossFight)
    return True


def can_pass_obstacle_courses(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to pass the obstacle courses in Bowser's Keep."""
    return can_access_keep(world, inventory) and can_damage_enemies_with_spells(
        world, inventory
    )


def can_access_factory(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Outer Factory."""
    if world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        return (
            inventory.has_item_count(StarPiecePrize, 6)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
        return (
            inventory.has_item(ExorBossFight)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
        return can_access_keep(world, inventory)
    if world.settings.is_flag_value(FactoryGate, FactoryGating.KEEP):
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)
    return True


def can_access_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the final Factory boss."""
    value = world.settings.get_flag(_get_flag("StarPiecesRequired")).value
    has_stars = inventory.has_item_count(StarPiecePrize, value)
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        fireworks_access = inventory.has_item(RegularFireworksPrize)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        fireworks_access = inventory.has_item_count(ProgressiveFireworksPrize, 3)
    else:
        fireworks_access = True
    can_access_bucket = (
        fireworks_access
        and can_clear_mines(world, inventory)
        and world.settings.isflag_enabled(_get_flag("BucketWarp"))
    )
    can_access_casino = world.settings.isflag_enabled(
        _get_flag("CasinoWarp")
    ) and inventory.has_item(BrightCardPrize)
    return (
        has_stars
        and (
            can_access_bucket
            or can_access_casino
            or can_access_factory(world, inventory)
        )
        and not_earlygame(world, inventory)
    )


def can_access_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the sealed door boss."""
    boss_reqs = can_access_monstro_town(world, inventory) and not_earlygame(
        world, inventory
    )
    item_reqs: bool = False
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        item_reqs = inventory.has_item(RegularFireworksPrize) and can_clear_mines(
            world, inventory
        )
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        item_reqs = inventory.has_item_count(ProgressiveFireworksPrize, 2)
    else:
        item_reqs = can_clear_mines(world, inventory)
    return item_reqs and boss_reqs


def can_access_sealed_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second sealed door boss."""
    return (
        can_access_sealed_door_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and inventory.has_item(ExtraShinyStonePrize)
        and not_earlygame(world, inventory)
    )


def can_access_invisible_flags(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the invisible item checks have been activated."""
    return world.settings.isflag_enabled(
        SkipMustyFearsSequence
    ) or can_access_monstro_town(world, inventory)

    # mimic 3 and postgame temple


def can_damage_enemies_with_spells(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to damage enemies with a non-elemental spell."""
    if not world.settings.isflag_enabled(
        CharacterLearnedSpells
    ) and not world.settings.isflag_enabled(SpellsAnywhere):
        # Spells aren't shuffled, so check if the player has recruited a character
        # whose vanilla spells include a non-elemental damage spell that isn't disabled.
        disabled_spells: set[type] = {
            m.value for m in world.settings.get_flag(AvailableSpells).disabled
        }

        def spell_available(*spell_classes: type) -> bool:
            return any(s not in disabled_spells for s in spell_classes)

        if inventory.has_item(MallowRecruitmentPrize) and spell_available(
            StarRainSpell
        ):
            return True
        if inventory.has_item(GenoRecruitmentPrize) and spell_available(
            GenoWhirlSpell, GenoBlastSpell
        ):
            return True
        if inventory.has_item(BowserRecruitmentPrize) and spell_available(
            PoisonGasSpell, TerrorizeSpell
        ):
            return True
        if not world.settings.isflag_enabled(InfuseSpellElements):
            if inventory.has_item(GenoRecruitmentPrize) and spell_available(
                GenoBeamSpell, GenoFlashSpell
            ):
                return True
            if inventory.has_item(BowserRecruitmentPrize) and spell_available(
                CrusherSpell, BowserCrushSpell
            ):
                return True
            if inventory.has_item(ToadstoolRecruitmentPrize) and spell_available(
                PsychBombSpell
            ):
                return True
        return False
    pool = [
        StarRainSpellPrize,
        GenoWhirlSpellPrize,
        GenoFlashSpellPrize,
        TerrorizeSpellPrize,
        PoisonGasSpellPrize,
    ]
    if not world.settings.isflag_enabled(InfuseSpellElements):
        pool.extend(
            [
                GenoBeamSpellPrize,
                GenoBlastSpellPrize,
                CrusherSpellPrize,
                BowserCrushSpellPrize,
                PsychBombSpellPrize,
            ]
        )
    return inventory.has_one_of(pool)


def is_all_starting_chars_set(world: GameWorld, inventory: Inventory | None = None):
    """Check if all starting character slots are filled.

    If inventory is provided, also counts character prizes in the inventory
    as "effectively set" for assumed-reachability placement.
    """
    from ..types.prize import CharacterPrize

    strchars = world.settings.get_flag(StartingCharacters)
    startmax = len(strchars.enabled)

    # Count how many character prizes are in the assumed inventory
    chars_in_inventory = 0
    if inventory is not None:
        chars_in_inventory = sum(
            1 for item in inventory if isinstance(item, CharacterPrize)
        )

    # Count how many starting slots are unfilled
    unfilled_slots = 0
    starting_locations = [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    ]
    for i in range(startmax):
        loc = world.get_location(starting_locations[i])
        if loc.prize is None:
            unfilled_slots += 1

    # All starting chars are "effectively set" if the inventory has enough
    # character prizes to fill the unfilled slots
    return chars_in_inventory >= unfilled_slots
