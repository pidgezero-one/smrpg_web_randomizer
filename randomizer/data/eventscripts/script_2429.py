from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2429_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_2429_ret_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_if_random_above_66_2',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2429_remove_from_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_9',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_if_random_above_66_11',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2429_remove_from_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_16',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_if_random_above_66_20',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2429_remove_from_level_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_24',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_25',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_if_random_above_66_29',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2429_remove_from_level_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_30',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_34',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_2429_jmp_if_random_above_66_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_36',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_37',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_if_random_above_66_38',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2429_remove_from_level_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_39',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_40',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_2429_ret_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_summon_to_level_43',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_2429_ret_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_45',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2429_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
