from ..types.prizelocation import PrizeLocation, TreasureChestLocationRow1, TreasureChestLocationRow2, TreasureChestLocationRow3, TreasureChestLocationRow4, TreasureChestLocationRow5, TreasureChestLocationRow6, NPCLocationRow1, NPCLocationRow2, NPCLocationRow3, NPCLocationRow4, NPCLocationRow5, NPCLocationRow6, NPCLocationRow7, StandingLocationRow1, StandingLocationRow2, StandingLocationRow3, StandingLocationRow4, StandingLocationRow5, StandingLocationRow6, StandingLocationRow7, StandingLocationRow8, StandingLocationRow9, StandingLocationRow10, StandingLocationRow11, StandingLocationRow12, StandingLocationRow13, StandingLocationRow14, StandingLocationRow15, RiverLocation, RiverLocationRow1, RiverLocationRow2, BossFightLocation, CharacterRecruitmentLocation, StarPieceLocation, ShopLocation, SpellSlotLocation, ShuffleLocationSelector
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from .prizes import *
from ..types.prize import Prize, CoinPrize, CoinPrize1, CoinPrize10, FPFlowerPrize, FrogCoinPrize1, EXPStarPrize, BossFightPrize, SlotsPrize, EmptyPrize, InfiniteCoinPrize
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
    # TODO: Make sure starter event removes this if remake content is disabled.

class MushroomWayRightItemRemake(StandingLocationRow2):
    _originally_held = PickMeUpPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.REMAKE_2
    _remake_only = True
    # Flag as checked: npc 11 in room 204 has been removed from the room.
    # TODO: Make sure starter event removes this if remake content is disabled.


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


class BanditsWayFlowerJumpLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BANDITS_WAY_1
    # Flag as checked: npc 9 in room 207 has its object trigger disabled.

class BanditsWayCoin1Location(StandingLocationRow3):
    _originally_held = CoinPrize1
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_1
    # Flag as checked: npc 3 in room 207 has been removed from the room.

class BanditsWayCoin2Location(StandingLocationRow2):
    _originally_held = CoinPrize1
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_2
    # Flag as checked: npc 4 in room 207 has been removed from the room.

class BanditsWayCoin3Location(StandingLocationRow1):
    _originally_held = CoinPrize1
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_3
    # Flag as checked: npc 5 in room 207 has been removed from the room.

class BanditsWayDogChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R077_BANDITS_WAY_AREA_03]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_2
    # Flag as checked: npc 0 in room 77 has its object trigger disabled.

class BanditsWayPlatformsLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_CHEST
    # Flag as checked: npc 0 in room 78 has its object trigger disabled.

class BanditsWayPlatformsRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BANDITS_WAY_DOG_JUMP
    # Flag as checked: npc 1 in room 78 has its object trigger disabled.

class BanditsWayDeadEndChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_CROCO
    # Flag as checked: npc 0 in room 206 has its object trigger disabled.

class BanditsWayBossFirstItemDropLocation(NPCLocationRow1):
    _originally_held = RareFrogCoinPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD
    # Flag as checked: BANDITS_WAY_LIBERATED set

class BanditsWayBossSecondItemDropLocation(NPCLocationRow2):
    _originally_held = WalletPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD_2
    # Flag as checked: BANDITS_WAY_LIBERATED set (checked at same time as BanditsWayBossSecondItemDropLocation)

class MushroomKingdomOccupiedVaultLeftLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids = [NPC_0]

