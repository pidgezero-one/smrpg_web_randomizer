"""Progress location definitions for items."""

from random import random
from typing import List, Optional, Type

from randomizer.entities.spells.spells import SuperJump
from randomizer.entities.items import (
    Amulet,
    AttackScarf,
    BambinoBomb,
    BanditsWayStar,
    Beetlemania,
    BigBooFlag,
    BrightCard,
    Brooch,
    CastleKey1,
    CastleKey2,
    Chomp,
    CoinTrick,
    Coins1,
    Coins10,
    Coins100,
    Coins150,
    Coins20,
    Coins5,
    Coins50,
    Coins8,
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
    FingerShot,
    FireBomb,
    Fireworks,
    Flower,
    FlowerBox,
    FlowerJar,
    FlowerTab,
    FrightBomb,
    FrogCoin,
    FrogCoins10,
    FrogCoins2,
    FrogCoins20,
    FrogCoins3,
    FroggieStick,
    FryingPan,
    GhostMedal,
    GoodieBag,
    GreaperFlag,
    Hammer,
    HoneySyrup,
    IceBomb,
    InfiniteCoins,
    JinxBelt,
    KeroSewersStar,
    KerokeroCola,
    LandsEndStar2,
    LandsEndStar3,
    LandsEndVolcanoStar,
    LazyShellArmor,
    LazyShellWeapon,
    LuckyJewel,
    Masher,
    MaxMushroom,
    MimicFightInitiator1,
    MimicFightInitiator2,
    MimicFightInitiator3,
    MolevilleMinesStar,
    Mushroom,
    NimbusLandStar,
    NokNokShell,
    PickMeUp,
    ProgressiveCard,
    ProgressiveEgg,
    ProgressiveFireworks,
    QuartzCharm,
    RareFrogCoin,
    RareScarf,
    RecoveryMushroom,
    RedEssence,
    Ring,
    RockCandy,
    RoomKey,
    RoyalSyrup,
    SafetyBadge,
    SafetyRing,
    ScroogeRing,
    SeaStar,
    SeeYa,
    Seed,
    ShedKey,
    Shoes,
    SignalRing,
    SlotMachineChest,
    SonicCymbal,
    StarEgg,
    StarGun,
    SuperSlap,
    SuperSuit,
    TempleKey,
    TroopaPin,
    TrueformPin,
    UltraHammer,
    WakeUpPin,
    Wallet,
    YoshiCookie,
    YouMissed,
    ZoomShoes,
)

from randomizer.types.dialogs.ids import (
    DI2908_TREASURE_SELLER_ITEM_2,
    DI2911_TREASURE_SELLER_ITEM_1,
    DI2914_TREASURE_SELLER_ITEM_3,
)
from randomizer.types.items import (
    InvincibilityStar,
    Item,
    MimicFightChestAssignment,
)
from randomizer.types.overworld_scripts.ids import (
    R007_MARRYMORE_INN_1F,
    R009_MARRYMORE_INN_REGULAR_ROOM,
    R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
    R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
    R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
    R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER,
    R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
    R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT,
    R034_YOSTER_ISLE,
    R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS,
    R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER,
    R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM,
    R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
    R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM,
    R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
    R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
    R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA,
    R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT,
    R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT,
    R074_TADPOLE_POND_AREA_02,
    R075_TADPOLE_POND_AREA_01,
    R077_BANDITS_WAY_AREA_03,
    R078_BANDITS_WAY_AREA_04,
    R079_ROSE_WAY_MAIN_AREA,
    R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS,
    R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA,
    R086_ROSE_TOWN_INN_1F,
    R087_ROSE_TOWN_ITEM_SHOP,
    R092_GRATE_GUYS_CASINO_INSIDE_CASINO,
    R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
    R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
    R096_ROSE_TOWN_INN_2F,
    R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
    R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    R100_BOOSTER_PASS_AREA_01,
    R108_MOLEVILLE_OUTSIDE,
    R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
    R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
    R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
    R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
    R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
    R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
    R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
    R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
    R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT,
    R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
    R134_SEA_AREA_03_SUPER_STAR_ROOM,
    R137_LANDS_END_AREA_01,
    R138_LANDS_END_AREA_02,
    R141_LANDS_END_AREA_04_ROTATING_FLOWERS,
    R143_PIPE_VAULT_GOOMBATHUMPING_ROOM,
    R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
    R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    R163_SUNKEN_SHIP_PUZZLE_ROOM_2,
    R166_SUNKEN_SHIP_PUZZLE_ROOM_1,
    R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS,
    R168_SUNKEN_SHIP_PUZZLE_ROOM_3,
    R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN,
    R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
    R172_SUNKEN_SHIP_PUZZLE_ROOM_5,
    R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
    R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL,
    R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
    R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN,
    R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT,
    R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING,
    R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
    R189_MARIOS_PIPEHOUSE,
    R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
    R191_MUSHROOM_KINGDOM_OUTSIDE,
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
    R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
    R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
    R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
    R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
    R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
    R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP,
    R203_MUSHROOM_WAY_AREA_01,
    R204_MUSHROOM_WAY_AREA_02,
    R205_MUSHROOM_WAY_AREA_03,
    R206_BANDITS_WAY_AREA_05,
    R207_BANDITS_WAY_AREA_02,
    R224_FOREST_MAZE_AREA_01,
    R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE,
    R228_FOREST_MAZE_AREA_04,
    R234_FOREST_MAZE_SECRET,
    R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT,
    R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER,
    R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
    R251_BEAN_VALLEY_PIRANHA_PIPE_AREA,
    R252_BEAN_VALLEY_MAIN_AREA,
    R254_BEAN_VALLEY_SMILAX_AREA,
    R255_MONSTRO_TOWN_JINXS_DOJO,
    R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS,
    R263_LANDS_END_UNDERGROUND_AREA_01,
    R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
    R267_MONSTRO_TOWN_ENTRANCE,
    R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
    R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
    R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
    R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC,
    R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM,
    R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM,
    R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
    R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
    R314_SEASIDE_TOWN_SHED,
    R316_SEASIDE_TOWN_BEACH,
    R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
    R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
    R324_MONSTRO_TOWN_OUTSIDE,
    R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
    R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM,
    R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE,
    R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
    R336_MOLEVILLE_ITEM_SHOP,
    R339_MOLEVILLE_FIREWORKS_SHOP,
    R344_NIMBUS_LAND_ITEM_SHOP,
    R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING,
    R346_NIMBUS_LAND_INN_BEDROOM,
    R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT,
    R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT,
    R351_CULEXS_ROOM,
    R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS,
    R358_VOLCANO_AREA_11,
    R361_VOLCANO_AREA_09,
    R366_VOLCANO_AREA_13_WSAVE_POINT,
    R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP,
    R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND,
    R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD,
    R378_BEAN_VALLEY_BEANSTALKS_AREA_01,
    R379_BEAN_VALLEY_BEANSTALKS_AREA_02,
    R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02,
    R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
    R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES,
    R384_VOLCANO_AREA_05,
    R385_VOLCANO_AREA_06,
    R397_MONSTRO_TOWN_SUPERJUMPING_ROOM,
    R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN,
    R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
    R405_BOOSTER_PASS_SECRET,
    R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
    R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS,
    R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
    R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR,
    R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE,
    R419_LAZY_SHELL_CLOUD,
    R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
    R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
    R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
    R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
    R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
    R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
    R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
    R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM,
    R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
    R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
    R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
    R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
    R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
    R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
    R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
    R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
    R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
    R493_MUSHROOM_KINGDOM_INN_1F,
    R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
    R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
    R500_NIMBUS_CASTLE_AREA_04_____DUMMY,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0227_FREESTANDING_15_GRANT,
    E0228_FREESTANDING_14_GRANT,
    E0229_FREESTANDING_13_GRANT,
    E0230_FREESTANDING_12_GRANT,
    E0231_FREESTANDING_11_GRANT,
    E0232_FREESTANDING_10_GRANT,
    E0233_FREESTANDING_9_GRANT,
    E0234_FREESTANDING_8_GRANT,
    E0235_FREESTANDING_7_GRANT,
    E0236_FREESTANDING_6_GRANT,
    E0237_FREESTANDING_5_GRANT,
    E0238_FREESTANDING_4_GRANT,
    E0239_FREESTANDING_3_GRANT,
    E0240_FREESTANDING_2_GRANT,
    E0241_FREESTANDING_1_GRANT,
    E0242_CHEST_6_GRANT,
    E0243_CHEST_5_GRANT,
    E0244_CHEST_4_GRANT,
    E0245_CHEST_3_GRANT,
    E0246_CHEST_2_GRANT,
    E0247_CHEST_1_GRANT,
    E0248_NPC_QUEST_6_GRANT,
    E0249_NPC_QUEST_5_GRANT,
    E0250_NPC_QUEST_4_GRANT,
    E0251_NPC_QUEST_3_GRANT,
    E0252_NPC_QUEST_2_GRANT,
    E0253_NPC_QUEST_1_GRANT,
    E3383_SHIP_TRAMPOLINE_PRIZE_PACKET_GRANT,
    E3384_SHIP_TROOPA_PRIZE_PACKET_GRANT,
    E3385_SHIP_UPPER_STAIRWAY_ITEM_PACKET_GRANT,
    E3386_SHIP_3D_MAZE_SPAWN_PRIZE,
    E3387_SHIP_CANNONBALL_PUZZLE_SPAWN_PRIZE,
    E3389_SHIP_BARREL_PUZZLE_SPAWN_PRIZE,
    E3412_MINES_SHYGUY_ITEM_CREATE_PACKET,
)
from randomizer.types.overworld_scripts.action_scripts.ids import (
    A0043_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH,
    A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH,
)
from randomizer.types.overworld_scripts.ids.room_names import R101_BOOSTER_PASS_AREA_02
from randomizer.types.progress_locations import (
    ChestLocationAllowSlots,
    EarlygameChestLocation,
    FrogDiscipleShopItem,
    Inventory,
    MidasRiverTunnelItem,
    MidgameChestLocation,
    GrantLocation,
    FreestandingLocation,
    MimicReloadRewardChest,
    PacketItem,
    StartingItemGrant,
    TreasureShopItem,
    PacketType,
)
from randomizer.types.progress_locations.classes import ChestLocationAllowCoins
from randomizer.types.world import GameWorld, ItemPlacementError
from randomizer.types.world.flags import (
    AvailableSpells,
    BowserDoorRequirements,
    BowserDoorShuffle,
    BucketWarp,
    FireworksSetting,
    ShuffleWeddingGear,
    FireworksOptions,
    ShuffleLocationSelector,
)
from randomizer.types.world.flags.enums import MonstroTownGating, PipeVaultGating
from randomizer.types.world.flags.flags import (
    MonstroTownGate,
    PipeVaultGate,
    RestrictSpecialEquips,
    SuperJump1Threshold,
)

from .helpers.area_access import (
    can_access_forest,
    can_access_tower,
    can_defeat_balcony_boss,
    can_defeat_battle_door_boss,
    can_defeat_chapel_boss,
    can_defeat_first_mimic,
    can_defeat_forest_boss,
    can_defeat_fourth_dojo_boss,
    can_defeat_inner_factory_first_boss,
    can_defeat_mushroom_kingdom_boss,
    can_defeat_mushroom_way_boss,
    can_defeat_nimbus_boss,
    can_defeat_post_obstacle_boss,
    can_defeat_sealed_door_boss,
    can_defeat_seaside_boss,
    can_defeat_second_mimic,
    can_defeat_second_moleville_boss,
    can_defeat_temple_boss,
    can_defeat_valley_boss,
)
from .helpers.classes import (
    BanditsWayLocation,
    BeanValleyLocation,
    BoosterPassLocation,
    BoosterTowerLocation,
    BowsersKeepObstacleLocation,
    CasinoLocation,
    ForestLocation,
    InnerMinesLocation,
    InnerSunkenShipLocation,
    InnerTempleLocation,
    KeroSewersLocation,
    LandsEndLocation,
    MariosPadLocation,
    MarrymoreChapelLocation,
    MarrymoreLocation,
    MidasRiverLocation,
    MinesLocation,
    MolevilleLocation,
    MonstroTownLocation,
    NimbusTownLocation,
    NimbusCastleLocation,
    NimbusMidCastleLocation,
    NimbusDeepCastleLocation,
    BarrelVolcanoLocation,
    BowsersKeepLocation,
    OuterFactoryLocation,
    MidFactoryLocation,
    InnerFactoryLocation,
    MushroomKingdomLocation,
    MushroomKingdomOccupiedLocation,
    MushroomWayLocation,
    PipeVaultLocation,
    RoseTownLocation,
    RoseWayLocation,
    SeaLocation,
    SeasideTownLocation,
    SunkenShipLocation,
    TadpolePondLocation,
    TempleLocation,
    TreasuryLocation,
    YosterIsleLocation,
)

