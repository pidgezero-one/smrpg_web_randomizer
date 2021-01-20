from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1553_set_short_0',
        "command": 'set_short',
        "args": [0x7026, 0x0023],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_1',
        "command": 'set_short',
        "args": [0x7028, 0x0024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_pause_5',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1553_pause_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_objects_action_script_running_7',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.NPC_3, 'EVENT_1553_pause_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_var_not_equals_short_8',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 20, 'EVENT_1553_set_short_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_9',
        "command": 'set',
        "args": [0x70af, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_10',
        "command": 'set_short',
        "args": [0x702a, 0x0014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7026, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_12',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x107f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x702c, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_pause_15',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_1553_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_objects_action_script_running_17',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.NPC_7, 'EVENT_1553_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_var_not_equals_short_18',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 24, 'EVENT_1553_set_short_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_19',
        "command": 'set',
        "args": [0x70af, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_20',
        "command": 'set_short',
        "args": [0x702a, 0x0018],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_21',
        "command": 'set_short_mem',
        "args": [0x7028, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_to_subroutine_23',
        "command": 'jmp_to_subroutine',
        "args": [0x107f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x702c, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1553_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_random_29',
        "command": 'set_random',
        "args": [0x7000, 4096],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_mem_compare_30',
        "command": 'mem_compare',
        "args": [0x7000, 2048],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_comparison_result_is_lesser_31',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1553_mem_7000_and_const_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_32',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_mem_7000_and_const_33',
        "command": 'mem_7000_and_const',
        "args": [0x07ff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_mem_compare_34',
        "command": 'mem_compare',
        "args": [0x7000, 1024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_comparison_result_is_lesser_35',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1553_jmp_if_7000_all_bits_clear_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_36',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_7000_all_bits_clear_37',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0], 'EVENT_1553_jmp_if_bit_clear_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_38',
        "command": 'set_bit',
        "args": [0x7044, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_clear_39',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'EVENT_1553_set_short_mem_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_clear_40',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_1553_set_short_mem_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_41',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_42',
        "command": 'set_short',
        "args": [0x702c, 0x0022],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_43',
        "command": 'set_short',
        "args": [0x7016, 0x2000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_44',
        "command": 'set_short',
        "args": [0x7018, 0x2e00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_1553_clear_mem_704x_at_7000_bit_55'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_47',
        "command": 'set_short',
        "args": [0x702c, 0x0023],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_48',
        "command": 'set_short',
        "args": [0x7016, 0x1800],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_49',
        "command": 'set_short',
        "args": [0x7018, 0x2b00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_1553_clear_mem_704x_at_7000_bit_55'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_52',
        "command": 'set_short',
        "args": [0x702c, 0x0024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_53',
        "command": 'set_short',
        "args": [0x7016, 0x1200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_54',
        "command": 'set_short',
        "args": [0x7018, 0x2700],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_mem_704x_at_7000_bit_55',
        "command": 'clear_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_mem_704x_at_7000_bit_57',
        "command": 'set_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_59',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_start_loop_n_times_60',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_61',
        "command": 'set_short',
        "args": [0x701a, 0x0100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1553_action_queue_async_62_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1553_action_queue_async_62_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1553_action_queue_async_62_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1553_action_queue_async_62_SUBSCRIPT_jmp_if_bit_set_3',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 1, 'EVENT_1553_add_63']
            },
            {
                "identifier": 'EVENT_1553_action_queue_async_62_SUBSCRIPT_shift_xy_pixels_4',
                "command": 'shift_xy_pixels',
                "args": [160, 48]
            }
        ]
    },
    {
        "identifier": 'EVENT_1553_add_63',
        "command": 'add',
        "args": [0x70a9, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_end_loop_64',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_clear_65',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_1553_set_short_mem_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_random_above_128_66',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_1553_set_short_mem_74'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_67',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_clear_bit_68',
        "command": 'clear_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_clear_69',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1553_jmp_if_bit_clear_71'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_70',
        "command": 'set_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_clear_71',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'EVENT_1553_jmp_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_bit_72',
        "command": 'set_bit',
        "args": [0x7044, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_1555_jmp_if_bit_set_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_74',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_short_mem_75',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_start_loop_n_times_76',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_if_bit_set_77',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1553_set_action_script_sync_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_action_script_sync_78',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_1553_add_81'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_set_action_script_sync_80',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_add_81',
        "command": 'add',
        "args": [0x70a9, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_end_loop_82',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1553_ret_83',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
