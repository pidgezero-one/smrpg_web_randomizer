from .types.prizelocation import TreasureChestLocationRow1, TreasureChestLocationRow2, TreasureChestLocationRow3, TreasureChestLocationRow4, TreasureChestLocationRow5, TreasureChestLocationRow6, NPCLocationRow1, NPCLocationRow2, NPCLocationRow3, NPCLocationRow4, NPCLocationRow5, NPCLocationRow6, NPCLocationRow7, StandingLocationRow1, StandingLocationRow2, StandingLocationRow3, StandingLocationRow4, StandingLocationRow5, StandingLocationRow6, StandingLocationRow7, StandingLocationRow8, StandingLocationRow9, StandingLocationRow10, StandingLocationRow11, StandingLocationRow12, StandingLocationRow13, StandingLocationRow14, StandingLocationRow15, RiverLocation, BossFightLocation, CharacterRecruitmentLocation, StarPieceLocation, ShopLocation, SpellSlotLocation
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from .prizes import *
from .types.prize import Prize, CoinPrize, FPFlowerPrize
from randomizer.types.world.flags import ShuffleLocationSelector

class StartingItem1Location(NPCLocationRow2):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_1

class StartingItem2Location(NPCLocationRow3):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_2

class StartingItem3Location(NPCLocationRow4):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_3

class StartingItem4Location(NPCLocationRow5):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4

class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = CoinPrize5
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1

class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = CoinPrize8
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_2

class MushroomWay1ToadRescue(NPCLocationRow1):
    _originally_held = HoneySyrupPrize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    # TODO: make unmissable and add to ShuffleLocationSelector

class MushroomWay2LedgeChest(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_3

class MushroomWay2ToadRescue(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    # TODO: make unmissable and add to ShuffleLocationSelector

class MushroomWayRightGoomba(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    # TODO: isn't this supposed to be repeatable? or did I get rid of that

class MushroomWayBossFightReward(NPCLocationRow1):
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD