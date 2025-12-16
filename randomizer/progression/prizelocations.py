from ..types.prizelocation import (
    PrizeLocation,
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
    StarPieceLocation,
    SpellSlotLocation,
    ShuffleLocationSelector,
    TreasureShopLocation,
    BoosterHillLocation,
    FrogDiscipleLocation,
    PacketLocationRow1,
    InvisibleFlagLocation,
)
from ..types.packet_type import PacketType
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from .prizes import *
from ..types.prize import (
    FPFlowerPrize,
    SlotsPrize,
    EmptyPrize,
)
from ..types.flags import *
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
    NPC_25,
    NPC_26,
    NPC_27,
)
from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types.logic import Inventory
    from ..types.gameworld import GameWorld

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


class StartingCharacter1(CharacterRecruitmentLocation):
    _originally_held = MarioRecruitmentPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_1


class MarioSpell1(SpellSlotLocation):
    _originally_held = JumpSpellPrize


class MarioSpell2(SpellSlotLocation):
    _originally_held = FireOrbSpellPrize


class MarioSpell3(SpellSlotLocation):
    _originally_held = SuperJumpSpellPrize


class MarioSpell4(SpellSlotLocation):
    _originally_held = SuperFlameSpellPrize


class MarioSpell5(SpellSlotLocation):
    _originally_held = UltraJumpSpellPrize


class MarioSpell6(SpellSlotLocation):
    _originally_held = UltraFlameSpellPrize


