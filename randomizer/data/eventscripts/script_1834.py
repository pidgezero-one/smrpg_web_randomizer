from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1834_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_1834_set_bit_2']
    },
    {
        "identifier": 'EVENT_1834_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1834_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1834_set_short_3',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_1834_set_7016_to_object_xyz_4',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1834_jmp_to_subroutine_5',
        "command": 'jmp_to_subroutine',
        "args": [0x580e]
    },
    {
        "identifier": 'EVENT_1834_move_script_to_background_thread_2_6',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1834_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1834_set_7000_to_tapped_button_8',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1834_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1834_action_queue_sync_50']
    },
    {
        "identifier": 'EVENT_1834_set_7000_to_pressed_button_10',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1834_mem_7000_and_const_11',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_1834_mem_compare_12',
        "command": 'mem_compare',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1834_jmp_if_loaded_memory_is_not_0_13',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_1834_clear_bit_17']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1834_pause_7']
    },
    {
        "identifier": 'EVENT_1834_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1834_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_48']
    },
    {
        "identifier": 'EVENT_1834_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1834_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 9, 'EVENT_1834_set_short_31']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_1834_set_short_33']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 10, 'EVENT_1834_set_short_35']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1834_set_short_37']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1834_set_short_43']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_1834_set_short_45']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_1834_set_short_39']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_1834_set_short_41']
    },
    {
        "identifier": 'EVENT_1834_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_28_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1834_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_1834_pause_7']
    },
    {
        "identifier": 'EVENT_1834_set_short_31',
        "command": 'set_short',
        "args": [0x7014, 0x0003]
    },
    {
        "identifier": 'EVENT_1834_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_33',
        "command": 'set_short',
        "args": [0x7014, 0x0005]
    },
    {
        "identifier": 'EVENT_1834_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_35',
        "command": 'set_short',
        "args": [0x7014, 0x0001]
    },
    {
        "identifier": 'EVENT_1834_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_37',
        "command": 'set_short',
        "args": [0x7014, 0x0007]
    },
    {
        "identifier": 'EVENT_1834_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_39',
        "command": 'set_short',
        "args": [0x7014, 0x0000]
    },
    {
        "identifier": 'EVENT_1834_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_41',
        "command": 'set_short',
        "args": [0x7014, 0x0002]
    },
    {
        "identifier": 'EVENT_1834_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_43',
        "command": 'set_short',
        "args": [0x7014, 0x0004]
    },
    {
        "identifier": 'EVENT_1834_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_set_short_45',
        "command": 'set_short',
        "args": [0x7014, 0x0006]
    },
    {
        "identifier": 'EVENT_1834_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_1834_action_queue_sync_47']
    },
    {
        "identifier": 'EVENT_1834_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_sync_47_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._048_MINECART_START, 4]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_47_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7014]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_47_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_47_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_47_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_jmp_if_bit_set_0',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 1, 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_set_short_mem_2']
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7014]
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_face_east_3',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1834_action_queue_sync_48_SUBSCRIPT_shift_f_direction_pixels_4',
                "command": 'shift_f_direction_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_1834_pause_7']
    },
    {
        "identifier": 'EVENT_1834_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_sync_50_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_async_51_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_51_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_51_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_move_script_to_main_thread_52',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1834_clear_bit_53',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1834_ret_54',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1834_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._043_POP_UP_FROM_WATER, 4]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_55_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_set_7000_to_object_coord_56',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'EVENT_1834_set_short_mem_57',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_1834_set_7000_to_object_coord_58',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1834_mem_compare_59',
        "command": 'mem_compare',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_1834_jmp_if_loaded_memory_is_0_60',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_1834_set_7000_to_object_coord_70']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_comparison_result_is_greater_or_equal_61',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1834_set_short_65']
    },
    {
        "identifier": 'EVENT_1834_set_short_62',
        "command": 'set_short',
        "args": [0x700c, 0x0000]
    },
    {
        "identifier": 'EVENT_1834_swap_short_mem_63',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_1834_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_1834_dec_short_mem_66']
    },
    {
        "identifier": 'EVENT_1834_set_short_65',
        "command": 'set_short',
        "args": [0x700c, 0x0004]
    },
    {
        "identifier": 'EVENT_1834_dec_short_mem_66',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_1834_mem_7000_shift_left_67',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_1834_set_short_mem_68',
        "command": 'set_short_mem',
        "args": [0x7010, 0x7000]
    },
    {
        "identifier": 'EVENT_1834_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_async_69_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._043_POP_UP_FROM_WATER, 4]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_69_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_69_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7010]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_69_SUBSCRIPT_walk_f_direction_16_pixels_3',
                "command": 'walk_f_direction_16_pixels'
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_set_7000_to_object_coord_70',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1834_mem_compare_71',
        "command": 'mem_compare',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_1834_jmp_if_loaded_memory_is_0_72',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_1834_action_queue_async_82']
    },
    {
        "identifier": 'EVENT_1834_jmp_if_comparison_result_is_greater_or_equal_73',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1834_set_short_77']
    },
    {
        "identifier": 'EVENT_1834_set_short_74',
        "command": 'set_short',
        "args": [0x700c, 0x0002]
    },
    {
        "identifier": 'EVENT_1834_swap_short_mem_75',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_1834_jmp_76',
        "command": 'jmp',
        "args": ['EVENT_1834_dec_short_mem_78']
    },
    {
        "identifier": 'EVENT_1834_set_short_77',
        "command": 'set_short',
        "args": [0x700c, 0x0006]
    },
    {
        "identifier": 'EVENT_1834_dec_short_mem_78',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_1834_mem_7000_shift_left_79',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_1834_set_short_mem_80',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7000]
    },
    {
        "identifier": 'EVENT_1834_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_async_81_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._043_POP_UP_FROM_WATER, 4]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_81_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_81_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7012]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_81_SUBSCRIPT_walk_f_direction_16_pixels_3',
                "command": 'walk_f_direction_16_pixels'
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7014]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_face_east_3',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1834_action_queue_async_82_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1834_ret_83',
        "command": 'ret'
    }
]
