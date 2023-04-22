# pylint: disable=C0301

"""E0949_FROGFUCIUS_HINT_TREASURE_CHESTS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R203_MUSHROOM_WAY_AREA_01, ["EVENT_991_mushroom_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R203_MUSHROOM_WAY_AREA_01, ["EVENT_991_mushroom_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R204_MUSHROOM_WAY_AREA_02, ["EVENT_991_mushroom_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R204_MUSHROOM_WAY_AREA_02, ["EVENT_991_mushroom_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_991_kingdom"]
        ),
        JmpIfBitClear(
            MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, ["EVENT_991_kingdom"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0, R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM, ["EVENT_991_kingdom"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_949_sewer_1"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9, R207_BANDITS_WAY_AREA_02, ["EVENT_991_bandits"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R077_BANDITS_WAY_AREA_03, ["EVENT_991_bandits"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R078_BANDITS_WAY_AREA_04, ["EVENT_991_bandits"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R078_BANDITS_WAY_AREA_04, ["EVENT_991_bandits"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R206_BANDITS_WAY_AREA_05, ["EVENT_991_bandits"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            ["EVENT_991_sewer"],
            identifier="EVENT_949_sewer_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            ["EVENT_991_sewer"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
            ["EVENT_991_sewer"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, ["EVENT_991_sewer"]
        ),
        JmpIfBitClear(MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED, ["EVENT_991_midas"]),
        JmpIfBitClear(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_991_midas"]),
        JmpIfBitClear(MIDAS_RIVER_TUNNEL_4_PRIZE, ["EVENT_991_midas"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_7, R079_ROSE_WAY_MAIN_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_8, R079_ROSE_WAY_MAIN_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["EVENT_991_rose_way"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_991_rose_town"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_991_rose_town"]
        ),
        JmpIfBitClear(FOREST_LIBERATED, ["EVENT_949_rose_town_3"]),
        JmpIfBitClear(ROSE_TOWN_GAZ_ITEM_GRANTED, ["EVENT_991_rose_town"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_949_rose_town_3"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["EVENT_949_ls_chest_1"]),
        JmpIfBitSet(GAVE_SEED, ["EVENT_949_has_fert"]),
        StoreItemAmountTo7000(Seed),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_rose_town_3"]),
        JmpIfBitSet(GAVE_FERTILIZER, ["EVENT_949_ls_chest_1"]),
        StoreItemAmountTo7000(Fertilizer, identifier="EVENT_949_has_fert"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_rose_town_3"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R419_LAZY_SHELL_CLOUD,
            ["EVENT_991_rose_town"],
            identifier="EVENT_949_ls_chest_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R419_LAZY_SHELL_CLOUD, ["EVENT_991_rose_town"]
        ),
        JmpIfBitClear(
            ROSE_TOWN_INN_TOAD_ITEM_RECEIVED,
            ["EVENT_991_rose_town"],
            identifier="EVENT_949_rose_town_3",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
            ["EVENT_991_rose_town"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
            ["EVENT_991_rose_town"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
            ["EVENT_991_rose_town"],
        ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["EVENT_949_pipe"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R224_FOREST_MAZE_AREA_01, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R228_FOREST_MAZE_AREA_04, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            ["EVENT_991_forest"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            ["EVENT_991_forest"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            ["EVENT_991_forest"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4, R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R234_FOREST_MAZE_SECRET, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R234_FOREST_MAZE_SECRET, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3, R234_FOREST_MAZE_SECRET, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4, R234_FOREST_MAZE_SECRET, ["EVENT_991_forest"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5, R234_FOREST_MAZE_SECRET, ["EVENT_991_forest"]
        ),
        JmpIfBitClear(TREASURE_HUNTER_HOUSE_PRIZE, ["EVENT_991_rose_town"]),
        JmpIfBitClear(
            PIPE_VAULT_GATED,
            ["EVENT_949_is_bucket_available"],
            identifier="EVENT_949_pipe",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_8,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_991_pipe"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_991_pipe"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_10,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_991_pipe"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_5,
            R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            ["EVENT_991_pipe"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
            ["EVENT_991_pipe"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
            ["EVENT_991_pipe"],
        ),
        JmpIfBitClear(GOOMBA_THUMPIN_PRIZE_2_GRANTED, ["EVENT_991_pipe"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, ["EVENT_991_yoster"]
        ),
        JmpIfBitClear(COMPLETED_MUSHROOM_DERBY, ["EVENT_991_yoster"]),
        JmpIfBitClear(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_949_pass_1"]),
        JmpIfBitClear(
            MINECART_CLEARED,
            ["EVENT_949_mines_open"],
            identifier="EVENT_949_is_bucket_available",
        ),
        JmpIfBitSet(BUCKET_WARP_ENABLED, ["EVENT_949_treasure_shop_1"]),
        JmpIfBitSet(FIRST_CARBO_COOKIE_GIVEN, ["EVENT_949_treasure_shop_1"]),
        RunEventAsSubroutine(E0982_FROGFUCIUS_HINT_OPTIONAL_2),
        JmpIfBitClear(
            TREASURE_SHOP_ITEM_1_PURCHASED,
            ["EVENT_991_moleville_proper"],
            identifier="EVENT_949_treasure_shop_1",
        ),
        JmpIfBitClear(SEASIDE_LIBERATED, ["EVENT_949_treasure_shop_3"]),
        JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_991_moleville_proper"]),
        JmpIfBitClear(
            VOLCANO_LIBERATED, ["EVENT_949_fw"], identifier="EVENT_949_treasure_shop_3"
        ),
        JmpIfBitClear(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_991_moleville_proper"]),
        RunEventAsSubroutine(
            E0981_FROGFUCIUS_HINT_OPTIONAL_1, identifier="EVENT_949_fw"
        ),
        JmpIfBitSet(
            MINES_BACK_OPENED, ["EVENT_949_mines_1"], identifier="EVENT_949_mines_open"
        ),
        StoreItemAmountTo7000(BambinoBomb),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_pass_1"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM,
            ["EVENT_991_mines"],
            identifier="EVENT_949_mines_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC,
            ["EVENT_991_mines"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            ["EVENT_991_mines"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            ["EVENT_991_mines"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_8,
            R100_BOOSTER_PASS_AREA_01,
            ["EVENT_991_pass"],
            identifier="EVENT_949_pass_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9, R100_BOOSTER_PASS_AREA_01, ["EVENT_991_pass"]
        ),
        JmpIfBitClear(BOOSTER_PASS_BUSH_ITEM_FOUND, ["EVENT_991_pass"]),
        JmpIfObjectInSpecificLevel(
            NPC_6, R101_BOOSTER_PASS_AREA_02, ["EVENT_991_pass"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["EVENT_949_tower_pass_open"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["EVENT_949_hotel_stays"]),
        JmpIfBitClear(
            BOOSTER_PASS_SECRET_OPEN,
            ["EVENT_991_tower"],
            identifier="EVENT_949_tower_pass_open",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_10, R405_BOOSTER_PASS_SECRET, ["EVENT_991_pass"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_11, R405_BOOSTER_PASS_SECRET, ["EVENT_991_pass"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_12, R405_BOOSTER_PASS_SECRET, ["EVENT_991_pass"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9,
            R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_8,
            R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS,
            ["EVENT_991_tower"],
        ),
        StoreItemAmountTo7000(RoomKey),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_tower"]),
        JmpIfObjectInSpecificLevel(
            NPC_6,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["EVENT_949_tower_11"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM, ["EVENT_991_tower"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["EVENT_991_tower"],
            identifier="EVENT_949_tower_11",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["EVENT_991_tower"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9,
            R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
            ["EVENT_991_tower"],
        ),
        StoreItemAmountTo7000(ElderKey),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_tower"]),
        JmpIfObjectInSpecificLevel(
            NPC_14,
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            ["EVENT_949_hotel_stays"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP, ["EVENT_991_tower"]
        ),
        RunEventAsSubroutine(
            E0980_FROGFUCIUS_HINT_MARRYMORE_SUITE, identifier="EVENT_949_hotel_stays"
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_991_marrymore"]
        ),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_1_PURCHASED, ["EVENT_991_seaside_frog"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_2_PURCHASED, ["EVENT_991_seaside_frog"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_3_PURCHASED, ["EVENT_991_seaside_frog"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_4_PURCHASED, ["EVENT_991_seaside_frog"]),
        JmpIfBitClear(FROG_DISCIPLE_ITEM_5_PURCHASED, ["EVENT_991_seaside_frog"]),
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_949_sea_open"]),
        JmpIfBitClear(SEASIDE_BOSS_SET, ["EVENT_949_sea_open"]),
        StoreItemAmountTo7000(ShedKey),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_seaside"]),
        JmpIfBitClear(
            MAP_SEA, ["EVENT_949_lands_end_1"], identifier="EVENT_949_sea_open"
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R134_SEA_AREA_03_SUPER_STAR_ROOM, ["EVENT_991_sea"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["EVENT_991_sea"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["EVENT_991_sea"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT, ["EVENT_991_sea"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS, ["EVENT_991_sea"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS,
            ["EVENT_991_ship"],
        ),
        JmpIfBitClear(SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED, ["EVENT_991_ship"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN,
            ["EVENT_991_ship"],
        ),
        JmpIfBitClear(SHIP_TROOPA_PRIZE, ["EVENT_991_ship"]),
        JmpIfBitClear(UNKNOWN_707D_1, ["EVENT_991_ship"]),
        JmpIfBitClear(SHIP_MAZE_PRIZE, ["EVENT_991_ship"]),
        JmpIfBitClear(SHIP_CANNONBALL_PRIZE, ["EVENT_991_ship"]),
        JmpIfBitClear(UNKNOWN_707D_5, ["EVENT_991_ship"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["EVENT_991_ship"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_5,
            R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER,
            ["EVENT_991_ship"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R137_LANDS_END_AREA_01,
            ["EVENT_991_lands_end"],
            identifier="EVENT_949_lands_end_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6, R138_LANDS_END_AREA_02, ["EVENT_991_lands_end"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7, R138_LANDS_END_AREA_02, ["EVENT_991_lands_end"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6, R141_LANDS_END_AREA_04_ROTATING_FLOWERS, ["EVENT_991_lands_end"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7,
            R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            ["EVENT_991_lands_end_secret"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            ["EVENT_991_lands_end_secret"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
            ["EVENT_991_lands_end_secret"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5, R263_LANDS_END_UNDERGROUND_AREA_01, ["EVENT_991_lands_end"]
        ),
        JmpIfBitClear(LANDS_END_CHEST_1_USED, ["EVENT_991_lands_end"]),
        JmpIfBitClear(LANDS_END_CHEST_2_USED, ["EVENT_991_lands_end"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_949_temple"]),
        JmpIfBitClear(UNKNOWN_LARGE_CONVEYOR_ROOM, ["EVENT_991_lands_end"]),
        JmpIfBitClear(
            BELOME_TEMPLE_OPEN, ["EVENT_949_mtown_open"], identifier="EVENT_949_temple"
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, ["EVENT_991_temple"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_8,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_991_temple"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_991_temple"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_991_temple"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_991_temple"]
        ),
        StoreItemAmountTo7000(TempleKey),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_temple"]),
        JmpIfBitClear(TEMPLE_KEY_USED, ["EVENT_949_mtown_open"]),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_5,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_6,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_7,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_8,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_9,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_10,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_11,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_13,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_14,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_15,
            R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            ["EVENT_991_temple"],
        ),
        JmpIfBitClear(
            MAP_MONSTRO_TOWN, ["EVENT_949_valley_1"], identifier="EVENT_949_mtown_open"
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R267_MONSTRO_TOWN_ENTRANCE, ["EVENT_991_monstro"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["EVENT_991_monstro"]
        ),
        StoreItemAmountTo7000(BigBooFlag),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_valley_1"]),
        StoreItemAmountTo7000(DryBonesFlag),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_valley_1"]),
        StoreItemAmountTo7000(GreaperFlag),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_949_valley_1"]),
        Jmp(["EVENT_991_monstro"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R252_BEAN_VALLEY_MAIN_AREA,
            ["EVENT_991_bean"],
            identifier="EVENT_949_valley_1",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4, R252_BEAN_VALLEY_MAIN_AREA, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5,
            R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            ["EVENT_991_bean"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7,
            R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            ["EVENT_991_bean"],
        ),
        JmpIfBitClear(BEAN_VALLEY_BIG_PIPE_ROOM_INVISIBLE_ITEM, ["EVENT_991_bean"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_13, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["EVENT_991_bean"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_6, R379_BEAN_VALLEY_BEANSTALKS_AREA_02, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_7,
            R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02,
            ["EVENT_991_beanstalk"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, ["EVENT_991_beanstalk"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_3, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["EVENT_991_beanstalk"]
        ),
        JmpIfBitSet(CASINO_PRIZE_WON, ["EVENT_949_nimbus_1"]),
        StoreItemAmountTo7000(BrightCard),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_casino"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R344_NIMBUS_LAND_ITEM_SHOP,
            ["EVENT_991_nimbus_proper"],
            identifier="EVENT_949_nimbus_1",
        ),
        JmpIfBitClear(NIMBUS_INN_PRIZE_GRANTED, ["EVENT_991_nimbus_proper"]),
        JmpIfBitClear(BLUE_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_991_nimbus_castle"],
        ),
        StoreItemAmountTo7000(CastleKey1),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_949_has_ck2"]),
        JmpIfObjectInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_949_volcano_open"],
        ),
        StoreItemAmountTo7000(CastleKey2, identifier="EVENT_949_has_ck2"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_949_nimbus_9"]),
        JmpIfObjectInSpecificLevel(
            NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_949_volcano_open"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_991_nimbus_castle"],
            identifier="EVENT_949_nimbus_9",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            ["EVENT_991_nimbus_castle"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING,
            ["EVENT_991_nimbus_proper"],
        ),
        JmpIfBitClear(NIMBUS_HOUSE_ITEM_SUMMONED, ["EVENT_991_lands_end"]),
        JmpIfObjectInSpecificLevel(
            NPC_5,
            R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING,
            ["EVENT_991_nimbus_proper"],
        ),
        JmpIfBitClear(
            NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED, ["EVENT_991_nimbus_castle"]
        ),
        JmpIfBitClear(
            MAP_BARREL_VOLCANO,
            ["EVENT_949_is_keep_open"],
            identifier="EVENT_949_volcano_open",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2, R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS, ["EVENT_991_volcano"]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_4, R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES, ["EVENT_991_volcano"]
        ),
        JmpIfObjectInSpecificLevel(NPC_1, R358_VOLCANO_AREA_11, ["EVENT_991_volcano"]),
        JmpIfObjectInSpecificLevel(NPC_2, R358_VOLCANO_AREA_11, ["EVENT_991_volcano"]),
        JmpIfObjectInSpecificLevel(NPC_1, R361_VOLCANO_AREA_09, ["EVENT_991_volcano"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R384_VOLCANO_AREA_05, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R384_VOLCANO_AREA_05, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R385_VOLCANO_AREA_06, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R366_VOLCANO_AREA_13_WSAVE_POINT, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R366_VOLCANO_AREA_13_WSAVE_POINT, ["EVENT_991_volcano"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP, ["EVENT_991_volcano"]
        ),
        JmpIfBitClear(
            MAP_VISTA_HILL,
            ["EVENT_949_mtown_open_2"],
            identifier="EVENT_949_is_keep_open",
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            ["EVENT_991_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM,
            ["EVENT_991_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM,
            ["EVENT_991_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5,
            R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7,
            R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_10,
            R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_11,
            R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_12,
            R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_13,
            R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_8,
            R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5,
            R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7,
            R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_4,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_5,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["EVENT_991_deep_keep"],
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 512),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        SetVarToConst(PRIMARY_TEMP_7000, 514),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        SetVarToConst(PRIMARY_TEMP_7000, 515),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        SetVarToConst(PRIMARY_TEMP_7000, 516),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        SetVarToConst(PRIMARY_TEMP_7000, 517),
        JmpIfMem704XAt7000BitClear(["EVENT_991_deep_keep"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, ["EVENT_991_keep"]
        ),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, ["EVENT_949_mtown_open_2"]),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1, R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT, ["EVENT_991_factory"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_7, R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, ["EVENT_991_factory"]
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_6,
            R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_2,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_8,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_9,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_1,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["EVENT_991_factory"],
        ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_3,
            R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            ["EVENT_991_factory"],
        ),
        JmpIfBitClear(TOAD_SHOP_FREEBIE_RECEIVED, ["EVENT_991_factory"]),
        JmpIfBitClear(
            MAP_MONSTRO_TOWN, ["EVENT_949_end"], identifier="EVENT_949_mtown_open_2"
        ),
        JmpIfBitClear(SUPER_JUMP_PRIZE_2_GRANTED, ["EVENT_991_sj"]),
        RunDialog(
            dialog_id=DI2758_FROGFUCIUS_DEFAULT_STUFF,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_949_end",
        ),
        Return(),
    ]
)
