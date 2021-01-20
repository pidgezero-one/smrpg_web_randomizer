from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_447_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_447_set_random_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 1, 'EVENT_447_set_random_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 2, 'EVENT_447_set_random_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_447_set_random_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_random_6',
        "command": 'set_random',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_447_jmp_if_bit_set_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_447_jmp_if_bit_set_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_447_jmp_if_bit_set_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_random_12',
        "command": 'set_random',
        "args": [0x7000, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_13',
        "command": 'mem_compare',
        "args": [0x7000, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_14',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_15',
        "command": 'mem_compare',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_16',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_17',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_18',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_447_jmp_if_random_above_66_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 416],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_21',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_22',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 416],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_24',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_25',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 416],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_27',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_28',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_random_31',
        "command": 'set_random',
        "args": [0x7000, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_32',
        "command": 'mem_compare',
        "args": [0x7000, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_33',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_34',
        "command": 'mem_compare',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_35',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_36',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_37',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_447_jmp_if_random_above_66_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 417],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_40',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_41',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 417],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_43',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_44',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 417],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_46',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_47',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_random_above_66_48',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_pause_49',
        "command": 'pause',
        "args": [71],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_50',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_random_above_128_51',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_pause_52',
        "command": 'pause',
        "args": [99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_53',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_set_54',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_random_56',
        "command": 'set_random',
        "args": [0x7000, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_57',
        "command": 'mem_compare',
        "args": [0x7000, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_58',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_64'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_59',
        "command": 'mem_compare',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_60',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_61',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_62',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_70'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_63',
        "command": 'jmp',
        "args": ['EVENT_447_jmp_if_random_above_66_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 418],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_65',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_66',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 418],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_68',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_69',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_70',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 418],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_71',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_72',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_bit_set_73',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_447_jmp_if_bit_clear_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_clear_bit_74',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_random_75',
        "command": 'set_random',
        "args": [0x7000, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_76',
        "command": 'mem_compare',
        "args": [0x7000, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_77',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_78',
        "command": 'mem_compare',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_79',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_86'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_mem_compare_80',
        "command": 'mem_compare',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_if_comparison_result_is_greater_or_equal_81',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_447_set_action_script_sync_89'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_82',
        "command": 'jmp',
        "args": ['EVENT_447_jmp_if_random_above_66_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_83',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 419],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_84',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_85',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_86',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 419],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_87',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_88',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 419],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_set_bit_90',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_447_jmp_to_event_91',
        "command": 'jmp_to_event',
        "args": [447],
        "subscript": []
    },
]
