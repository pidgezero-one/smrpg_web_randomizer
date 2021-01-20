from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2425_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7047, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_2',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_7, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_4',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_13, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_object_trigger_disabled_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_6',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_1, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_7',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_7, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_8',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_13, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_9',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_2, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_10',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_8, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_11',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_14, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_object_trigger_disabled_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_13',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_2, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_14',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_8, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_15',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_14, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_16',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_3, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_17',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_9, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_18',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_15, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_object_trigger_disabled_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_20',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_3, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_21',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_9, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_22',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_15, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_23',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_24',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_10, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_25',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_16, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_object_trigger_disabled_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_27',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_4, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_28',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_10, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_29',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_16, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_30',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_5, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_31',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_11, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_32',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_17, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_object_trigger_disabled_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_34',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_5, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_35',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_11, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_36',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_17, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_37',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_6, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_38',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_12, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_object_trigger_disabled_39',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_18, Rooms._234_FOREST_MAZE_SECRET, 'EVENT_2425_disable_trigger_in_level_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_if_bit_set_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_41',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_6, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_42',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_12, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_disable_trigger_in_level_43',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_18, Rooms._234_FOREST_MAZE_SECRET],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 5, 'EVENT_2425_remove_from_current_level_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 6, 'EVENT_2425_remove_from_current_level_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_46',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_47',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_48',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_49',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_50',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_51',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_52',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_53',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_54',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_55',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_56',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_57',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_58',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_87'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_60',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_61',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_62',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_63',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_64',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_65',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_66',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_67',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_68',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_69',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_70',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_71',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_72',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_2425_jmp_87'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_74',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_75',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_76',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_77',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_78',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_79',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_80',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_81',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_82',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_83',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_84',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_85',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_remove_from_current_level_86',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2425_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_2418_play_sound_63'],
        "subscript": []
    }
]
