# pylint: disable=C0301

"""E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BATTLE_DOOR_STAR_PIECE, ["EVENT_3400_exor_eject"]),
        JmpIfBitSet(UNUSED_7093_3, ["EVENT_3400_v"]),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3400_play_marrymore_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 7, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 9, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 12, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 10, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 16, ["EVENT_3400_play_marios_pad_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 17, ["EVENT_3400_play_mushroom_kingdom_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 18, ["EVENT_3400_play_mushroom_kingdom_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 20, ["EVENT_3400_play_mushroom_kingdom_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 24, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 25, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 26, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 27, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 28, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 31, ["EVENT_3400_play_mushroom_kingdom_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 33, ["EVENT_3400_play_yoster_isle_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 34, ["EVENT_3400_play_yoster_isle_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 35, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 36, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 37, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 38, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 39, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 40, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 41, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 42, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 43, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 48, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 55, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 56, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 57, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 58, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 59, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 60, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 61, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 62, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_3400_play_marrymore_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 65, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 66, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 67, ["EVENT_3400_play_midas_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 72, ["EVENT_3400_play_midas_tunnel_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 73, ["EVENT_3400_play_midas_tunnel_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 74, ["EVENT_3400_play_melody_bay_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 75, ["EVENT_3400_play_tadpole_pond_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 76, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 77, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 78, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 79, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 80, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 81, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 82, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 83, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 84, ["EVENT_3400_play_rose_town_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 85, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 86, ["EVENT_3400_play_rose_town_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 87, ["EVENT_3400_determine_rose_town_shop_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 92, ["EVENT_3400_play_casino_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 93, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 94, ["EVENT_3400_play_rose_town_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 95, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 96, ["EVENT_3400_play_rose_town_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 97, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 98, ["EVENT_3400_play_rose_town_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 100, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 101, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 102, ["EVENT_3400_play_moleville_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 103, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 107, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 108, ["EVENT_3400_play_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 109, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 110, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 111, ["EVENT_3400_play_valentina_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 112, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 113, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 114, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 115, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 116, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 117, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 118, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 119, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 120, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 121, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 122, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 123, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 124, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 125, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 126, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 127, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 129, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 130, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 131, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 132, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 133, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 134, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 135, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 136, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 137, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 138, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 139, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 141, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 142, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 143, ["EVENT_3400_play_pipe_vault_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 144, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 152, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 154, ["EVENT_3400_determine_marrymore_music_speed"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 155, ["EVENT_3400_play_marrymore_music_indoors"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 158, ["EVENT_3400_play_star_hill_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 159, ["EVENT_3400_play_star_hill_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 160, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 161, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 162, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 163, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 164, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 165, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 166, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 167, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 168, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 169, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 170, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 171, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 172, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 173, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 174, ["EVENT_3400_play_sea_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 175, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 176, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 177, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 178, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 179, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 180, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 181, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 182, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 183, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 184, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 185, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 186, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 187, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 188, ["EVENT_3400_play_sunken_ship_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 189, ["EVENT_3400_play_marios_pad_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 190, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 191, ["EVENT_3400_play_mushroom_kingdom_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 192, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 193, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 194, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 195, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 196, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 197, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 198, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 199, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 200, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 201, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 202, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 203, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 204, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 205, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 206, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 207, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 208, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 217, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 220, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 221, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 222, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 223, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 224, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 225, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 226, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 227, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 228, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 229, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 230, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 231, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 233, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 235, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 236, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 237, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 238, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 239, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 251, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 252, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 253, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 254, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 255, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 256, ["EVENT_3400_play_forest_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 258, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 259, ["EVENT_3400_play_booster_tower_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 262, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 263, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 264, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 265, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 266, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 267, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 268, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 270, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 272, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 273, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 274, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 275, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 276, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 277, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 278, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 279, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 280, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 281, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 282, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 283, ["EVENT_3400_determine_moleville_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 284, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 285, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 286, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 287, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 288, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 289, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 290, ["EVENT_3400_play_moleville_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 301, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 302, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 303, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 313, ["EVENT_3400_play_seaside_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 314, ["EVENT_3400_determine_seaside_indoor_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 316, ["EVENT_3400_play_seaside_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 317, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 318, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 319, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 321, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 322, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 323, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 324, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 325, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 326, ["EVENT_3400_play_occupied_music_only_if_occupied"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 327, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 328, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 329, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 330, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 331, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 332, ["EVENT_3400_play_occupied_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 333, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 334, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 335, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 337, ["EVENT_3400_play_moleville_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 339, ["EVENT_3400_play_moleville_indoor_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 341, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 342, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 343, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 344, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 345, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 346, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 347, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 348, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 349, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 350, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 353, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 354, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 355, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 356, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 357, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 358, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 359, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 360, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 361, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 362, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 363, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 364, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 365, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 366, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 367, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 368, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 369, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 370, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 371, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 372, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 373, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 374, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 376, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 377, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 378, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 379, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 380, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 381, ["EVENT_3400_play_overworld_2_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 383, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 384, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 385, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 386, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 387, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 388, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 389, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 390, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 391, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 392, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 393, ["EVENT_3400_play_volcano_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 394, ["EVENT_3400_play_axem_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 395, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 397, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 398, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 399, ["EVENT_3400_play_monstro_town_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 400, ["EVENT_3400_boomer_eject"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 401, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 402, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 403, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 404, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 405, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 406, ["EVENT_3400_play_inner_factory_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 407, ["EVENT_3400_play_overworld_1_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 408, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 409, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 410, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 411, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 412, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 413, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 414, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 415, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 416, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 417, ["EVENT_3400_play_rose_town_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 419, ["EVENT_3400_play_rose_town_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 420, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 424, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 426, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 428, ["EVENT_3400_play_dungeon_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 430, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 431, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 433, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 434, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 435, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 436, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 437, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 438, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 439, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 440, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 442, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 444, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 445, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 446, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 447, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 448, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 449, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 450, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 451, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 452, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 453, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 454, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 455, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 456, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 457, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 458, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 459, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 460, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 461, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 462, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 463, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 464, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 465, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 466, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 467, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 468, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 469, ["EVENT_3400_play_inner_factory_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 470, ["EVENT_3400_play_inner_factory_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 471, ["EVENT_3400_play_inner_factory_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 472, ["EVENT_3400_play_inner_factory_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 473, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 474, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 475, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 476, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 477, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 478, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 479, ["EVENT_3400_play_bowsers_keep_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 480, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 481, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 482, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 483, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 487, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 490, ["EVENT_3400_play_mushroom_kingdom_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 491, ["EVENT_3400_play_mushroom_kingdom_indoor_music"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            492,
            ["EVENT_3400_determine_mushroom_kingdom_indoor_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            493,
            ["EVENT_3400_determine_mushroom_kingdom_indoor_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 497, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 498, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 499, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 500, ["EVENT_3400_play_nimbus_music"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 501, ["EVENT_3400_determine_nimbus_music"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 507, ["EVENT_3400_play_factory_music"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 508, ["EVENT_3400_play_factory_music"]),
        Return(),
        FadeOutMusicToVolume(
            duration=1, volume=96, identifier="EVENT_3400_play_marrymore_music_indoors"
        ),
        PlayMusicAtCurrentVolume(
            M39_MARRYMORE, identifier="EVENT_3400_play_marrymore_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M02_MUSHROOM_KINGDOM, identifier="EVENT_3400_play_mushroom_kingdom_music"
        ),
        Return(),
        JmpIfBitClear(
            MUSHROOM_KINGDOM_OCCUPIED,
            ["EVENT_3400_play_mushroom_kingdom_indoor_music"],
            identifier="EVENT_3400_determine_mushroom_kingdom_indoor_music"),
        JmpIfBitClear(
            MUSHROOM_KINGDOM_LIBERATED, ["EVENT_3400_play_occupied_indoor_music"]
        ),
        PlayMusicAtCurrentVolume(
            M02_MUSHROOM_KINGDOM,
            identifier="EVENT_3400_play_mushroom_kingdom_indoor_music"),
        FadeOutMusicToVolume(duration=1, volume=96),
        Return(),
        PlayMusicAtCurrentVolume(
            M41_SUNKEN_SHIP, identifier="EVENT_3400_play_sunken_ship_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M04_YOSTER_ISLAND, identifier="EVENT_3400_play_yoster_isle_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M32_AND_MY_NAMES_BOOSTER, identifier="EVENT_3400_play_booster_tower_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M27_DUNGEON_IS_FULL_OF_MONSTERS, identifier="EVENT_3400_play_dungeon_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M22_MIDAS_RIVER, identifier="EVENT_3400_play_midas_music"
        ),
        Return(),
        PlayMusicAtCurrentVolume(
            M22_MIDAS_RIVER, identifier="EVENT_3400_play_midas_tunnel_music"
        ),
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        Return(),
        PlayMusicAtDefaultVolume(
            M17_TADPOLE_POND, identifier="EVENT_3400_play_melody_bay_music"
        ),
        DeactivateSoundChannels([0, 1, 2, 3]),
        Return(),
        PlayMusicAtDefaultVolume(
            M17_TADPOLE_POND, identifier="EVENT_3400_play_tadpole_pond_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
            identifier="EVENT_3400_play_overworld_2_music"),
        Return(),
        PlayMusicAtDefaultVolume(
            M13_ROAD_IS_FULL_OF_DANGERS, identifier="EVENT_3400_play_overworld_1_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M18_ROSE_TOWN, identifier="EVENT_3400_play_rose_town_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M18_ROSE_TOWN, identifier="EVENT_3400_play_rose_town_indoor_music"
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        Return(),
        PlayMusicAtDefaultVolume(
            M15_HERES_SOME_WEAPONS, identifier="EVENT_3400_play_occupied_music"
        ),
        Return(),
        JmpIfBitClear(
            MUSHROOM_KINGDOM_LIBERATED,
            ["EVENT_3400_play_occupied_music"],
            identifier="EVENT_3400_play_occupied_music_only_if_occupied"),
        Return(),
        JmpIfBitSet(
            FOREST_LIBERATED,
            ["EVENT_3400_play_rose_town_indoor_music"],
            identifier="EVENT_3400_determine_rose_town_shop_music"),
        PlayMusicAtDefaultVolume(
            M15_HERES_SOME_WEAPONS, identifier="EVENT_3400_play_occupied_indoor_music"
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        Return(),
        PlayMusicAtDefaultVolume(
            M47_GRATE_GUYS_CASINO, identifier="EVENT_3400_play_casino_music"
        ),
        Return(),
        JmpIfBitSet(
            MINECART_CLEARED,
            ["EVENT_3400_play_moleville_music"],
            identifier="EVENT_3400_determine_moleville_music"),
        Jmp(["EVENT_3400_play_dungeon_music"]),
        PlayMusicAtDefaultVolume(
            M33_MOLEVILLE, identifier="EVENT_3400_play_moleville_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M33_MOLEVILLE, identifier="EVENT_3400_play_moleville_indoor_music"
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        Return(),
        PlayMusicAtDefaultVolume(
            M50_NIMBUS_LAND, identifier="EVENT_3400_play_nimbus_music"
        ),
        Return(),
        JmpIfBitSet(
            NIMBUS_LAND_LIBERATED,
            ["EVENT_3400_play_nimbus_music"],
            identifier="EVENT_3400_determine_nimbus_music"),
        PlayMusicAtDefaultVolume(
            M61_VALENTINA, identifier="EVENT_3400_play_valentina_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M07_PIPE_VAULT, identifier="EVENT_3400_play_pipe_vault_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M66_BOWSERS_CASTLE_2ND_TIME, identifier="EVENT_3400_play_bowsers_keep_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M14_MARIOS_PAD, identifier="EVENT_3400_play_marios_pad_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M05_SEASIDE_TOWN, identifier="EVENT_3400_play_seaside_music"
        ),
        Return(),
        JmpIfBitClear(
            SEASIDE_LIBERATED,
            ["EVENT_3400_play_occupied_indoor_music"],
            identifier="EVENT_3400_determine_seaside_indoor_music"),
        PlayMusicAtDefaultVolume(
            M05_SEASIDE_TOWN, identifier="EVENT_3400_play_seaside_indoor_music"
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        Return(),
        PlayMusicAtDefaultVolume(
            M26_FOREST_MAZE, identifier="EVENT_3400_play_forest_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M67_WEAPONS_FACTORY, identifier="EVENT_3400_play_factory_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M51_MONSTRO_TOWN, identifier="EVENT_3400_play_monstro_town_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M62_BARREL_VOLCANO, identifier="EVENT_3400_play_volcano_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(
            M56_FACTORY, identifier="EVENT_3400_play_inner_factory_music"
        ),
        Return(),
        PlayMusicAtDefaultVolume(M44_SEA, identifier="EVENT_3400_play_sea_music"),
        Return(),
        PlayMusicAtDefaultVolume(
            M63_AXEM_RANGERS_DROP_IN, identifier="EVENT_3400_play_axem_music"
        ),
        Return(),
        JmpIfBitClear(
            MARRYMORE_LIBERATED,
            ["EVENT_3400_play_marrymore_music_indoors"],
            identifier="EVENT_3400_determine_marrymore_music_speed"),
        SpeedUpMusicTempoBy(duration=0, change=12),
        Jmp(["EVENT_3400_play_marrymore_music_indoors"]),
        Return(),
        PlayMusicAtDefaultVolume(
            M34_STAR_HILL, identifier="EVENT_3400_play_star_hill_music"
        ),
        Return(),
        ClearBit(UNUSED_7093_3, identifier="EVENT_3400_v"),
        ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True),
        Return(),
        JmpToEvent(E2226_KEEP_3RD_BOSS, identifier="EVENT_3400_boomer_eject"),
        ClearBit(BATTLE_DOOR_STAR_PIECE, identifier="EVENT_3400_exor_eject"),
        JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
    ]
)