# *** Marios Pad


def _restrict_best_monstro_item(world: Optional[GameWorld], item: Item) -> bool:
    if world is None:
        return False
    if not world.settings.is_boolean_flag_enabled(RestrictSpecialEquips):
        return False
    equips = [
        world.get_item_instance(FroggieStick),
        world.get_item_instance(Chomp),
        world.get_item_instance(ZoomShoes),
        world.get_item_instance(LazyShellArmor),
        world.get_item_instance(LazyShellWeapon),
        world.get_item_instance(JinxBelt),
        world.get_item_instance(QuartzCharm),
        world.get_item_instance(AttackScarf),
        world.get_item_instance(SuperSuit),
        world.get_item_instance(GhostMedal),
    ]
    equips.sort(key=lambda x: x.rank_value, reverse=True)
    if equips[0] == item:
        return random() > 0.7
    return False


class StartingItem1(StartingItemGrant, MariosPadLocation):
    """StartingItem1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_1
    _original_item: Type[Item] = Mushroom
    _room_ids: List[int] = [R189_MARIOS_PIPEHOUSE]
    _container_event: int = E0252_NPC_QUEST_2_GRANT


class StartingItem2(StartingItemGrant, MariosPadLocation):
    """StartingItem2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_2
    _original_item: Type[Item] = Mushroom
    _room_ids: List[int] = [R189_MARIOS_PIPEHOUSE]
    _container_event: int = E0251_NPC_QUEST_3_GRANT


class StartingItem3(StartingItemGrant, MariosPadLocation):
    """StartingItem3 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_3
    _original_item: Type[Item] = Mushroom
    _room_ids: List[int] = [R189_MARIOS_PIPEHOUSE]
    _container_event: int = E0250_NPC_QUEST_4_GRANT


class StartingItem4(StartingItemGrant, MariosPadLocation):
    """StartingItem4 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4
    _original_item: Type[Item] = Mushroom
    _room_ids: List[int] = [R189_MARIOS_PIPEHOUSE]
    _container_event: int = E0249_NPC_QUEST_5_GRANT


# *** Mushroom Way


class MushroomWayRoom1Lower(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomWayLocation
):
    """MushroomWayRoom1Lower progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_WAY_1
    _original_item: Type[Item] = Coins5
    _room_ids: List[int] = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class MushroomWayRoom1Upper(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomWayLocation
):
    """MushroomWayRoom1Upper progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_WAY_2
    _original_item: Type[Item] = Coins8
    _room_ids: List[int] = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class MushroomWayToadRescueFirstRoom(GrantLocation, MushroomWayLocation):
    """MushroomWayToadRescueFirstRoom progress location class"""

    _original_item: Type[Item] = HoneySyrup
    _room_ids: List[int] = [R203_MUSHROOM_WAY_AREA_01]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class MushroomWayLedge(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomWayLocation
):
    """MushroomWayLedge progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_WAY_3
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class MushroomWayToadRescueSecondRoom(GrantLocation, MushroomWayLocation):
    """MushroomWayToadRescueSecondRoom progress location class"""

    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R204_MUSHROOM_WAY_AREA_02]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class MushroomWayRightGoomba(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomWayLocation
):
    """MushroomWayRightGoomba progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_WAY_4
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class MushroomWayBossReward(GrantLocation, MushroomWayLocation):
    """MushroomWayBossReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.HAMMER_BROS_REWARD
    _original_item: Type[Item] = Hammer
    _room_ids: List[int] = [R205_MUSHROOM_WAY_AREA_03]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_mushroom_way_boss(self.world, inventory)


# *** Liberated Mushroom Kingdom


class MushroomKingdomCastleMainHall(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomCastleMainHall progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_HALLWAY
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
        R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
    ]
    _npc_ids: List[int] = [2, 6]
    _container_event: int = E0247_CHEST_1_GRANT


class MushroomKingdomCastleVaultLeft(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomCastleVaultLeft progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R031_MUSHROOM_KINGDOM_CASTLE_VAULT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class MushroomKingdomCastleVaultRight(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomCastleVaultRight progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_2
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R031_MUSHROOM_KINGDOM_CASTLE_VAULT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class MushroomKingdomCastleVaultMiddle(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomCastleVaultMiddle progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_3
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R031_MUSHROOM_KINGDOM_CASTLE_VAULT]
    _npc_ids: List[int] = [2]
    _container_event: int = E0245_CHEST_3_GRANT


class MushroomKingdomStoreBasementCenter(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomStoreBasementCenter progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class MushroomKingdomStoreBasementStairs(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomLocation
):
    """MushroomKingdomStoreBasementStairs progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class MushroomKingdomPeachsChair(GrantLocation, MushroomKingdomLocation):
    """MushroomKingdomPeachsChair progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PEACH_SURPRISE
    _original_item: Type[Item] = Mushroom
    _room_ids: List[int] = [
        R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class MushroomKingdomFreeShopItem(GrantLocation, MushroomKingdomLocation):
    """MushroomKingdomFreeShopItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE
    _original_item: Type[Item] = PickMeUp
    _room_ids: List[int] = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


# *** Bandit's Way


class BanditsWayFlowerJump(
    ChestLocationAllowSlots, EarlygameChestLocation, BanditsWayLocation
):
    """BanditsWayFlowerJump progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_1
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R207_BANDITS_WAY_AREA_02]
    _npc_ids: List[int] = [9]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BanditsWayCoin1(FreestandingLocation, BanditsWayLocation):
    """BanditsWayCoin1 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R207_BANDITS_WAY_AREA_02]
    _npc_ids: List[int] = [3]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class BanditsWayCoin2(FreestandingLocation, BanditsWayLocation):
    """BanditsWayCoin2 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R207_BANDITS_WAY_AREA_02]
    _npc_ids: List[int] = [4]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class BanditsWayCoin3(FreestandingLocation, BanditsWayLocation):
    """BanditsWayCoin3 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R207_BANDITS_WAY_AREA_02]
    _npc_ids: List[int] = [5]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class BanditsWayDogChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BanditsWayLocation
):
    """BanditsWayDogChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_2
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R077_BANDITS_WAY_AREA_03]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BanditsWayPlatformsLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BanditsWayLocation
):
    """BanditsWayPlatformsLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_STAR_CHEST
    _original_item: Type[Item] = BanditsWayStar
    _room_ids: List[int] = [R078_BANDITS_WAY_AREA_04]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class BanditsWayPlatformsRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BanditsWayLocation
):
    """BanditsWayPlatformsRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_DOG_JUMP
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R078_BANDITS_WAY_AREA_04]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class BanditsWayDeadEndChest(EarlygameChestLocation, BanditsWayLocation):
    """BanditsWayDeadEndChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_CROCO
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R206_BANDITS_WAY_AREA_05]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BanditsWayBossFirstItemDrop(GrantLocation, BanditsWayLocation):
    """BanditsWayBossFirstItemDrop progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_1_REWARD
    _original_item: Type[Item] = RareFrogCoin
    _room_ids: List[int] = [R206_BANDITS_WAY_AREA_05]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class BanditsWayBossSecondItemDrop(GrantLocation, BanditsWayLocation):
    """BanditsWayBossSecondItemDrop progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_1_REWARD_2
    _original_item: Type[Item] = Wallet
    _room_ids: List[int] = [R206_BANDITS_WAY_AREA_05]
    _container_event: int = E0252_NPC_QUEST_2_GRANT


# *** Occupied Mushroom Kingdom


