
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": "EVENT_3400_exor",
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 4, 'EVENT_3400_exor_eject']
    },
    {
        "identifier": "EVENT_3400_axem",
        "command": 'jmp_if_bit_set',
        "args": [0x7093, 3, "EVENT_3400_v"]
    },
    {
        "identifier": "EVENT_3400_check_room",
        "command": "set_7000_to_current_level"
    },
    {
        "identifier": "EVENT_3400_room_5_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 5, 'EVENT_3400_play_marrymore_music']
    },
    {
        "identifier": "EVENT_3400_room_7_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 7, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_9_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 9, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_12_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 12, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_10_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 10, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_16_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 16, 'EVENT_3400_play_marios_pad_music']
    },
    {
        "identifier": "EVENT_3400_room_17_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 17, "EVENT_3400_play_mushroom_kingdom_music"]
    },
    {
        "identifier": "EVENT_3400_room_18_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 18, 'EVENT_3400_play_mushroom_kingdom_music']
    },
    {
        "identifier": "EVENT_3400_room_20_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 20, "EVENT_3400_play_mushroom_kingdom_music"]
    },
    {
        "identifier": "EVENT_3400_room_24_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 24, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_25_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 25, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_26_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 26, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_27_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 27, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_28_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 28, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_31_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 31, "EVENT_3400_play_mushroom_kingdom_music"]
    },
    {
        "identifier": "EVENT_3400_room_33_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 33, "EVENT_3400_play_yoster_isle_music"]
    },
    {
        "identifier": "EVENT_3400_room_34_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 34, "EVENT_3400_play_yoster_isle_music"]
    },
    {
        "identifier": "EVENT_3400_room_35_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 35, "EVENT_3400_play_booster_tower_music"]
    },
    {
        "identifier": "EVENT_3400_room_36_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 36, "EVENT_3400_play_booster_tower_music"]
    },
    {
        "identifier": "EVENT_3400_room_37_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 37, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_38_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 38, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_39_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 39, "EVENT_3400_play_booster_tower_music"]
    },
    {
        "identifier": "EVENT_3400_room_40_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 40, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_41_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 41, "EVENT_3400_play_booster_tower_music"]
    },
    {
        "identifier": "EVENT_3400_room_42_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 42, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_43_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 43, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_48_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 48, "EVENT_3400_play_booster_tower_music"]
    },
    {
        "identifier": "EVENT_3400_room_55_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 55, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_56_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 56, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_57_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 57, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_58_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 58, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_59_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 59, "EVENT_3400_play_dungeon_music"]
    },
    {
        "identifier": "EVENT_3400_room_60_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 60, "EVENT_3400_play_dungeon_music"]
    },
    {
        "identifier": "EVENT_3400_room_61_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 61, "EVENT_3400_play_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_62_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 62, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_64_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 64, 'EVENT_3400_play_marrymore_music']
    },
    {
        "identifier": "EVENT_3400_room_65_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 65, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_66_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 66, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_67_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 67, "EVENT_3400_play_midas_music"]
    },
    {
        "identifier": "EVENT_3400_room_72_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 72, "EVENT_3400_play_midas_tunnel_music"]
    },
    {
        "identifier": "EVENT_3400_room_73_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 73, "EVENT_3400_play_midas_tunnel_music"]
    },
    {
        "identifier": "EVENT_3400_room_74_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 74, "EVENT_3400_play_melody_bay_music"]
    },
    {
        "identifier": "EVENT_3400_room_75_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 75, "EVENT_3400_play_tadpole_pond_music"]
    },
    {
        "identifier": "EVENT_3400_room_76_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 76, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_77_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 77, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_78_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 78, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_79_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 79, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_80_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 80, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_81_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 81, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_82_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 82, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_83_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 83, "EVENT_3400_play_occupied_music"]
    },
    {
        "identifier": "EVENT_3400_room_84_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 84, "EVENT_3400_play_rose_town_music"]
    },
    {
        "identifier": "EVENT_3400_room_85_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 85, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_86_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 86, "EVENT_3400_play_rose_town_indoor_music"]
    },
    {
        "identifier": "EVENT_3400_room_87_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 87, 'EVENT_3400_determine_rose_town_shop_music']
    },
    {
        "identifier": "EVENT_3400_room_92_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 92, 'EVENT_3400_play_casino_music']
    },
    {
        "identifier": "EVENT_3400_room_93_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 93, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_94_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 94, 'EVENT_3400_play_rose_town_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_95_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 95, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_96_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 96, 'EVENT_3400_play_rose_town_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_97_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 97, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_98_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 98, 'EVENT_3400_play_rose_town_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_100_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 100, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_101_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 101, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_102_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 102, "EVENT_3400_play_moleville_music"]
    },
    {
        "identifier": "EVENT_3400_room_103_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 103, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_107_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 107, "EVENT_3400_play_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_108_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 108, "EVENT_3400_play_moleville_music"]
    },
    {
        "identifier": "EVENT_3400_room_109_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 109, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_110_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 110, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_111_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 111, 'EVENT_3400_play_valentina_music']
    },
    {
        "identifier": "EVENT_3400_room_112_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 112, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_113_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 113, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_114_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 114, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_115_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 115, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_116_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 116, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_117_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 117, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_118_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 118, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_119_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 119, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_120_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 120, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_121_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 121, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_122_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 122, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_123_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 123, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_124_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 124, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_125_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 125, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_126_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 126, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_127_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 127, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_128_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 128, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_129_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 129, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_130_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 130, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_131_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 131, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_132_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 132, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_133_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 133, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_134_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 134, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_135_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 135, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_136_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 136, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_137_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 137, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_138_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 138, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_139_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 139, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_141_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 141, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_142_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 142, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_143_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 143, 'EVENT_3400_play_pipe_vault_music']
    },
    {
        "identifier": "EVENT_3400_room_144_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 144, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_152_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 152, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_154_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 154, 'EVENT_3400_determine_marrymore_music_speed']
    },
    {
        "identifier": "EVENT_3400_room_155_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 155, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_room_158_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 158, "EVENT_3400_play_star_hill_music"]
    },
    {
        "identifier": "EVENT_3400_room_159_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 159, "EVENT_3400_play_star_hill_music"]
    },
    {
        "identifier": "EVENT_3400_room_160_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 160, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_161_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 161, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_162_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 162, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_163_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 163, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_164_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 164, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_165_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 165, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_166_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 166, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_167_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 167, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_168_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 168, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_169_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 169, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_170_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 170, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_171_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 171, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_172_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 172, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_173_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 173, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_174_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 174, 'EVENT_3400_play_sea_music']
    },
    {
        "identifier": "EVENT_3400_room_175_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 175, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_176_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 176, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_177_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 177, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_178_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 178, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_179_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 179, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_180_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 180, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_181_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 181, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_182_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 182, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_183_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 183, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_184_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 184, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_185_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 185, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_186_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 186, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_187_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 187, 'EVENT_3400_play_sunken_ship_music']
    },
    {
        "identifier": "EVENT_3400_room_188_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 188, "EVENT_3400_play_sunken_ship_music"]
    },
    {
        "identifier": "EVENT_3400_room_189_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 189, 'EVENT_3400_play_marios_pad_music']
    },
    {
        "identifier": "EVENT_3400_room_190_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 190, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_191_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 191, 'EVENT_3400_play_mushroom_kingdom_music']
    },
    {
        "identifier": "EVENT_3400_room_192_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 192, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_193_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 193, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_194_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 194, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_195_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 195, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_196_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 196, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_197_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 197, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_198_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 198, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_199_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 199, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_200_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 200, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_201_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 201, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_202_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 202, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_203_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 203, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_204_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 204, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_205_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 205, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_206_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 206, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_207_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 207, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_208_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 208, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_217_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 217, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_220_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 220, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_221_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 221, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_222_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 222, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_223_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 223, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_224_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 224, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_225_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 225, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_226_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 226, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_227_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 227, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_228_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 228, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_229_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 229, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_230_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 230, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_231_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 231, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_232_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 232, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_233_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 233, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_234_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 234, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_235_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 235, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_236_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 236, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_237_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 237, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_238_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 238, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_239_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 239, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_242_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 242, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_251_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 251, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_252_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 252, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_253_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 253, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_254_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 254, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_255_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 255, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_256_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 256, 'EVENT_3400_play_forest_music']
    },
    {
        "identifier": "EVENT_3400_room_258_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 258, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_259_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 259, 'EVENT_3400_play_booster_tower_music']
    },
    {
        "identifier": "EVENT_3400_room_262_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 262, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_263_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 263, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_264_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 264, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_265_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 265, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_266_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 266, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_267_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 267, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_268_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 268, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_270_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 270, 'EVENT_3400_play_dungeon_music']
    },
    # dont need 271 - it automatically fades in from parent event
    {
        "identifier": "EVENT_3400_room_272_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 272, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_273_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 273, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_274_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 274, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_275_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 275, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_276_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 276, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_277_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 277, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_278_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 278, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_279_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 279, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_280_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 280, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_281_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 281, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_282_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 282, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_283_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 283, 'EVENT_3400_determine_moleville_music']
    },
    {
        "identifier": "EVENT_3400_room_284_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 284, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_285_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 285, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_286_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 286, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_287_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 287, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_288_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 288, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_289_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 289, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_290_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 290, "EVENT_3400_play_moleville_music"]
    },
    {
        "identifier": "EVENT_3400_room_301_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 301, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_302_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 302, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_303_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 303, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_313_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 313, 'EVENT_3400_play_seaside_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_314_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 314, 'EVENT_3400_determine_seaside_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_316_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 316, 'EVENT_3400_play_seaside_music']
    },
    {
        "identifier": "EVENT_3400_room_317_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 317, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_318_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 318, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_319_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 319, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_321_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 321, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_322_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 322, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_323_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 323, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_324_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 324, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_325_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 325, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_326_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 326, 'EVENT_3400_play_occupied_music_only_if_occupied']
    },
    {
        "identifier": "EVENT_3400_room_327_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 327, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_328_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 328, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_329_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 329, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_330_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 330, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_331_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 331, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_332_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 332, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_room_333_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 333, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_334_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 334, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_335_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 335, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_337_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 337, "EVENT_3400_play_moleville_indoor_music"]
    },
    {
        "identifier": "EVENT_3400_room_339_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 339, "EVENT_3400_play_moleville_indoor_music"]
    },
    {
        "identifier": "EVENT_3400_room_341_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 341, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_342_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 342, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_343_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 343, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_344_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 344, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_345_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 345, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_346_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 346, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_347_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 347, 'EVENT_3400_play_overworld_2_music']
    },
    {
        "identifier": "EVENT_3400_room_348_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 348, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_349_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 349, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_350_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 350, "EVENT_3400_play_overworld_2_music"]
    },
    # dont need 351 - it automatically fades in from parent event
    {
        "identifier": "EVENT_3400_room_352_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 352, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_353_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 353, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_354_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 354, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_355_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 355, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_356_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 356, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_357_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 357, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_358_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 358, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_359_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 359, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_360_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 360, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_361_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 361, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_362_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 362, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_363_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 363, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_364_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 364, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_365_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 365, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_366_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 366, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_367_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 367, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_368_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 368, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_369_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 369, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_370_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 370, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_371_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 371, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_372_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 372, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_373_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 373, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_374_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 374, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_376_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 376, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_377_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 377, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_378_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 378, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_379_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 379, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_380_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 380, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_381_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 381, "EVENT_3400_play_overworld_2_music"]
    },
    {
        "identifier": "EVENT_3400_room_383_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 383, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_384_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 384, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_385_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 385, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_386_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 386, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_387_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 387, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_388_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 388, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_389_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 389, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_390_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 390, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_391_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 391, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_392_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 392, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_393_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 393, 'EVENT_3400_play_volcano_music']
    },
    {
        "identifier": "EVENT_3400_room_394_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 394, 'EVENT_3400_play_axem_music']
    },
    {
        "identifier": "EVENT_3400_room_395_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 395, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_397_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 397, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_398_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 398, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_399_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 399, 'EVENT_3400_play_monstro_town_music']
    },
    {
        "identifier": "EVENT_3400_room_400_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 400, 'EVENT_3400_boomer_eject']
    },
    {
        "identifier": "EVENT_3400_room_401_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 401, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_402_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 402, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_403_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 403, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_404_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 404, 'EVENT_3400_play_overworld_1_music']
    },
    {
        "identifier": "EVENT_3400_room_405_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 405, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_406_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 406, "EVENT_3400_play_inner_factory_music"]
    },
    {
        "identifier": "EVENT_3400_room_407_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 407, "EVENT_3400_play_overworld_1_music"]
    },
    {
        "identifier": "EVENT_3400_room_408_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 408, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_409_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 409, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_410_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 410, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_411_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 411, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_412_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 412, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_413_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 413, "EVENT_3400_play_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_414_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 414, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_415_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 415, "EVENT_3400_determine_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_416_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 416, "EVENT_3400_play_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_417_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 417, "EVENT_3400_play_rose_town_music"]
    },
    {
        "identifier": "EVENT_3400_room_419_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 419, "EVENT_3400_play_rose_town_music"]
    },
    {
        "identifier": "EVENT_3400_room_420_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 420, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_421_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 421, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_422_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 422, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_424_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 424, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_425_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 425, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_426_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 426, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_428_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 428, 'EVENT_3400_play_dungeon_music']
    },
    {
        "identifier": "EVENT_3400_room_430_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 430, "EVENT_3400_play_nimbus_music"]
    },
    {
        "identifier": "EVENT_3400_room_431_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 431, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_433_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 433, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_434_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 434, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_435_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 435, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_436_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 436, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_437_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 437, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_438_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 438, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_439_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 439, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_440_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 440, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_442_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 442, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_443_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 443, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_444_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 444, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_445_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 445, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_446_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 446, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_447_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 447, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_448_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 448, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_449_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 449, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_450_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 450, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_451_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 451, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_452_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 452, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_453_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 453, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_454_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 454, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_455_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 455, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_456_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 456, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_457_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 457, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_458_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 458, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_459_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 459, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_460_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 460, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_461_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 461, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_462_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 462, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_463_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 463, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_464_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 464, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_465_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 465, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_466_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 466, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_467_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 467, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_468_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 468, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_469_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 469, 'EVENT_3400_play_inner_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_470_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 470, 'EVENT_3400_play_inner_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_471_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 471, 'EVENT_3400_play_inner_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_472_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 472, 'EVENT_3400_play_inner_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_473_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 473, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_474_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 474, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_475_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 475, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_476_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 476, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_477_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 477, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_478_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 478, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_479_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 479, 'EVENT_3400_play_bowsers_keep_music']
    },
    {
        "identifier": "EVENT_3400_room_480_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 480, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_481_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 481, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_482_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 482, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_483_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 483, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_487_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 487, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_490_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 490, 'EVENT_3400_play_mushroom_kingdom_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_491_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 491, 'EVENT_3400_play_mushroom_kingdom_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_492_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 492, 'EVENT_3400_determine_mushroom_kingdom_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_493_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 493, 'EVENT_3400_determine_mushroom_kingdom_indoor_music']
    },
    {
        "identifier": "EVENT_3400_room_497_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 497, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_498_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 498, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_499_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 499, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_500_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 500, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_501_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 501, 'EVENT_3400_determine_nimbus_music']
    },
    {
        "identifier": "EVENT_3400_room_507_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 507, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_room_508_jump",
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 508, 'EVENT_3400_play_factory_music']
    },
    {
        "identifier": "EVENT_3400_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_marrymore_music_indoors",
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_marrymore_music",
        "command": 'play_music_current_volume',
        "args": [Music._39_MARRYMORE]
    },
    {
        "identifier": "EVENT_3400_play_marrymore_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_mushroom_kingdom_music",
        "command": 'play_music_current_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": "EVENT_3400_play_mushroom_kingdom_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_determine_mushroom_kingdom_indoor_music',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 7, "EVENT_3400_play_mushroom_kingdom_indoor_music"]
    },
    {
        "identifier": 'EVENT_3400_determine_mushroom_kingdom_indoor_music_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 0, "EVENT_3400_play_occupied_indoor_music"]
    },
    {
        "identifier": "EVENT_3400_play_mushroom_kingdom_indoor_music",
        "command": 'play_music_current_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": "EVENT_3400_play_mushroom_kingdom_indoor_music_",
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_mushroom_kingdom_indoor)music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_sunken_ship_music",
        "command": 'play_music_current_volume',
        "args": [Music._41_SUNKEN_SHIP]
    },
    {
        "identifier": "EVENT_3400_play_sunken_ship_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_yoster_isle_music",
        "command": 'play_music_current_volume',
        "args": [Music._04_YOSTER_ISLAND]
    },
    {
        "identifier": "EVENT_3400_play_yoster_isle_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_booster_tower_music",
        "command": 'play_music_current_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": "EVENT_3400_play_booster_tower_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_dungeon_music",
        "command": 'play_music_current_volume',
        "args": [Music._27_DUNGEON_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": "EVENT_3400_play_dungeon_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_midas_music",
        "command": 'play_music_current_volume',
        "args": [Music._22_MIDAS_RIVER]
    },
    {
        "identifier": "EVENT_3400_play_midas_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_play_midas_tunnel_music",
        "command": 'play_music_current_volume',
        "args": [Music._22_MIDAS_RIVER]
    },
    {
        "identifier": 'EVENT_3400_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [2, 96]
    },
    {
        "identifier": 'EVENT_3400_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4]
    },
    {
        "identifier": "EVENT_3400_play_midas_tunnel_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_melody_bay_music',
        "command": 'play_music_default_volume',
        "args": [Music._17_TADPOLE_POND]
    },
    {
        "identifier": 'EVENT_3400_deactivate_sound_channels_1',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]]
    },
    {
        "identifier": "EVENT_3400_play_melody_bay_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_tadpole_pond_music',
        "command": 'play_music_default_volume',
        "args": [Music._17_TADPOLE_POND]
    },
    {
        "identifier": "EVENT_3400_play_tadpole_pond_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_overworld_2_music',
        "command": 'play_music_default_volume',
        "args": [Music._42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": "EVENT_3400_play_overworld_2_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_overworld_1_music',
        "command": 'play_music_default_volume',
        "args": [Music._13_ROAD_IS_FULL_OF_DANGERS]
    },
    {
        "identifier": "EVENT_3400_play_overworld_1_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_rose_town_music',
        "command": 'play_music_default_volume',
        "args": [Music._18_ROSE_TOWN]
    },
    {
        "identifier": "EVENT_3400_play_rose_town_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_rose_town_indoor_music',
        "command": 'play_music_default_volume',
        "args": [Music._18_ROSE_TOWN]
    },
    {
        "identifier": "EVENT_3400_play_rose_town_indoor_music_1",
        "command": "fade_out_music_to_volume",
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_rose_town_indoor_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_occupied_music',
        "command": 'play_music_default_volume',
        "args": [Music._15_HERES_SOME_WEAPONS]
    },
    {
        "identifier": "EVENT_3400_play_occupied_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_occupied_music_only_if_occupied',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 0, 'EVENT_3400_play_occupied_music']
    },
    {
        "identifier": "EVENT_3400_play_occupied_music_if_occupied_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_determine_rose_town_shop_music',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'EVENT_3400_play_rose_town_indoor_music']
    },
    {
        "identifier": 'EVENT_3400_play_occupied_indoor_music',
        "command": 'play_music_default_volume',
        "args": [Music._15_HERES_SOME_WEAPONS]
    },
    {
        "identifier": "EVENT_3400_play_occupied_indoor_music_1",
        "command": "fade_out_music_to_volume",
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_occupied_indoor_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_casino_music',
        "command": 'play_music_default_volume',
        "args": [Music._47_GRATE_GUYS_CASINO]
    },
    {
        "identifier": "EVENT_3400_play_casino_music_ret",
        "command": 'ret'
    },
    
    {
        "identifier": 'EVENT_3400_determine_moleville_music',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_3400_play_moleville_music']
    },
    {
        "identifier": 'EVENT_3400_determine_moleville_music_2',
        "command": 'jmp',
        "args": ["EVENT_3400_play_dungeon_music"]
    },


    {
        "identifier": 'EVENT_3400_play_moleville_music',
        "command": 'play_music_default_volume',
        "args": [Music._33_MOLEVILLE]
    },
    {
        "identifier": "EVENT_3400_play_moleville_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_moleville_indoor_music',
        "command": 'play_music_default_volume',
        "args": [Music._33_MOLEVILLE]
    },
    {
        "identifier": "EVENT_3400_play_moleville_indoor_music_1",
        "command": "fade_out_music_to_volume",
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_moleville_indoor_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_nimbus_music',
        "command": 'play_music_default_volume',
        "args": [Music._50_NIMBUS_LAND]
    },
    {
        "identifier": "EVENT_3400_play_nimbus_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_determine_nimbus_music',
        "command": 'jmp_if_bit_set',
        "args": [0x705F, 4, 'EVENT_3400_play_nimbus_music']
    },
    {
        "identifier": 'EVENT_3400_play_valentina_music',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA]
    },
    {
        "identifier": "EVENT_3400_play_valentina_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_pipe_vault_music',
        "command": 'play_music_default_volume',
        "args": [Music._07_PIPE_VAULT]
    },
    {
        "identifier": "EVENT_3400_play_pipe_vault_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_bowsers_keep_music',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": "EVENT_3400_play_bowsers_keep_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_marios_pad_music',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": "EVENT_3400_play_marios_pad_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_seaside_music',
        "command": 'play_music_default_volume',
        "args": [Music._05_SEASIDE_TOWN]
    },
    {
        "identifier": "EVENT_3400_play_seaside_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_determine_seaside_indoor_music',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 0, 'EVENT_3400_play_occupied_indoor_music']
    },
    {
        "identifier": 'EVENT_3400_play_seaside_indoor_music',
        "command": 'play_music_default_volume',
        "args": [Music._05_SEASIDE_TOWN]
    },
    {
        "identifier": "EVENT_3400_play_seaside_indoor_music_1",
        "command": "fade_out_music_to_volume",
        "args": [1, 96]
    },
    {
        "identifier": "EVENT_3400_play_seaside_indoor_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_forest_music',
        "command": 'play_music_default_volume',
        "args": [Music._26_FOREST_MAZE]
    },
    {
        "identifier": "EVENT_3400_play_forest_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_factory_music',
        "command": 'play_music_default_volume',
        "args": [Music._67_WEAPONS_FACTORY]
    },
    {
        "identifier": "EVENT_3400_play_factory_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_monstro_town_music',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN]
    },
    {
        "identifier": "EVENT_3400_play_monstro_town_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_volcano_music',
        "command": 'play_music_default_volume',
        "args": [Music._62_BARREL_VOLCANO]
    },
    {
        "identifier": "EVENT_3400_play_volcano_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_inner_factory_music',
        "command": 'play_music_default_volume',
        "args": [Music._56_FACTORY]
    },
    {
        "identifier": "EVENT_3400_play_inner_factory_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_sea_music',
        "command": 'play_music_default_volume',
        "args": [Music._44_SEA]
    },
    {
        "identifier": "EVENT_3400_play_sea_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_axem_music',
        "command": 'play_music_default_volume',
        "args": [Music._63_AXEM_RANGERS_DROP_IN]
    },
    {
        "identifier": "EVENT_3400_play_axem_music_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_determine_marrymore_music_speed',
        "command": 'jmp_if_bit_clear',
        "args": [0x704C, 6, "EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": 'EVENT_3400_determine_marrymore_music_speed_1',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 12, 0]
    },
    {
        "identifier": 'EVENT_3400_determine_marrymore_music_speed_2',
        "command": 'jmp',
        "args": ["EVENT_3400_play_marrymore_music_indoors"]
    },
    {
        "identifier": "EVENT_3400_determine_marrymore_music_speed_ret",
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3400_play_star_hill_music',
        "command": 'play_music_default_volume',
        "args": [Music._34_STAR_HILL]
    },
    {
        "identifier": "EVENT_3400_play_star_hill_music_ret",
        "command": 'ret'
    },
    {
        "identifier": "EVENT_3400_v",
        "command": 'clear_bit',
        "args": [0x7093, 3]
    },
    {
        "identifier": "EVENT_3400_v_",
        "command": "open_location",
        "args": [Locations._050_BARREL_VOLCANO, [6, 7]],
    },
    {"identifier": "EVENT_3400_ret_v", "command": "ret"},
    {
        "identifier": "EVENT_3400_boomer_eject",
        "command": 'jmp_to_event',
        "args": [2226]
    },
    {
        "identifier": "EVENT_3400_exor_eject",
        "command": 'clear_bit',
        "args": [0x7092, 4]
    },
    {
        "identifier": "EVENT_3400_exor_eject_",
        "command": 'jmp_to_event',
        "args": [2149]
    },
]
