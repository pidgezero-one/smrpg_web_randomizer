from .types.prizelocation import TreasureChestLocationRow1, TreasureChestLocationRow2, TreasureChestLocationRow3, TreasureChestLocationRow4, TreasureChestLocationRow5, TreasureChestLocationRow6, NPCLocationRow1, NPCLocationRow2, NPCLocationRow3, NPCLocationRow4, NPCLocationRow5, NPCLocationRow6, NPCLocationRow7, StandingLocationRow1, StandingLocationRow2, StandingLocationRow3, StandingLocationRow4, StandingLocationRow5, StandingLocationRow6, StandingLocationRow7, StandingLocationRow8, StandingLocationRow9, StandingLocationRow10, StandingLocationRow11, StandingLocationRow12, StandingLocationRow13, StandingLocationRow14, StandingLocationRow15, RiverLocation, BossFightLocation, CharacterRecruitmentLocation, StarPieceLocation, ShopLocation, SpellSlotLocation
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from .prizes import *
from .types.prize import Prize, CoinPrize, FPFlowerPrize, FrogCoinPrize1
from randomizer.types.world.flags import ShuffleLocationSelector
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9, NPC_10, NPC_11, NPC_12, NPC_13, NPC_14, NPC_15, NPC_16, NPC_17, NPC_18, NPC_19, NPC_20, NPC_21, NPC_22, NPC_23, NPC_24, NPC_25, NPC_26, NPC_27

# Comments are included here to document what condition is met for a location to be considered checked.
# Anything that takes a flag has a variable name listed, ie TOAD_IN_MUSHROOM_WAY_1.
# The actual memory address this corresponds to can be found in data/variables/variable_names.py
# ie TOAD_IN_MUSHROOM_WAY_1 = Flag(0x7052, 4) = $7052 bit 4

class StartingItem1Location(NPCLocationRow2):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_1
    # this is granted at the start of the game by default

class StartingItem2Location(NPCLocationRow3):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_2
    # this is granted at the start of the game by default

class StartingItem3Location(NPCLocationRow4):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_3
    # this is granted at the start of the game by default

class StartingItem4Location(NPCLocationRow5):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4
    # this is granted at the start of the game by default

class PostgameVoucherLocation(NPCLocationRow5):
    _originally_held = StayVoucherPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.POSTGAME_VOUCHER
    _remake_only = True
    # TODO: need to build the logic for this
    # TODO: needs frogfucius hint, needs entire event

class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = CoinPrize5
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    # Flag as checked: npc 0 in room 203 has its object trigger disabled.

class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = CoinPrize8
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_2
    # Flag as checked: npc 1 in room 203 has its object trigger disabled.

class MushroomWay1ToadRescue(NPCLocationRow2):
    _originally_held = HoneySyrupPrize
    _rooms = [R203_MUSHROOM_WAY_AREA_01, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_1
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_1

class MushroomWay2LedgeChest(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_3
    # Flag as checked: npc 0 in room 204 has its object trigger disabled.

class MushroomWay2ToadRescue(NPCLocationRow3):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_2
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_2

class MushroomWayRightGoomba(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    # Flag as checked: npc 1 in room 204 has its object trigger disabled.

class MushroomWayLeftItemRemake(StandingLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.REMAKE_1
    _remake_only = True
    # Flag as checked: npc 10 in room 204 has been removed from the room.
    # TODO: needs frogfucius hint

class MushroomWayRightItemRemake(StandingLocationRow2):
    _originally_held = PickMeUpPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.REMAKE_2
    _remake_only = True
    # Flag as checked: npc 11 in room 204 has been removed from the room.
    # TODO: needs frogfucius hint


class MushroomWayBossFightReward(NPCLocationRow1):
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomKingdomMainHall(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL]
    _npc_ids = [NPC_2, NPC_6]
    # Flag as checked: either npc 2 in room 17 or npc 6 in room 325 has its object trigger disabled.

# TODO: Can we add the 2 extra FCs to midas river? Too many NPCs?


class LandsEndCaveSideRemake(TreasureChestLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _npc_ids = [NPC_19]
    _remake_only = True
    # Flag as checked: npc 19 in room 142 is removed.