class MushroomKingdomOccupiedVaultLeft(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedVaultLeft progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedVaultRight(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedVaultRight progress location class"""

    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedVaultMiddle(
    ChestLocationAllowSlots, EarlygameChestLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedVaultMiddle progress location class"""

    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT]
    _npc_ids: List[int] = [2]
    _container_event: int = E0245_CHEST_3_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedOutdoorGuard(
    GrantLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedOutdoorGuard progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class MushroomKingdomWalletGuyFirstReward(
    GrantLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomWalletGuyFirstReward progress location class"""

    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _missable: bool = True


class MushroomKingdomWalletGuySecondReward(
    GrantLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomWalletGuySecondReward progress location class"""

    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _container_event: int = E0251_NPC_QUEST_3_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedCastleToadRescue(
    GrantLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedCastleToadRescue progress location class"""

    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedFamilyRescue(
    GrantLocation, MushroomKingdomOccupiedLocation
):
    """MushroomKingdomOccupiedFamilyRescue progress location class"""

    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [
        R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
        R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class MushroomKingdomOccupiedGuestRoom(GrantLocation, MushroomKingdomOccupiedLocation):
    """MushroomKingdomOccupiedGuestRoom progress location class"""

    _original_item: Type[Item] = WakeUpPin
    _room_ids: List[int] = [R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class MushroomKingdomStoreExchange(GrantLocation, MushroomKingdomLocation):
    """MushroomKingdomStoreExchange progress location class"""

    _original_item: Type[Item] = CricketPie
    _room_ids: List[int] = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE
    )
    _container_event: int = E0252_NPC_QUEST_2_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_mushroom_kingdom_boss(
            self.world, inventory
        ) and inventory.has_item(RareFrogCoin)


class MushroomKingdomInnPurchase(GrantLocation, MushroomKingdomLocation):
    """MushroomKingdomInnPurchase progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN
    _original_item: Type[Item] = Beetlemania
    _room_ids: List[int] = [
        R493_MUSHROOM_KINGDOM_INN_1F,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_mushroom_kingdom_boss(self.world, inventory)


# *** Kero Sewers


class KeroSewersStairRoomLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersStairRoomLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.KERO_SEWERS_PANDORITE_ROOM
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class KeroSewersStairRoomRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersStairRoomRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PANDORITE_CHEST
    _original_item: Type[Item] = MimicFightInitiator1
    _room_ids: List[int] = [
        R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class Mimic1DropReward(GrantLocation):
    """Mimic1DropReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PANDORITE_REWARD_1
    _original_item: Type[Item] = TrueformPin
    _identifier: int = 512
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_first_mimic(self.world, inventory)


class Mimic1ReloadReward(EarlygameChestLocation, MimicReloadRewardChest):
    """Mimic1ReloadReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PANDORITE_REWARD_2
    _original_item: Type[Item] = Coins50
    _identifier: int = 512
    _container_event: int = E0245_CHEST_3_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_access(self, inventory: Inventory):
        return can_defeat_first_mimic(self.world, inventory)

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if isinstance(item, (MimicFightChestAssignment, InfiniteCoins)):
            return False
        chest = next(
            (
                loc
                for loc in self.world.item_locations
                if loc.does_contain(MimicFightInitiator1)
            ),
            None,
        )
        if chest is None:
            return False
        return chest.can_accept(item)

    def set_contents(self, contents: Optional[Item]) -> None:
        chest = next(
            (
                loc
                for loc in self.world.item_locations
                if loc.does_contain(MimicFightInitiator1)
            ),
            None,
        )
        if chest is None:
            raise ItemPlacementError(
                "how are we setting contents on a reload reward that can't be accessed yet?"
            )
        self.set_room_ids(chest.room_ids)
        super().set_contents(contents)


class KeroSewersFourRatRoomChest(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersFourRatRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST
    _original_item: Type[Item] = KeroSewersStar
    _room_ids: List[int] = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class KeroSewersBeforeBelomeLower(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersBeforeBelomeLower progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_LOWER
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class KeroSewersBeforeBelomeUpperBeforeFlip(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersBeforeBelomeUpperBeforeFlip progress location class"""

    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT
    _missable: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class KeroSewersBeforeBelomeUpperAfterFlip(
    ChestLocationAllowSlots, EarlygameChestLocation, KeroSewersLocation
):
    """KeroSewersBeforeBelomeUpperAfterFlip progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_2
    )
    _original_item: Type[Item] = CricketJam
    _room_ids: List[int] = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids: List[int] = [1]
    _container_event: int = E0245_CHEST_3_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Midas River


class MidasRiverFirstCompletionReward(GrantLocation, MidasRiverLocation):
    """MidasRiverFirstCompletionReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MIDAS_RIVER_FIRST_TIME
    _original_item: Type[Item] = NokNokShell
    _room_ids: List[int] = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class MidasRiverBottomLeftCave(MidasRiverTunnelItem, MidasRiverLocation):
    """MidasRiverBottomLeftCave progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_LEFT_CAVE
    )
    _original_item: Type[Item] = FrogCoin
    _midas_action_script: int = A0043_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH
    _room_ids: List[int] = [R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT]
    _container_event: int = 241
    _npc_ids: List[int] = [1]


class MidasRiverBottomRightCave(MidasRiverTunnelItem, MidasRiverLocation):
    """MidasRiverBottomRightCave progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_RIGHT_CAVE
    )
    _original_item: Type[Item] = Flower
    _midas_action_script: int = A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH
    _room_ids: List[int] = [R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT]
    _container_event: int = 241
    _npc_ids: List[int] = [4]


# *** Tadpole Pond


class TadpolePondCricketPieExchange(GrantLocation, TadpolePondLocation):
    """TadpolePondCricketPieExchange progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CRICKET_PIE_REWARD
    _original_item: Type[Item] = FroggieStick
    _room_ids: List[int] = [R075_TADPOLE_POND_AREA_01]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )

    def can_access(self, inventory: Inventory):
        return inventory.has_item(CricketPie)


class TadpolePondCricketJamExchange(GrantLocation, TadpolePondLocation):
    """TadpolePondCricketJamExchange progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CRICKET_JAM_REWARD
    _original_item: Type[Item] = FrogCoins10
    _room_ids: List[int] = [R075_TADPOLE_POND_AREA_01]
    _container_event: int = E0252_NPC_QUEST_2_GRANT

    def can_access(self, inventory: Inventory):
        return inventory.has_item(CricketPie) and inventory.has_item(CricketJam)


class MelodyBayFirstReward(GrantLocation, TadpolePondLocation):
    """MelodyBayFirstReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MELODY_BAY_1
    _original_item: Type[Item] = ProgressiveCard
    _room_ids: List[int] = [R074_TADPOLE_POND_AREA_02]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class MelodyBaySecondReward(GrantLocation, TadpolePondLocation):
    """MelodyBaySecondReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MELODY_BAY_2
    _original_item: Type[Item] = ProgressiveCard
    _room_ids: List[int] = [R074_TADPOLE_POND_AREA_02]
    _container_event: int = E0252_NPC_QUEST_2_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_second_moleville_boss(self.world, inventory)


class MelodyBayThirdReward(GrantLocation, TadpolePondLocation):
    """MelodyBayThirdReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MELODY_BAY_3
    _original_item: Type[Item] = ProgressiveCard
    _room_ids: List[int] = [R074_TADPOLE_POND_AREA_02]
    _container_event: int = E0251_NPC_QUEST_3_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_second_moleville_boss(
            self.world, inventory
        ) and can_defeat_temple_boss(self.world, inventory)


# *** Rose Way


class RoseWaySwingingPlatformRoom(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWaySwingingPlatformRoom progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_PLATFORM
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class RoseWayLeftIsland(FreestandingLocation, RoseWayLocation):
    """RoseWayLeftIsland progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FLOWER
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [7]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class RoseWayMiddleIsland(FreestandingLocation, RoseWayLocation):
    """RoseWayMiddleIsland progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_MUSHROOM
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [8]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class RoseWayCoin1(FreestandingLocation, RoseWayLocation):
    """RoseWayCoin1 progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [17]
    _container_event: int = E0235_FREESTANDING_7_GRANT


class RoseWayCoin2(FreestandingLocation, RoseWayLocation):
    """RoseWayCoin2 progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [18]
    _container_event: int = E0236_FREESTANDING_6_GRANT


class RoseWayCoin3(FreestandingLocation, RoseWayLocation):
    """RoseWayCoin3 progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [19]
    _container_event: int = E0237_FREESTANDING_5_GRANT


class RoseWayCoin4(FreestandingLocation, RoseWayLocation):
    """RoseWayCoin4 progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [20]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class RoseWayCoin5(FreestandingLocation, RoseWayLocation):
    """RoseWayCoin5 progress location class"""

    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids: List[int] = [21]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class RoseWayFiveChestRoomTop(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWayFiveChestRoomTop progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_1
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class RoseWayFiveChestRoomBottomLeft(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWayFiveChestRoomBottomLeft progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2
    _original_item: Type[Item] = Coins5
    _room_ids: List[int] = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class RoseWayFiveChestRoomRight(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWayFiveChestRoomRight progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3
    _original_item: Type[Item] = Coins5
    _room_ids: List[int] = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids: List[int] = [2]
    _container_event: int = E0245_CHEST_3_GRANT


class RoseWayFiveChestRoomLeft(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWayFiveChestRoomLeft progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_4
    _original_item: Type[Item] = Coins5
    _room_ids: List[int] = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids: List[int] = [3]
    _container_event: int = E0244_CHEST_4_GRANT


class RoseWayFiveChestRoomBottomRight(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseWayLocation
):
    """RoseWayFiveChestRoomBottomRight progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_5
    _original_item: Type[Item] = Coins5
    _room_ids: List[int] = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids: List[int] = [4]
    _container_event: int = E0243_CHEST_5_GRANT


# *** Rose Town


class RoseTownShopLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownShopLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_TOWN_STORE_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids: List[int] = [4]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class RoseTownShopRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownShopRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_TOWN_STORE_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids: List[int] = [5]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 2


class RoseTownCloudRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownCloudRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.GARDENER_CLOUD_1
    _original_item: Type[Item] = LazyShellArmor
    _room_ids: List[int] = [R419_LAZY_SHELL_CLOUD]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return (
            inventory.has_item(Seed)
            and inventory.has_item(Fertilizer)
            and can_defeat_forest_boss(self.world, inventory)
            and can_defeat_chapel_boss(self.world, inventory)
        )

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )


class RoseTownCloudLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownCloudLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.GARDENER_CLOUD_2
    _original_item: Type[Item] = LazyShellWeapon
    _room_ids: List[int] = [R419_LAZY_SHELL_CLOUD]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_access(self, inventory: Inventory):
        return (
            inventory.has_item(Seed)
            and inventory.has_item(Fertilizer)
            and can_defeat_forest_boss(self.world, inventory)
            and can_defeat_chapel_boss(self.world, inventory)
        )

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )


class RoseTownInnToadPrize(GrantLocation, RoseTownLocation):
    """RoseTownInnToadPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_TOWN_TOAD
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [
        R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
        R096_ROSE_TOWN_INN_2F,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class RoseTownInnGazPrize(GrantLocation, RoseTownLocation):
    """RoseTownInnGazPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.GAZ
    _original_item: Type[Item] = FingerShot
    _room_ids: List[int] = [R086_ROSE_TOWN_INN_1F]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_forest_boss(self.world, inventory)


class RoseTownTreasureHouseLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownTreasureHouseLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class RoseTownTreasureHouseRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownTreasureHouseRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids: List[int] = [1, 1]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 2


class RoseTownTreasureHouseMazeReward(GrantLocation, RoseTownLocation):
    """RoseTownTreasureHouseMazeReward progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_access_forest(self.world, inventory)


class RoseTownTreasureHouseUpperChest(
    ChestLocationAllowSlots, EarlygameChestLocation, RoseTownLocation
):
    """RoseTownTreasureHouseUpperChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    ]
    _npc_ids: List[int] = [1, 1]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2

    # flowers do weird things in this room
    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return (not isinstance(item, Flower)) and super().can_accept(item, inventory)


# *** Forest Maze


class ForestMazeFirstRoom(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeFirstRoom progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_1
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R224_FOREST_MAZE_AREA_01]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeFirstUndergroundExit(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeFirstUndergroundExit progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R228_FOREST_MAZE_AREA_04]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeUndergroundWigglerChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeUndergroundWigglerChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_1
    )
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeUndergroundBottomRightTrunkChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeUndergroundBottomRightTrunkChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids: List[int] = [3]
    _container_event: int = E0246_CHEST_2_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeUndergroundMiddleLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeUndergroundMiddleLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_3
    )
    _original_item: Type[Item] = YouMissed
    _room_ids: List[int] = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids: List[int] = [4]
    _container_event: int = E0245_CHEST_3_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeInnerMazeEntrance(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeInnerMazeEntrance progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FOREST_MAZE_RED_ESSENCE
    )
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    _npc_ids: List[int] = [4]
    _container_event: int = E0247_CHEST_1_GRANT


class ForestMazeSecretTopRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeSecretTopRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_SECRET_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R234_FOREST_MAZE_SECRET]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeSecretBottomRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeSecretBottomRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_SECRET_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R234_FOREST_MAZE_SECRET]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeSecretTopMiddleChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeSecretTopMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_SECRET_3
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R234_FOREST_MAZE_SECRET]
    _npc_ids: List[int] = [3]
    _container_event: int = E0245_CHEST_3_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeSecretBottomMiddleChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeSecretBottomMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_SECRET_4
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R234_FOREST_MAZE_SECRET]
    _npc_ids: List[int] = [4]
    _container_event: int = E0244_CHEST_4_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ForestMazeSecretLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, ForestLocation
):
    """ForestMazeSecretLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_SECRET_5
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R234_FOREST_MAZE_SECRET]
    _npc_ids: List[int] = [5]
    _container_event: int = E0243_CHEST_5_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Pipe Vault


class PipeVaultSlidingCoinRoomBackChest(
    ChestLocationAllowSlots, EarlygameChestLocation, PipeVaultLocation
):
    """PipeVaultSlidingCoinRoomBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PIPE_VAULT_SLIDE_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [8]
    _container_event: int = E0245_CHEST_3_GRANT


class PipeVaultSlidingCoinRoomMiddleChest(
    ChestLocationAllowSlots, EarlygameChestLocation, PipeVaultLocation
):
    """PipeVaultSlidingCoinRoomMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [9]
    _container_event: int = E0246_CHEST_2_GRANT


class PipeVaultSlidingCoinRoomFrontChest(
    ChestLocationAllowSlots, EarlygameChestLocation, PipeVaultLocation
):
    """PipeVaultSlidingCoinRoomFrontChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PIPE_VAULT_SLIDE_3
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [10]
    _container_event: int = E0247_CHEST_1_GRANT


class PipeVaultSlidingCoinRoomCoin1(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCoin1 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [0]
    _container_event: int = E0237_FREESTANDING_5_GRANT


class PipeVaultSlidingCoinRoomCoin2(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCoin2 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [1]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class PipeVaultSlidingCoinRoomCoin3(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCoin3 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [2]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class PipeVaultSlidingCoinRoomCoin4(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCoin4 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [3]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class PipeVaultSlidingCoinRoomCoin5(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCoin5 progress location class"""

    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [4]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class PipeVaultSlidingCoinRoomCrouchItem(FreestandingLocation, PipeVaultLocation):
    """PipeVaultSlidingCoinRoomCrouchItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.PIPE_VAULT_SLIDE_FROG_COIN
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids: List[int] = [5]
    _container_event: int = E0236_FREESTANDING_6_GRANT


class PipeVaultGoombaThumpinFirstPrize(GrantLocation, PipeVaultLocation):
    """PipeVaultGoombaThumpinFirstPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.GOOMBA_THUMPING_1
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class PipeVaultGoombaThumpinSecondPrize(GrantLocation, PipeVaultLocation):
    """PipeVaultGoombaThumpinSecondPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.GOOMBA_THUMPING_2
    _original_item: Type[Item] = FlowerJar
    _room_ids: List[int] = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _container_event: int = E0252_NPC_QUEST_2_GRANT


class PipeVaultRisingPlatformChest(
    ChestLocationAllowSlots, EarlygameChestLocation, PipeVaultLocation
):
    """PipeVaultRisingPlatformChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class PipeVaultChompweedChest(
    ChestLocationAllowSlots, EarlygameChestLocation, PipeVaultLocation
):
    """PipeVaultChompweedChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_2
    _original_item: Type[Item] = Coins20
    _room_ids: List[int] = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


# *** Yo'ster Isle
class YosterEntranceChest(
    ChestLocationAllowSlots, EarlygameChestLocation, YosterIsleLocation
):
    """YosterEntranceChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.YOSTER_ISLE_ENTRANCE
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.OPEN):
            return 2
        return 4


class YosterRacePrize1(GrantLocation, YosterIsleLocation):
    """YosterRacePrize1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_1
    )
    _original_item: Type[Item] = YoshiCookie
    _room_ids: List[int] = [R034_YOSTER_ISLE]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class YosterRacePrize2(GrantLocation, YosterIsleLocation):
    """YosterRacePrize2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2
    )
    _original_item: Type[Item] = YoshiCookie
    _room_ids: List[int] = [R034_YOSTER_ISLE]
    _container_event: int = E0251_NPC_QUEST_3_GRANT


class YosterRacePrize3(GrantLocation, YosterIsleLocation):
    """YosterRacePrize3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_3
    )
    _original_item: Type[Item] = YoshiCookie
    _room_ids: List[int] = [R034_YOSTER_ISLE]
    _container_event: int = E0250_NPC_QUEST_4_GRANT


# *** Moleville Town


class BucketGirlReward(GrantLocation, MolevilleLocation):
    """BucketGirlReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BUCKET_GIRL
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R108_MOLEVILLE_OUTSIDE]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def __init__(self, world: GameWorld):
        if world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        ) or not self.world.settings.is_boolean_flag_enabled(BucketWarp):
            # set this so it's ignored in the shuffler
            self.set_excluded(True)
            self.set_contents(FrogCoin(world))
        super().__init__(world)

    def can_access(self, inventory: Inventory):
        if not self.world.settings.is_boolean_flag_enabled(BucketWarp):
            return False
        if self.world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        ):
            return False
        fireworks_access = can_defeat_second_moleville_boss(self.world, inventory)
        if self.world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.SHUFFLE_ONE
        ):
            fireworks_access &= inventory.has_item(Fireworks)
        elif self.world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.PROGRESSIVE
        ):
            fireworks_access &= inventory.has_item_count(ProgressiveFireworks, 3)
        return fireworks_access


class TreasureShopItem1(TreasureShopItem, MolevilleLocation):
    """TreasureShopItem1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.TREASURE_SELLER_1
    _original_item: Type[Item] = LuckyJewel
    _room_ids: List[int] = [R336_MOLEVILLE_ITEM_SHOP]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _affected_dialog_ids: List[int] = [DI2911_TREASURE_SELLER_ITEM_1]


class TreasureShopItem2(TreasureShopItem, MolevilleLocation):
    """TreasureShopItem2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.TREASURE_SELLER_2
    _original_item: Type[Item] = ProgressiveEgg
    _room_ids: List[int] = [R336_MOLEVILLE_ITEM_SHOP]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _affected_dialog_ids: List[int] = [DI2908_TREASURE_SELLER_ITEM_2]


class TreasureShopItem3(TreasureShopItem, MolevilleLocation):
    """TreasureShopItem3 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.TREASURE_SELLER_3
    _original_item: Type[Item] = FryingPan
    _room_ids: List[int] = [R336_MOLEVILLE_ITEM_SHOP]
    _container_event: int = E0251_NPC_QUEST_3_GRANT
    _affected_dialog_ids: List[int] = [DI2914_TREASURE_SELLER_ITEM_3]


class FireworksShopItem(GrantLocation, MolevilleLocation):
    """FireworksShopItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FIREWORKS_SHOP
    _original_item: Type[Item] = Fireworks
    _room_ids: List[int] = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    @property
    def key_item_location(self) -> bool:
        return not self.world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        )

    def __init__(self, world: GameWorld):
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.VANILLA):
            # set this so it's ignored in the shuffler
            self.set_excluded(True)
            self.initiate_vanilla()
        super().__init__(world)

    def can_access(self, inventory: Inventory):
        return can_defeat_second_moleville_boss(self.world, inventory)


# *** Moleville Mines
class OuterMinesTrampolineHenchman(GrantLocation, MinesLocation):
    """OuterMinesTrampolineHenchman progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_FLUNKIE_1
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class OuterMinesLeftHenchman(GrantLocation, MinesLocation):
    """OuterMinesLeftHenchman progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_FLUNKIE_2
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class OuterMinesRightHenchman(GrantLocation, MinesLocation):
    """OuterMinesRightHenchman progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_FLUNKIE_3
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class OuterMinesBossPrize(GrantLocation, MinesLocation):
    """OuterMinesBossPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CROCO_2_ITEM
    _original_item: Type[Item] = BambinoBomb
    _identifier: int = 518
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class InnerMinesTracksChest(
    ChestLocationAllowSlots, EarlygameChestLocation, InnerMinesLocation
):
    """InnerMinesTracksChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST
    )
    _original_item: Type[Item] = MolevilleMinesStar
    _room_ids: List[int] = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class InnerMinesShyguyCart(PacketItem, InnerMinesLocation):
    """InnerMinesShyguyCart progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MOLEVILLE_MINES_SHY_GUY
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM
    ]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3412_MINES_SHYGUY_ITEM_CREATE_PACKET


class InnerMinesBoxesChest(
    ChestLocationAllowSlots, EarlygameChestLocation, InnerMinesLocation
):
    """InnerMinesBoxesChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MOLEVILLE_MINES_COINS
    _original_item: Type[Item] = Coins150
    _room_ids: List[int] = [
        R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class InnerMinesSaveBlockChest(
    ChestLocationAllowSlots, EarlygameChestLocation, InnerMinesLocation
):
    """InnerMinesSaveBlockChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_1
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class InnerMinesHighUpChest(
    ChestLocationAllowSlots, EarlygameChestLocation, InnerMinesLocation
):
    """InnerMinesHighUpChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Booster Pass


class BoosterPassBush(GrantLocation, BoosterPassLocation):
    """BoosterPassBush progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_BUSH
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R100_BOOSTER_PASS_AREA_01]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class BoosterPassFirstRoomLeftChest(
    ChestLocationAllowCoins, EarlygameChestLocation, BoosterPassLocation
):
    """BoosterPassFirstRoomLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids: List[int] = [8]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class BoosterPassFirstRoomRightChest(
    ChestLocationAllowCoins, EarlygameChestLocation, BoosterPassLocation
):
    """BoosterPassFirstRoomRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_2
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids: List[int] = [9]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 2