class MushroomKingdomOccupiedVaultRightLocation(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids = [NPC_1]

class MushroomKingdomOccupiedVaultMiddleLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids = [NPC_2]

class MushroomKingdomOccupiedOutdoorGuardLocation(NPCLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE]

class MushroomKingdomWalletGuyFirstRewardLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [ R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE, ]

class MushroomKingdomWalletGuySecondRewardLocation(NPCLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [ R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE, ]

class MushroomKingdomOccupiedCastleToadRescueLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [ R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM, ]

class MushroomKingdomOccupiedFamilyRescueLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [ R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ]

class MushroomKingdomOccupiedGuestRoomLocation(NPCLocationRow1):
    _originally_held = WakeUpPinPrize
    _rooms = [R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM]

class MushroomKingdomStoreExchangeLocation(NPCLocationRow2):
    _originally_held = CricketPiePrize
    _rooms = [ R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR, R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR, ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE

class MushroomKingdomInnPurchaseLocation(NPCLocationRow1):
    _originally_held = BeetlemaniaPrize
    _rooms = [ R493_MUSHROOM_KINGDOM_INN_1F, ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN

class KeroSewersStairRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_PANDORITE_ROOM

class KeroSewersStairRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = BossFightPrize
    _rooms = [ R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PANDORITE_CHEST

class Mimic1DropRewardLocation(NPCLocationRow1):
    _originally_held = TrueformPinPrize
    _id = ShuffleLocationSelector.PANDORITE_REWARD_1

class Mimic1ReloadRewardLocation(TreasureChestLocationRow3):
    _originally_held = CoinPrize
    _id = ShuffleLocationSelector.PANDORITE_REWARD_2

class KeroSewersFourRatRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST

class KeroSewersBeforeBelomeLowerLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_LOWER

class KeroSewersBeforeBelomeUpperBeforeFlipLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]

class KeroSewersBeforeBelomeUpperAfterFlipLocation(TreasureChestLocationRow3):
    _originally_held = CricketJamPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_2

class MidasRiverFirstCompletionRewardLocation(NPCLocationRow1):
    _originally_held = NokNokShellPrize
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _id = ShuffleLocationSelector.MIDAS_RIVER_FIRST_TIME

class MidasRiverBottomLeftCaveLocation(RiverLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_LEFT_CAVE

class MidasRiverBottomRightCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_RIGHT_CAVE

class TadpolePondCricketPieExchangeLocation(NPCLocationRow1):
    _originally_held = FroggiestickPrize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_PIE_REWARD

class TadpolePondCricketJamExchangeLocation(NPCLocationRow2):
    _originally_held = FrogCoinPrize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_JAM_REWARD

class MelodyBayFirstRewardLocation(NPCLocationRow1):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_1

class MelodyBaySecondRewardLocation(NPCLocationRow2):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_2

class MelodyBayThirdRewardLocation(NPCLocationRow3):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_3

class RoseWaySwingingPlatformRoomLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_PLATFORM

class RoseWayLeftIslandLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.ROSE_WAY_FLOWER

class RoseWayMiddleIslandLocation(StandingLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.ROSE_WAY_MUSHROOM

class RoseWayCoin1Location(StandingLocationRow7):
    _originally_held = CoinPrize10
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_17]

class RoseWayCoin2Location(StandingLocationRow6):
    _originally_held = CoinPrize10
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_18]

class RoseWayCoin3Location(StandingLocationRow5):
    _originally_held = CoinPrize10
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_19]

class RoseWayCoin4Location(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_20]

class RoseWayCoin5Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_21]

class RoseWayFiveChestRoomTopLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_1

class RoseWayFiveChestRoomBottomLeftLocation(TreasureChestLocationRow2):
    _originally_held = CoinPrize5
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2

class RoseWayFiveChestRoomRightLocation(TreasureChestLocationRow3):
    _originally_held = CoinPrize5
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3

class RoseWayFiveChestRoomLeftLocation(TreasureChestLocationRow4):
    _originally_held = CoinPrize5
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_4

class RoseWayFiveChestRoomBottomRightLocation(TreasureChestLocationRow5):
    _originally_held = CoinPrize5
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_5

class RoseTownShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_2

class RoseTownShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_1

class RoseTownCloudRightChestLocation(TreasureChestLocationRow1):
    _originally_held = LazyShellArmorPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_1

class RoseTownCloudLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = LazyShellWeaponPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_2

class RoseTownInnToadPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [ R095_ROSE_TOWN_DURING_BOWYER_INN_2F, R096_ROSE_TOWN_INN_2F, ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TOAD

class RoseTownInnGazPrizeLocation(NPCLocationRow1):
    _originally_held = FingerShotPrize
    _rooms = [R086_ROSE_TOWN_INN_1F]
    _id = ShuffleLocationSelector.GAZ

class RoseTownTreasureHouseLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1

class RoseTownTreasureHouseRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [ R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_2

class RoseTownTreasureHouseMazeRewardLocation(NPCLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD

class RoseTownTreasureHouseUpperChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, R098_ROSE_TOWN_TREASURE_HOUSE_2F, ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3

class ForestMazeFirstRoomLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R224_FOREST_MAZE_AREA_01]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_1

class ForestMazeFirstUndergroundExitLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R228_FOREST_MAZE_AREA_04]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_2

class ForestMazeUndergroundWigglerChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_1

class ForestMazeUndergroundBottomRightTrunkChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2

class ForestMazeUndergroundMiddleLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = EmptyPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_3

class ForestMazeInnerMazeEntranceLocation(TreasureChestLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_RED_ESSENCE

class ForestMazeSecretTopRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_1

class ForestMazeSecretBottomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_2

class ForestMazeSecretTopMiddleChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_3

class ForestMazeSecretBottomMiddleChestLocation(TreasureChestLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_4

class ForestMazeSecretLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_5

class PipeVaultSlidingCoinRoomBackChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_1

class PipeVaultSlidingCoinRoomMiddleChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2

class PipeVaultSlidingCoinRoomFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_3

class PipeVaultSlidingCoinRoomCoin1Location(StandingLocationRow5):
    _originally_held = CoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_0]

class PipeVaultSlidingCoinRoomCoin2Location(StandingLocationRow4):
    _originally_held = CoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_1]

class PipeVaultSlidingCoinRoomCoin3Location(StandingLocationRow3):
    _originally_held = CoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_2]

class PipeVaultSlidingCoinRoomCoin4Location(StandingLocationRow2):
    _originally_held = CoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_3]

class PipeVaultSlidingCoinRoomCoin5Location(StandingLocationRow1):
    _originally_held = CoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_4]