class StartingCharacter2(CharacterRecruitmentLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_2


class StartingCharacter3(CharacterRecruitmentLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_3


class StartingCharacter4(CharacterRecruitmentLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_4


class StartingCharacter5(CharacterRecruitmentLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_5


class PostgameVoucherLocation(NPCLocationRow6):
    _originally_held = StayVoucherPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.POSTGAME_VOUCHER
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return world.settings.get_flag(Remake).enabled

    # Flag as checked: VOUCHER_CHECK_DONE


########## mushroom way


class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = Coins5Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    # Flag as checked: npc 0 in room 203 has its object trigger disabled.


class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = Coins8Prize
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


class MushrooomWayBossFight(BossFightLocation):
    _originally_held = HammerBrosFight
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_BOSS_FIGHT
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_STAR_PIECE
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayBossFightRewardItem(NPCLocationRow1):
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayCharacter(CharacterRecruitmentLocation):
    _originally_held = MallowRecruitmentPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MallowSpell1(SpellSlotLocation):
    _originally_held = ThunderboltSpellPrize


class MallowSpell2(SpellSlotLocation):
    _originally_held = HPRainSpellPrize


class MallowSpell3(SpellSlotLocation):
    _originally_held = PsychopathSpellPrize


class MallowSpell4(SpellSlotLocation):
    _originally_held = ShockerSpellPrize


class MallowSpell5(SpellSlotLocation):
    _originally_held = SnowyPrize


class MallowSpell6(SpellSlotLocation):
    _originally_held = StarRainSpellPrize


########## mushroom kingdom - available before and during invasion


class MushroomKingdomMainHall(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
        R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
    ]
    _npc_ids = [NPC_2, NPC_6]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_HALLWAY
    # Flag as checked: either npc 2 in room 17 or npc 6 in room 325 has its object trigger disabled.


class MushroomKingdomLiberatedVaultLeft(TreasureChestLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_1
    # Flag as checked: npc 0 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultRight(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_2
    # Flag as checked: npc 1 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultMiddle(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_2, NPC_2]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_3
    # Flag as checked: npc 2 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomChair(NPCLocationRow1):
    _originally_held = MushroomPrize
    _rooms = [
        R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _id = ShuffleLocationSelector.PEACH_SURPRISE
    # flag as checked: npc 0 is missing/despawned from room 20 or npc 7 is missing/despawned from room 328


class MushroomKingdomFreeShopItem(NPCLocationRow1):
    _originally_held = PickMeUpPrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE
    # flag as checked: MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED


class MushroomKingdomShopBasementLeft(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_1
    # Flag as checked: npc 0 in room 492 has its object trigger disabled.


class MushroomKingdomShopBasementRight(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_2
    # Flag as checked: npc 1 in room 492 has its object trigger disabled.


class MushroomKingdomWalletGuyFirstRewardLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_1
    # Flag as checked: RETURNED_WALLET


class MushroomKingdomWalletGuySecondRewardLocation(NPCLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_2
    # Flag as checked: SECOND_WALLET_PRIZE_RECEIVED


########## mushroom kingdom = available only during occupation or later


class MushroomKingdomOccupiedOutdoorGuardLocation(NPCLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE]
    _id = ShuffleLocationSelector.INVASION_EASTERN_GUARD
    # Flag as checked: NPC 5 removed from room 190
    # Remember you need to define an additional henchman slot for the liberated room


class MushroomKingdomOccupiedCastleToadRescueLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _id = ShuffleLocationSelector.INVASION_TOAD_RESCUE
    # Remember you need to define an additional henchman slot for the liberated room
    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED


class MushroomKingdomOccupiedFamilyRescueLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [
        R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
        R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
    ]
    _id = ShuffleLocationSelector.INVASION_FAMILY
    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED and OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED must BOTH be set


class MushroomKingdomOccupiedGuestRoomLocation(NPCLocationRow1):
    _originally_held = WakeUpPinPrize
    _rooms = [R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM]
    _id = ShuffleLocationSelector.INVASION_GUEST_ROOM
    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED


class MushroomKingdomBossFight(BossFightLocation):
    _originally_held = MackBossFight
    _rooms = [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_BOSS_FIGHT
    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


class MushroomKingdomStarPiece(StarPieceLocation):
    _originally_held = StarPiece1
    _rooms = [R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_STAR_PIECE
    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


########## mushroom kingdom: only available AFTER liberation


class MushroomKingdomStoreExchangeLocation(NPCLocationRow2):
    _originally_held = CricketPiePrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE
    # Flag as checked: RARE_FROG_COIN_EXCHANGED


class MushroomKingdomInnPurchaseLocation(NPCLocationRow1):
    _originally_held = BeetlemaniaPrize
    _rooms = [
        R493_MUSHROOM_KINGDOM_INN_1F,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN
    # Flag as checked: GAMEBOY_KID_PURCHASE_COMPLETE


########## bandit's way


class BanditsWayFlowerJumpLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BANDITS_WAY_1
    # Flag as checked: npc 9 in room 207 has its object trigger disabled.


class BanditsWayCoin1Location(StandingLocationRow3):
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_1
    # Flag as checked: npc 3 in room 207 has been removed from the room.


class BanditsWayCoin2Location(StandingLocationRow2):
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_2
    # Flag as checked: npc 4 in room 207 has been removed from the room.


class BanditsWayCoin3Location(StandingLocationRow1):
    _originally_held = Coins1Prize
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
    _originally_held = BanditsWayStarPrize
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


class BanditsWayBossFight(BossFightLocation):
    _originally_held = Croco1BossFight
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_BOSS_FIGHT
    # Flag as checked: BANDITS_WAY_LIBERATED


class BanditsWayStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_PIECE
    # Flag as checked: BANDITS_WAY_LIBERATED


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


########## kero sewers


class KeroSewersStairRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_PANDORITE_ROOM
    # flag as checked: npc 0 in room 60 has its object trigger disabled.


class KeroSewersStairRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FirstMimicFightLauncher
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PANDORITE_CHEST
    # flag as checked: npc 1 in room 60 has its object trigger disabled.


class Mimic1BossFight(BossFightLocation):
    _originally_held = PandoriteBossFight
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS_FIGHT
    # Flag as checked: MIMIC_1_CLEARED


class Mimic1DropRewardLocation(NPCLocationRow1):
    _originally_held = TrueformPinPrize
    _rooms = [512]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.PANDORITE_REWARD_1
    _override_id = 512
    # flag as checked: MIMIC_1_CLEARED


class Mimic1StarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS
    # Flag as checked: MIMIC_1_CLEARED


class Mimic1ReloadRewardLocation(TreasureChestLocationRow3):
    _originally_held = Coins50Prize
    _rooms = [512]  # can be in any room.
    _id = ShuffleLocationSelector.PANDORITE_REWARD_2
    _override_id = 512
    # flag as checked: the host chest for FirstMimicFightLauncher has its object trigger disabled


class KeroSewersFourRatRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = KeroSewersStarPrize
    _rooms = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST
    # flag as checked: npc 0 in room 59 has its object trigger disabled.


class KeroSewersBeforeBelomeLowerLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_LOWER
    # flag as checked: npc 0 in room 301 has its object trigger disabled.


class KeroSewersBeforeBelomeUpperBeforeFlipLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_1
    # flag as checked: SEWER_CHEST_FIRST_PRIZE_OBTAINED


class KeroSewersBeforeBelomeUpperAfterFlipLocation(TreasureChestLocationRow3):
    _originally_held = CricketJamPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_2
    # flag as checked: SEWERS_FLIPPED_CHEST_OPENED


class KeroSewersBossFight(BossFightLocation):
    _originally_held = Belome1BossFight
    _rooms = [R302_KERO_SEWERS_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.KERO_SEWERS_BOSS
    # Flag as checked: SEWER_BOSS_DEFEATED


class KeroSewersStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_PIECE
    # Flag as checked: SEWER_BOSS_DEFEATED


########## Midas River


class MidasRiverFirstCompletionRewardLocation(NPCLocationRow1):
    _originally_held = NokNokShellPrize
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _id = ShuffleLocationSelector.MIDAS_RIVER_FIRST_TIME
    # Flag as checked: MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED


class MidasRiverBottomLeftCaveLocation(RiverLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_LEFT_CAVE
    # Flag as checked: MIDAS_RIVER_TUNNEL_3_PRIZE


class MidasRiverBottomRightCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_RIGHT_CAVE
    # Flag as checked: MIDAS_RIVER_TUNNEL_4_PRIZE


########## tadpole pond


class TadpolePondCricketPieExchangeLocation(NPCLocationRow1):
    _originally_held = FroggiestickPrize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_PIE_REWARD
    # Flag as checked: CRICKET_PIE_EXCHANGED


class TadpolePondCricketJamExchangeLocation(NPCLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_JAM_REWARD
    # Flag as checked: CRICKET_JAM_EXCHANGED


class MelodyBayFirstRewardLocation(NPCLocationRow1):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_1
    # Flag as checked: MELODY_BAY_ITEM_1_GRANTED


class MelodyBaySecondRewardLocation(NPCLocationRow2):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_2
    # Flag as checked: MELODY_BAY_ITEM_2_GRANTED


class MelodyBayThirdRewardLocation(NPCLocationRow3):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_3
    # Flag as checked: MELODY_BAY_ITEM_3_GRANTED


########## rose way


class RoseWaySwingingPlatformRoomLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_PLATFORM
    # Flag as checked: npc 0 in room 80 has its object trigger disabled.


class RoseWayLeftIslandLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.ROSE_WAY_FLOWER
    # Flag as checked: npc 7 in room 79 has been removed from the room.


class RoseWayMiddleIslandLocation(StandingLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.ROSE_WAY_MUSHROOM
    # Flag as checked: npc 8 in room 79 has been removed from the room.


class RoseWayCoin1Location(StandingLocationRow7):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_17]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_1
    # Flag as checked: npc 17 in room 79 has been removed from the room.


class RoseWayCoin2Location(StandingLocationRow6):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_2
    # Flag as checked: npc 18 in room 79 has been removed from the room.


class RoseWayCoin3Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_3
    # Flag as checked: npc 19 in room 79 has been removed from the room


class RoseWayCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_20]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_4
    # Flag as checked: npc 20 in room 79 has been removed from the room


class RoseWayCoin5Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_21]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_5
    # Flag as checked: npc 21 in room 79 has been removed from the room


class RoseWayFiveChestRoomTopLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_1
    # Flag as checked: npc 0 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomLeftLocation(TreasureChestLocationRow2):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2
    # Flag as checked: npc 1 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomRightLocation(TreasureChestLocationRow3):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3
    # Flag as checked: npc 2 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomLeftLocation(TreasureChestLocationRow4):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_4
    # Flag as checked: npc 3 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomRightLocation(TreasureChestLocationRow5):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_5
    # Flag as checked: npc 4 in room 81 has its object trigger disabled.


########### rose town


class RoseTownShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_2
    # Flag as checked: npc 4 in room 87 has its object trigger disabled.


class RoseTownShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_1
    # Flag as checked: npc 5 in room 87 has its object trigger disabled.


class RoseTownCloudRightChestLocation(TreasureChestLocationRow1):
    _originally_held = LazyShellArmorPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_1
    # Flag as checked: npc 0 in room 419 has its object trigger disabled.


class RoseTownCloudLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = LazyShellWeaponPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_2
    # Flag as checked: npc 1 in room 419 has its object trigger disabled.


class RoseTownInnToadPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [
        R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
        R096_ROSE_TOWN_INN_2F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TOAD
    # Flag as checked:  ROSE_TOWN_TOAD


class RoseTownInnGazPrizeLocation(NPCLocationRow1):
    _originally_held = FingerShotPrize
    _rooms = [R086_ROSE_TOWN_INN_1F]
    _id = ShuffleLocationSelector.GAZ
    # Flag as checked: ROSE_TOWN_GAZ_ITEM_GRANTED


class RoseTownTreasureHouseLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1
    # Flag as checked: npc 0 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_2
    # Flag as checked: npc 1 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseMazeRewardLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD
    # Flag as checked: TREASURE_HUNTER_HOUSE_PRIZE


class RoseTownTreasureHouseUpperChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3
    # Flag as checked: npc 1 in room 97 or 98 has its object trigger disabled.


class ForestMazeFirstRoomLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R224_FOREST_MAZE_AREA_01]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_1
    # Flag as checked: npc 2 in room 224 has its object trigger disabled.


class ForestMazeFirstUndergroundExitLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R228_FOREST_MAZE_AREA_04]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_2
    # Flag as checked: npc 2 in room 228 has its object trigger disabled.


class ForestMazeUndergroundWigglerChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_1
    # Flag as checked: npc 2 in room 242 has its object trigger disabled.


class ForestMazeUndergroundBottomRightTrunkChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2
    # Flag as checked: npc 3 in room 242 has its object trigger disabled.


class ForestMazeUndergroundMiddleLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = EmptyPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_3
    # Flag as checked: npc 4 in room 242 has its object trigger disabled.


class ForestMazeInnerMazeEntranceLocation(TreasureChestLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_RED_ESSENCE
    # Flag as checked: npc 4 in room 227 has its object trigger disabled.


class ForestMazeSecretTopRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_1
    # Flag as checked: npc 1 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_2
    # Flag as checked: npc 2 in room 234 has its object trigger disabled.


class ForestMazeSecretTopMiddleChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_3
    # Flag as checked: npc 3 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomMiddleChestLocation(TreasureChestLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_4
    # Flag as checked: npc 4 in room 234 has its object trigger disabled.


class ForestMazeSecretLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_5
    # Flag as checked: npc 5 in room 234 has its object trigger disabled.


class ForestMazeBossFight(BossFightLocation):
    _originally_held = BowyerBossFight
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_BOSS
    # Flag as checked: FOREST_LIBERATED


class ForestMazeStarPiece(StarPieceLocation):
    _originally_held = StarPiece2
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_STAR_PIECE
    # Flag as checked: FOREST_LIBERATED


class ForestMazeCharacter(CharacterRecruitmentLocation):
    _originally_held = GenoRecruitmentPrize
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    # Flag as checked: FOREST_LIBERATED


class GenoSpell1(SpellSlotLocation):
    _originally_held = GenoBeamSpellPrize


class GenoSpell2(SpellSlotLocation):
    _originally_held = GenoBoostSpellPrize


class GenoSpell3(SpellSlotLocation):
    _originally_held = GenoWhirlSpellPrize


class GenoSpell4(SpellSlotLocation):
    _originally_held = GenoBlastSpellPrize


class GenoSpell5(SpellSlotLocation):
    _originally_held = GenoFlashSpellPrize


class GenoSpell6(SpellSlotLocation):
    _originally_held = None


########## pipe vault


class PipeVaultSlidingCoinRoomBackChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_1
    # flag as checked: npc 8 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomMiddleChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2
    # flag as checked: npc 9 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_3
    # flag as checked: npc 10 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomCoin1Location(StandingLocationRow5):
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1
    # id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1


class PipeVaultSlidingCoinRoomCoin2Location(StandingLocationRow4):
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_2
    # flag as checked: npc 1 in room 125 has been removed from the room.


class PipeVaultSlidingCoinRoomCoin3Location(StandingLocationRow3):
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_3
    # flag as checked: npc 2 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin4Location(StandingLocationRow2):
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_4
    # flag as checked: npc 3 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin5Location(StandingLocationRow1):
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_5
    # flag as checked: npc 4 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCrouchItemLocation(StandingLocationRow6):
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_FROG_COIN
    # flag as checked: npc 5 in room 125 has been removed from the room.


class PipeVaultGoombaThumpinFirstPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_1
    # flag as checked: GOOMBA_THUMPING_1


class PipeVaultGoombaThumpinSecondPrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_2
    # flag as checked: GOOMBA_THUMPING_2


class PipeVaultRisingPlatformChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_1
    # flag as checked: npc 0 in room 128 has its object trigger disabled.


class PipeVaultChompweedChestLocation(TreasureChestLocationRow2):
    _originally_held = Coins20Prize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_2
    # flag as checked: npc 1 in room 128 has its object trigger disabled.


########### yoster isle


class YosterEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.YOSTER_ISLE_ENTRANCE
    # Flag as checked: npc 1 in room 33 has its object trigger disabled.


class YosterRacePrize1Location(NPCLocationRow1):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_1
    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize2Location(NPCLocationRow3):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2
    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize3Location(NPCLocationRow4):
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_3
    # Flag as checked: COMPLETED_MUSHROOM_DERBY


########## moleville


class BucketGirlRewardLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.BUCKET_GIRL
    # Flag as checked: BUCKET_PRIZE_GRANT_NO_WARP
    # Not available if bucket warp is enabled
    # TODO: make it available?


# TODO: progressive fireworks checks


class TreasureShopItem1(TreasureShopLocation, NPCLocationRow1):
    _originally_held = LuckyJewelPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_1
    # Flag as checked: TREASURE_SHOP_ITEM_1_PURCHASED


class TreasureShopItem2(TreasureShopLocation, NPCLocationRow2):
    _originally_held = ProgressiveEggPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_2
    # Flag as checked: TREASURE_SHOP_ITEM_2_PURCHASED


class TreasureShopItem3(TreasureShopLocation, NPCLocationRow3):
    _originally_held = FryingPanPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_3
    # Flag as checked: TREASURE_SHOP_ITEM_3_PURCHASED


class FireworksShopItemLocation(NPCLocationRow1):
    _originally_held = RegularFireworksPrize
    _rooms = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _id = ShuffleLocationSelector.FIREWORKS_SHOP
    # Flag as checked: FIREWORKS_HOUSE_ITEM_SOLD
    # not a check if progressive fireworks is turned off


# TODO: Did I make these permanent already? Can't find the code that removes them indirectly


class OuterMinesTrampolineHenchmanLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_1
    # Flag as checked: NPC 1 invisible in room 273


class OuterMinesLeftHenchmanLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_2
    # Flag as checked: NPC 1 invisible in room 277


class OuterMinesRightHenchmanLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_3
    # Flag as checked: NPC 1 invisible in room 283


class OuterMinesBossPrizeLocation(NPCLocationRow1):
    _originally_held = BambinoBombPrize
    _id = ShuffleLocationSelector.CROCO_2_ITEM
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    # flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesBossFight(BossFightLocation):
    _originally_held = Croco2BossFight
    _rooms = [518]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_1
    # Flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [518]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_1
    # Flag as checked: MINES_BOSS_1_DEFEATED


class InnerMinesTracksChestLocation(TreasureChestLocationRow1):
    _originally_held = MolevilleMinesStarPrize
    _rooms = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST
    # Flag as checked: npc 0 in room 285 has its object trigger disabled.


class InnerMinesShyguyCartLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = (
        ShuffleLocationSelector.MOLEVILLE_MINES_SHY_GUY
    )  # Flag as checked: RUNAWAY_MINECART_ITEM_OBTAINED


class InnerMinesBoxesChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins150Prize
    _rooms = [R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_COINS
    # Flag as checked: npc 0 in room 280 has its object trigger disabled.


class InnerMinesSaveBlockChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_1
    # Flag as checked: npc 0 in room 288 has its object trigger disabled.


class InnerMinesHighUpChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2
    # Flag as checked: npc 1 in room 288 has its object trigger disabled.


class InnerMinesBossFight(BossFightLocation):
    _originally_held = PunchinelloBossFight
    _rooms = [R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT
    # Flag as checked: MINES_BOSS_2_DEFEATED


class InnerMinesStarPiece(StarPieceLocation):
    _originally_held = StarPiece3
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_2
    # Flag as checked: MINES_BOSS_2_DEFEATED


class InnerMinesCharacter(CharacterRecruitmentLocation):
    _originally_held = BowserRecruitmentPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    # Flag as checked: MINES_BOSS_2_DEFEATED


class BowserSpell1(SpellSlotLocation):
    _originally_held = TerrorizeSpellPrize


class BowserSpell2(SpellSlotLocation):
    _originally_held = PoisonGasSpellPrize


class BowserSpell3(SpellSlotLocation):
    _originally_held = CrusherSpellPrize


class BowserSpell4(SpellSlotLocation):
    _originally_held = BowserCrushSpellPrize


class BowserSpell5(SpellSlotLocation):
    _originally_held = None


class BowserSpell6(SpellSlotLocation):
    _originally_held = None


class InnerMinesPostgameBossFight(BossFightLocation):
    _originally_held = Punchinello2BossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_3
    _remake_only = True
    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_3
    _remake_only = True
    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameDrop(NPCLocationRow1):
    _originally_held = WonderChompPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_POSTGAME_DROP
    _remake_only = True
    # Flag as checked: MINES_POSTGAME_COMPLETED


########## booster pass


class BoosterPassBushLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _id = ShuffleLocationSelector.BOOSTER_PASS_BUSH
    # flag as checked: BOOSTER_PASS_BUSH_ITEM_FOUND


class BoosterPassFirstRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_PASS_1
    # flag as checked: npc 8 in room 100 has its object trigger disabled.


class BoosterPassFirstRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RockCandyPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_PASS_2
    # flag as checked: npc 9 in room 100 has its object trigger disabled.


class BoosterPassSecondRoomFlowerLocation(StandingLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_PASS_FLOWER
    # flag as checked: npc 6 in room 101 has been removed from the room.


class BoosterPassSecretMiddleChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_1
    # flag as checked: npc 10 in room 405 has its object trigger disabled.


class BoosterPassSecretRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_2
    # flag as checked: npc 11 in room 405 has its object trigger disabled.


class BoosterPassSecretLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = KerokeroColaPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_3
    # flag as checked: npc 12 in room 405 has its object trigger disabled.


########## booster tower


class BoosterTowerSpookumStairsLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_SPOOKUM
    # flag as checked: npc 6 in room 196 has its object trigger disabled.


class BoosterTowerTrainRoomCreviceLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_RAILWAY
    # flag as checked: NPC 1 removed from room 194


class BoosterTowerChestNearThwompLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_THWOMP
    # flag as checked: npc 2 in room 36 has its object trigger disabled.


class BoosterTowerFallingChestLocation(
    StandingLocationRow1
):  # this looks like a chest, requires an overworld item, but acts like a npc reward
    _originally_held = MasherPrize
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MASHER
    _container_event = E0253_NPC_QUEST_1_GRANT
    # flag as checked: TOWER_SEESAW_CHEST_OPENED


class BoosterTowerKnifeGuyPrizeLocation(NPCLocationRow1):
    _originally_held = BrightCardPrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    # flag as checked: KNIFE_GUY_PRIZE_GRANTED


class BoosterTowerPortraitPrizeLocation(StandingLocationRow1):
    _originally_held = ElderKeyPrize
    _rooms = [R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PORTRAITS
    # flag as checked: npc 7 in room 195 has been removed from the room
    # AND
    # PORTRAIT_GAME_COMPLETED is set


class BoosterTowerElderKeyItemLocation(StandingLocationRow1):
    _originally_held = ChompPrize
    _rooms = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP
    # flag as checked: npc 0 in room 200 has been removed from the room.


class BoosterTowerParachuteRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE
    # flag as checked: npc 9 in room 35 has its object trigger disabled.


class BoosterTowerParachuteRoomCreviceLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE_CREVICE
    # flag as checked: NPC 8 removed from room 35


class BoosterTowerCheckerboardRightmostItemLocation(StandingLocationRow14):
    _originally_held = RoomKeyPrize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY
    # flag as checked: npc 5 in room 41 has been removed from the room.


class BoosterTowerCheckerboardTopItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_1
    # flag as checked: npc 0 in room 41 has been removed from the room.


class BoosterTowerCheckerboardLeftmostItemLocation(StandingLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_2
    # flag as checked: npc 1 in room 41 has been removed from the room.


class BoosterTowerCheckerboardUpperRightItemLocation(StandingLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_3
    # flag as checked: npc 2 in room 41 has been removed from the room.


class BoosterTowerCheckerboardBottomItemLocation(StandingLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_4
    # flag as checked: npc 3 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin1Location(StandingLocationRow5):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_1
    # flag as checked: npc 7 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin2Location(StandingLocationRow6):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_2
    # flag as checked: npc 8 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin3Location(StandingLocationRow7):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_3
    # flag as checked: npc 9 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin4Location(StandingLocationRow8):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_4
    # flag as checked: npc 10 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin5Location(StandingLocationRow9):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_5
    # flag as checked: npc 11 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin6Location(StandingLocationRow10):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_6
    # flag as checked: npc 12 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin7Location(StandingLocationRow11):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_7
    # flag as checked: npc 13 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin8Location(StandingLocationRow12):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_8
    # flag as checked: npc 14 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin9Location(StandingLocationRow13):
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_9
    # flag as checked: npc 15 in room 41 has been removed from the room.


class BoosterTowerRoomKeyChestLocation(TreasureChestLocationRow1):
    _originally_held = ZoomShoesPrize
    _rooms = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES
    # flag as checked: npc 0 in room 48 has its object trigger disabled.


class BoosterTowerTopFloorLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_1
    # flag as checked: npc 0 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = GoodieBagPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_2
    # flag as checked: npc 1 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorCornerChestLocation(TreasureChestLocationRow3):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_3
    # flag as checked: npc 9 in room 199 has its object trigger disabled.


class BoosterTowerCurtainGamePrizeLocation(NPCLocationRow1):
    _originally_held = AmuletPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    # flag as checked: TOWER_BOSS_1_STAR_PIECE
    # will be granted regardless of whether they do curtain game or fight boss


class BoosterTowerIndoorBossFight(BossFightLocation):
    _originally_held = BoosterBossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorBossFightRemake(BossFightLocation):
    _originally_held = Booster2BossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _override_id = 528
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    _remake_only = True
    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerIndoorStarPieceRemake(StarPieceLocation):
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _override_id = 528
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    _remake_only = True
    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerRemakeBossFightPrizeLocation(NPCLocationRow2):
    _originally_held = Stella023Prize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_POSTGAME_DROP
    _remake_only = True
    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerBalconyBossFight(BossFightLocation):
    _originally_held = KnifeGuyGrateGuyBossFight
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_2
    # Flag as checked: TOWER_BOSS_2_DEFEATED


class BoosterTowerBalconyStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_2
    # Flag as checked: TOWER_BOSS_2_DEFEATED


########## booster hill


class BoosterHillGuaranteedItem1(StandingLocation, BoosterHillLocation):
    _70B1_id = 0
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_9, NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_1
    # flag as checked $70B1 goes from 0 to 1


class BoosterHillGuaranteedItem2(StandingLocation, BoosterHillLocation):
    _70B1_id = 1
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_10, NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_2
    # flag as checked $70B1 goes from 1 to 2


class BoosterHillGuaranteedItem3(StandingLocation, BoosterHillLocation):
    _70B1_id = 2
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_11, NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_3
    # flag as checked $70B1 goes from 2 to 3


class BoosterHillGuaranteedItem4(StandingLocation, BoosterHillLocation):
    _70B1_id = 3
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_12, NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_4
    # flag as checked $70B1 goes from 3 to 4


class BoosterHillGuaranteedItem5(StandingLocation, BoosterHillLocation):
    _70B1_id = 4
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_13, NPC_13]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_5
    # flag as checked $70B1 goes from 4 to 5


class BoosterHillGuaranteedItem6(StandingLocation, BoosterHillLocation):
    _70B1_id = 5
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_14, NPC_14]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_6
    # flag as checked $70B1 goes from 5 to 6


class BoosterHillGuaranteedItem7(StandingLocation, BoosterHillLocation):
    _70B1_id = 6
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_15, NPC_15]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_7
    # flag as checked $70B1 goes from 6 to 7


class BoosterHillGuaranteedItem8(StandingLocation, BoosterHillLocation):
    _70B1_id = 7
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_16, NPC_16]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_8
    # flag as checked $70B1 goes from 7 to 8


class BoosterHillGuaranteedItem9(StandingLocation, BoosterHillLocation):
    _70B1_id = 8
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_17, NPC_17]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_9
    # flag as checked $70B1 goes from 8 to 9


class BoosterHillGuaranteedItem10(StandingLocation, BoosterHillLocation):
    _70B1_id = 9
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_18, NPC_18]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_10
    # flag as checked $70B1 goes from 9 to 10


class BoosterHillGuaranteedItem11(StandingLocation, BoosterHillLocation):
    _70B1_id = 10
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_19, NPC_19]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_11
    # flag as checked $70B1 goes from 10 to 11


class BoosterHillGuaranteedItem12(StandingLocation, BoosterHillLocation):
    _70B1_id = 11
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_20, NPC_20]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_12
    # flag as checked $70B1 goes from 11 to 12


class BoosterHillGuaranteedItem13(StandingLocation, BoosterHillLocation):
    _70B1_id = 12
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_21, NPC_21]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_13
    # flag as checked $70B1 goes from 12 to 13


class BoosterHillGuaranteedItem14(StandingLocation, BoosterHillLocation):
    _70B1_id = 13
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_22, NPC_22]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_14
    # flag as checked $70B1 goes from 13 to 14


class BoosterHillGuaranteedItem15(StandingLocation, BoosterHillLocation):
    _70B1_id = 14
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_23, NPC_23]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_15
    # flag as checked $70B1 goes from 14 to 15


class BoosterHillGuaranteedItem16(StandingLocation, BoosterHillLocation):
    _70B1_id = 15
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _npc_ids = [NPC_24, NPC_24]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_16
    # flag as checked $70B1 goes from 15 to 16


########## marrymore


class MarrymoreFirstSuitePrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_1
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize1Threshold setting


class MarrymoreSecondSuitePrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_2
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize2Threshold setting


class MarrymoreThirdSuitePrizeLocation(NPCLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_3
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize3Threshold setting


class MarrymoreFourthSuitePrizeLocation(NPCLocationRow4):
    _originally_held = FrogCoin2Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_4
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize4Threshold setting


class MarrymoreFifthSuitePrizeLocation(NPCLocationRow5):
    _originally_held = FrogCoin3Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_5
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize5Threshold setting


class MarrymoreSixthSuitePrizeLocation(NPCLocationRow6):
    _originally_held = FrogCoin20Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_6
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize6Threshold setting
    # LMK if these need dedicated bits or if AP is able to figure out the threshold on its own


class MarrymoreBigTipLocation(NPCLocationRow7):
    _originally_held = FlowerBoxPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_BIG_TIP
    # flag as checked: MARRYMORE_MAJOR_TIP_GIVEN


class MarrymoreHotelChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R009_MARRYMORE_INN_REGULAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MARRYMORE_INN
    # flag as checked: npc 0 in room 9 has its object trigger disabled.


# These are really NPC grants but they need sprite replacements.
# Override container event
class MarrymoreSnifit1Location(StandingLocationRow1):
    _originally_held = BroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_1
    _container_event = E0253_NPC_QUEST_1_GRANT
    _npc_ids = [NPC_6]
    # flag as checked: CHAPEL_ITEM_1_RETRIEVED


class MarrymoreSnifit2Location(StandingLocationRow2):
    _originally_held = RingPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_2
    _container_event = E0252_NPC_QUEST_2_GRANT
    _npc_ids = [NPC_7]
    # flag as checked: CHAPEL_ITEM_2_RETRIEVED


class MarrymoreSnifit3Location(StandingLocationRow3):
    _originally_held = ShoesPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_3
    _container_event = E0251_NPC_QUEST_3_GRANT
    _npc_ids = [NPC_4]
    # flag as checked: CHAPEL_ITEM_3_RETRIEVED


class MarrymoreAltarHeadLocation(StandingLocationRow1):
    _originally_held = CrownPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.MARRYMORE_ALTAR
    # flag as checked: npc 5 in room 154 has been removed from the room.


class MarrymoreBossFight(BossFightLocation):
    _originally_held = BundtBossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_BOSS_FIGHT
    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreBossFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_STAR_PIECE
    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreCharacter(CharacterRecruitmentLocation):
    _originally_held = ToadstoolRecruitmentPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_CHARACTER
    # Flag as checked: MARRYMORE_LIBERATED


class ToadstoolSpell1(SpellSlotLocation):
    _originally_held = TherapySpellPrize


class ToadstoolSpell2(SpellSlotLocation):
    _originally_held = GroupHugSpellPrize


class ToadstoolSpell3(SpellSlotLocation):
    _originally_held = SleepyTimeSpellPrize


class ToadstoolSpell4(SpellSlotLocation):
    _originally_held = ComeBackSpellPrize


class ToadstoolSpell5(SpellSlotLocation):
    _originally_held = MuteSpellPrize


class ToadstoolSpell6(SpellSlotLocation):
    _originally_held = PsychBombSpellPrize


class MarrymoreBossFightRemake(BossFightLocation):
    _originally_held = Bundt2BossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_BOSS_FIGHT
    _override_id = 529
    _remake_only = True
    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightStarPieceRemake(StarPieceLocation):
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_STAR_PIECE
    _override_id = 529
    _remake_only = True
    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightRemakeItemDrop(NPCLocationRow4):
    _originally_held = EnduringBroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_ITEM_DROP
    _remake_only = True
    # flag as checked: POSTGAME_CHAPEL_COMPLETE


########### star hill


class StarHillStarPiece(StarPieceLocation):
    _originally_held = StarPiece4
    _rooms = [R159_STAR_HILL_AREA_04]
    _id = ShuffleLocationSelector.STAR_HILL_STAR_PIECE_1
    # Flag as checked (send item, which i guess we can't do yet with SP checks):  NPC 9 removed from room and STAR_HILL_CHECKED
    # Flag as checked (tracker): STAR_HILL_CHECKED
    # TODO this is a special case where the star is a npc


########### seaside town pre-liberation


class FrogDiscipleLocation1(FrogDiscipleLocation):
    _originally_held = SeeYaPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_1
    # flag as checked: FROG_DISCIPLE_ITEM_1_PURCHASED


class FrogDiscipleLocation2(FrogDiscipleLocation):
    _originally_held = EarlierTimesPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_2
    # flag as checked: FROG_DISCIPLE_ITEM_2_PURCHASED


class FrogDiscipleLocation3(FrogDiscipleLocation):
    _originally_held = ExpBoosterPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_3
    # flag as checked: FROG_DISCIPLE_ITEM_3_PURCHASED


class FrogDiscipleLocation4(FrogDiscipleLocation):
    _originally_held = CoinTrickPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_4
    # flag as checked: FROG_DISCIPLE_ITEM_4_PURCHASED


class FrogDiscipleLocation5(FrogDiscipleLocation):
    _originally_held = ScroogeRingPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_5
    # flag as checked: FROG_DISCIPLE_ITEM_5_PURCHASED


########### seaside town when boss fight available


class SeasideBeachBossFight(BossFightLocation):
    _originally_held = YaridovichBossFight
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_FIGHT
    # Flag as checked: SEASIDE_LIBERATED


class SeasideBeachStarPiece(StarPieceLocation):
    _originally_held = StarPiece5
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS
    # Flag as checked: SEASIDE_LIBERATED


class SeasideTownBossPrizeLocation(StandingLocationRow1):
    _originally_held = ShedKeyPrize
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE
    # flag as checked: npc 0 in room 316 has been removed from the room.
    # TODO probably need a bit for this, item is absent by default and only summoned when boss defeated


########### seaside town gated by shed key


class SeasideTownShedRescueLocation(NPCLocationRow1):
    _originally_held = FlowerBoxPrize
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE
    # flag as checked: SEASIDE_SHED_EMPTIED


########## sea


class SeaStarslapRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = SeaStarPrize
    _rooms = [R134_SEA_AREA_03_SUPER_STAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_STAR_CHEST
    # flag as checked: npc 0 in room 134 has its object trigger disabled.


class SeaSaveRoomBackChestLocation(TreasureChestLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_1
    # flag as checked: npc 0 in room 132 has its object trigger disabled.


class SeaSaveRoomMiddleChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_2
    # flag as checked: npc 1 in room 132 has its object trigger disabled.


class SeaSaveRoomFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_3
    # flag as checked: npc 2 in room 132 has its object trigger disabled.


class SeaWhirlpoolChestLocation(TreasureChestLocationRow1):
    _originally_held = MaxMushroomPrize
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST
    # flag as checked: npc 0 in room 133 has its object trigger disabled.


########## sunken ship


class ShipRatStairsChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins100Prize
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS
    # flag as checked: npc 0 in room 167 has its object trigger disabled.


class ShipRatStairsBoxesLocation(PacketLocationRow1):
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_box_item"
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _packet_type = PacketType.CHEST
    # flag as checked: SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED


class ShipTroopaPuzzleLocation(PacketLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_troopa_item"
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _packet_type = PacketType.FALLING
    # flag as checked: SHIP_TROOPA_PRIZE


class ShipTrampolinePuzzle(PacketLocationRow1):
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_trampoline_item"
    _rooms = [R163_SUNKEN_SHIP_PUZZLE_ROOM_2]
    _packet_type = PacketType.FALLING
    # flag as checked: UNKNOWN_707D_1


class Ship3DMazePuzzle(PacketLocationRow1):
    _originally_held = RoyalSyrupPrize
    _replace = "spawn_ship_3d_maze_item"
    _rooms = [R168_SUNKEN_SHIP_PUZZLE_ROOM_3]
    _packet_type = PacketType.FALLING
    # flag as checked: SHIP_MAZE_PRIZE


class ShipShopChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins100Prize
    _rooms = [R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SHOP
    # flag as checked: npc 0 in room 169 has its object trigger disabled.


class ShipCoinSnakePuzzleLocation(StandingLocationRow1):
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
    # flag as checked: SHIP_COIN_PRIZE


class ShipCannonballPuzzle(PacketLocationRow1):
    _originally_held = MushroomPrize
    _replace = "spawn_ship_cannonball_item"
    _rooms = [R172_SUNKEN_SHIP_PUZZLE_ROOM_5]
    _packet_type = PacketType.FALLING
    # flag as checked: SHIP_CANNONBALL_PRIZE


class ShipBarrelPuzzle(PacketLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_barrel_item"
    _rooms = [R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL]
    _packet_type = PacketType.FALLING
    # flag as checked: UNKNOWN_707D_5


class ShipPasswordBossFight(BossFightLocation):
    _originally_held = KingCalamariBossFight
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS_BOSS_FIGHT
    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class ShipPasswordStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS
    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class EarlyInnerShipLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    # flag as checked: npc 0 in room 175 has its object trigger disabled.


class EarlyInnerShipRightChestLocation(TreasureChestLocationRow2):
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    # flag as checked: npc 1 in room 175 has its object trigger disabled.


class InnerShipCloneRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM
    # flag as checked: npc 2 in room 179 has its object trigger disabled.


class InnerShipBehindBoxesChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_FROG_COIN_ROOM
    # flag as checked: npc 0 in room 183 has its object trigger disabled.


class InnerShipSaveRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_HIDON_MUSHROOM
    # flag as checked: npc 1 in room 184 has its object trigger disabled.


class InnerShipSaveRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = SecondMimicFightLauncher
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.HIDON_CHEST
    # flag as checked: npc 2 in room 184 has its object trigger disabled.


class Mimic2DropRewardLocation(NPCLocationRow1):
    _originally_held = SafetyBadgePrize
    _rooms = [513]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.HIDON_REWARD_1
    _override_id = 513
    # flag as checked: MIMIC_2_CLEARED


class Mimic2BossFight(BossFightLocation):
    _originally_held = HidonBossFight
    _rooms = [513]  # can be in any room.
    _override_id = 513
    _id = ShuffleLocationSelector.HIDON_BOSS_FIGHT
    # Flag as checked: MIMIC_2_CLEARED


class Mimic2StarPiece(StarPieceLocation):
    _originally_held = None
    _id = ShuffleLocationSelector.HIDON_BOSS
    _rooms = [513]
    _override_id = 513
    # Flag as checked: MIMIC_2_CLEARED


class Mimic2ReloadRewardLocation(TreasureChestLocationRow3):
    _originally_held = Coins100Prize
    _rooms = [513]  # can be in any room.
    _id = ShuffleLocationSelector.HIDON_REWARD_2
    _override_id = 513
    # flag as checked: the host chest for SecondMimicFightLauncher has its object trigger disabled


class InnerShipFirstUnderwaterRoomBottomItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1
    # flag as checked: npc 0 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomTopItemLocation(StandingLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_2
    # flag as checked: npc 1 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomLeftItemLocation(StandingLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_3
    # flag as checked: npc 2 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomMiddleItemLocation(StandingLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_4
    # flag as checked: npc 3 in room 187 has been removed from the room.


class InnerShipSecretRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = SafetyRingPrize
    _rooms = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING
    # flag as checked: npc 0 in room 185 has its object trigger disabled.


class InnerShipPoolRoomLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BLOOBER_ROOM
    # flag as checked: npc 5 in room 27 has been removed from the room.


class InnerShipBeforeBossChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS
    # flag as checked: npc 4 in room 24 has its object trigger disabled.


class ShipFinalBossFight(BossFightLocation):
    _originally_held = JohnnyBossFight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS_FIGHT
    # Flag as checked: SHIP_LIBERATED


class ShipFinalStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS
    # Flag as checked: SHIP_LIBERATED


class ShipPostgameBossFight(BossFightLocation):
    _originally_held = Johnny2Fight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT
    _override_id = 526
    _remake_only = True
    # Flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameFightItemDrop(NPCLocationRow1):
    _originally_held = ExtraShinyStonePrize
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_DROP
    _remake_only = True
    # flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS
    _override_id = 526
    _remake_only = True
    # Flag as checked: POSTGAME_SHIP_COMPLETED


########## lands end


class LandsEndRisingPlatformChestLocation(TreasureChestLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R137_LANDS_END_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.LANDS_END_RED_ESSENCE
    # flag as checked: npc 4 in room 137 has its object trigger disabled.


class LandsEndChowPitStaticChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_1
    # flag as checked: npc 6 in room 138 has its object trigger disabled.


class LandsEndChowPitMovingChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_2
    # flag as checked: npc 7 in room 138 has its object trigger disabled.


class LandsEndBeeTowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LNDS_END_BEE_ROOM
    # flag as checked: npc 6 in room 141 has its object trigger disabled.


class LandsEndCaveSideRemake(TreasureChestLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _npc_ids = [NPC_19]
    _remake_only = True
    # Flag as checked: npc 19 in room 142 is removed.
    # TODO: Make sure starter event removes this if remake content is disabled.


class LandsEndGrottoEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_1
    # flag as checked: npc 7 in room 270 has its object trigger disabled.


class LandsEndGrottoCornerChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_2
    # flag as checked: npc 6 in room 270 has its object trigger disabled.


class LandsEndGrottoEndChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SHY_AWAY
    # flag as checked: npc 6 in room 401 has its object trigger disabled.


class LandsEndUndergroundSaveBoxChestLocation(TreasureChestLocationRow1):
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1
    # flag as checked: npc 5 in room 263 has its object trigger disabled.


class LandsEndFirstPurchasableChestLocation(TreasureChestLocationRow1):
    _originally_held = LandsEndStar2Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2
    # flag as checked: npc 18 in room 262 has its object trigger disabled.


class LandsEndSecondPurchasableChestLocation(TreasureChestLocationRow2):
    _originally_held = LandsEndStar3Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3
    # flag as checked: npc 19 in room 262 has its object trigger disabled.


class TroopaClimbSub12PrizeLocation(NPCLocationRow1):
    _originally_held = TroopaPinPrize
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _id = ShuffleLocationSelector.TROOPA_CLIMB
    # flag as checked: TROOPA_CLIMB_COMPLETED


class LandsEndCloudBoss(BossFightLocation):
    _originally_held = MokuraBossFight
    _id = ShuffleLocationSelector.LANDS_END_CLOUD_BOSS_FIGHT
    _rooms = [519]
    _override_id = 519
    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE_COMPLETED


class LandsEndCloudStarPiece(StarPieceLocation):
    _originally_held = None
    _id = ShuffleLocationSelector.LANDS_END_STAR_PIECE_1
    _rooms = [519]
    _override_id = 519
    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE_COMPLETED


class BelomeTempleFortuneTellerLocation(TreasureChestLocationRow1):
    _originally_held = Coins50Prize
    _rooms = [R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_TELLER
    # flag as checked: npc 5 in room 420 has its object trigger disabled.


class BelomeTempleLMRChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_1
    # flag as checked: npc 6 in room 421 has its object trigger disabled.


class BelomeTempleLRMChestLocation(TreasureChestLocationRow2):
    _originally_held = YoshiCookiePrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_2
    # flag as checked: npc 7 in room 421 has its object trigger disabled.


class BelomeTempleRLMChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_3
    # flag as checked: npc 8 in room 421 has its object trigger disabled.


class BelomeTempleRMLChestLocation(TreasureChestLocationRow4):
    _originally_held = Coins100Prize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4
    # flag as checked: npc 9 in room 421 has its object trigger disabled.


class BelomeBeforeBossRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_1
    # flag as checked: npc 0 in room 425 has its object trigger disabled.


class BelomeBeforeBossLowerLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = Coins150Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2
    # flag as checked: npc 1 in room 425 has its object trigger disabled.


class BelomeBeforeBossMiddleChestLocation(TreasureChestLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    # flag as checked: npc 2 in room 425 has its object trigger disabled.


class BelomeBeforeBossUpperLeftChestLocation(TreasureChestLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    # flag as checked: npc 3 in room 425 has its object trigger disabled.


class BelomeTempleTreasuryUpperCornerLeftItemLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1
    # flag as checked: npc 0 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(StandingLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_2
    # flag as checked: npc 1 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerTopItemLocation(StandingLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_3
    # flag as checked: npc 2 in room 422 has been removed from the room.


class BelomeTempleTreasuryTopmostItemLocation(StandingLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_4
    # flag as checked: npc 3 in room 422 has been removed from the room.


class BelomeTempleTreasuryMidLeftItemLocation(StandingLocationRow5):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_1
    # flag as checked: npc 4 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostTopItemLocation(StandingLocationRow6):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_2
    # flag as checked: npc 5 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostLeftmostItemLocation(StandingLocationRow7):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_3
    # flag as checked: npc 6 in room 422 has been removed from the room.


class BelomeTempleTreasuryOuterUpperRightItemLocation(StandingLocationRow8):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_4
    # flag as checked: npc 7 in room 422 has been removed from the room.


class BelomeTempleTreasuryInnerUpperRightItemLocation(StandingLocationRow9):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_5
    # flag as checked: npc 8 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsRightLocation(StandingLocationRow10):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_6
    # flag as checked: npc 9 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowerOuterBottomRightItemLocation(StandingLocationRow11):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_7
    # flag as checked: npc 10 in room 422 has been removed from the room.


class BelomeTempleTreasuryRightmostItemLocation(StandingLocationRow12):
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_8
    # flag as checked: npc 11 in room 422 has been removed from the room.


class BelomeTempleTreasuryBottomLeftCornerItemLocation(StandingLocationRow13):
    _originally_held = MaxMushroomPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_2
    # flag as checked: npc 13 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsLeftLocation(StandingLocationRow14):
    _originally_held = RoyalSyrupPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_1
    # flag as checked: npc 14 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperOuterBottomRightItemLocation(StandingLocationRow15):
    _originally_held = FireBombPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3
    # flag as checked: npc 15 in room 422 has been removed from the room.


class TempleBossFight(BossFightLocation):
    _originally_held = Belome2BossFight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_FIGHT
    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS
    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightPostgame(BossFightLocation):
    _originally_held = Belome3Dight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_FIGHT
    _override_id = 523
    _remake_only = True
    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TempleBossFightStarPiecePostgame(StarPieceLocation):
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME
    _override_id = 523
    _remake_only = True
    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TemplePostgameFightItemDrop(NPCLocationRow1):
    _originally_held = SageStickPrize
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_DROP
    _remake_only = True
    # flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


########## monstro town


class MonstroEntranceLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE
    # flag as checked: npc 1 in room 267 has its object trigger disabled.


class MonstroThwompItemLocation(StandingLocationRow1):
    _originally_held = TempleKeyPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP
    # flag as checked: npc 0 in room 324 has been removed from the room.


class DojoFirstFight(BossFightLocation):
    _originally_held = JaggerBossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_1
    # Flag as checked: DOJO_BOSS_1_DEFEATED


class DojoFirstFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_1
    # Flag as checked: DOJO_BOSS_1_DEFEATED


class DojoSecondFight(BossFightLocation):
    _originally_held = Jinx1BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_2
    _override_id = 515
    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoSecondFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_2
    _override_id = 515
    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoThirdFight(BossFightLocation):
    _originally_held = Jinx2BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_3
    _override_id = 516
    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoThirdFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_3
    _override_id = 516
    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoFourthFight(BossFightLocation):
    _originally_held = Jinx3BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_4
    _override_id = 517
    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFourthFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_4
    _override_id = 517
    # Flag as checked: DOJO_BOSS_4_DEFEATED


class MonstroDojoClearRewardLocation(NPCLocationRow1):
    _originally_held = JinxBeltPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.JINX_DOJO_REWARD
    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFifthFight(BossFightLocation):
    _originally_held = Jinx4BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_POSTGAME
    _override_id = 525
    _remake_only = True
    # Flag as checked: DOJO_POSTGAME_COMPLETED


class DojoFifthFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME
    _override_id = 525
    _remake_only = True
    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroDojoPostgameClearRewardLocation(NPCLocationRow2):
    _originally_held = TeamworkBandPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME_REWARD
    _remake_only = True
    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroSealedDoorBossFight(BossFightLocation):
    _originally_held = CulexBossFight
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_BOSS_FIGHT
    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_BOSS
    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorClearRewardLocation(NPCLocationRow1):
    _originally_held = QuartzCharmPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_REWARD
    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorBossFightPostgame(BossFightLocation):
    _originally_held = Culex3DBossFight
    _rooms = [R351_CULEXS_ROOM]
    _override_id = 524
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS_FIGHT
    _remake_only = True
    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorStarPiecePostgame(StarPieceLocation):
    _originally_held = None
    _override_id = 524
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS
    _remake_only = True
    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorClearRewardLocationPostgame(NPCLocationRow2):
    _originally_held = CrystalShardPrize
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_REWARD
    _remake_only = True
    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroFirstSuperJumpRewardLocation(NPCLocationRow1):
    _originally_held = AttackScarfPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_30
    # Flag as checked: SUPER_JUMP_PRIZE_1_GRANTED


class MonstroSecondSuperJumpRewardLocation(NPCLocationRow2):
    _originally_held = SuperSuitPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_100
    # Flag as checked: SUPER_JUMP_PRIZE_2_GRANTED


class MonstroFlagExchangeLocation(NPCLocationRow1):
    _originally_held = GhostMedalPrize
    _rooms = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS
    # Flag as checked: INVISIBLE_FLAG_CHECK_DONE


########## bean valley


class BeanValleyFirstDeadEndLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_1
    # flag as checked: npc 3 in room 252 has its object trigger disabled.


class BeanValleyFirstProgressChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_2
    # flag as checked: npc 4 in room 252 has its object trigger disabled.


class BeanValleyLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE
    # flag as checked: npc 0 in room 334 has its object trigger disabled.


class BeanValleyBottomLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE
    # flag as checked: npc 0 in room 348 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeUpperLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER
    # flag as checked: npc 0 in room 349 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeLowerLocation(TreasureChestLocationRow2):
    _originally_held = KerokeroColaPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER
    # flag as checked: npc 2 in room 349 has its object trigger disabled.


class BeanValleyRightPipeLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = ThirdMimicFightLauncher
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1
    # flag as checked: npc 5 in room 335 has its object trigger disabled.


class Mimic3BossFight(BossFightLocation):
    _originally_held = BoxBoyBossFight
    _rooms = [514]  # can be in any room.
    _override_id = 514
    _id = ShuffleLocationSelector.BOX_BOY_BOSS_FIGHT
    # Flag as checked: MIMIC_3_CLEARED


class Mimic3StarPiece(StarPieceLocation):
    _originally_held = None
    _id = ShuffleLocationSelector.BOX_BOY_BOSS
    _rooms = [514]
    _override_id = 514
    # Flag as checked: MIMIC_3_CLEARED


class BeanValleyRightPipeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_2
    # flag as checked: npc 7 in room 335 has its object trigger disabled.


class BeanValleyRightPipeUnderStairsLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN
    # flag as checked: npc 8 in room 335 has its object trigger disabled.


class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    # flag as checked: npc 13 in room 251 has its object trigger disabled.


class BeanValleyPlanterBossFight(BossFightLocation):
    _originally_held = MegasmilaxBossFight
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS_FIGHT
    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyPlanterStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS
    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyBossNoteLocation(NPCLocationRow1):
    _originally_held = SeedPrize
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM
    # flag as checked: SEED_CHECKED


class BeanstalkLowestChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK
    # flag as checked: npc 9 in room 379 has its object trigger disabled.


class BeanValley1stRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN
    # flag as checked: npc 3 in room 378 has been removed from the room.


class BeanValley1stRoomMiddleCoinLocation(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN
    # flag as checked: npc 4 in room 378 has been removed from the room.


class BeanValley1stRoomUpperCoinLocation(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN
    # flag as checked: npc 5 in room 378 has been removed from the room.


class BeanValley1stRoomLowerCoinLocation(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN
    # flag as checked: npc 6 in room 378 has been removed from the room.


class Beanstalk2ndRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_FROG_COIN
    # flag as checked: npc 6 in room 379 has been removed from the room.


class Beanstalk2ndRoomCoin1Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_1
    # flag as checked: npc 3 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin2Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_2
    # flag as checked: npc 4 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin3Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_3
    # flag as checked: npc 5 in room 379 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_1
    # flag as checked: npc 3 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_2
    # flag as checked: npc 4 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3
    # flag as checked: npc 5 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_4
    # flag as checked: npc 6 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin5Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_5
    # flag as checked: npc 7 in room 380 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1
    # flag as checked: npc 4 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_2
    # flag as checked: npc 5 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_3
    # flag as checked: npc 6 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkFloatingItemLocation(StandingLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN
    # flag as checked: npc 7 in room 381 has been removed from the room.


class BeanstalkUpperCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1
    # flag as checked: npc 1 in room 372 has its object trigger disabled.


class BeanstalkUpperCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RareScarfPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2
    # flag as checked: npc 2 in room 372 has its object trigger disabled.


class BeanstalkLowerCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_1
    # flag as checked: npc 1 in room 373 has its object trigger disabled.


class BeanstalkLowerCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_2
    # flag as checked: npc 2 in room 373 has its object trigger disabled.


########## casino


class CasinoGrateGuyPrizeLocation(NPCLocationRow1):
    _originally_held = StarEggPrize
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _id = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE
    # flag as checked: CASINO_PRIZE_WON


########## nimbus land


class NimbusShopChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SHOP
    # flag as checked: npc 0 in room 344 has its object trigger disabled.


class NimbusInnDreamPrize1Location(NPCLocationRow1):
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN
    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


class NimbusInnDreamPrize2Location(NPCLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


class NimbusCastleStatueGamePrizeLocation(NPCLocationRow1):
    _originally_held = FeatherPrize
    _rooms = [R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM]
    _override_id = 520
    _id = ShuffleLocationSelector.DODO_REWARD
    # flag as checked: STATUE_GAME_DONE


class StatueRoomBossFight(BossFightLocation):
    _originally_held = DodoBossFight
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STATUE_BOSS_FIGHT
    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class StatueRoomStarPiece(StarPieceLocation):
    _originally_held = None
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STAR_PIECE_1
    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class NimbusCastleOuterPrisonCellarRightNPCLocation(NPCLocationRow1):
    _originally_held = FlowerJarPrize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS
    # flag as checked: BLUE_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleOuterPrisonCellarLeftNPCLocation(NPCLocationRow2):
    _originally_held = CastleKey1Prize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS_2
    # flag as checked: RED_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleBusinessCentreOccupiedChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    # flag as checked: NIMBUS_MISSABLE_CHECK_CLEARED
    # (not really missable anymore. the chest that replaces this in the liberated castle will simply give you its item first if you didn't already get it)


class NimbusCastleCornerBridgeChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
        R500_NIMBUS_CASTLE_AREA_04_DUMMY,
    ]
    _npc_ids = [NPC_2, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_BEFORE_BIRDETTA_2
    # flag as checked: npc 2 in room 111 has its object trigger disabled.
    # or npc 0 in room 500 has its object trigger disabled


class NimbusCastleOutOfBoundsChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_1
    # flag as checked: npc 0 in room 410 has its object trigger disabled


class NimbusCastleAboveJawfulChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_2
    # flag as checked: npc 1 in room 410 has its object trigger disabled


class NimbusCastleSingleGoldBirdChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_SINGLE_GOLD_BIRD
    # flag as checked: npc 1 in room 113 has its object trigger disabled.


class NimbusCastleTwoLevelLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_1
    # flag as checked: npc 0 in room 114 has its object trigger disabled.


### nimbus castle gated by ck1


class GiantEggBossFight(BossFightLocation):
    _originally_held = BirdettaBossFight
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_EGG_BOSS_FIGHT
    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class GiantEggStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_2
    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class NimbusCastleGiantEggRewardLocation(NPCLocationRow1):
    _originally_held = CastleKey2Prize
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_BIRDETTA
    # flag as checked: NIMBUS_MID_BOSS_COMPLETED


### nimbus land gated by ck2


class NimbusCastleTwoLevelUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_2
    # flag as checked: npc 1 in room 114 has its object trigger disabled.


class NimbusCastleBackHallwayOccupiedChestLocation(TreasureChestLocationRow1):
    _originally_held = NimbusLandStarPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST
    # flag as checked: npc 0 in room 121 has its object trigger disabled.


class NimbusFinalBossFight(BossFightLocation):
    _originally_held = ValentinaBossFight
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_FINAL_BOSS_FIGHT
    # Flag as checked: NIMBUS_LAND_LIBERATED


class NimbusFinalStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_3
    # Flag as checked: NIMBUS_LAND_LIBERATED


### nimbus land gated by liberation


class NimbusCastleBackHallwayLiberatedChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_AFTER_VALENTINA
    # flag as checked: npc 1 in room 121 has its object trigger disabled.


class NimbusCastleBusinessCentreLiberatedChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA
    # flag as checked: NIMBUS_MISSABLE_CHECK_CLEARED


class NimbusLandRightSideLocation(NPCLocationRow1):
    _originally_held = FertilizerPrize
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_LAND_RIGHT_SIDE
    # flag as checked: NPC 9 removed from room 438.


class NimbusLandCrocoItemLocation(StandingLocationRow1):
    _originally_held = SignalRingPrize
    _rooms = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING
    # flag as checked: npc 5 in room 345 has been removed from the room.


class NimbusLandInnerCellarLocation(NPCLocationRow1):
    _originally_held = FlowerJarPrize
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _id = ShuffleLocationSelector.NIMBUS_LAND_CELLAR
    # flag as checked: NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED


########## barrel volcano


class VolcanoLavaCoveLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    # flag as checked: npc 1 in room 355 has its object trigger disabled.


class VolcanoLavaCoveRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    # flag as checked: npc 2 in room 355 has its object trigger disabled.


class VolcanoEarlyProgressChestLeftLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_1
    # flag as checked: npc 0 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressChestRightLocation(TreasureChestLocationRow2):
    _originally_held = Coins100Prize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_2
    # flag as checked: npc 1 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressThirdChestLocation(TreasureChestLocationRow1):
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R385_VOLCANO_AREA_06]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_STAR_ROOM
    # flag as checked: npc 0 in room 385 has its object trigger disabled.


class VolcanoLavaPoolLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R361_VOLCANO_AREA_09]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_LAVA_POOL
    # flag as checked: npc 1 in room 361 has been removed from the room.


class VolcanoReverseRecoilItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_REVERSE
    # flag as checked: npc 4 in room 383 has been removed from the room.


class VolcanoRightDonutItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_1
    # flag as checked: npc 1 in room 358 has been removed from the room.


class VolcanoLeftDonutItemLocation(StandingLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_2
    # flag as checked: npc 2 in room 358 has been removed from the room.


class VolcanoSaveRoomLowerChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_1
    # flag as checked: npc 0 in room 366 has its object trigger disabled.


class VolcanoSaveRoomUpperChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2
    # flag as checked: npc 1 in room 366 has its object trigger disabled.


class VolcanoShopEntranceChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins100Prize
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_HINOPIO
    # flag as checked: npc 0 in room 367 has its object trigger disabled.


class VolcanoBridgeBossFight(BossFightLocation):
    _originally_held = CzarDragonBossFight
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_1
    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoBridgeStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_1
    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoExitBossFight(BossFightLocation):
    _originally_held = AxemRangersBossFight
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_2
    # Flag as checked: VOLCANO_LIBERATED


class VolcanoExitStarPiece(StarPieceLocation):
    _originally_held = StarPiece6
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_2
    # Flag as checked: VOLCANO_LIBERATED


########## bowser's keep


class KeepDarkRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DARK_ROOM
    # flag as checked: npc 0 in room 453 has its object trigger disabled.


class KeepFirstCrocoShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = Coins150Prize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_1
    # flag as checked: npc 0 in room 451 has its object trigger disabled.


class KeepFirstCrocoShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_2
    # flag as checked: npc 1 in room 451 has its object trigger disabled.


class KeepInvisibleBridgeFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FrightBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1
    # flag as checked: npc 4 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RoyalSyrupPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_2
    # flag as checked: npc 5 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = IceBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_3
    # flag as checked: npc 6 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeBackChestLocation(TreasureChestLocationRow4):
    _originally_held = RockCandyPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_4
    # flag as checked: npc 7 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1
    # flag as checked: npc 8 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2
    # flag as checked: npc 9 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3
    # flag as checked: npc 10 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4
    # flag as checked: npc 11 in room 322 has been removed from the room.


class KeepXYPlatformsBackLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1
    # flag as checked: npc 10 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_2
    # flag as checked: npc 11 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontRightChestLocation(TreasureChestLocationRow3):
    _originally_held = MaxMushroomPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_3
    # flag as checked: npc 12 in room 458 has its object trigger disabled.


class KeepXYPlatformsBackRightChestLocation(TreasureChestLocationRow4):
    _originally_held = FireBombPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_4
    # flag as checked: npc 13 in room 458 has its object trigger disabled.


class KeepElevatorRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = KerokeroColaPrize
    _rooms = [R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ELEVATOR_PLATFORMS
    # flag as checked: npc 8 in room 321 has its object trigger disabled.


class KeepCannonballRoomFrontRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_1
    # flag as checked: npc 3 in room 457 has its object trigger disabled.


class KeepCannonballRoomBackChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_2
    # flag as checked: npc 4 in room 457 has its object trigger disabled.


class KeepCannonballFrontLeftChestLocation(TreasureChestLocationRow3):
    _originally_held = PickMeUpPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_3
    # flag as checked: npc 5 in room 457 has its object trigger disabled.


class KeepCannonballMidRightChestLocation(TreasureChestLocationRow4):
    _originally_held = RockCandyPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_4
    # flag as checked: npc 6 in room 457 has its object trigger disabled.


class KeepCannonballMidLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = MaxMushroomPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_5
    # flag as checked: npc 7 in room 457 has its object trigger disabled.


class KeepCannonballCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1
    # flag as checked: npc 8 in room 457 has been removed from the room.


class KeepCannonballCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2
    # flag as checked: npc 9 in room 457 has been removed from the room.


class KeepCannonballCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3
    # flag as checked: npc 10 in room 457 has been removed from the room.


class KeepCannonballCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4
    # flag as checked: npc 11 in room 457 has been removed from the room.


class KeepCannonballCoin5Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5
    # flag as checked: npc 12 in room 457 has been removed from the room.


class KeepCannonballCoin6Location(StandingLocationRow6):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6
    # flag as checked: npc 13 in room 457 has been removed from the room.


class KeepCannonballCoin7Location(StandingLocationRow7):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7
    # flag as checked: npc 14 in room 457 has been removed from the room.


class KeepCannonballCoin8Location(StandingLocationRow8):
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8
    # flag as checked: npc 15 in room 457 has been removed from the room.


class KeepRotatingPlatformsFrontChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_1
    # flag as checked: npc 1 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidLeftChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2
    # flag as checked: npc 2 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidRightChestLocation(TreasureChestLocationRow3):
    _originally_held = FireBombPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_3
    # flag as checked: npc 3 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidRightChestLocation(TreasureChestLocationRow4):
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_4
    # flag as checked: npc 4 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidLeftChestLocation(TreasureChestLocationRow5):
    _originally_held = PickMeUpPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_5
    # flag as checked: npc 5 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackChestLocation(TreasureChestLocationRow6):
    _originally_held = KerokeroColaPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6
    # flag as checked: npc 6 in room 455 has its object trigger disabled.


class ObstacleCourseFinalFight(BossFightLocation):
    _originally_held = ChesterBossFight
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_CHESTER
    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class ObstacleCourseFinalFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_CHESTER
    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class KeepDoorRewardChest1Location(TreasureChestLocationRow1):
    _originally_held = SonicCymbalPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_1
    # flag as checked: BK_OBSTACLE_1_PRIZE_RETRIEVED


class KeepDoorRewardChest2Location(TreasureChestLocationRow2):
    _originally_held = SuperSlapPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2
    # flag as checked: BK_OBSTACLE_2_PRIZE_RETRIEVED


class KeepDoorRewardChest3Location(TreasureChestLocationRow3):
    _originally_held = DrillClawPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_3
    # flag as checked: BK_OBSTACLE_3_PRIZE_RETRIEVED


class KeepDoorRewardChest4Location(TreasureChestLocationRow4):
    _originally_held = StarGunPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_4
    # flag as checked: BK_OBSTACLE_4_PRIZE_RETRIEVED


class KeepDoorRewardChest5Location(TreasureChestLocationRow5):
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_5
    # flag as checked: BK_OBSTACLE_5_PRIZE_RETRIEVED


class KeepDoorRewardChest6Location(TreasureChestLocationRow6):
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_6
    # flag as checked: BK_OBSTACLE_6_PRIZE_RETRIEVED


class KeepAfterObstaclesBossFight(BossFightLocation):
    _originally_held = KamekBossFight
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_1
    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_1
    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesBossChestLocation(TreasureChestLocationRow1):
    _originally_held = InfiniteCoinsPrize
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA
    # flag as checked: npc 0 in room 266 has its object trigger disabled.


class KeepChandelierBossFight(BossFightLocation):
    _originally_held = BoomerBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_2
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepChandelierStarPiece(StarPieceLocation):
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_2
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepFinalBossFight(BossFightLocation):
    _originally_held = ExorBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_3
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    # Flag as checked: KEEP_BOSS_3_DEFEATED


class KeepFinalStarPiece(StarPieceLocation):
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_3
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    # Flag as checked: KEEP_BOSS_3_DEFEATED


########## outer factory


class OuterFactorySaveRoomChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_SAVE_ROOM
    # flag as checked: npc 0 in room 237 has its object trigger disabled.


class FactoryBoltPlatformsChestLocation(TreasureChestLocationRow1):
    _originally_held = UltraHammerPrize
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.FACTORY_BOLT_PLATFORMS
    # flag as checked: npc 7 in room 239 has its object trigger disabled.


class FactoryEntranceBossFight(BossFightLocation):
    _originally_held = CountdownBossFight
    _rooms = [R433_SMITHY_FACTORY_AREA_01_DUMMY]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_1
    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryEntranceStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R433_SMITHY_FACTORY_AREA_01_DUMMY]
    _id = ShuffleLocationSelector.FACTORY_BOSS_1
    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryAxemConveyorsChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.FACTORY_FALLING_AXEMS
    # flag as checked: npc 6 in room 434 has its object trigger disabled.


class FactoryTreasurePitBackChestLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_1
    # flag as checked: npc 0 in room 443 has its object trigger disabled.


class FactoryTreasurePitFrontChestLocation(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_2
    # flag as checked: npc 2 in room 443 has its object trigger disabled.


class FactoryBigConveyorRoomFirstChestLocation(TreasureChestLocationRow1):
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1
    # flag as checked: npc 8 in room 475 has its object trigger disabled.


class FactoryBigConveyorRoomSecondChestLocation(TreasureChestLocationRow2):
    _originally_held = MaxMushroomPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2
    # flag as checked: npc 9 in room 475 has its object trigger disabled.


class FactoryBehindNinjasRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_1
    # flag as checked: npc 1 in room 443 has its object trigger disabled.


class FactoryBehindNinjasLeftChestLocation(TreasureChestLocationRow4):
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_2
    # flag as checked: npc 3 in room 443 has its object trigger disabled.


class FactoryTransitionBossFight(BossFightLocation):
    _originally_held = CloakerDominoBossFight
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_2
    # Flag as checked: ABYSS_BOSS_2_DEFEATED


class FactoryTransitionStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_2
    # Flag as checked: ABYSS_BOSS_2_DEFEATED


########## inner factory


class InnerFactoryFirstFight(BossFightLocation):
    _originally_held = ClerkBossFight
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_1
    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryFirstFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_1
    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryToadGiftLocation(NPCLocationRow1):
    _originally_held = RockCandyPrize
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _id = ShuffleLocationSelector.FACTORY_TOAD_GIFT
    # flag as checked: TOAD_SHOP_FREEBIE_RECEIVED


class InnerFactorySecondFight(BossFightLocation):
    _originally_held = ManagerBossFight
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_2
    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactorySecondFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_2
    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactoryThirdFight(BossFightLocation):
    _originally_held = DirectorBossFight
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_3
    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryThirdFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_3
    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryFourthFight(BossFightLocation):
    _originally_held = GunyolkBossFight
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_4
    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class InnerFactoryFourthFightStarPiece(StarPieceLocation):
    _originally_held = None
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_4
    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class FinalBossFight(BossFightLocation):
    _originally_held = SmithyBossFight
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_FINAL
    # Flag as checked: FACTORY_BOSS_DEFEATED


class FinalBossFightStarPiece(StarPieceLocation):
    _originally_held = StarPiece7
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL
    # Flag as checked: FACTORY_BOSS_DEFEATED


########## invisible flag check pool

# Three of the following locations will be chosen at random and included in the seed. If the setting is disabled, then it will be the first three (defaults).
# In a tracker, their exact locations should not be known, but these will be considered checked when a certain bit is set.
# INVISIBLE_FLAG_1_FOUND, INVISIBLE_FLAG_2_FOUND, INVISIBLE_FLAG_3_FOUND


class MariosPadBedFlag(InvisibleFlagLocation):
    _room_ids = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 11
    _clue_text = """\n My flag's underneath a green bed.[await]"""


class RoseTownSignFlag(InvisibleFlagLocation):
    _room_ids = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 10
    _y_coord = 47
    _clue_text = """\n My flag's behind a wooden flower.[await]"""


class YosterIsleGoalFlag(InvisibleFlagLocation):
    _room_ids = [R034_YOSTER_ISLE]
    _x_coord = 21
    _y_coord = 62
    _y_shift = -4
    _clue_text = """\n My flag's between "O" and "A".[await]"""


class MariosPadSteamwhistleFlag(InvisibleFlagLocation):
    _room_ids = [R016_MARIOS_PAD]
    _x_coord = 11
    _y_coord = 34
    _z_coord = 1
    _clue_text = "\n  Mine is underneath a steamwhistle.[await]"


class MariosPadLanternFlag(InvisibleFlagLocation):
    _room_ids = [R016_MARIOS_PAD]
    _x_coord = 13
    _y_coord = 35
    _x_shift = 8
    _y_shift = -8
    _clue_text = "\n    Mine is under a white lantern.[await]"


class MariosPadHatFlag(InvisibleFlagLocation):
    _room_ids = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 13
    _z_coord = 1
    _clue_text = """\n      My flag's under a red hat.[await]"""


class MushroomWayTreeFlag(InvisibleFlagLocation):
    _room_ids = [R204_MUSHROOM_WAY_AREA_02]
    _x_coord = 11
    _y_coord = 16
    _z_coord = 3
    _x_shift = -16
    _clue_text = " Mine's under a tree, up on a ledge\n by itself.[await]"


class MushroomKingdomSignFlag(InvisibleFlagLocation):
    _room_ids = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _x_coord = 22
    _y_coord = 116
    _z_coord = 2
    _y_shift = -8
    _clue_text = "\n  Mine's behind a wooden mushroom.[await]"


class MushroomKingdomEmptyHouseFlag(InvisibleFlagLocation):
    _room_ids = [
        R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
        R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE,
    ]
    _x_coord = 14
    _y_coord = 61
    _y_shift = 8
    _clue_text = " Mine is under the bed in an empty\n house.[await]"


class ChancellorThroneFlag(InvisibleFlagLocation):
    _room_ids = [
        R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
        R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    ]
    _x_coord = 19
    _y_coord = 24
    _z_coord = 3
    _clue_text = "\n       Mine's under a blue chair.[await]"


class BanditsWayFlowerFlag(InvisibleFlagLocation):
    _room_ids = [R207_BANDITS_WAY_AREA_02]
    _x_coord = 25
    _y_coord = 89
    _x_shift = 16
    _clue_text = "\n      Mine's on a landing flower.[await]"


class KeroStairsFlag(InvisibleFlagLocation):
    _room_ids = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _x_coord = 5
    _y_coord = 41
    _z_coord = 4
    _y_shift = 8
    _clue_text = " Mine's in a corner, nearby lots of\n dank stairs.[await]"


class KeroGateFlag(InvisibleFlagLocation):
    _room_ids = [R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE]
    _x_coord = 4
    _y_coord = 88
    _z_coord = 4
    _x_shift = -16
    _clue_text = "\n Mine is by a lone metal spike fence.[await]"


class MidasTreesFlag(InvisibleFlagLocation):
    _room_ids = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _x_coord = 24
    _y_coord = 26
    _x_shift = -8
    _clue_text = " Mine's between a lone pair of\n palm trees, near water.[await]"


class TadpoleCabinetFlag(InvisibleFlagLocation):
    _room_ids = [R075_TADPOLE_POND_AREA_01]
    _x_coord = 25
    _y_coord = 29
    _z_coord = 2
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n       Mine is in a frog cabinet.[await]"


class RoseWayDirtPatchFlag(InvisibleFlagLocation):
    _room_ids = [R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    _x_coord = 25
    _y_coord = 88
    _clue_text = " Mine is in the middle of a HUGE\n patch of dirt.[await]"


class RoseTownHydrantFlag(InvisibleFlagLocation):
    _room_ids = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 15
    _y_coord = 63
    _y_shift = -8
    _clue_text = "\n  Mine is under a low steel hydrant.[await]"


class RoseTownSinkFlag(InvisibleFlagLocation):
    _room_ids = [
        R089_ROSE_TOWN_DURING_BOWYER_THREE_GRANDKIDS_HOUSE,
        R090_ROSE_TOWN_THREE_GRANDKIDS_HOUSE,
    ]
    _x_coord = 15
    _y_coord = 10
    _y_shift = 1
    _clue_text = "\n My flag is in a kitchen sink under\n some green curtains.[await]"


class RoseTownBowserFlag(InvisibleFlagLocation):
    _room_ids = [
        R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        R086_ROSE_TOWN_INN_1F,
    ]
    _x_coord = 7
    _y_coord = 21
    _clue_text = "\n   Mine's under a miniature turtle.[await]"


class RoseTownGardenerHydrantFlag(InvisibleFlagLocation):
    _room_ids = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 2
    _y_coord = 85
    _y_shift = -8
    _clue_text = "\n   Mine is under a private hydrant.[await]"


class RoseTownGardenerBucketFlag(InvisibleFlagLocation):
    _room_ids = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 5
    _y_coord = 87
    _clue_text = "\n   Mine is under a private bucket.[await]"


class RoseTownGardenerLeafFlag(InvisibleFlagLocation):
    _room_ids = [R419_LAZY_SHELL_CLOUD]
    _x_coord = 4
    _y_coord = 111
    _z_coord = 10
    _clue_text = "\n Mine's on a big leaf between\n two chests.[await]"


class ForestMazeSecretStumpFlag(InvisibleFlagLocation):
    _room_ids = [R231_FOREST_MAZE_SECRET_ENTRANCE]
    _x_coord = 18
    _y_coord = 72
    _x_shift = 16
    _clue_text = " Mine is behind a brightly\n illuminated tree stump.[await]"


class ForestMazeSecretMushroomsFlag(InvisibleFlagLocation):
    _room_ids = [R235_FOREST_MAZE_AREA_08_UNDERGROUND]
    _x_coord = 25
    _y_coord = 93
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"


class ForestMazeSecretWigglerFlag(InvisibleFlagLocation):
    _room_ids = [R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER]
    _x_coord = 2
    _y_coord = 39
    _clue_text = "\n        Mine is on a sleepy bug.[await]"


class PipeVaultExteriorFlag(InvisibleFlagLocation):
    _room_ids = [R055_PIPE_VAULT_ENTRANCE]
    _x_coord = 17
    _y_coord = 19
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is by a pipe in the middle of\n the road.[await]"


class PipeVaultRedPipeFlag(InvisibleFlagLocation):
    _room_ids = [R129_PIPE_VAULT_AREA_05]
    _x_coord = 21
    _y_coord = 107
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n     Mine is behind a low red pipe.[await]"


class YosterIsleHutFlag(InvisibleFlagLocation):
    _room_ids = [R034_YOSTER_ISLE]
    _x_coord = 11
    _y_coord = 70
    _clue_text = "\n         Mine's in a fruity hut.[await]"


class MolevilleHydrantFlag(InvisibleFlagLocation):
    _room_ids = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 6
    _y_coord = 63
    _y_shift = -8
    _clue_text = "\n     Mine's under a gold hydrant.[await]"


class MolevilleMountainBushFlag(InvisibleFlagLocation):
    _room_ids = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 19
    _y_coord = 31
    _z_coord = 12
    _clue_text = " Mine's in a bush at the top of\n a mountain.[await]"


class MolevilleBedFlag(InvisibleFlagLocation):
    _room_ids = [R337_MOLEVILLE_INN]
    _x_coord = 6
    _y_coord = 12
    _x_shift = 16
    _clue_text = "\n       Mine's under a middle bed.[await]"


class MolevilleMinesArrowsFlag(InvisibleFlagLocation):
    _room_ids = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _x_coord = 5
    _y_coord = 51
    _clue_text = " Mine's between two arrows,\n pointing away from each other.[await]"


class MolevilleMinesCeilingFlag(InvisibleFlagLocation):
    _room_ids = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _x_coord = 8
    _y_coord = 13
    _z_coord = 4
    _clue_text = " Mine's in a zig-zag room, up\n on the ceiling.[await]"


class MolevilleMinesEntryFlag(InvisibleFlagLocation):
    _room_ids = [R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING]
    _x_coord = 22
    _y_coord = 23
    _z_coord = 3
    _x_shift = 16
    _clue_text = '\n My flag?[delay]\n ...[delay]It\'s on the word "IN",\n [delay]above a big hole.[await]'


class BoosterPassCornerBushFlag(InvisibleFlagLocation):
    _room_ids = [R101_BOOSTER_PASS_AREA_02]
    _x_coord = 17
    _y_coord = 112
    _x_shift = -8
    _y_shift = 8
    _clue_text = "\n        Mine's in a corner bush.[await]"


class BoosterTowerExteriorSignFlag(InvisibleFlagLocation):
    _room_ids = [R202_BOOSTER_TOWER_ENTRANCE]
    _x_coord = 4
    _y_coord = 110
    _x_shift = 16
    _clue_text = " Mine's behind a sign with Japanese\n letters.[await]"


class BoosterTowerDeskFlag(InvisibleFlagLocation):
    _room_ids = [R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    _x_coord = 24
    _y_coord = 113
    _x_shift = 16
    _clue_text = '\n      Mine\'s under "B" and "K".[await]'


class BoosterTowerMasherRoomFlag(InvisibleFlagLocation):
    _room_ids = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _x_coord = 19
    _y_coord = 122
    _y_shift = 8
    _clue_text = "\n Mine's on a lightly-loaded see-saw.[await]"


class BoosterTowerCurtainFlag(InvisibleFlagLocation):
    _room_ids = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _x_coord = 7
    _y_coord = 64
    _z_coord = 9
    _y_shift = 8
    _clue_text = " Mine's in a corner, between a\n window and a red curtain.[await]"


class BoosterTowerThwompInvisibleFlag(InvisibleFlagLocation):
    _room_ids = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _x_coord = 5
    _y_coord = 114
    _z_coord = 12
    _clue_text = "\n     Mine is near a lonely thwomp.[await]"


class BoosterTowerBrokenFrameFlag(InvisibleFlagLocation):
    _room_ids = [R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    _x_coord = 15
    _y_coord = 83
    _x_shift = -8
    _y_shift = -9
    _clue_text = "\n       Mine is in a broken frame.[await]"


class BoosterTowerBeetleCageFlag(InvisibleFlagLocation):
    _room_ids = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 18
    _clue_text = "\n     Mine is on an insect cage.[await]"


class BoosterTowerToyBoxFlag(InvisibleFlagLocation):
    _room_ids = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 24
    _x_shift = 16
    _clue_text = "\n       Mine is behind a toy box.[await]"


class MarrymoreOutsideCrateFlag(InvisibleFlagLocation):
    _room_ids = [
        R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
        R064_MARRYMORE_OUTSIDE,
    ]
    _x_coord = 23
    _y_coord = 60
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n  Mine is under a lone backyard box.[await]"


class MarrymoreHallwayFlag(InvisibleFlagLocation):
    _room_ids = [R011_MARRYMORE_INN_3F]
    _x_coord = 18
    _y_coord = 76
    _z_coord = 3
    _clue_text = " My flag is in a flower pot in a\n hallway.[await]"


class MarrymoreSuiteBedFlag(InvisibleFlagLocation):
    _room_ids = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 7
    _y_coord = 13
    _z_coord = 6
    _x_shift = -16
    _clue_text = " Mine's beneath two adjoined\n red beds.[await]"


class MarrymoreKitchenFlag(InvisibleFlagLocation):
    _room_ids = [R155_MARRYMORE_CHAPEL_KITCHEN]
    _x_coord = 2
    _y_coord = 20
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is in a big cabinet full of\n dishes.[await]"


class MarrymoreFireplaceFlag(InvisibleFlagLocation):
    _room_ids = [R152_MARRYMORE_CHAPEL_MAIN_HALL]
    _x_coord = 9
    _y_coord = 33
    _z_coord = 2
    _y_shift = -8
    _clue_text = "\n    Mine is in an empty fireplace.[await]"


class MarrymoreOrganFlag(InvisibleFlagLocation):
    _room_ids = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 65
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine is behind a big musical\n instrument.[await]"


class MarrymoreAltarFlag(InvisibleFlagLocation):
    _room_ids = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 70
    _z_coord = 1
    _clue_text = "\n        Mine's behind a podium.[await]"


class StarHillNorthStarFlag(InvisibleFlagLocation):
    _room_ids = [R158_STAR_HILL_AREA_02]
    _x_coord = 8
    _y_coord = 69
    _z_coord = 2
    _x_shift = -10
    _clue_text = "\n     Mine is atop the North Star.[await]"


class SeasideTownAnchorFlag(InvisibleFlagLocation):
    _room_ids = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 14
    _y_coord = 57
    _x_shift = 16
    _clue_text = "\n       Mine is behind an anchor.[await]"


class SeasideTownHydrantFlag(InvisibleFlagLocation):
    _room_ids = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 16
    _y_coord = 25
    _z_coord = 5
    _x_shift = 0
    _y_shift = -8
    _clue_text = "\n  Mine is under a high steel hydrant.[await]"


class SeasideTownBucketFlag(InvisibleFlagLocation):
    _room_ids = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 20
    _y_coord = 31
    _z_coord = 3
    _clue_text = "\n Mine is in a bucket between two\n staircases.[await]"


class SeasideTownFlowersFlag(InvisibleFlagLocation):
    _room_ids = [
        R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
        R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    ]
    _x_coord = 26
    _y_coord = 60
    _y_shift = 8
    _clue_text = " Mine's in the middle of three\n pink flowers.[await]"


class SeasideTownShedBoxFlag(InvisibleFlagLocation):
    _room_ids = [R314_SEASIDE_TOWN_SHED]
    _x_coord = 5
    _y_coord = 23
    _y_shift = 8
    _clue_text = " Mine's under a lone crate in an\n empty house.[await]"


class SeaArrowFlag(InvisibleFlagLocation):
    _room_ids = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 8
    _y_coord = 21
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n   Mine is beside a mossy up-arrow.[await]"


class SeaBoxesFlag(InvisibleFlagLocation):
    _room_ids = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 9
    _y_coord = 36
    _y_shift = -8
    _clue_text = "\n    Mine's in some V-shaped boxes.[await]"


class SeaStalagnateFlag(InvisibleFlagLocation):
    _room_ids = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _x_coord = 18
    _y_coord = 43
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is behind a big gray\n stalagnate.[await]"


class SeaUnderwaterSailFlag(InvisibleFlagLocation):
    _room_ids = [R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP]
    _x_coord = 4
    _y_coord = 41
    _clue_text = "\n        Mine's behind a big sail.[await]"


class ShipBarrelPileFlag(InvisibleFlagLocation):
    _room_ids = [R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES]
    _x_coord = 7
    _y_coord = 66
    _z_coord = 3
    _clue_text = "\n  Mine is atop a big pile of barrels.[await]"


class ShipDoorMarkerFlag(InvisibleFlagLocation):
    _room_ids = [R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY]
    _x_coord = 18
    _y_coord = 82
    _z_coord = 1
    _y_shift = 8
    _clue_text = ' Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number "4".[await]'


class ShipButtonFlag(InvisibleFlagLocation):
    _room_ids = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _x_coord = 16
    _y_coord = 133
    _clue_text = "\n   Mine is under a floating button.[await]"


class ShipSwitchFlag(InvisibleFlagLocation):
    _room_ids = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _x_coord = 17
    _y_coord = 121
    _clue_text = '\n  Mine is underneath a floating "J".[await]'


class LandsEndPlatformFlag(InvisibleFlagLocation):
    _room_ids = [R137_LANDS_END_AREA_01]
    _x_coord = 6
    _y_coord = 29
    _clue_text = "\n   Mine is under a rising platform.[await]"


class LandsEndCannonFlag(InvisibleFlagLocation):
    _room_ids = [R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL]
    _x_coord = 11
    _y_coord = 115
    _y_shift = -8
    _clue_text = " Mine's under a big and quiet\n cannon.[await]"


class LandsEndArrowFlag(InvisibleFlagLocation):
    _room_ids = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _x_coord = 28
    _y_coord = 29
    _x_shift = 16
    _clue_text = "\n Mine is beside an orange up-arrow.[await]"


class LandsEndHillFlag(InvisibleFlagLocation):
    _room_ids = [R404_LANDS_END_DESERT_AREA_04]
    _x_coord = 23
    _y_coord = 96
    _x_shift = 8
    _y_shift = 8
    _clue_text = " Mine is on a short, red hill in a\n remote area.[await]"


class LandsEndTwoHillFlag(InvisibleFlagLocation):
    _room_ids = [R319_LANDS_END_DESERT_AREA_06]
    _x_coord = 8
    _y_coord = 121
    _clue_text = "   My flag's between two red hills.[await]"


class LandsEndStalagmiteFlag(InvisibleFlagLocation):
    _room_ids = [R265_LANDS_END_UNDERGROUND_AREA_03]
    _x_coord = 22
    _y_coord = 80
    _x_shift = 8
    _y_shift = 8
    _clue_text = (
        " Mine's on a big stalagmite\n formation in an underground cave.[await]"
    )


class LandsEndCliffBushFlag(InvisibleFlagLocation):
    _room_ids = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 23
    _y_coord = 103
    _z_coord = 22
    _clue_text = " Mine is on a bush, way up high on\n a cliff.[await]"


class LandsEndSignFlag(InvisibleFlagLocation):
    _room_ids = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 24
    _y_coord = 118
    _z_coord = 0
    _y_shift = -4
    _x_shift = 8
    _clue_text = "     My flag's on a yellow arrow.[await]"


class DojoBonsaiFlag(InvisibleFlagLocation):
    _room_ids = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _x_coord = 6
    _y_coord = 9
    _y_shift = 8
    _clue_text = "\n   Mine's underneath a bonsai tree.[await]"


class MonstroEntranceSignFlag(InvisibleFlagLocation):
    _room_ids = [R267_MONSTRO_TOWN_ENTRANCE]
    _x_coord = 9
    _y_coord = 102
    _clue_text = "\n     Mine's in a lone flowery bush.[await]"


class MonstroBatFlag(InvisibleFlagLocation):
    _room_ids = [R324_MONSTRO_TOWN_OUTSIDE]
    _x_coord = 5
    _y_coord = 51
    _z_coord = 4
    _y_shift = 8
    _clue_text = "\n     Mine's behind a wooden bat.[await]"


class MonstroFanFlag(InvisibleFlagLocation):
    _room_ids = [R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F]
    _x_coord = 12
    _y_coord = 80
    _z_coord = 1
    _x_shift = -16
    _clue_text = "\n         Mine's beside a fan.[await]"


class MonstroShellFlag(InvisibleFlagLocation):
    _room_ids = [R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP]
    _x_coord = 16
    _y_coord = 15
    _z_coord = 1
    _y_shift = 8
    _clue_text = "\n   Mine's beneath a spinning shell.[await]"


class BeanValleyPipeFlag(InvisibleFlagLocation):
    _room_ids = [R252_BEAN_VALLEY_MAIN_AREA]
    _x_coord = 17
    _y_coord = 85
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine's on an isolated, dead-end\n pipe.[await]"


class BeanValleyBeanstalkBlockFlag(InvisibleFlagLocation):
    _room_ids = [R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA]
    _x_coord = 27
    _y_coord = 27
    _clue_text = "\n  Mine's underneath a big beanstalk.[await]"


class CasinoBellFlag(InvisibleFlagLocation):
    _room_ids = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _x_coord = 14
    _y_coord = 19
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n       Mine is beside a tiny bell.[await][pause]\n I don't think it does anything.[await]"


class NimbusGoldGoombaFlag(InvisibleFlagLocation):
    _room_ids = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _x_coord = 5
    _y_coord = 14
    _z_coord = 1
    _clue_text = "\n     Mine is on a golden Goomba.[await]"


class NimbusInnLobbyFlag(InvisibleFlagLocation):
    _room_ids = [R343_NIMBUS_LAND_INN]
    _x_coord = 6
    _y_coord = 84
    _z_coord = 2
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is under a stove with two\n pots.[await]"


class NimbusPlantFlag(InvisibleFlagLocation):
    _room_ids = [
        R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT
    ]
    _x_coord = 27
    _y_coord = 74
    _z_coord = 1
    _clue_text = " Mine is behind a big potted plant\n in a corner.[await]"


class NimbusBirdFlag(InvisibleFlagLocation):
    _room_ids = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _x_coord = 28
    _y_coord = 48
    _y_shift = -8
    _clue_text = " Mine is under a birdcage, in a\n restricted dead-end area.[await]"


class NimbusHotSpringsFlag(InvisibleFlagLocation):
    _room_ids = [R447_NIMBUS_LAND_HOT_SPRINGS]
    _x_coord = 19
    _y_coord = 114
    _z_coord = 5
    _clue_text = " Mine's on the right side of a\n hot pool.[await]"


class VolcanoShipsFlag(InvisibleFlagLocation):
    _room_ids = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 11
    _y_coord = 61
    _z_coord = 2
    _clue_text = "\n    Mine is between two vehicles.[await]"


class KeepPostObstacleBossRoomFlag(InvisibleFlagLocation):
    _room_ids = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _x_coord = 26
    _y_coord = 97
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n  Mine is between two big red doors.[await]"


class KeepThwompFlag(InvisibleFlagLocation):
    _room_ids = [R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM]
    _x_coord = 19
    _y_coord = 47
    _clue_text = "\n      Mine is under a big thwomp.[await]"


class FactoryCanopyFlag(InvisibleFlagLocation):
    _room_ids = [R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT]
    _x_coord = 16
    _y_coord = 15
    _z_coord = 10
    _y_shift = 8
    _clue_text = "  My flag's under a bolted canopy.[await]"


class FactoryLugnutFlag(InvisibleFlagLocation):
    _room_ids = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _x_coord = 23
    _y_coord = 52
    _z_coord = 7
    _clue_text = "    My flag's underneath a lugnut.[await]"


class FactoryTrampolineFlag(InvisibleFlagLocation):
    _room_ids = [R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN]
    _x_coord = 14
    _y_coord = 9
    _y_shift = 16
    _clue_text = " My flag is under the world's\n loneliest trampoline.[await]"


class FactoryButtonFlag(InvisibleFlagLocation):
    _room_ids = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _x_coord = 4
    _y_coord = 36
    _z_coord = 5
    _clue_text = " Mine is on a jammed machine\n button.[await]"


def can_defeat_some_of(
    world: GameWorld,
    inventory: Inventory,
    conditions: list[Callable[[GameWorld, Inventory], bool]],
    amount: int = 1,
) -> bool:
    """If true, the player is expected to be able to defeat at least some of
    the provided bosses."""
    bosses: list[bool] = [cond(world, inventory) for cond in conditions]
    completable: list[bool] = [cond for cond in bosses if cond]
    return len(completable) >= amount


def can_defeat_all_of(
    world: GameWorld,
    inventory: Inventory,
    conditions: list[Callable[[GameWorld, Inventory], bool]],
) -> bool:
    """If true, the player is expected to be able to defeat all of the provided
    bosses."""
    return can_defeat_some_of(world, inventory, conditions, len(conditions))


def can_defeat_boss(
    world: GameWorld, inventory: Inventory, location_type: type[BossFightLocation]
) -> bool:
    if (
        world.settings.get_flag(ProgressionLogicDifficulty).selected
        == ProgressionLogicDifficultyOptions.HARD
    ):
        return True
    location = world.get_location(location_type)
    if location.prize is None:  # not assigned yet
        return False
    return inventory.has_item(type(location.prize))


def can_defeat_mushroom_way_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Mushroom Way."""
    return can_defeat_boss(world, inventory, MushrooomWayBossFight)


def can_access_bandits_way(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bandit's Way."""
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.HAMMER_BRO):
        return inventory.has_item(HammerBrosFight)
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MUSHROOM_WAY):
        return can_defeat_mushroom_way_boss(world, inventory)
    return True


def can_defeat_bandits_way_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Bandit's Way."""
    return can_access_bandits_way(world, inventory) and can_defeat_boss(
        world, inventory, BanditsWayBossFight
    )


def can_access_invaded_kingdom(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Invaded Kingdom."""
    return can_defeat_bandits_way_boss(world, inventory)


def can_defeat_mushroom_kingdom_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Mushroom Kingdom."""
    return can_defeat_bandits_way_boss(world, inventory) and can_defeat_boss(
        world, inventory, MushroomKingdomBossFight
    )


def can_defeat_mimic(
    world: GameWorld, inventory: Inventory, mimic: type[MimicFightInitiatorPrize]
) -> bool:
    """If true, the player is expected to be able to defeat the specified mimic chest fight."""
    location = next(
        (v for (_, v) in world.locations.items() if isinstance(v.prize, mimic)), None
    )
    if location is None:
        return False
    return location.can_access(inventory, world)


def can_access_first_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the first mimic chest fight."""
    return can_defeat_mimic(world, inventory, FirstMimicFightLauncher)


def can_defeat_first_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the first mimic chest fight."""
    return can_access_first_mimic(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_mushroom_way_boss,
            can_defeat_bandits_way_boss,
            can_defeat_mushroom_kingdom_boss,
        ],
    )


def can_access_sewer(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Kero Sewers."""
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MACK):
        return inventory.has_item(MackBossFight)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
        return can_defeat_mushroom_kingdom_boss(world, inventory)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
        return can_defeat_mushroom_kingdom_boss(
            world, inventory
        ) and inventory.has_item(RareFrogCoinPrize)
    return True


def can_access_sewer_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss at Kero Sewers."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_mushroom_way_boss,
            can_defeat_bandits_way_boss,
            can_defeat_mushroom_kingdom_boss,
        ],
    )


def can_defeat_sewer_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Kero Sewers."""
    return can_access_sewer_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeroSewersBossFight
    )


def can_access_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Forest Maze."""
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        return inventory.has_item(CricketPiePrize)
    return True


def can_access_forest_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss at Forest Maze."""
    return can_access_forest(world, inventory) and can_defeat_some_of(
        world, inventory, [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss]
    )


def can_defeat_forest_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Forest Maze."""
    return can_defeat_boss(
        world, inventory, ForestMazeBossFight
    ) and can_access_forest_boss(world, inventory)


def can_access_pipe_vault(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Pipe Vault."""
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
        return can_defeat_forest_boss(world, inventory)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    return True


def can_access_moleville_entrance(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the uper entrance to the mines."""
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
        return can_defeat_forest_boss(world, inventory)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
        return can_access_pipe_vault(world, inventory)
    return True


def can_access_first_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st boss at Moleville."""
    return can_access_moleville_entrance(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss],
            2,
        )
        or can_defeat_some_of(world, inventory, [can_defeat_forest_boss])
    )


def can_access_second_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second mimic chest fight."""
    return can_defeat_mimic(world, inventory, SecondMimicFightLauncher)


def can_defeat_second_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the second mimic chest fight."""
    return can_access_second_mimic(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss],
            2,
        )
        or can_defeat_some_of(world, inventory, [can_defeat_forest_boss])
    )


def can_defeat_first_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st boss at Moleville."""
    return can_access_first_moleville_boss(world, inventory) and can_defeat_boss(
        world, inventory, OuterMinesBossFight
    )


def can_access_inner_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the inner half
    of Moleville Mines (beyond the exploding wall)."""
    return can_access_moleville_entrance(world, inventory) and inventory.has_item(
        BambinoBombPrize
    )


def can_access_second_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd boss at Moleville."""
    return can_access_inner_mines(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_sewer_boss,
                can_defeat_first_moleville_boss,
            ],
        )
    )


def can_defeat_second_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss at Moleville."""
    return can_access_second_moleville_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerMinesBossFight
    )


def can_access_moleville_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Moleville."""
    return (
        can_defeat_second_moleville_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_postgame_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss at Moleville."""
    return can_access_moleville_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerMinesPostgameBossFight
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
        return can_defeat_second_moleville_boss(world, inventory)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        return inventory.has_item(PunchinelloBossFight)
    return True


def can_access_curtain_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st boss of Booster Tower."""
    return can_access_tower(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
            ],
        )
    )


def can_defeat_curtain_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st boss of Booster Tower."""
    return can_access_curtain_boss(world, inventory) and can_defeat_boss(
        world, inventory, BoosterTowerIndoorBossFight
    )


def can_access_balcony_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd boss of Booster Tower."""
    return can_access_tower(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
            ],
        )
    )


def can_defeat_balcony_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss of Booster Tower."""
    return can_access_balcony_boss(world, inventory) and can_defeat_boss(
        world, inventory, BoosterTowerBalconyBossFight
    )


def can_access_tower_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Booster Tower."""
    return (
        can_defeat_curtain_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_postgame_tower_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss at Moleville."""
    return can_access_tower_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, BoosterTowerIndoorBossFightRemake
    )


def can_access_hill(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Booster Hill."""
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
        return can_defeat_balcony_boss(world, inventory)
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    return True


def can_access_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter the Marrymore chapel."""
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
        return can_defeat_balcony_boss(world, inventory)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
        return can_access_hill(world, inventory)
    return True


def can_access_chapel_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss of Marrymore."""
    has_gear = True
    if world.settings.isflag_enabled(ShuffleWeddingGear):
        has_gear = (
            inventory.has_item(ShoesPrize)
            and inventory.has_item(RingPrize)
            and inventory.has_item(BroochPrize)
            and inventory.has_item(CrownPrize)
        )
    return (
        has_gear
        and can_access_chapel(world, inventory)
        and can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
                can_defeat_balcony_boss,
            ],
        )
    )


def can_defeat_chapel_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss of Marrymore."""
    return can_access_chapel_boss(world, inventory) and can_defeat_boss(
        world, inventory, MarrymoreBossFight
    )


def can_access_chapel_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Marrymore."""
    return (
        can_defeat_chapel_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_postgame_chapel_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss at Marrymore."""
    return can_access_chapel_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, MarrymoreBossFightRemake
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
        return can_defeat_chapel_boss(world, inventory)
    return True


def can_access_ship_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st ship boss."""
    return can_access_sea(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
                can_defeat_balcony_boss,
                can_defeat_chapel_boss,
            ],
        )
    )


def can_defeat_ship_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st ship boss."""
    return can_access_ship_midboss(world, inventory) and can_defeat_boss(
        world, inventory, ShipPasswordBossFight
    )


def can_access_ship_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd ship boss."""
    return can_defeat_ship_midboss(world, inventory)


def can_defeat_ship_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd ship boss."""
    return can_access_ship_boss(world, inventory) and can_defeat_boss(
        world, inventory, ShipFinalBossFight
    )


def can_access_ship_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Sunken Ship."""
    return (
        can_defeat_ship_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_postgame_ship_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the postgame boss at Sunken Ship."""
    return can_access_ship_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, ShipPostgameBossFight
    )


def can_access_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Seaside Town boss."""
    sufficient_bosses = can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_second_moleville_boss,
            can_defeat_first_moleville_boss,
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
        ],
        2,
    )
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
        return can_defeat_ship_boss(world, inventory) and sufficient_bosses
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.JOHNNY):
        return inventory.has_item(JohnnyBossFight) and sufficient_bosses
    return sufficient_bosses


def can_defeat_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Seaside Town boss."""
    return can_access_seaside_boss(world, inventory) and can_defeat_boss(
        world, inventory, SeasideBeachBossFight
    )


def can_access_lands_end(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Land's End."""
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        return inventory.has_item_count(StarPiecePrize, 5)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
        return inventory.has_item(ShedKeyPrize) and can_access_seaside_boss(
            world, inventory
        )
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.YARIDOVICH):
        return inventory.has_item(YaridovichBossFight)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
        return can_defeat_seaside_boss(world, inventory)
    return True


def can_access_lands_end_cloud(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the random cloud spawn
    in Land's End.

    note: Mokura can appear at Mario's elevation before the cannon, so this is not gated behind LE access.
    """
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
        ],
        2,
    )


def can_defeat_lands_end_cloud_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Land's End cloud spawn boss."""
    return can_access_lands_end_cloud(world, inventory) and can_defeat_boss(
        world, inventory, LandsEndCloudBoss
    )


def can_access_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Belome Temple."""
    sufficient_bosses = can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
        ],
        2,
    )
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
        return inventory.has_item(TempleKeyPrize) and sufficient_bosses
    return sufficient_bosses


def can_defeat_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Belome Temple boss."""
    return can_access_temple_boss(world, inventory) and can_defeat_boss(
        world, inventory, TempleBossFight
    )


def can_access_temple_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Belome Temple."""
    return (
        can_defeat_temple_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_postgame_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the postgame boss at Belome Temple."""
    return can_access_temple_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, TempleBossFightPostgame
    )


def can_access_monstro_town(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Monstro Town."""
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
        return can_defeat_temple_boss(world, inventory)
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
        return inventory.has_item(Belome2BossFight)
    return True


def can_access_first_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Monstro dojo boss."""
    return can_access_monstro_town(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
        ],
    )


def can_defeat_first_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Monstro dojo boss."""
    return can_access_first_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoFirstFight
    )


def can_access_second_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Monstro dojo boss."""
    return can_defeat_first_dojo_boss(world, inventory)


def can_defeat_second_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Monstro dojo boss."""
    return can_access_second_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoSecondFight
    )


def can_access_third_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Monstro dojo boss."""
    return can_defeat_second_dojo_boss(world, inventory)


def can_defeat_third_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Monstro dojo boss."""
    return can_access_third_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoThirdFight
    )


def can_access_fourth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 4th Monstro dojo boss."""
    return can_defeat_third_dojo_boss(world, inventory)


def can_defeat_fourth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 4th Monstro dojo boss."""
    return can_access_third_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoFourthFight
    )


def can_access_fifth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 5th Monstro dojo boss."""
    return (
        can_defeat_fourth_dojo_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_fifth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 5th Monstro dojo boss."""
    return can_access_fifth_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoFifthFight
    )


def can_access_valley_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Bean Valley boss."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
        ],
    )


def can_defeat_valley_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Bean Valley boss."""
    return can_access_valley_boss(world, inventory) and can_defeat_boss(
        world, inventory, BeanValleyPlanterBossFight
    )


def can_access_third_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the third mimic chest fight."""
    return can_defeat_mimic(world, inventory, ThirdMimicFightLauncher)


def can_defeat_third_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the third mimic chest fight."""
    return can_access_third_mimic(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
        ],
    )


def can_access_statue_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Nimbus boss."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
        ],
    )


def can_defeat_statue_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Nimbus boss."""
    return can_access_statue_boss(world, inventory) and can_defeat_boss(
        world, inventory, StatueRoomBossFight
    )


def can_access_outer_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get to Nimbus Land."""
    if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
        return can_defeat_valley_boss(world, inventory)
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
    return can_access_nimbus_castle(world, inventory) and inventory.has_item(CastleKey1Prize)


def can_access_egg_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Nimbus boss."""
    return can_access_inner_nimbus(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
        ],
    )


def can_defeat_egg_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Nimbus boss."""
    return can_access_egg_boss(world, inventory) and can_defeat_boss(
        world, inventory, GiantEggBossFight
    )


def can_access_late_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 2 door."""
    return can_access_inner_nimbus(world, inventory) and inventory.has_item(CastleKey2Prize)


def can_access_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Nimbus boss."""
    return can_access_late_nimbus(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
            can_defeat_egg_boss,
        ])


def can_defeat_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Nimbus boss."""
    return can_access_nimbus_boss(world, inventory) and can_defeat_boss(
        world, inventory, NimbusFinalBossFight
    )

def can_access_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Barrel Volcano."""
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
        return can_defeat_nimbus_boss(world, inventory)
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA):
        return inventory.has_item(ValentinaBossFight)
    return True


def can_access_volcano_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st volcano boss."""
    return can_access_volcano(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_seaside_boss,
            can_defeat_temple_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
            can_defeat_egg_boss,
            can_defeat_nimbus_boss,
        ])

def can_defeat_volcano_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st volcano boss."""
    return can_access_volcano_midboss(world, inventory) and can_defeat_boss(
        world, inventory, VolcanoBridgeBossFight
    )


def can_access_volcano_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd volcano boss."""
    return can_defeat_volcano_midboss(world, inventory)


def can_defeat_volcano_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd volcano boss."""
    return can_access_volcano_boss(world, inventory) and can_defeat_boss(
        world, inventory, VolcanoExitBossFight
    )




def can_take_lategame_bosses(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to reasonably have progressed enough in the seed
    to fight lategame bosses."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_fourth_dojo_boss,
            can_defeat_egg_boss,
            can_access_nimbus_boss,
            can_defeat_volcano_midboss,
            can_defeat_volcano_boss,
        ],
    )



def can_access_keep(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bowser's Keep."""
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
        return can_defeat_volcano_boss(world, inventory)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        return inventory.has_item_count(StarPiecePrize, 6)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.AXEM):
        return inventory.has_item(AxemRangersBossFight)
    return True


def can_access_battle_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the battle door
    that normally contains the Chester fight."""
    return can_access_keep(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_battle_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the battle door
    that normally contains the Chester fight."""
    return can_access_battle_door_boss(world, inventory) and can_defeat_boss(
        world, inventory, ObstacleCourseFinalFight
    )


def can_access_post_obstacle_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss fight
    after completing the Bowser's Keep red doors."""
    return can_access_keep(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_post_obstacle_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss fight
    after completing the Bowser's Keep red doors."""
    return can_access_post_obstacle_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepAfterObstaclesBossFight
    )


def can_access_keep_chandelier_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the first back-to-back Keep boss."""
    return can_defeat_post_obstacle_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_keep_chandelier_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the first back-to-back Keep boss."""
    return can_access_keep_chandelier_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepChandelierBossFight
    )


def can_access_keep_exit_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second back-to-back Keep boss."""
    return can_defeat_keep_chandelier_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_keep_exit_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the second back-to-back Keep boss."""
    return can_access_keep_exit_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepFinalBossFight
    )


def can_access_factory(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Outer Factory."""
    if world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        return inventory.has_item_count(StarPiecePrize, 6) and can_defeat_keep_exit_boss(
            world, inventory
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
        return inventory.has_item(ExorBossFight) and can_defeat_keep_exit_boss(
            world, inventory
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
        return can_access_keep(
            world, inventory
        )
    return can_defeat_keep_exit_boss(world, inventory)


def can_access_first_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Outer Factory boss."""
    return can_access_factory(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_first_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Outer Factory boss."""
    return can_access_first_factory_boss(world, inventory) and can_defeat_boss(
        world, inventory, FactoryEntranceBossFight
    )


def can_access_second_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Outer Factory boss."""
    return can_defeat_first_factory_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_second_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Outer Factory boss."""
    return can_access_second_factory_boss(world, inventory) and can_defeat_boss(
        world, inventory, FactoryTransitionBossFight
    )


def can_access_inner_factory_first_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Inner Factory boss."""
    return can_defeat_second_factory_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_first_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Inner Factory boss."""
    return can_access_inner_factory_first_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryFirstFight
    )


def can_access_inner_factory_second_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to access the 2nd Inner Factory boss."""
    return can_defeat_first_factory_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_inner_factory_second_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Inner Factory boss."""
    return can_access_inner_factory_second_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactorySecondFight
    )


def can_access_inner_factory_third_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Inner Factory boss."""
    return can_defeat_inner_factory_second_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_third_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Inner Factory boss."""
    return can_access_inner_factory_third_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryThirdFight
    )


def can_access_inner_factory_fourth_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to access the 4th Inner Factory boss."""
    return can_defeat_inner_factory_third_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_fourth_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to defeat the 4th Inner Factory boss."""
    return can_access_inner_factory_fourth_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryFourthFight
    )

# TODO do we want bucket warp / casino warp to take us to the boss fight or to the inner factory?
def can_access_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the final Factory boss."""
    value = world.settings.get_flag(StarPiecesRequired).value
    has_stars = inventory.has_item_count(StarPiecePrize, value)
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        fireworks_access = inventory.has_item(RegularFireworksPrize)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        fireworks_access = inventory.has_item_count(ProgressiveFireworksPrize, 3)
    else:
        fireworks_access = can_defeat_second_moleville_boss(world, inventory)
    can_access_bucket = (
        fireworks_access
        and can_defeat_second_moleville_boss(world, inventory)
        and world.settings.isflag_enabled(BucketWarp)
    )
    can_access_casino = world.settings.isflag_enabled(
        CasinoWarp
    ) and inventory.has_item(BrightCardPrize)
    return (
        has_stars
        and (
            can_access_bucket
            or can_access_casino
            or can_defeat_inner_factory_fourth_boss(world, inventory)
        )
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the final Factory boss."""
    return can_access_inner_factory_final_boss(world, inventory) and can_defeat_boss(
        world, inventory, FinalBossFight
    )



def can_access_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the sealed door boss."""
    boss_reqs = can_access_monstro_town(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )
    item_reqs: bool = False
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        item_reqs = inventory.has_item(
            RegularFireworksPrize
        ) and can_defeat_second_moleville_boss(world, inventory)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        item_reqs = inventory.has_item_count(ProgressiveFireworksPrize, 2)
    else:
        item_reqs = can_defeat_second_moleville_boss(world, inventory)
    return item_reqs and boss_reqs


def can_defeat_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the sealed door boss."""
    return can_access_sealed_door_boss(world, inventory) and can_defeat_boss(
        world, inventory, MonstroSealedDoorBossFight
    )


def can_access_sealed_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second sealed door boss."""
    return (
        can_defeat_sealed_door_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and inventory.has_item(ExtraShinyStonePrize)
        and world.settings.is_flag_value(Remake, True)
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_sealed_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the second sealed door boss."""
    return can_access_sealed_postgame_boss(world, inventory) and can_defeat_boss(
        world, inventory, MonstroSealedDoorBossFightPostgame
    )


def can_access_invisible_flags(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the invisible item checks have been activated."""
    return world.settings.isflag_enabled(
        SkipMustyFearsSequence
    ) or can_access_monstro_town(world, inventory)

    # mimic 3 and postgame temple