class BoosterPassSecondRoomFlower(FreestandingLocation, BoosterPassLocation):
    """BoosterPassSecondRoomFlower progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_FLOWER
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids: List[int] = [6]
    _container_event: int = E0239_FREESTANDING_3_GRANT
    _tier: int = 2


class BoosterPassSecretMiddleChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BoosterPassLocation
):
    """BoosterPassSecretMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_SECRET_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R405_BOOSTER_PASS_SECRET]
    _npc_ids: List[int] = [10]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_access_tower(self.world, inventory)


class BoosterPassSecretRightChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BoosterPassLocation
):
    """BoosterPassSecretRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_SECRET_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R405_BOOSTER_PASS_SECRET]
    _npc_ids: List[int] = [11]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_access(self, inventory: Inventory):
        return can_access_tower(self.world, inventory)


class BoosterPassSecretLeftChest(
    ChestLocationAllowSlots, EarlygameChestLocation, BoosterPassLocation
):
    """BoosterPassSecretLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_PASS_SECRET_3
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R405_BOOSTER_PASS_SECRET]
    _npc_ids: List[int] = [12]
    _container_event: int = E0245_CHEST_3_GRANT

    def can_access(self, inventory: Inventory):
        return can_access_tower(self.world, inventory)


# *** Booster Tower


class BoosterTowerSpookumStairs(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerSpookumStairs progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_SPOOKUM
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT


class BoosterTowerTrainRoomCrevice(GrantLocation, BoosterTowerLocation):
    """BoosterTowerTrainRoomCrevice progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_RAILWAY
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class BoosterTowerChestNearThwomp(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerChestNearThwomp progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_THWOMP
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER
    ]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BoosterTowerFallingChest(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerFallingChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_MASHER
    _original_item: Type[Item] = Masher
    _room_ids: List[int] = [
        R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER
    ]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _npc_ids: List[int] = [3]
    _keep_original_item_if_excluded: bool = False

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and item.npc_event > 0

    # this looks like a chest, requires an overworld item, but acts like a npc reward

    @property
    def tier(self) -> int:
        return 4


class BoosterTowerKnifeGuyPrize(GrantLocation, BoosterTowerLocation):
    """BoosterTowerKnifeGuyPrize progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    )
    _original_item: Type[Item] = BrightCard
    _room_ids: List[int] = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_balcony_boss(self.world, inventory)

    @property
    def tier(self) -> int:
        return 4


class BoosterTowerPortraitPrize(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerPortraitPrize progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_PORTRAITS
    )
    _original_item: Type[Item] = ElderKey
    _room_ids: List[int] = [R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [7]
    _keep_original_item_if_excluded: bool = False


class BoosterTowerElderKeyItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerElderKeyItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP
    _original_item: Type[Item] = Chomp
    _room_ids: List[int] = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [0]
    _keep_original_item_if_excluded: bool = False

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )

    @property
    def tier(self) -> int:
        return 4


class BoosterTowerRightmostItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerRightmostItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY
    _original_item: Type[Item] = RoomKey
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0228_FREESTANDING_14_GRANT
    _npc_ids: List[int] = [5]
    _keep_original_item_if_excluded: bool = False


class BoosterTowerTopItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerTopItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_1
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [0]


class BoosterTowerLeftmostItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerLeftmostItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0240_FREESTANDING_2_GRANT
    _npc_ids: List[int] = [1]


class BoosterTowerUpperRightItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerUpperRightItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0239_FREESTANDING_3_GRANT
    _npc_ids: List[int] = [2]


