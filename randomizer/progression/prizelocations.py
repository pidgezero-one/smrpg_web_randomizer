from .types.prizelocation import TreasureChestLocationRow1, TreasureChestLocationRow2, TreasureChestLocationRow3, TreasureChestLocationRow4, TreasureChestLocationRow5, TreasureChestLocationRow6, NPCLocationRow1, NPCLocationRow2, NPCLocationRow3, NPCLocationRow4, NPCLocationRow5, NPCLocationRow6, NPCLocationRow7, StandingLocationRow1, StandingLocationRow2, StandingLocationRow3, StandingLocationRow4, StandingLocationRow5, StandingLocationRow6, StandingLocationRow7, StandingLocationRow8, StandingLocationRow9, StandingLocationRow10, StandingLocationRow11, StandingLocationRow12, StandingLocationRow13, StandingLocationRow14, StandingLocationRow15, RiverLocation, BossFightLocation, CharacterRecruitmentLocation, StarPieceLocation, ShopLocation, SpellSlotLocation
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from .prizes import *
from .types.prize import Prize, CoinPrize, FPFlowerPrize, FrogCoinPrize1
from randomizer.types.world.flags import ShuffleLocationSelector

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

class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = CoinPrize5
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    # Flag as checked: npc 0 in room 203 has its object trigger disabled.

class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = CoinPrize8
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [1]
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
    _npc_ids = [0]
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
    _npc_ids = [1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    # TODO: isn't this supposed to be repeatable? or did I get rid of that
    # Flag as checked: npc 1 in room 204 has its object trigger disabled.

class MushroomWayBossFightReward(NPCLocationRow1):
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3

class MushroomKingdomMainHall(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL]
    _npc_ids = [2, 6]
    # Flag as checked: either npc 2 in room 17 or npc 6 in room 325 has its object trigger disabled.