class PipeVaultSlidingCoinRoomCrouchItemLocation(StandingLocationRow6):
    _originally_held = FrogCoinPrize1
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_FROG_COIN

class PipeVaultGoombaThumpinFirstPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_1

class PipeVaultGoombaThumpinSecondPrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_2

class PipeVaultRisingPlatformChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_1

class PipeVaultChompweedChestLocation(TreasureChestLocationRow2):
    _originally_held = CoinPrize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_2

class YosterEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.YOSTER_ISLE_ENTRANCE

class YosterRacePrize1Location(NPCLocationRow1):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_1

class YosterRacePrize2Location(NPCLocationRow3):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2

class YosterRacePrize3Location(NPCLocationRow4):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_3

class BucketGirlRewardLocation(NPCLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.BUCKET_GIRL

# TODO: TreasureShopItem1 - original bases: TreasureShopItem, MolevilleLocation

# TODO: TreasureShopItem2 - original bases: TreasureShopItem, MolevilleLocation

# TODO: TreasureShopItem3 - original bases: TreasureShopItem, MolevilleLocation

class FireworksShopItemLocation(NPCLocationRow1):
    _originally_held = RegularFireworksPrize
    _rooms = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _id = ShuffleLocationSelector.FIREWORKS_SHOP

class OuterMinesTrampolineHenchmanLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_1

class OuterMinesLeftHenchmanLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_2

class OuterMinesRightHenchmanLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [ R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM ]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_3

class OuterMinesBossPrizeLocation(NPCLocationRow1):
    _originally_held = BambinoBombPrize
    _id = ShuffleLocationSelector.CROCO_2_ITEM

class InnerMinesTracksChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST

# TODO: InnerMinesShyguyCart - original bases: PacketItem, InnerMinesLocation

class InnerMinesBoxesChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [ R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_COINS

class InnerMinesSaveBlockChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_1

class InnerMinesHighUpChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [ R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2

class BoosterPassBushLocation(NPCLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _id = ShuffleLocationSelector.BOOSTER_PASS_BUSH

class BoosterPassFirstRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_PASS_1

class BoosterPassFirstRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RockCandyPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_PASS_2

class BoosterPassSecondRoomFlowerLocation(StandingLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_PASS_FLOWER

class BoosterPassSecretMiddleChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_1

class BoosterPassSecretRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_2

class BoosterPassSecretLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = KerokeroColaPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_3

class BoosterTowerSpookumStairsLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_SPOOKUM

class BoosterTowerTrainRoomCreviceLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_RAILWAY

class BoosterTowerChestNearThwompLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_THWOMP

class BoosterTowerFallingChestLocation(StandingLocationRow1):  # TODO: unknown container_event E0253_NPC_QUEST_1_GRANT
    _originally_held = MasherPrize
    _rooms = [ R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MASHER

class BoosterTowerKnifeGuyPrizeLocation(NPCLocationRow1):
    _originally_held = BrightCardPrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY

class BoosterTowerPortraitPrizeLocation(StandingLocationRow1):
    _originally_held = ElderKeyPrize
    _rooms = [R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PORTRAITS

class BoosterTowerElderKeyItemLocation(StandingLocationRow1):
    _originally_held = ChompPrize
    _rooms = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP

class BoosterTowerRightmostItemLocation(StandingLocationRow14):
    _originally_held = RoomKeyPrize
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY

class BoosterTowerTopItemLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_1

class BoosterTowerLeftmostItemLocation(StandingLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_2

class BoosterTowerUpperRightItemLocation(StandingLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_3

class BoosterTowerBottomItemLocation(StandingLocationRow4):
    _originally_held = FrogCoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_4

class BoosterTowerCoin1Location(StandingLocationRow5):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_1

class BoosterTowerCoin2Location(StandingLocationRow6):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_2

class BoosterTowerCoin3Location(StandingLocationRow7):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_3

class BoosterTowerCoin4Location(StandingLocationRow8):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_4

class BoosterTowerCoin5Location(StandingLocationRow9):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_5

class BoosterTowerCoin6Location(StandingLocationRow10):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_6

class BoosterTowerCoin7Location(StandingLocationRow11):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_7

class BoosterTowerCoin8Location(StandingLocationRow12):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_8

class BoosterTowerCoin9Location(StandingLocationRow13):
    _originally_held = CoinPrize1
    _rooms = [ R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS ]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_9

class BoosterTowerParachuteRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE

class BoosterTowerParachuteRoomCreviceLocation(NPCLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE_CREVICE

class BoosterTowerRoomKeyChestLocation(TreasureChestLocationRow1):
    _originally_held = ZoomShoesPrize
    _rooms = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES

class BoosterTowerTopFloorLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_1

class BoosterTowerTopFloorUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = GoodieBagPrize
    _rooms = [ R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_2

class BoosterTowerTopFloorCornerChestLocation(TreasureChestLocationRow3):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_3

class BoosterTowerCurtainGamePrizeLocation(NPCLocationRow1):
    _originally_held = AmuletPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    # TOWER_BOSS_1_STAR_PIECE

class MarrymoreFirstSuitePrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_1

class MarrymoreSecondSuitePrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_2

class MarrymoreThirdSuitePrizeLocation(NPCLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_3

class MarrymoreFourthSuitePrizeLocation(NPCLocationRow4):
    _originally_held = FrogCoinPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_4

class MarrymoreFifthSuitePrizeLocation(NPCLocationRow5):
    _originally_held = FrogCoinPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_5

class MarrymoreSixthSuitePrizeLocation(NPCLocationRow6):
    _originally_held = FrogCoinPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_6

class MarrymoreBigTipLocation(NPCLocationRow7):
    _originally_held = FlowerBoxPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _npc_ids = [NPC_6, NPC_7]
    _id = ShuffleLocationSelector.MARRYMORE_BIG_TIP

class MarrymoreHotelChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R009_MARRYMORE_INN_REGULAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MARRYMORE_INN

class MarrymoreSnifit1Location(NPCLocationRow1):
    _originally_held = BroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_1

class MarrymoreSnifit2Location(NPCLocationRow2):
    _originally_held = RingPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_2

class MarrymoreSnifit3Location(NPCLocationRow3):
    _originally_held = ShoesPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_3

class MarrymoreAltarHeadLocation(StandingLocationRow1):
    _originally_held = CrownPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.MARRYMORE_ALTAR

# TODO: FrogDiscipleItem1 - original bases: FrogDiscipleShopItem, SeasideTownLocation

# TODO: FrogDiscipleItem2 - original bases: FrogDiscipleShopItem, SeasideTownLocation

# TODO: FrogDiscipleItem3 - original bases: FrogDiscipleShopItem, SeasideTownLocation

# TODO: FrogDiscipleItem4 - original bases: FrogDiscipleShopItem, SeasideTownLocation

# TODO: FrogDiscipleItem5 - original bases: FrogDiscipleShopItem, SeasideTownLocation

class SeasideTownBossPrizeLocation(StandingLocationRow1):
    _originally_held = ShedKeyPrize
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE

class SeasideTownShedRescueLocation(NPCLocationRow1):
    _originally_held = FlowerBoxPrize
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE

class SeaStarslapRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R134_SEA_AREA_03_SUPER_STAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_STAR_CHEST

class SeaSaveRoomBackChestLocation(TreasureChestLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_1

class SeaSaveRoomMiddleChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_2

class SeaSaveRoomFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_3

class SeaWhirlpoolChestLocation(TreasureChestLocationRow1):
    _originally_held = MaxMushroomPrize
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST

class ShipRatStairsChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [ R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS

# TODO: ShipRatStairsBoxes - original bases: PacketItem, SunkenShipLocation

# TODO: ShipTroopaPuzzle - original bases: PacketItem, SunkenShipLocation

# TODO: ShipTrampolinePuzzle - original bases: PacketItem, SunkenShipLocation

# TODO: Ship3DMazePuzzle - original bases: PacketItem, SunkenShipLocation

class ShipShopChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [ R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SHOP

class ShipCoinSnakePuzzleLocation(NPCLocationRow1):
    _originally_held = CoinPrize
    _rooms = [R171_SUNKEN_SHIP_PUZZLE_ROOM_4]
    _npc_ids = [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9, NPC_10, NPC_11, NPC_12, NPC_13, NPC_14, NPC_15, NPC_16]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COIN_SNAKE

# TODO: ShipCannonballPuzzle - original bases: PacketItem, SunkenShipLocation

# TODO: ShipBarrelPuzzle - original bases: PacketItem, SunkenShipLocation

class EarlyInnerShipLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [ R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1

class InnerShipCloneRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM

class InnerShipBehindBoxesChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_FROG_COIN_ROOM

class InnerShipSaveRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_HIDON_MUSHROOM

class InnerShipSaveRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = BossFightPrize
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.HIDON_CHEST

class Mimic2DropRewardLocation(NPCLocationRow1):
    _originally_held = SafetyBadgePrize
    _id = ShuffleLocationSelector.HIDON_REWARD_1

class Mimic2ReloadRewardLocation(TreasureChestLocationRow3):
    _originally_held = CoinPrize
    _id = ShuffleLocationSelector.HIDON_REWARD_2

class InnerShipFirstUnderwaterRoomBottomItemLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1

class InnerShipFirstUnderwaterRoomTopItemLocation(StandingLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_2

class InnerShipFirstUnderwaterRoomLeftItemLocation(StandingLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_3

class InnerShipFirstUnderwaterRoomMiddleItemLocation(StandingLocationRow4):
    _originally_held = FrogCoinPrize1
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_4

class InnerShipSecretRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = SafetyRingPrize
    _rooms = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING

class InnerShipPoolRoomLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BLOOBER_ROOM

class InnerShipBeforeBossChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS

class LandsEndRisingPlatformChestLocation(TreasureChestLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R137_LANDS_END_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.LANDS_END_RED_ESSENCE

class LandsEndChowPitStaticChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_1

class LandsEndChowPitMovingChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_2

class LandsEndBeeTowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LNDS_END_BEE_ROOM

class LandsEndCaveSideRemake(TreasureChestLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _npc_ids = [NPC_19]
    _remake_only = True
    # Flag as checked: npc 19 in room 142 is removed.
    # TODO: Make sure starter event removes this if remake content is disabled.

class LandsEndGrottoEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_1

class LandsEndGrottoCornerChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [ R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_2

class LandsEndGrottoEndChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SHY_AWAY

class LandsEndUndergroundSaveBoxChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1

class LandsEndFirstPurchasableChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2

class LandsEndSecondPurchasableChestLocation(TreasureChestLocationRow2):
    _originally_held = EXPStarPrize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3

class TroopaClimbSub12PrizeLocation(NPCLocationRow1):
    _originally_held = TroopaPinPrize
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _id = ShuffleLocationSelector.TROOPA_CLIMB

class BelomeTempleFortuneTellerLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_TELLER

class BelomeTempleLMRChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_1

class BelomeTempleLRMChestLocation(TreasureChestLocationRow2):
    _originally_held = YoshiCookiePrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_2

class BelomeTempleRLMChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_3

class BelomeTempleRMLChestLocation(TreasureChestLocationRow4):
    _originally_held = CoinPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4

class BelomeBeforeBossRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_1

class BelomeBeforeBossLowerLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = CoinPrize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2

class BelomeBeforeBossMiddleChestLocation(TreasureChestLocationRow3):
    _originally_held = FrogCoinPrize1
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3

class BelomeBeforeBossUpperLeftChestLocation(TreasureChestLocationRow4):
    _originally_held = FrogCoinPrize1
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3

class BelomeTemplTreasuryeUpperCornerLeftItemLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1

class BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(StandingLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_2

class BelomeTempleTreasuryUpperCornerTopItemLocation(StandingLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_3

class BelomeTempleTreasuryTopmostItemLocation(StandingLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_4

class BelomeTempleTreasuryMidLeftItemLocation(StandingLocationRow5):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_1

class BelomeTempleTreasuryAlmostTopItemLocation(StandingLocationRow6):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_2

class BelomeTempleTreasuryAlmostLeftmostItemLocation(StandingLocationRow7):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_3

class BelomeTempleTreasuryOuterUpperRightItemLocation(StandingLocationRow8):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_4

class BelomeTempleTreasuryInnerUpperRightItemLocation(StandingLocationRow9):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_5

class BelomeTempleTreasuryLowestItemsRightLocation(StandingLocationRow10):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_6

class BelomeTempleTreasuryLowerOuterBottomRightItemLocation(StandingLocationRow11):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_7

class BelomeTempleTreasuryRightmostItemLocation(StandingLocationRow12):
    _originally_held = FrogCoinPrize1
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_8

class BelomeTempleTreasuryBottomLeftCornerItemLocation(StandingLocationRow13):
    _originally_held = MaxMushroomPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_2

class BelomeTempleTreasuryLowestItemsLeftLocation(StandingLocationRow14):
    _originally_held = RoyalSyrupPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_1

class BelomeTempleTreasuryUpperOuterBottomRightItemLocation(StandingLocationRow15):
    _originally_held = FireBombPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3

class MonstroEntranceLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE

class MonstroThwompItemLocation(StandingLocationRow1):
    _originally_held = TempleKeyPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP

class MonstroDojoClearRewardLocation(NPCLocationRow1):
    _originally_held = JinxBeltPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.JINX_DOJO_REWARD

class MonstroSealedDoorClearRewardLocation(NPCLocationRow1):
    _originally_held = QuartzCharmPrize
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_REWARD

class MonstroFirstSuperJumpRewardLocation(NPCLocationRow1):
    _originally_held = AttackScarfPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_30

class MonstroSecondSuperJumpRewardLocation(NPCLocationRow2):
    _originally_held = SuperSuitPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_100

class MonstroFlagExchangeLocation(NPCLocationRow1):
    _originally_held = GhostMedalPrize
    _rooms = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS

class BeanValleyFirstDeadEndLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_1

class BeanValleyFirstProgressChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_2

class BeanValleyLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE

class BeanValleyBottomLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE

class BeanValleyBottomRightPiranhaPipeUpperLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER

class BeanValleyBottomRightPiranhaPipeLowerLocation(TreasureChestLocationRow2):
    _originally_held = KerokeroColaPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER

class BeanValleyRightPipeLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = BossFightPrize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1

class BeanValleyRightPipeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_2

class BeanValleyRightPipeUnderStairsLocation(NPCLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN

class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS

class BeanValleyBossNoteLocation(NPCLocationRow1):
    _originally_held = SeedPrize
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM

class BeanstalkLowestChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK

class BeanValley1stRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN

class BeanValley1stRoomMiddleCoinLocation(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN

class BeanValley1stRoomUpperCoinLocation(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN

class BeanValley1stRoomLowerCoinLocation(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN

class Beanstalk2ndRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_FROG_COIN

class Beanstalk2ndRoomCoin1Location(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_1

class Beanstalk2ndRoomCoin2Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_2

class Beanstalk2ndRoomCoin3Location(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_3

class BeanValleyEastBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [ R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_1

class BeanValleyEastBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [ R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_2

class BeanValleyEastBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [ R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3

class BeanValleyEastBeanstalkCoin4Location(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [ R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_4

class BeanValleyEastBeanstalkCoin5Location(StandingLocationRow5):
    _originally_held = CoinPrize10
    _rooms = [ R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_5

class BeanValleyWestBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [ R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1

class BeanValleyWestBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [ R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_2

class BeanValleyWestBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [ R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_3

class BeanValleyWestBeanstalkFloatingItemLocation(StandingLocationRow4):
    _originally_held = FrogCoinPrize1
    _rooms = [ R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02 ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN

class BeanstalkUpperCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1

class BeanstalkUpperCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RareScarfPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2

class BeanstalkLowerCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_1

class BeanstalkLowerCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_2

class CasinoGrateGuyPrizeLocation(NPCLocationRow1):
    _originally_held = StarEggPrize
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _id = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE

class NimbusShopChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SHOP

class NimbusInnDreamPrize1Location(NPCLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN

class NimbusInnDreamPrize2Location(NPCLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2

class NimbusCastleStatueGamePrizeLocation(NPCLocationRow1):
    _originally_held = FeatherPrize
    _rooms = [R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM]
    _id = ShuffleLocationSelector.DODO_REWARD

class NimbusCastleOuterPrisonCellarRightNPCLocation(NPCLocationRow1):
    _originally_held = FlowerJarPrize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS

class NimbusCastleOuterPrisonCellarLeftNPCLocation(NPCLocationRow2):
    _originally_held = CastleKey1Prize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS_2

class NimbusCastleBusinessCentreOccupiedChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2

class NimbusCastleCornerBridgeChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE, R500_NIMBUS_CASTLE_AREA_04_____DUMMY, ]
    _npc_ids = [NPC_2, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_BEFORE_BIRDETTA_2

class NimbusCastleOutOfBoundsChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [ R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_1

class NimbusCastleAboveJawfulChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [ R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_2

class NimbusCastleSingleGoldBirdChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15, ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_SINGLE_GOLD_BIRD

class NimbusCastleTwoLevelLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, R498_NIMBUS_CASTLE_AREA_10_____DUMMY, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_1

class NimbusCastleGiantEggRewardLocation(NPCLocationRow1):
    _originally_held = CastleKey2Prize
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_BIRDETTA

class NimbusCastleTwoLevelUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [ R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, R498_NIMBUS_CASTLE_AREA_10_____DUMMY, ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_2

class NimbusCastleBackHallwayOccupiedChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST

class NimbusCastleBackHallwayLiberatedChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_AFTER_VALENTINA

class NimbusCastleBusinessCentreLiberatedChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA

class NimbusLandRightSideLocation(NPCLocationRow1):
    _originally_held = FertilizerPrize
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_LAND_RIGHT_SIDE

class NimbusLandCrocoItemLocation(StandingLocationRow1):
    _originally_held = SignalRingPrize
    _rooms = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING

class NimbusLandInnerCellarLocation(NPCLocationRow1):
    _originally_held = FlowerJarPrize
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _id = ShuffleLocationSelector.NIMBUS_LAND_CELLAR

class VolcanoLavaCoveLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1

class VolcanoLavaCoveRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1

class VolcanoEarlyProgressChestLeftLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_1

class VolcanoEarlyProgressChestRightLocation(TreasureChestLocationRow2):
    _originally_held = CoinPrize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_2

class VolcanoEarlyProgressThirdChestLocation(TreasureChestLocationRow1):
    _originally_held = EXPStarPrize
    _rooms = [R385_VOLCANO_AREA_06]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_STAR_ROOM

class VolcanoLavaPoolLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R361_VOLCANO_AREA_09]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_LAVA_POOL

class VolcanoReverseRecoilItemLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_REVERSE

class VolcanoRightDonutItemLocation(StandingLocationRow1):
    _originally_held = FrogCoinPrize1
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_1

class VolcanoLeftDonutItemLocation(StandingLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_2

class VolcanoSaveRoomLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_1

class VolcanoSaveRoomUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoinPrize1
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2

class VolcanoShopEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_HINOPIO

class KeepDarkRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DARK_ROOM

class KeepFirstCrocoShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = CoinPrize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_1

class KeepFirstCrocoShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_2

class KeepInvisibleBridgeFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FrightBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1

class KeepInvisibleBridgeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RoyalSyrupPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_2

class KeepInvisibleBridgeLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = IceBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_3

class KeepInvisibleBridgeBackChestLocation(TreasureChestLocationRow4):
    _originally_held = RockCandyPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_4

class KeepInvisibleBridgeCoin1Location(StandingLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1

class KeepInvisibleBridgeCoin2Location(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2

class KeepInvisibleBridgeCoin3Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3

class KeepInvisibleBridgeCoin4Location(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4

class KeepXYPlatformsBackLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1

class KeepXYPlatformsFrontLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_2

class KeepXYPlatformsFrontRightChestLocation(TreasureChestLocationRow3):
    _originally_held = MaxMushroomPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_3

class KeepXYPlatformsBackRightChestLocation(TreasureChestLocationRow4):
    _originally_held = FireBombPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_4

class KeepElevatorRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [ R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ELEVATOR_PLATFORMS

class KeepCannonballRoomFrontRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_1

class KeepCannonballRoomBackChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_2

class KeepCannonballFrontLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = PickMeUpPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_3

class KeepCannonballMidRightChestLocation(TreasureChestLocationRow4):
    _originally_held = RockCandyPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_4

class KeepCannonballMidLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = MaxMushroomPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_5

class KeepCannonballCoin1Location(StandingLocationRow1):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1

class KeepCannonballCoin2Location(StandingLocationRow2):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2

class KeepCannonballCoin3Location(StandingLocationRow3):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3

class KeepCannonballCoin4Location(StandingLocationRow4):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4

class KeepCannonballCoin5Location(StandingLocationRow5):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5

class KeepCannonballCoin6Location(StandingLocationRow6):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6

class KeepCannonballCoin7Location(StandingLocationRow7):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7

class KeepCannonballCoin8Location(StandingLocationRow8):
    _originally_held = CoinPrize10
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8

class KeepRotatingPlatformsFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_1

class KeepRotatingPlatformsFrontMidLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2

class KeepRotatingPlatformsBackMidRightChestLocation(TreasureChestLocationRow3):
    _originally_held = FireBombPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_3

class KeepRotatingPlatformsFrontMidRightChestLocation(TreasureChestLocationRow4):
    _originally_held = RoyalSyrupPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_4

class KeepRotatingPlatformsBackMidLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = PickMeUpPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_5

class KeepRotatingPlatformsBackChestLocation(TreasureChestLocationRow6):
    _originally_held = KerokeroColaPrize
    _rooms = [ R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6

class KeepDoorRewardChest1Location(TreasureChestLocationRow1):
    _originally_held = SonicCymbalPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_1

class KeepDoorRewardChest2Location(TreasureChestLocationRow2):
    _originally_held = SuperSlapPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2

class KeepDoorRewardChest3Location(TreasureChestLocationRow3):
    _originally_held = DrillClawPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_3

class KeepDoorRewardChest4Location(TreasureChestLocationRow4):
    _originally_held = StarGunPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_4

class KeepDoorRewardChest5Location(TreasureChestLocationRow5):
    _originally_held = RockCandyPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_5

class KeepDoorRewardChest6Location(TreasureChestLocationRow6):
    _originally_held = RockCandyPrize
    _rooms = [ R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_6

class KeepAfterObstaclesBossChestLocation(TreasureChestLocationRow1):
    _originally_held = InfiniteCoinPrize
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA

class OuterFactorySaveRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_SAVE_ROOM

class FactoryBoltPlatformsChestLocation(TreasureChestLocationRow1):
    _originally_held = UltraHammerPrize
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.FACTORY_BOLT_PLATFORMS

class FactoryAxemConveyorsChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.FACTORY_FALLING_AXEMS

class FactoryTreasurePitBackChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_1

class FactoryTreasurePitFrontChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [ R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_2

class FactoryBigConveyorRoomFirstChestLocation(TreasureChestLocationRow1):
    _originally_held = RoyalSyrupPrize
    _rooms = [ R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1

class FactoryBigConveyorRoomSecondChestLocation(TreasureChestLocationRow2):
    _originally_held = MaxMushroomPrize
    _rooms = [ R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2

class FactoryBehindNinjasRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [ R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_1

class FactoryBehindNinjasLeftChestLocation(TreasureChestLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [ R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_2

class InnerFactoryToadGiftLocation(NPCLocationRow1):
    _originally_held = RockCandyPrize
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _id = ShuffleLocationSelector.FACTORY_TOAD_GIFT


CHECK_POOL: list[PrizeLocation] = [

]