class BoosterTowerBottomItem(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerBottomItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_4
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0238_FREESTANDING_4_GRANT
    _npc_ids: List[int] = [3]


class BoosterTowerCoin1(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_1
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0237_FREESTANDING_5_GRANT
    _npc_ids: List[int] = [7]


class BoosterTowerCoin2(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_2
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0236_FREESTANDING_6_GRANT
    _npc_ids: List[int] = [8]


class BoosterTowerCoin3(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_3
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0235_FREESTANDING_7_GRANT
    _npc_ids: List[int] = [9]


class BoosterTowerCoin4(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin4 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_4
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0234_FREESTANDING_8_GRANT
    _npc_ids: List[int] = [10]


class BoosterTowerCoin5(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin5 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_5
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0233_FREESTANDING_9_GRANT
    _npc_ids: List[int] = [11]


class BoosterTowerCoin6(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin6 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_6
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0232_FREESTANDING_10_GRANT
    _npc_ids: List[int] = [12]


class BoosterTowerCoin7(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin7 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_7
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0231_FREESTANDING_11_GRANT
    _npc_ids: List[int] = [13]


class BoosterTowerCoin8(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin8 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_8
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0230_FREESTANDING_12_GRANT
    _npc_ids: List[int] = [14]


class BoosterTowerCoin9(FreestandingLocation, BoosterTowerLocation):
    """BoosterTowerCoin9 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_COIN_9
    _original_item: Type[Item] = Coins1
    _room_ids: List[int] = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _container_event: int = E0229_FREESTANDING_13_GRANT
    _npc_ids: List[int] = [15]


class BoosterTowerParachuteRoomChest(
    ChestLocationAllowCoins, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerParachuteRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids: List[int] = [9]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BoosterTowerParachuteRoomCrevice(GrantLocation, BoosterTowerLocation):
    """BoosterTowerParachuteRoomCrevice progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE_CREVICE
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class BoosterTowerRoomKeyChest(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerRoomKeyChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES
    )
    _original_item: Type[Item] = ZoomShoes
    _room_ids: List[int] = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return (
            super().can_accept(item, inventory)
            and not isinstance(item, InvincibilityStar)
            and not _restrict_best_monstro_item(self.world, item)
        )

    @property
    def tier(self) -> int:
        return 4


class BoosterTowerTopFloorLowerChest(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerTopFloorLowerChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_TOP_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BoosterTowerTopFloorUpperChest(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerTopFloorUpperChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_TOP_2
    _original_item: Type[Item] = GoodieBag
    _room_ids: List[int] = [
        R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BoosterTowerTopFloorCornerChest(
    ChestLocationAllowSlots, MidgameChestLocation, BoosterTowerLocation
):
    """BoosterTowerTopFloorCornerChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOOSTER_TOWER_TOP_3
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT
    ]
    _npc_ids: List[int] = [9]
    _container_event: int = E0245_CHEST_3_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class BoosterTowerCurtainGamePrize(GrantLocation, BoosterTowerLocation):
    """BoosterTowerCurtainGamePrize progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    )
    _original_item: Type[Item] = Amulet
    _room_ids: List[int] = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True

    @property
    def tier(self) -> int:
        return 4


# *** Marrymore


class MarrymoreFirstSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreFirstSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_1
    _original_item: Type[Item] = FlowerTab
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class MarrymoreSecondSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreSecondSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_2
    _original_item: Type[Item] = FlowerJar
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0252_NPC_QUEST_2_GRANT


class MarrymoreThirdSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreThirdSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_3
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0251_NPC_QUEST_3_GRANT


class MarrymoreFourthSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreFourthSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_4
    _original_item: Type[Item] = FrogCoins2
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0250_NPC_QUEST_4_GRANT


class MarrymoreFifthSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreFifthSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_5
    _original_item: Type[Item] = FrogCoins3
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0249_NPC_QUEST_5_GRANT


class MarrymoreSixthSuitePrize(GrantLocation, MarrymoreLocation):
    """MarrymoreSixthSuitePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_PRIZE_6
    _original_item: Type[Item] = FrogCoins20
    _room_ids: List[int] = [R007_MARRYMORE_INN_1F]
    _container_event: int = E0248_NPC_QUEST_6_GRANT


class MarrymoreHotelChest(
    ChestLocationAllowSlots, MidgameChestLocation, MarrymoreLocation
):
    """MarrymoreHotelChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_INN
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R009_MARRYMORE_INN_REGULAR_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class MarrymoreSnifit1(GrantLocation, MarrymoreChapelLocation):
    """MarrymoreSnifit1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_SNIFIT_1
    _original_item: Type[Item] = Brooch
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _keep_original_item_if_excluded: bool = True

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
            self.set_missable(True)
        else:
            self.set_excluded(True)


class MarrymoreSnifit2(GrantLocation, MarrymoreChapelLocation):
    """MarrymoreSnifit2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_SNIFIT_2
    _original_item: Type[Item] = Ring
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _keep_original_item_if_excluded: bool = True

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
            self.set_missable(True)
        else:
            self.set_excluded(True)


class MarrymoreSnifit3(GrantLocation, MarrymoreChapelLocation):
    """MarrymoreSnifit3 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_SNIFIT_3
    _original_item: Type[Item] = Shoes
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _container_event: int = E0251_NPC_QUEST_3_GRANT
    _keep_original_item_if_excluded: bool = True

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
            self.set_missable(True)
        else:
            self.set_excluded(True)


class MarrymoreAltarHead(FreestandingLocation, MarrymoreChapelLocation):
    """MarrymoreAltarHead progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_ALTAR
    _original_item: Type[Item] = Crown
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [5]

    def __init__(self, world: GameWorld):
        super().__init__(world)
        if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
            self.set_missable(True)
        else:
            self.set_excluded(True)


# *** Seaside Town


class FrogDiscipleItem1(FrogDiscipleShopItem, SeasideTownLocation):
    """FrogDiscipleItem1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FROG_DISCIPLE_1
    _original_item: Type[Item] = SeeYa


class FrogDiscipleItem2(FrogDiscipleShopItem, SeasideTownLocation):
    """FrogDiscipleItem2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FROG_DISCIPLE_2
    _original_item: Type[Item] = EarlierTimes


class FrogDiscipleItem3(FrogDiscipleShopItem, SeasideTownLocation):
    """FrogDiscipleItem3 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FROG_DISCIPLE_3
    _original_item: Type[Item] = ExpBooster


class FrogDiscipleItem4(FrogDiscipleShopItem, SeasideTownLocation):
    """FrogDiscipleItem4 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FROG_DISCIPLE_4
    _original_item: Type[Item] = CoinTrick


class FrogDiscipleItem5(FrogDiscipleShopItem, SeasideTownLocation):
    """FrogDiscipleItem5 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FROG_DISCIPLE_5
    _original_item: Type[Item] = ScroogeRing


class SeasideTownBossPrize(FreestandingLocation, SeasideTownLocation):
    """SeasideTownBossPrize progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE
    )
    _original_item: Type[Item] = ShedKey
    _room_ids: List[int] = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids: List[int] = [0]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _keep_original_item_if_excluded: bool = False

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_seaside_boss(self.world, inventory)


class SeasideTownShedRescue(GrantLocation, SeasideTownLocation):
    """SeasideTownShedRescue progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE
    _original_item: Type[Item] = FlowerBox
    _room_ids: List[int] = [R314_SEASIDE_TOWN_SHED]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_seaside_boss(self.world, inventory) and inventory.has_item(
            ShedKey
        )


# *** Sea


class SeaStarslapRoomChest(ChestLocationAllowSlots, MidgameChestLocation, SeaLocation):
    """SeaStarslapRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEA_STAR_CHEST
    _original_item: Type[Item] = SeaStar
    _room_ids: List[int] = [R134_SEA_AREA_03_SUPER_STAR_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class SeaSaveRoomBackChest(ChestLocationAllowSlots, MidgameChestLocation, SeaLocation):
    """SeaSaveRoomBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEA_SAVE_ROOM_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0245_CHEST_3_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class SeaSaveRoomMiddleChest(
    ChestLocationAllowSlots, MidgameChestLocation, SeaLocation
):
    """SeaSaveRoomMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEA_SAVE_ROOM_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class SeaSaveRoomFrontChest(ChestLocationAllowSlots, MidgameChestLocation, SeaLocation):
    """SeaSaveRoomFrontChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEA_SAVE_ROOM_3
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class SeaWhirlpoolChest(ChestLocationAllowSlots, MidgameChestLocation, SeaLocation):
    """SeaWhirlpoolChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST
    _original_item: Type[Item] = MaxMushroom
    _room_ids: List[int] = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Sunken Ship


class ShipRatStairsChest(
    ChestLocationAllowSlots, MidgameChestLocation, SunkenShipLocation
):
    """ShipRatStairsChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [
        R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class ShipRatStairsBoxes(PacketItem, SunkenShipLocation):
    """ShipRatStairsBoxes progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS_FLOWER
    )
    _room_ids: List[int] = [
        R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS
    ]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3385_SHIP_UPPER_STAIRWAY_ITEM_PACKET_GRANT
    _original_item: Type[Item] = Flower
    _packet_type: PacketType = PacketType.CHEST


class ShipTroopaPuzzle(PacketItem, SunkenShipLocation):
    """ShipTroopaPuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_TROOPA_PUZZLE
    )
    _room_ids: List[int] = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3384_SHIP_TROOPA_PRIZE_PACKET_GRANT
    _original_item: Type[Item] = RecoveryMushroom
    _packet_type: PacketType = PacketType.FALLING


class ShipTrampolinePuzzle(PacketItem, SunkenShipLocation):
    """ShipTrampolinePuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_TRAMPOLINE_PUZZLE
    )
    _room_ids: List[int] = [R163_SUNKEN_SHIP_PUZZLE_ROOM_2]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3383_SHIP_TRAMPOLINE_PRIZE_PACKET_GRANT
    _original_item: Type[Item] = Flower
    _packet_type: PacketType = PacketType.FALLING


class Ship3DMazePuzzle(PacketItem, SunkenShipLocation):
    """Ship3DMazePuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_3D_MAZE
    _room_ids: List[int] = [R168_SUNKEN_SHIP_PUZZLE_ROOM_3]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3386_SHIP_3D_MAZE_SPAWN_PRIZE
    _original_item: Type[Item] = RoyalSyrup
    _packet_type: PacketType = PacketType.FALLING
    _keep_original_item_if_excluded: bool = False

    @property
    def tier(self) -> int:
        return 4


class ShipShopChest(ChestLocationAllowSlots, MidgameChestLocation, SunkenShipLocation):
    """ShipShopChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_SHOP
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [
        R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class ShipCoinSnakePuzzle(GrantLocation, SunkenShipLocation):
    """ShipCoinSnakePuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_COIN_SNAKE
    _room_ids: List[int] = [R171_SUNKEN_SHIP_PUZZLE_ROOM_4]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _original_item: Type[Item] = Coins150
    _keep_original_item_if_excluded: bool = True
    _npc_ids: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    # Needs special considerations for the sound played in 3216
    # and the sequences performed in 3216 and 3215
    # depending on the item


class ShipCannonballPuzzle(PacketItem, SunkenShipLocation):
    """ShipCannonballPuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_CANNONBALL_PUZZLE
    )
    _room_ids: List[int] = [R172_SUNKEN_SHIP_PUZZLE_ROOM_5]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3387_SHIP_CANNONBALL_PUZZLE_SPAWN_PRIZE
    _original_item: Type[Item] = Mushroom
    _packet_type: PacketType = PacketType.FALLING
    _keep_original_item_if_excluded: bool = False


class ShipBarrelPuzzle(PacketItem, SunkenShipLocation):
    """ShipBarrelPuzzle progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_BARREL_PUZZLE
    )
    _room_ids: List[int] = [
        R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL
    ]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _creation_script: int = E3389_SHIP_BARREL_PUZZLE_SPAWN_PRIZE
    _original_item: Type[Item] = RecoveryMushroom
    _packet_type: PacketType = PacketType.FALLING


class EarlyInnerShipLeftChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerSunkenShipLocation
):
    """EarlyInnerShipLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [
        R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class InnerShipCloneRoomChest(MidgameChestLocation, InnerSunkenShipLocation):
    """InnerShipCloneRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids: List[int] = [2]
    _container_event: int = E0247_CHEST_1_GRANT


class InnerShipBehindBoxesChest(MidgameChestLocation, InnerSunkenShipLocation):
    """InnerShipBehindBoxesChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_FROG_COIN_ROOM
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class InnerShipSaveRoomLeftChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerSunkenShipLocation
):
    """InnerShipSaveRoomLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_HIDON_MUSHROOM
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class InnerShipSaveRoomRightChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerSunkenShipLocation
):
    """InnerShipSaveRoomRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.HIDON_CHEST
    _original_item: Type[Item] = MimicFightInitiator2
    _room_ids: List[int] = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class Mimic2DropReward(GrantLocation):
    """Mimic2DropReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.HIDON_REWARD_1
    _original_item: Type[Item] = SafetyBadge
    _identifier: int = 513
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory):
        return can_defeat_second_mimic(self.world, inventory)


class Mimic2ReloadReward(MimicReloadRewardChest):
    """Mimic2ReloadReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.HIDON_REWARD_2
    _original_item: Type[Item] = Coins100
    _identifier: int = 513
    _container_event: int = E0245_CHEST_3_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_access(self, inventory: Inventory):
        return can_defeat_second_mimic(self.world, inventory)

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        if isinstance(item, (MimicFightChestAssignment, InfiniteCoins)):
            return False
        chest = next(
            (
                loc
                for loc in self.world.item_locations
                if loc.does_contain(MimicFightInitiator2)
            ),
            None,
        )
        if chest is None:
            return False
        return chest.can_accept(item)

    def set_contents(self, contents: Optional[Item]) -> None:
        chest = next(
            (
                loc
                for loc in self.world.item_locations
                if loc.does_contain(MimicFightInitiator2)
            ),
            None,
        )
        if chest is None:
            raise ItemPlacementError(
                "how are we setting contents on a reload reward that can't be accessed yet?"
            )
        self.set_room_ids(chest.room_ids)
        super().set_contents(contents)


class InnerShipFirstUnderwaterRoomBottomItem(
    FreestandingLocation, InnerSunkenShipLocation
):
    """InnerShipFirstUnderwaterRoomBottomItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids: List[int] = [0]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class InnerShipFirstUnderwaterRoomTopItem(
    FreestandingLocation, InnerSunkenShipLocation
):
    """InnerShipFirstUnderwaterRoomTopItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids: List[int] = [1]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class InnerShipFirstUnderwaterRoomLeftItem(
    FreestandingLocation, InnerSunkenShipLocation
):
    """InnerShipFirstUnderwaterRoomLeftItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids: List[int] = [2]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class InnerShipFirstUnderwaterRoomMiddleItem(
    FreestandingLocation, InnerSunkenShipLocation
):
    """InnerShipFirstUnderwaterRoomMiddleItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_4
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids: List[int] = [3]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class InnerShipSecretRoomChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerSunkenShipLocation
):
    """InnerShipSecretRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING
    )
    _original_item: Type[Item] = SafetyRing
    _room_ids: List[int] = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class InnerShipPoolRoom(FreestandingLocation, InnerSunkenShipLocation):
    """InnerShipPoolRoom progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_BLOOBER_ROOM
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER
    ]
    _npc_ids: List[int] = [5]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class InnerShipBeforeBossChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerSunkenShipLocation
):
    """InnerShipBeforeBossChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL
    ]
    _npc_ids: List[int] = [4]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Land's End


class LandsEndRisingPlatformChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndRisingPlatformChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_RED_ESSENCE
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R137_LANDS_END_AREA_01]
    _npc_ids: List[int] = [4]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class LandsEndChowPitStaticChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndChowPitStaticChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_CHOW_PIT_1
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R138_LANDS_END_AREA_02]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT


class LandsEndChowPitMovingChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndChowPitMovingChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_CHOW_PIT_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R138_LANDS_END_AREA_02]
    _npc_ids: List[int] = [7]
    _container_event: int = E0246_CHEST_2_GRANT


class LandsEndBeeTowerChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndBeeTowerChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LNDS_END_BEE_ROOM
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT


class LandsEndGrottoEntranceChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndGrottoEntranceChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_SECRET_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS
    ]
    _npc_ids: List[int] = [7]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class LandsEndGrottoCornerChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndGrottoCornerChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_SECRET_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0246_CHEST_2_GRANT


class LandsEndGrottoEndChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndGrottoEndChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_SHY_AWAY
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class LandsEndUndergroundSaveBoxChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndUndergroundSaveBoxChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1
    _original_item: Type[Item] = LandsEndVolcanoStar
    _room_ids: List[int] = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids: List[int] = [5]
    _container_event: int = E0247_CHEST_1_GRANT


class LandsEndFirstPurchasableChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndFirstPurchasableChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2
    _original_item: Type[Item] = LandsEndStar2
    _room_ids: List[int] = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids: List[int] = [18]
    _container_event: int = E0247_CHEST_1_GRANT


class LandsEndSecondPurchasableChest(
    ChestLocationAllowSlots, MidgameChestLocation, LandsEndLocation
):
    """LandsEndSecondPurchasableChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3
    _original_item: Type[Item] = LandsEndStar3
    _room_ids: List[int] = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids: List[int] = [19]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 4


class TroopaClimbSub12Prize(GrantLocation, LandsEndLocation):
    """TroopaClimbSub12Prize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.TROOPA_CLIMB
    _original_item: Type[Item] = TroopaPin
    _room_ids: List[int] = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 4

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_temple_boss(self.world, inventory)


# *** Belome Temple


class BelomeTempleFortuneTeller(
    ChestLocationAllowSlots, MidgameChestLocation, TempleLocation
):
    """BelomeTempleFortuneTeller progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_TELLER
    )
    _original_item: Type[Item] = Coins50
    _room_ids: List[int] = [R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]
    _npc_ids: List[int] = [5]
    _container_event: int = E0247_CHEST_1_GRANT


class BelomeTempleLMRChest(
    ChestLocationAllowCoins, MidgameChestLocation, InnerTempleLocation
):
    """BelomeTempleLMRChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_1
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT


class BelomeTempleLRMChest(
    ChestLocationAllowCoins, MidgameChestLocation, InnerTempleLocation
):
    """BelomeTempleLRMChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_2
    )
    _original_item: Type[Item] = YoshiCookie
    _room_ids: List[int] = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids: List[int] = [7]
    _container_event: int = E0246_CHEST_2_GRANT


class BelomeTempleRLMChest(
    ChestLocationAllowCoins, MidgameChestLocation, InnerTempleLocation
):
    """BelomeTempleRLMChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_3
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids: List[int] = [8]
    _container_event: int = E0245_CHEST_3_GRANT


class BelomeTempleRMLChest(
    ChestLocationAllowCoins, MidgameChestLocation, InnerTempleLocation
):
    """BelomeTempleRMLChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4
    )
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids: List[int] = [9]
    _container_event: int = E0244_CHEST_4_GRANT


class BelomeBeforeBossRightChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerTempleLocation
):
    """BelomeBeforeBossRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_1
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class BelomeBeforeBossLowerLeftChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerTempleLocation
):
    """BelomeBeforeBossLowerLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2
    )
    _original_item: Type[Item] = Coins150
    _room_ids: List[int] = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class BelomeBeforeBossMiddleChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerTempleLocation
):
    """BelomeBeforeBossMiddleChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids: List[int] = [2]
    _container_event: int = E0245_CHEST_3_GRANT


class BelomeBeforeBossUpperLeftChest(
    ChestLocationAllowSlots, MidgameChestLocation, InnerTempleLocation
):
    """BelomeBeforeBossUpperLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids: List[int] = [3]
    _container_event: int = E0244_CHEST_4_GRANT


