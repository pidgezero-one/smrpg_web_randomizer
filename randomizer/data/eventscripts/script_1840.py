from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1840_jmp_fork_mario_on_object_0',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1840_set_short_mem_2', 'EVENT_1840_ret_24'],
        "subscript": [
        ]
    },
    {
        "identifier": 'EVENT_1840_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_1840_ret_24'],
        "subscript": [
        ]
    },
    {
        "identifier": 'EVENT_1840_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1840_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000]
    },
    {
        "identifier": 'EVENT_1840_set_bit_4',
        "command": 'set_bit',
        "args": [0x7095, 4]
    },
    {
        "identifier": 'EVENT_1840_resume_action_script_5',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_current_level_6',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 321, 'EVENT_1840_play_sound_25']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 455, 'EVENT_1840_play_sound_25']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 458, 'EVENT_1840_play_sound_25']
    },
    {
        "identifier": 'EVENT_1840_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_11',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_13',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_ret_24']
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_14',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_16',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_ret_24']
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_17',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_start_loop_n_times_18',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1840_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_20',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_ret_24']
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_pressed_button_21',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_all_bits_clear_22',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0, 1, 2, 3, 4, 5, 6, 7], 'EVENT_1840_ret_24']
    },
    {
        "identifier": 'EVENT_1840_end_loop_23',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1840_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1840_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_26',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_tapped_button_28',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_29',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1840_set_7000_to_current_level_53']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_30',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_set_bit_70']
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_31',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_pause_32',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_tapped_button_33',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_34',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1840_set_7000_to_current_level_53']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_35',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_set_bit_70']
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_36',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_start_loop_n_times_37',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1840_pause_38',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_tapped_button_39',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_40',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1840_set_7000_to_current_level_53']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_41',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_set_bit_70']
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_pressed_button_42',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_all_bits_clear_43',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0, 1, 2, 3, 4, 5, 6, 7], 'EVENT_1840_enable_controls_until_return_45']
    },
    {
        "identifier": 'EVENT_1840_end_loop_44',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_45',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_pause_46',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_tapped_button_47',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_48',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1840_set_7000_to_current_level_53']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_49',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_set_bit_70']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_on_object_50',
        "command": 'jmp_if_mario_on_object',
        "args": [AreaObjects.MEM_70A8, 'EVENT_1840_pause_46']
    },
    {
        "identifier": 'EVENT_1840_load_600f_51',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1840_ret_52',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_current_level_53',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_54',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 321, 'EVENT_1840_enable_controls_until_return_56']
    },
    {
        "identifier": 'EVENT_1840_ret_55',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_56',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_pressed_button_57',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_58',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3], 'EVENT_1840_action_queue_async_63']
    },
    {
        "identifier": 'EVENT_1840_jmp_if_7000_any_bits_set_59',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 2], 'EVENT_1840_action_queue_async_65']
    },
    {
        "identifier": 'EVENT_1840_pause_60',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1840_jmp_if_mario_in_air_61',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1840_set_7000_to_pressed_button_57']
    },
    {
        "identifier": 'EVENT_1840_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_1840_enable_controls_until_return_67']
    },
    {
        "identifier": 'EVENT_1840_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1840_action_queue_async_63_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_63_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_63_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1840_action_queue_async_63_SUBSCRIPT_shift_northeast_pixels_1']
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_63_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1840_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_1840_enable_controls_until_return_67']
    },
    {
        "identifier": 'EVENT_1840_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1840_action_queue_async_65_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_65_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_65_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1840_action_queue_async_65_SUBSCRIPT_shift_southwest_pixels_1']
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_65_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1840_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_1840_enable_controls_until_return_67']
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_67',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_load_600f_68',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1840_ret_69',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1840_set_bit_70',
        "command": 'set_bit',
        "args": [0x704d, 1]
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_71',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_current_level_72',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_73',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 455, 'EVENT_1840_action_queue_async_75']
    },
    {
        "identifier": 'EVENT_1840_freeze_all_npcs_until_return_74',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1840_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1840_action_queue_async_75_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1840_action_queue_async_75_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1840_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e]
    },
    {
        "identifier": 'EVENT_1840_set_short_mem_77',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1840_set_7016_to_object_xyz_78',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1840_jmp_to_subroutine_79',
        "command": 'jmp_to_subroutine',
        "args": [0x580e]
    },
    {
        "identifier": 'EVENT_1840_enable_controls_until_return_80',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1840_set_7000_to_current_level_81',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_1840_jmp_if_var_equals_short_82',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 455, 'EVENT_1840_load_600f_85']
    },
    {
        "identifier": 'EVENT_1840_unfreeze_all_npcs_83',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_1840_clear_bit_84',
        "command": 'clear_bit',
        "args": [0x704d, 1]
    },
    {
        "identifier": 'EVENT_1840_load_600f_85',
        "command": 'load_600f'
    },
    {
        "identifier": 'EVENT_1840_ret_86',
        "command": 'ret'
    }
]
