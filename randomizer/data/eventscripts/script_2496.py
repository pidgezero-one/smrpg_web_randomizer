from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2496_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_1',
        "command": 'apply_tile_mod',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_3',
        "command": 'apply_tile_mod',
        "args": [Rooms._226_FOREST_MAZE_AREA_02, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_6',
        "command": 'apply_tile_mod',
        "args": [Rooms._401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._433_SMITHY_FACTORY_AREA_01_____DUMMY, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_9',
        "command": 'apply_tile_mod',
        "args": [Rooms._442_SMITHY_FACTORY_AREA_11_CONVEYOR_BELTS_SPAWNING_DRILL_BITS_AND_MACKS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_11',
        "command": 'apply_tile_mod',
        "args": [Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2496_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2496_set_15',
        "command": 'set',
        "args": [0x70df, 8]
    },
    {
        "identifier": 'EVENT_2496_set_bit_16',
        "command": 'set_bit',
        "args": [0x706d, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_17',
        "command": 'set_bit',
        "args": [0x706d, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_18',
        "command": 'set_bit',
        "args": [0x706d, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_19',
        "command": 'set_bit',
        "args": [0x706d, 5]
    },
    {
        "identifier": 'EVENT_2496_set_bit_20',
        "command": 'set_bit',
        "args": [0x706d, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_21',
        "command": 'set_bit',
        "args": [0x706d, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_22',
        "command": 'set_bit',
        "args": [0x706e, 0]
    },
    {
        "identifier": 'EVENT_2496_set_bit_23',
        "command": 'set_bit',
        "args": [0x706e, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_24',
        "command": 'set_bit',
        "args": [0x706e, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_25',
        "command": 'set_bit',
        "args": [0x706e, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_26',
        "command": 'set_bit',
        "args": [0x706e, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_27',
        "command": 'set_bit',
        "args": [0x706e, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_28',
        "command": 'set_bit',
        "args": [0x706f, 0]
    },
    {
        "identifier": 'EVENT_2496_set_bit_29',
        "command": 'set_bit',
        "args": [0x706f, 1]
    },
    {
        "identifier": 'EVENT_2496_set_bit_30',
        "command": 'set_bit',
        "args": [0x706f, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_31',
        "command": 'set_bit',
        "args": [0x706f, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_32',
        "command": 'set_bit',
        "args": [0x706f, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_33',
        "command": 'set_bit',
        "args": [0x706f, 5]
    },
    {
        "identifier": 'EVENT_2496_set_bit_34',
        "command": 'set_bit',
        "args": [0x706f, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_35',
        "command": 'set_bit',
        "args": [0x706f, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_36',
        "command": 'set_bit',
        "args": [0x7070, 0]
    },
    {
        "identifier": 'EVENT_2496_set_bit_37',
        "command": 'set_bit',
        "args": [0x7070, 1]
    },
    {
        "identifier": 'EVENT_2496_set_bit_38',
        "command": 'set_bit',
        "args": [0x7070, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_39',
        "command": 'set_bit',
        "args": [0x7070, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_40',
        "command": 'set_bit',
        "args": [0x7065, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_41',
        "command": 'set_bit',
        "args": [0x7065, 5]
    },
    {
        "identifier": 'EVENT_2496_set_bit_42',
        "command": 'set_bit',
        "args": [0x7065, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_43',
        "command": 'set_bit',
        "args": [0x7065, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_44',
        "command": 'set_bit',
        "args": [0x7066, 1]
    },
    {
        "identifier": 'EVENT_2496_set_bit_45',
        "command": 'set_bit',
        "args": [0x7066, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_46',
        "command": 'set_bit',
        "args": [0x7066, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_47',
        "command": 'set_bit',
        "args": [0x7066, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_48',
        "command": 'set_bit',
        "args": [0x7066, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_49',
        "command": 'set_bit',
        "args": [0x7066, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_50',
        "command": 'set_bit',
        "args": [0x7067, 0]
    },
    {
        "identifier": 'EVENT_2496_set_bit_51',
        "command": 'set_bit',
        "args": [0x7067, 1]
    },
    {
        "identifier": 'EVENT_2496_set_bit_52',
        "command": 'set_bit',
        "args": [0x7067, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_53',
        "command": 'set_bit',
        "args": [0x7067, 3]
    },
    {
        "identifier": 'EVENT_2496_set_bit_54',
        "command": 'set_bit',
        "args": [0x7067, 4]
    },
    {
        "identifier": 'EVENT_2496_set_bit_55',
        "command": 'set_bit',
        "args": [0x7067, 5]
    },
    {
        "identifier": 'EVENT_2496_set_bit_56',
        "command": 'set_bit',
        "args": [0x7067, 6]
    },
    {
        "identifier": 'EVENT_2496_set_bit_57',
        "command": 'set_bit',
        "args": [0x7067, 7]
    },
    {
        "identifier": 'EVENT_2496_set_bit_58',
        "command": 'set_bit',
        "args": [0x7068, 0]
    },
    {
        "identifier": 'EVENT_2496_set_bit_59',
        "command": 'set_bit',
        "args": [0x7068, 1]
    },
    {
        "identifier": 'EVENT_2496_set_bit_60',
        "command": 'set_bit',
        "args": [0x7068, 2]
    },
    {
        "identifier": 'EVENT_2496_set_bit_61',
        "command": 'set_bit',
        "args": [0x7068, 4]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_62',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._324_MONSTRO_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_63',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._021_MUSHROOM_KINGDOM_CASTLE_BRANCH_ROOM_TO_VAULTGUEST_ROOM]
    },
    {
        "identifier": 'EVENT_2496_set_bit_64',
        "command": 'set_bit',
        "args": [0x7081, 6]
    },
    {
        "identifier": 'EVENT_2496_run_background_event_65',
        "command": 'run_background_event',
        "args": [343, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_66',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_67',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_68',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_69',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_70',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_71',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_72',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_73',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_74',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_75',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_remove_from_level_76',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    },
    {
        "identifier": 'EVENT_2496_jmp_to_event_77',
        "command": 'jmp_to_event',
        "args": [2502]
    },
    {
        "identifier": 'EVENT_2496_stop_music_78',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_2496_ret_79',
        "command": 'ret'
    }
]