class BelomeTemplTreasuryeUpperCornerLeftItem(FreestandingLocation, TreasuryLocation):
    """BelomeTemplTreasuryeUpperCornerLeftItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class BelomeTempleTreasuryUpperCornerLowerLeftItem(
    FreestandingLocation, TreasuryLocation
):
    """BelomeTempleTreasuryUpperCornerLowerLeftItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [1]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class BelomeTempleTreasuryUpperCornerTopItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryUpperCornerTopItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_3
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [2]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class BelomeTempleTreasuryTopmostItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryTopmostItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_4
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [3]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class BelomeTempleTreasuryMidLeftItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryMidLeftItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_1
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [4]
    _container_event: int = E0237_FREESTANDING_5_GRANT


class BelomeTempleTreasuryAlmostTopItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryAlmostTopItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [5]
    _container_event: int = E0236_FREESTANDING_6_GRANT


class BelomeTempleTreasuryAlmostLeftmostItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryAlmostLeftmostItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_3
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [6]
    _container_event: int = E0235_FREESTANDING_7_GRANT


class BelomeTempleTreasuryOuterUpperRightItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryOuterUpperRightItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_4
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [7]
    _container_event: int = E0234_FREESTANDING_8_GRANT


class BelomeTempleTreasuryInnerUpperRightItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryInnerUpperRightItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_5
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [8]
    _container_event: int = E0233_FREESTANDING_9_GRANT


class BelomeTempleTreasuryLowestItemsRight(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryLowestItemsRight progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_6
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [9]
    _container_event: int = E0232_FREESTANDING_10_GRANT


class BelomeTempleTreasuryLowerOuterBottomRightItem(
    FreestandingLocation, TreasuryLocation
):
    """BelomeTempleTreasuryLowerOuterBottomRightItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_7
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [10]
    _container_event: int = E0231_FREESTANDING_11_GRANT


class BelomeTempleTreasuryRightmostItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryRightmostItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_8
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [11]
    _container_event: int = E0230_FREESTANDING_12_GRANT


class BelomeTempleTreasuryBottomLeftCornerItem(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryBottomLeftCornerItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_2
    )
    _original_item: Type[Item] = MaxMushroom
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [13]
    _container_event: int = E0229_FREESTANDING_13_GRANT


class BelomeTempleTreasuryLowestItemsLeft(FreestandingLocation, TreasuryLocation):
    """BelomeTempleTreasuryLowestItemsLeft progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_1
    )
    _original_item: Type[Item] = RoyalSyrup
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [14]
    _container_event: int = E0228_FREESTANDING_14_GRANT


class BelomeTempleTreasuryUpperOuterBottomRightItem(
    FreestandingLocation, TreasuryLocation
):
    """BelomeTempleTreasuryUpperOuterBottomRightItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3
    )
    _original_item: Type[Item] = FireBomb
    _room_ids: List[int] = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids: List[int] = [15]
    _container_event: int = E0227_FREESTANDING_15_GRANT


# *** Monstro Town


class MonstroEntrance(ChestLocationAllowSlots, MonstroTownLocation):
    """MonstroEntrance progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
            return 2
        return 4


class MonstroThwompItem(FreestandingLocation, MonstroTownLocation):
    """MonstroThwompItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP
    _original_item: Type[Item] = TempleKey
    _room_ids: List[int] = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids: List[int] = [0]
    _container_event: int = E0241_FREESTANDING_1_GRANT

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
            return 2
        return 4


class MonstroDojoClearReward(GrantLocation, MonstroTownLocation):
    """MonstroDojoClearReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.JINX_DOJO_REWARD
    _original_item: Type[Item] = JinxBelt
    _room_ids: List[int] = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_fourth_dojo_boss(self.world, inventory)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )


class MonstroSealedDoorClearReward(GrantLocation, MonstroTownLocation):
    """MonstroSealedDoorClearReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CULEX_REWARD
    _original_item: Type[Item] = QuartzCharm
    _room_ids: List[int] = [R351_CULEXS_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_sealed_door_boss(self.world, inventory)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )


class MonstroFirstSuperJumpReward(GrantLocation, MonstroTownLocation):
    """MonstroFirstSuperJumpReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUPER_JUMPS_30
    _original_item: Type[Item] = AttackScarf
    _room_ids: List[int] = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return super().can_access(inventory) and inventory.has_item(SuperJump)

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )

    def __init__(self, world: GameWorld) -> None:
        super().__init__(world)
        if SuperJump.title in world.settings.get_flag(AvailableSpells).disabled:
            self.set_allow_empty_when_finished_shuffling(True)

    @property
    def tier(self) -> int:
        if self.world.settings.get_flag(SuperJump1Threshold).value < 30:
            return 2
        return 4


class MonstroSecondSuperJumpReward(GrantLocation, MonstroTownLocation):
    """MonstroSecondSuperJumpReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUPER_JUMPS_100
    _original_item: Type[Item] = SuperSuit
    _room_ids: List[int] = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _container_event: int = E0252_NPC_QUEST_2_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return super().can_access(inventory) and inventory.has_item(SuperJump)

    def __init__(self, world: GameWorld) -> None:
        super().__init__(world)
        if SuperJump.title in world.settings.get_flag(AvailableSpells).disabled:
            self.set_allow_empty_when_finished_shuffling(True)

    @property
    def tier(self) -> int:
        if self.world.settings.get_flag(SuperJump1Threshold).value < 31:
            return 2
        return 4


class MonstroFlagExchange(GrantLocation, MonstroTownLocation):
    """MonstroFlagExchange progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.THREE_MUSTY_FEARS
    _original_item: Type[Item] = GhostMedal
    _room_ids: List[int] = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return (
            super().can_access(inventory)
            and inventory.has_item(DryBonesFlag)
            and inventory.has_item(GreaperFlag)
            and inventory.has_item(BigBooFlag)
        )

    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return super().can_accept(item, inventory) and not _restrict_best_monstro_item(
            self.world, item
        )


# *** Bean Valley


class BeanValleyFirstDeadEnd(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyFirstDeadEnd progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids: List[int] = [3]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyFirstProgressChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyFirstProgressChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids: List[int] = [4]
    _container_event: int = E0246_CHEST_2_GRANT


class BeanValleyLeftPiranhaPipe(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyLeftPiranhaPipe progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE
    )
    _original_item: Type[Item] = SlotMachineChest
    _room_ids: List[int] = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyBottomLeftPiranhaPipe(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyBottomLeftPiranhaPipe progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE
    )
    _original_item: Type[Item] = SlotMachineChest
    _room_ids: List[int] = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyBottomRightPiranhaPipeUpper(
    ChestLocationAllowSlots, BeanValleyLocation
):
    """BeanValleyBottomRightPiranhaPipeUpper progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER
    )
    _original_item: Type[Item] = SlotMachineChest
    _room_ids: List[int] = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyBottomRightPiranhaPipeLower(
    ChestLocationAllowSlots, BeanValleyLocation
):
    """BeanValleyBottomRightPiranhaPipeLower progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER
    )
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT


class BeanValleyRightPipeLeftChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyRightPipeLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1
    )
    _original_item: Type[Item] = MimicFightInitiator3
    _room_ids: List[int] = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids: List[int] = [5]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyRightPipeRightChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyRightPipeRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_2
    )
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids: List[int] = [7]
    _container_event: int = E0246_CHEST_2_GRANT


class BeanValleyRightPipeUnderStairs(GrantLocation, BeanValleyLocation):
    """BeanValleyRightPipeUnderStairs progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class BeanValleyRightPipeAboveGround(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanValleyRightPipeAboveGround progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids: List[int] = [13]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValleyBossNote(GrantLocation, BeanValleyLocation):
    """BeanValleyBossNote progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM
    )
    _original_item: Type[Item] = Seed
    _room_ids: List[int] = [R254_BEAN_VALLEY_SMILAX_AREA]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 4

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_valley_boss(self.world, inventory)


class BeanstalkLowestChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanstalkLowestChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids: List[int] = [9]
    _container_event: int = E0247_CHEST_1_GRANT


class BeanValley1stRoomFloatingItem(FreestandingLocation, BeanValleyLocation):
    """BeanValley1stRoomFloatingItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids: List[int] = [3]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class BeanValley1stRoomMiddleCoin(FreestandingLocation, BeanValleyLocation):
    """BeanValley1stRoomMiddleCoin progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids: List[int] = [4]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class BeanValley1stRoomUpperCoin(FreestandingLocation, BeanValleyLocation):
    """BeanValley1stRoomUpperCoin progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids: List[int] = [5]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class BeanValley1stRoomLowerCoin(FreestandingLocation, BeanValleyLocation):
    """BeanValley1stRoomLowerCoin progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids: List[int] = [6]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class Beanstalk2ndRoomFloatingItem(FreestandingLocation, BeanValleyLocation):
    """Beanstalk2ndRoomFloatingItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_FROG_COIN
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids: List[int] = [6]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class Beanstalk2ndRoomCoin1(FreestandingLocation, BeanValleyLocation):
    """Beanstalk2ndRoomCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids: List[int] = [3]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class Beanstalk2ndRoomCoin2(FreestandingLocation, BeanValleyLocation):
    """Beanstalk2ndRoomCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_2
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids: List[int] = [4]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class Beanstalk2ndRoomCoin3(FreestandingLocation, BeanValleyLocation):
    """Beanstalk2ndRoomCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_3
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids: List[int] = [5]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class BeanValleyEastBeanstalkCoin1(FreestandingLocation, BeanValleyLocation):
    """BeanValleyEastBeanstalkCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [3]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class BeanValleyEastBeanstalkCoin2(FreestandingLocation, BeanValleyLocation):
    """BeanValleyEastBeanstalkCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_2
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [4]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class BeanValleyEastBeanstalkCoin3(FreestandingLocation, BeanValleyLocation):
    """BeanValleyEastBeanstalkCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [5]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class BeanValleyEastBeanstalkCoin4(FreestandingLocation, BeanValleyLocation):
    """BeanValleyEastBeanstalkCoin4 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_4
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class BeanValleyEastBeanstalkCoin5(FreestandingLocation, BeanValleyLocation):
    """BeanValleyEastBeanstalkCoin5 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_5
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [7]
    _container_event: int = E0237_FREESTANDING_5_GRANT


class BeanValleyWestBeanstalkCoin1(FreestandingLocation, BeanValleyLocation):
    """BeanValleyWestBeanstalkCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [4]
    _container_event: int = E0241_FREESTANDING_1_GRANT


class BeanValleyWestBeanstalkCoin2(FreestandingLocation, BeanValleyLocation):
    """BeanValleyWestBeanstalkCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_2
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [5]
    _container_event: int = E0240_FREESTANDING_2_GRANT


class BeanValleyWestBeanstalkCoin3(FreestandingLocation, BeanValleyLocation):
    """BeanValleyWestBeanstalkCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_3
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [
        R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0239_FREESTANDING_3_GRANT


class BeanValleyWestBeanstalkFloatingItem(FreestandingLocation, BeanValleyLocation):
    """BeanValleyWestBeanstalkFloatingItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02
    ]
    _npc_ids: List[int] = [7]
    _container_event: int = E0238_FREESTANDING_4_GRANT


class BeanstalkUpperCloudLeftChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanstalkUpperCloudLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 4


class BeanstalkUpperCloudRightChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanstalkUpperCloudRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2
    _original_item: Type[Item] = RareScarf
    _room_ids: List[int] = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 4


class BeanstalkLowerCloudLeftChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanstalkLowerCloudLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_FALL_1
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 4


class BeanstalkLowerCloudRightChest(ChestLocationAllowSlots, BeanValleyLocation):
    """BeanstalkLowerCloudRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_FALL_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 4


# *** Grate Guy's Casino


class CasinoGrateGuyPrize(GrantLocation, CasinoLocation):
    """CasinoGrateGuyPrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE
    _original_item: Type[Item] = StarEgg
    _room_ids: List[int] = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


# *** Nimbus Land


class NimbusShopChest(ChestLocationAllowSlots, NimbusTownLocation):
    """NimbusShopChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_SHOP
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class NimbusInnDreamPrize1(GrantLocation, NimbusTownLocation):
    """NimbusInnDreamPrize1 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_INN
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R346_NIMBUS_LAND_INN_BEDROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class NimbusInnDreamPrize2(GrantLocation, NimbusTownLocation):
    """NimbusInnDreamPrize2 progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R346_NIMBUS_LAND_INN_BEDROOM]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _tier: int = 2


class NimbusCastleStatueGamePrize(GrantLocation, NimbusCastleLocation):
    """NimbusCastleStatueGamePrize progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.DODO_REWARD
    _original_item: Type[Item] = Feather
    _room_ids: List[int] = [R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _missable: bool = True


class NimbusCastleOuterPrisonCellarRightNPC(GrantLocation, NimbusCastleLocation):
    """NimbusCastleOuterPrisonCellarRightNPC progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS
    _original_item: Type[Item] = FlowerJar
    _room_ids: List[int] = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _container_event: int = E0253_NPC_QUEST_1_GRANT
    _tier: int = 2


class NimbusCastleOuterPrisonCellarLeftNPC(GrantLocation, NimbusCastleLocation):
    """NimbusCastleOuterPrisonCellarLeftNPC progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_LAND_PRISONERS_2
    )
    _original_item: Type[Item] = CastleKey1
    _room_ids: List[int] = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _tier: int = 2


class NimbusCastleBusinessCentreOccupiedChest(
    ChestLocationAllowSlots, NimbusCastleLocation
):
    """NimbusCastleBusinessCentreOccupiedChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _missable: bool = True
    _tier: int = 2


class NimbusCastleCornerBridgeChest(ChestLocationAllowSlots, NimbusCastleLocation):
    """NimbusCastleCornerBridgeChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_LAND_BEFORE_BIRDETTA_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
        R500_NIMBUS_CASTLE_AREA_04_____DUMMY,
    ]
    _npc_ids: List[int] = [2, 0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class NimbusCastleOutOfBoundsChest(ChestLocationAllowSlots, NimbusCastleLocation):
    """NimbusCastleOutOfBoundsChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_1
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class NimbusCastleAboveJawfulChest(ChestLocationAllowSlots, NimbusCastleLocation):
    """NimbusCastleAboveJawfulChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT
    _tier: int = 2

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class NimbusCastleSingleGoldBirdChest(ChestLocationAllowSlots, NimbusCastleLocation):
    """NimbusCastleSingleGoldBirdChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_SINGLE_GOLD_BIRD
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2


class NimbusCastleTwoLevelLowerChest(ChestLocationAllowSlots, NimbusCastleLocation):
    """NimbusCastleTwoLevelLowerChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0247_CHEST_1_GRANT
    _tier: int = 2

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class NimbusCastleGiantEggReward(GrantLocation, NimbusMidCastleLocation):
    """NimbusCastleGiantEggReward progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_CASTLE_BIRDETTA
    _original_item: Type[Item] = CastleKey2
    _room_ids: List[int] = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _container_event: int = E0253_NPC_QUEST_1_GRANT


class NimbusCastleTwoLevelUpperChest(ChestLocationAllowSlots, NimbusDeepCastleLocation):
    """NimbusCastleTwoLevelUpperChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_____DUMMY,
    ]
    _npc_ids: List[int] = [1, 1]
    _container_event: int = E0246_CHEST_2_GRANT


class NimbusCastleBackHallwayOccupiedChest(
    ChestLocationAllowSlots, NimbusDeepCastleLocation
):
    """NimbusCastleBackHallwayOccupiedChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST
    )
    _original_item: Type[Item] = NimbusLandStar
    _room_ids: List[int] = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT
    _missable: bool = True


class NimbusCastleBackHallwayLiberatedChest(
    ChestLocationAllowSlots, NimbusDeepCastleLocation
):
    """NimbusCastleBackHallwayLiberatedChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_STAR_AFTER_VALENTINA
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


class NimbusCastleBusinessCentreLiberatedChest(
    ChestLocationAllowSlots, NimbusCastleLocation
):
    """NimbusCastleBusinessCentreLiberatedChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


class NimbusLandRightSide(GrantLocation, NimbusTownLocation):
    """NimbusLandRightSide progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_RIGHT_SIDE
    _original_item: Type[Item] = Fertilizer
    _room_ids: List[int] = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


class NimbusLandCrocoItem(FreestandingLocation, NimbusMidCastleLocation):
    """NimbusLandCrocoItem progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING
    )
    _original_item: Type[Item] = SignalRing
    _room_ids: List[int] = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [5]
    _keep_original_item_if_excluded: bool = False

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


class NimbusLandInnerCellar(GrantLocation, NimbusMidCastleLocation):
    """NimbusLandInnerCellar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.NIMBUS_LAND_CELLAR
    _original_item: Type[Item] = FlowerJar
    _room_ids: List[int] = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


# *** Barrel Volcano


class VolcanoLavaCoveLeftChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoLavaCoveLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_nimbus_boss(self.world, inventory) and super().can_access(
            inventory
        )


class VolcanoLavaCoveRightChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoLavaCoveRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class VolcanoEarlyProgressChestLeft(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoEarlyProgressChestLeft progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R384_VOLCANO_AREA_05]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class VolcanoEarlyProgressChestRight(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoEarlyProgressChestRight progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_2
    )
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [R384_VOLCANO_AREA_05]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


class VolcanoEarlyProgressThirdChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoEarlyProgressThirdChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_STAR_ROOM
    )
    _original_item: Type[Item] = LandsEndVolcanoStar
    _room_ids: List[int] = [R385_VOLCANO_AREA_06]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class VolcanoLavaPool(FreestandingLocation, BarrelVolcanoLocation):
    """VolcanoLavaPool progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_LAVA_POOL
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R361_VOLCANO_AREA_09]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [1]


class VolcanoReverseRecoilItem(FreestandingLocation, BarrelVolcanoLocation):
    """VolcanoReverseRecoilItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_REVERSE
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [4]


class VolcanoRightDonutItem(FreestandingLocation, BarrelVolcanoLocation):
    """VolcanoRightDonutItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_1
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R358_VOLCANO_AREA_11]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [1]


class VolcanoLeftDonutItem(FreestandingLocation, BarrelVolcanoLocation):
    """VolcanoLeftDonutItem progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_2
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R358_VOLCANO_AREA_11]
    _container_event: int = E0240_FREESTANDING_2_GRANT
    _npc_ids: List[int] = [2]


class VolcanoSaveRoomLowerChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoSaveRoomLowerChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class VolcanoSaveRoomUpperChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoSaveRoomUpperChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2
    )
    _original_item: Type[Item] = FrogCoin
    _room_ids: List[int] = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class VolcanoShopEntranceChest(ChestLocationAllowSlots, BarrelVolcanoLocation):
    """VolcanoShopEntranceChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_HINOPIO
    _original_item: Type[Item] = Coins100
    _room_ids: List[int] = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InvincibilityStar
        )


# *** Bowser's Keep


class KeepDarkRoomChest(ChestLocationAllowSlots, BowsersKeepLocation):
    """KeepDarkRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOWSERS_KEEP_DARK_ROOM
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepFirstCrocoShopLeftChest(ChestLocationAllowSlots, BowsersKeepLocation):
    """KeepFirstCrocoShopLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_1
    )
    _original_item: Type[Item] = Coins150
    _room_ids: List[int] = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepFirstCrocoShopRightChest(ChestLocationAllowSlots, BowsersKeepLocation):
    """KeepFirstCrocoShopRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_2
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class KeepInvisibleBridgeFrontChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepInvisibleBridgeFrontChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1
    )
    _original_item: Type[Item] = FrightBomb
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids: List[int] = [4]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepInvisibleBridgeRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepInvisibleBridgeRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_2
    )
    _original_item: Type[Item] = RoyalSyrup
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids: List[int] = [5]
    _container_event: int = E0246_CHEST_2_GRANT


class KeepInvisibleBridgeLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepInvisibleBridgeLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_3
    )
    _original_item: Type[Item] = IceBomb
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids: List[int] = [6]
    _container_event: int = E0245_CHEST_3_GRANT


class KeepInvisibleBridgeBackChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepInvisibleBridgeBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_4
    )
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids: List[int] = [7]
    _container_event: int = E0244_CHEST_4_GRANT


class KeepInvisibleBridgeCoin1(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepInvisibleBridgeCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [8]


class KeepInvisibleBridgeCoin2(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepInvisibleBridgeCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _container_event: int = E0240_FREESTANDING_2_GRANT
    _npc_ids: List[int] = [9]


class KeepInvisibleBridgeCoin3(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepInvisibleBridgeCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _container_event: int = E0239_FREESTANDING_3_GRANT
    _npc_ids: List[int] = [10]


class KeepInvisibleBridgeCoin4(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepInvisibleBridgeCoin4 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _container_event: int = E0238_FREESTANDING_4_GRANT
    _npc_ids: List[int] = [11]


class KeepXYPlatformsBackLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepXYPlatformsBackLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids: List[int] = [10]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepXYPlatformsFrontLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepXYPlatformsFrontLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_2
    )
    _original_item: Type[Item] = RedEssence
    _room_ids: List[int] = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids: List[int] = [11]
    _container_event: int = E0246_CHEST_2_GRANT


class KeepXYPlatformsFrontRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepXYPlatformsFrontRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_3
    )
    _original_item: Type[Item] = MaxMushroom
    _room_ids: List[int] = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids: List[int] = [12]
    _container_event: int = E0245_CHEST_3_GRANT


class KeepXYPlatformsBackRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepXYPlatformsBackRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_4
    )
    _original_item: Type[Item] = FireBomb
    _room_ids: List[int] = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids: List[int] = [13]
    _container_event: int = E0244_CHEST_4_GRANT


class KeepElevatorRoomChest(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepElevatorRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ELEVATOR_PLATFORMS
    )
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [
        R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS
    ]
    _npc_ids: List[int] = [8]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepCannonballRoomFrontRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepCannonballRoomFrontRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids: List[int] = [3]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepCannonballRoomBackChest(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepCannonballRoomBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids: List[int] = [4]
    _container_event: int = E0246_CHEST_2_GRANT


class KeepCannonballFrontLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepCannonballFrontLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_3
    )
    _original_item: Type[Item] = PickMeUp
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids: List[int] = [5]
    _container_event: int = E0245_CHEST_3_GRANT


class KeepCannonballMidRightChest(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepCannonballMidRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_4
    )
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids: List[int] = [6]
    _container_event: int = E0244_CHEST_4_GRANT


class KeepCannonballMidLeftChest(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepCannonballMidLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_5
    )
    _original_item: Type[Item] = MaxMushroom
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids: List[int] = [7]
    _container_event: int = E0243_CHEST_5_GRANT


class KeepCannonballCoin1(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0241_FREESTANDING_1_GRANT
    _npc_ids: List[int] = [8]


class KeepCannonballCoin2(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0240_FREESTANDING_2_GRANT
    _npc_ids: List[int] = [9]


class KeepCannonballCoin3(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0239_FREESTANDING_3_GRANT
    _npc_ids: List[int] = [10]


class KeepCannonballCoin4(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin4 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0238_FREESTANDING_4_GRANT
    _npc_ids: List[int] = [11]


class KeepCannonballCoin5(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin5 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0237_FREESTANDING_5_GRANT
    _npc_ids: List[int] = [12]


class KeepCannonballCoin6(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin6 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0236_FREESTANDING_6_GRANT
    _npc_ids: List[int] = [13]


class KeepCannonballCoin7(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin7 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0235_FREESTANDING_7_GRANT
    _npc_ids: List[int] = [14]


class KeepCannonballCoin8(FreestandingLocation, BowsersKeepObstacleLocation):
    """KeepCannonballCoin8 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8
    )
    _original_item: Type[Item] = Coins10
    _room_ids: List[int] = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _container_event: int = E0234_FREESTANDING_8_GRANT
    _npc_ids: List[int] = [15]


class KeepRotatingPlatformsFrontChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsFrontChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_1
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0247_CHEST_1_GRANT


class KeepRotatingPlatformsFrontMidLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsFrontMidLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [2]
    _container_event: int = E0246_CHEST_2_GRANT


class KeepRotatingPlatformsBackMidRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsBackMidRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_3
    )
    _original_item: Type[Item] = FireBomb
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [3]
    _container_event: int = E0245_CHEST_3_GRANT


class KeepRotatingPlatformsFrontMidRightChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsFrontMidRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_4
    )
    _original_item: Type[Item] = RoyalSyrup
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [4]
    _container_event: int = E0244_CHEST_4_GRANT


class KeepRotatingPlatformsBackMidLeftChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsBackMidLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_5
    )
    _original_item: Type[Item] = PickMeUp
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [5]
    _container_event: int = E0243_CHEST_5_GRANT


class KeepRotatingPlatformsBackChest(
    ChestLocationAllowSlots, BowsersKeepObstacleLocation
):
    """KeepRotatingPlatformsBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6
    )
    _original_item: Type[Item] = KerokeroCola
    _room_ids: List[int] = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0242_CHEST_6_GRANT


class KeepDoorRewardChest1(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest1 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_1
    )
    _original_item: Type[Item] = SonicCymbal
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0247_CHEST_1_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )


class KeepDoorRewardChest2(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest2 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2
    )
    _original_item: Type[Item] = SuperSlap
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0246_CHEST_2_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )


class KeepDoorRewardChest3(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest3 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_3
    )
    _original_item: Type[Item] = DrillClaw
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0245_CHEST_3_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )

    def can_access(self, inventory: Inventory) -> bool:
        if not self.world.settings.is_boolean_flag_enabled(BowserDoorShuffle):
            return can_defeat_battle_door_boss(
                self.world, inventory
            )  # This is actually behind Chester 100% of the time if door shuffle is off.
        return super().can_access(inventory)


class KeepDoorRewardChest4(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest4 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_4
    )
    _original_item: Type[Item] = StarGun
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0244_CHEST_4_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )


class KeepDoorRewardChest5(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest5 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_5
    )
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0243_CHEST_5_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )


class KeepDoorRewardChest6(ChestLocationAllowSlots, BowsersKeepObstacleLocation):
    """KeepDoorRewardChest6 progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_6
    )
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids: List[int] = [0, 0]
    _container_event: int = E0242_CHEST_6_GRANT
    _set_70a7_manually_in_event_script: bool = True

    def can_accept(self, item: Item, inventory: Optional[Inventory] = None) -> bool:
        return super().can_accept(item, inventory) and not isinstance(
            item, InfiniteCoins
        )


class KeepAfterObstaclesBossChest(ChestLocationAllowSlots, BowsersKeepLocation):
    """KeepAfterObstaclesBossChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA
    _original_item: Type[Item] = InfiniteCoins
    _room_ids: List[int] = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        if self.world.settings.is_flag_value(BowserDoorRequirements, 6):
            return can_defeat_battle_door_boss(
                self.world, inventory
            )  # With 6 doors required you always have to beat the battle door.
        return super().can_access(inventory) and can_defeat_post_obstacle_boss(
            self.world, inventory
        )


# *** Factory


class OuterFactorySaveRoomChest(ChestLocationAllowSlots, OuterFactoryLocation):
    """OuterFactorySaveRoomChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_SAVE_ROOM
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class FactoryBoltPlatformsChest(ChestLocationAllowSlots, OuterFactoryLocation):
    """FactoryBoltPlatformsChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_BOLT_PLATFORMS
    _original_item: Type[Item] = UltraHammer
    _room_ids: List[int] = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _npc_ids: List[int] = [7]
    _container_event: int = E0247_CHEST_1_GRANT


class FactoryAxemConveyorsChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryAxemConveyorsChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_FALLING_AXEMS
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS
    ]
    _npc_ids: List[int] = [6]
    _container_event: int = E0247_CHEST_1_GRANT


class FactoryTreasurePitBackChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryTreasurePitBackChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_TREASURE_PIT_1
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids: List[int] = [0]
    _container_event: int = E0247_CHEST_1_GRANT


class FactoryTreasurePitFrontChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryTreasurePitFrontChest progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_TREASURE_PIT_2
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids: List[int] = [2]
    _container_event: int = E0245_CHEST_3_GRANT


class FactoryBigConveyorRoomFirstChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryBigConveyorRoomFirstChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1
    )
    _original_item: Type[Item] = RoyalSyrup
    _room_ids: List[int] = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids: List[int] = [8]
    _container_event: int = E0247_CHEST_1_GRANT


class FactoryBigConveyorRoomSecondChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryBigConveyorRoomSecondChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2
    )
    _original_item: Type[Item] = MaxMushroom
    _room_ids: List[int] = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids: List[int] = [9]
    _container_event: int = E0246_CHEST_2_GRANT


class FactoryBehindNinjasRightChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryBehindNinjasRightChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_1
    )
    _original_item: Type[Item] = RecoveryMushroom
    _room_ids: List[int] = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids: List[int] = [1]
    _container_event: int = E0246_CHEST_2_GRANT


class FactoryBehindNinjasLeftChest(ChestLocationAllowSlots, MidFactoryLocation):
    """FactoryBehindNinjasLeftChest progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_2
    )
    _original_item: Type[Item] = Flower
    _room_ids: List[int] = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids: List[int] = [3]
    _container_event: int = E0244_CHEST_4_GRANT


class InnerFactoryToadGift(GrantLocation, InnerFactoryLocation):
    """InnerFactoryToadGift progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_TOAD_GIFT
    _original_item: Type[Item] = RockCandy
    _room_ids: List[int] = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _container_event: int = E0253_NPC_QUEST_1_GRANT

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_inner_factory_first_boss(
            self.world, inventory
        ) and super().can_access(inventory)
