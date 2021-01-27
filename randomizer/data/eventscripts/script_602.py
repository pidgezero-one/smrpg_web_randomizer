from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_602_jmp_if_bit_set_137']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 2, 'EVENT_602_jmp_if_bit_set_137']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_602_run_dialog_135']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_602_run_dialog_133']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_602_run_dialog_133']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_602_run_dialog_61']
    },
    {
        "identifier": 'EVENT_602_run_dialog_6',
        "command": 'run_dialog',
        "args": [2470, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_jmp_if_dialog_option_b_or_c_7',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_602_set_7000_to_70A0_short_mem_12', 'EVENT_602_run_dialog_59']
    },
    {
        "identifier": 'EVENT_602_close_dialog_8',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_602_open_shop_9',
        "command": 'open_shop',
        "args": [Shops._05_MARRYMORE_SHOP]
    },
    {
        "identifier": 'EVENT_602_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_602_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_set_7000_to_70A0_short_mem_12',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d7]
    },
    {
        "identifier": 'EVENT_602_mem_compare_val_13',
        "command": 'mem_compare_val',
        "args": [1]
    },
    {
        "identifier": 'EVENT_602_jmp_if_comparison_result_is_greater_or_equal_14',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_602_run_dialog_18']
    },
    {
        "identifier": 'EVENT_602_run_dialog_15',
        "command": 'run_dialog',
        "args": [2471, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_jmp_if_dialog_option_b_or_c_16',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_602_set_short_31', 'EVENT_602_run_dialog_59']
    },
    {
        "identifier": 'EVENT_602_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_602_set_short_20']
    },
    {
        "identifier": 'EVENT_602_run_dialog_18',
        "command": 'run_dialog',
        "args": [2508, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_jmp_if_dialog_option_b_or_c_19',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_602_set_short_31', 'EVENT_602_run_dialog_59']
    },
    {
        "identifier": 'EVENT_602_set_short_20',
        "command": 'set_short',
        "args": [0x7024, 0x000a]
    },
    {
        "identifier": 'EVENT_602_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7049, 4]
    },
    {
        "identifier": 'EVENT_602_run_event_as_subroutine_22',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_602_run_dialog_29']
    },
    {
        "identifier": 'EVENT_602_set_7000_to_7000_short_mem_24',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_602_dec_coins_25',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_602_run_dialog_26',
        "command": 'run_dialog',
        "args": [974, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_set_bit_27',
        "command": 'set_bit',
        "args": [0x7062, 4]
    },
    {
        "identifier": 'EVENT_602_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17']
    },
    {
        "identifier": 'EVENT_602_run_dialog_29',
        "command": 'run_dialog',
        "args": [2475, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_set_short_31',
        "command": 'set_short',
        "args": [0x7024, 0x00c8]
    },
    {
        "identifier": 'EVENT_602_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7049, 4]
    },
    {
        "identifier": 'EVENT_602_run_event_as_subroutine_33',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_34',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_602_run_dialog_29']
    },
    {
        "identifier": 'EVENT_602_set_7000_to_7000_short_mem_35',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_602_dec_coins_36',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_602_set_7000_to_70A0_short_mem_37',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d7]
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_38',
        "command": 'jmp_if_7000_equals_short',
        "args": [255, 'EVENT_602_set_bit_63']
    },
    {
        "identifier": 'EVENT_602_inc_39',
        "command": 'inc',
        "args": [0x70d7]
    },
    {
        "identifier": 'EVENT_602_set_7000_to_70A0_short_mem_40',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d7]
    },
    {
        "identifier": 'EVENT_602_mem_compare_val_41',
        "command": 'mem_compare_val',
        "args": [2]
    },
    {
        "identifier": 'EVENT_602_jmp_if_comparison_result_is_greater_or_equal_42',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_602_set_bit_63']
    },
    {
        "identifier": 'EVENT_602_run_dialog_43',
        "command": 'run_dialog',
        "args": [2472, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_shift_northwest_pixels_12',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_44_SUBSCRIPT_walk_1_step_northeast_15',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_602_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_45_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_602_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_sync_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_47_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_47_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_602_pause_48',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_602_run_dialog_49',
        "command": 'run_dialog',
        "args": [977, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_play_sound_50',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_602_set_51',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_602_run_dialog_52',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_602_put_inventory_53',
        "command": 'put_inventory',
        "args": [items.FlowerTab]
    },
    {
        "identifier": 'EVENT_602_run_dialog_54',
        "command": 'run_dialog',
        "args": [978, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_set_bit_55',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_602_set_action_script_async_56',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 636]
    },
    {
        "identifier": 'EVENT_602_set_action_script_sync_57',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 301]
    },
    {
        "identifier": 'EVENT_602_ret_58',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_59',
        "command": 'run_dialog',
        "args": [976, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_60',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_61',
        "command": 'run_dialog',
        "args": [973, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_62',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_set_bit_63',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_602_set_7000_to_70A0_short_mem_64',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d7]
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_65',
        "command": 'jmp_if_7000_equals_short',
        "args": [255, 'EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_66',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_602_pause_83']
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_67',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_602_pause_93']
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_68',
        "command": 'jmp_if_7000_equals_short',
        "args": [10, 'EVENT_602_pause_100']
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_69',
        "command": 'jmp_if_7000_equals_short',
        "args": [15, 'EVENT_602_pause_109']
    },
    {
        "identifier": 'EVENT_602_mem_compare_val_70',
        "command": 'mem_compare_val',
        "args": [200]
    },
    {
        "identifier": 'EVENT_602_jmp_if_comparison_result_is_greater_or_equal_71',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_602_jmp_if_bit_set_120']
    },
    {
        "identifier": 'EVENT_602_set_7010_to_object_xyz_72',
        "command": 'set_7010_to_object_xyz',
        "args": [0x99]
    },
    {
        "identifier": 'EVENT_602_mem_compare_73',
        "command": 'mem_compare',
        "args": [0x7010, 5]
    },
    {
        "identifier": 'EVENT_602_jmp_if_comparison_result_is_greater_or_equal_74',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_602_start_embedded_action_script_sync_F1_81']
    },
    {
        "identifier": 'EVENT_602_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_sync_75_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_75_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_602_action_queue_sync_75_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_76_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_602_run_dialog_77',
        "command": 'run_dialog',
        "args": [2473, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_unsync_dialog_78',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_602_remember_last_object_79',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_602_jmp_80',
        "command": 'jmp',
        "args": ['EVENT_602_set_bit_55']
    },
    {
        "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [6, 61]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_602_start_embedded_action_script_sync_F1_81_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_602_jmp_82',
        "command": 'jmp',
        "args": ['EVENT_602_run_dialog_77']
    },
    {
        "identifier": 'EVENT_602_pause_83',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_set_84',
        "command": 'set',
        "args": [0x7000, 3]
    },
    {
        "identifier": 'EVENT_602_run_dialog_85',
        "command": 'run_dialog',
        "args": [2477, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_86_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_602_run_dialog_87',
        "command": 'run_dialog',
        "args": [1022, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_set_88',
        "command": 'set',
        "args": [0x70a7, 116]
    },
    {
        "identifier": 'EVENT_602_set_89',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_602_run_event_as_subroutine_90',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_602_pause_91',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_pause_93',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_set_94',
        "command": 'set',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_602_run_dialog_95',
        "command": 'run_dialog',
        "args": [2477, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_play_sound_96',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_add_frog_coins_97',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_602_run_dialog_98',
        "command": 'run_dialog',
        "args": [526, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_602_jmp_99',
        "command": 'jmp',
        "args": ['EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_pause_100',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_set_101',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_602_run_dialog_102',
        "command": 'run_dialog',
        "args": [2477, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_play_sound_103',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_pause_104',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_602_play_sound_105',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_add_frog_coins_106',
        "command": 'add_frog_coins',
        "args": [2]
    },
    {
        "identifier": 'EVENT_602_run_dialog_107',
        "command": 'run_dialog',
        "args": [526, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_602_jmp_108',
        "command": 'jmp',
        "args": ['EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_pause_109',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_set_110',
        "command": 'set',
        "args": [0x7000, 15]
    },
    {
        "identifier": 'EVENT_602_run_dialog_111',
        "command": 'run_dialog',
        "args": [2477, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_play_sound_112',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_pause_113',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_602_play_sound_114',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_pause_115',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_602_play_sound_116',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_add_frog_coins_117',
        "command": 'add_frog_coins',
        "args": [3]
    },
    {
        "identifier": 'EVENT_602_run_dialog_118',
        "command": 'run_dialog',
        "args": [526, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_602_jmp_119',
        "command": 'jmp',
        "args": ['EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_120',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 4, 'EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_pause_121',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_602_set_122',
        "command": 'set',
        "args": [0x7000, 200]
    },
    {
        "identifier": 'EVENT_602_run_dialog_123',
        "command": 'run_dialog',
        "args": [2477, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_start_loop_n_times_124',
        "command": 'start_loop_n_times',
        "args": [19]
    },
    {
        "identifier": 'EVENT_602_play_sound_125',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_602_pause_126',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_602_end_loop_127',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_602_add_frog_coins_128',
        "command": 'add_frog_coins',
        "args": [20]
    },
    {
        "identifier": 'EVENT_602_run_dialog_129',
        "command": 'run_dialog',
        "args": [526, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_602_set_130',
        "command": 'set',
        "args": [0x70d7, 255]
    },
    {
        "identifier": 'EVENT_602_set_bit_131',
        "command": 'set_bit',
        "args": [0x709f, 4]
    },
    {
        "identifier": 'EVENT_602_jmp_132',
        "command": 'jmp',
        "args": ['EVENT_602_set_7010_to_object_xyz_72']
    },
    {
        "identifier": 'EVENT_602_run_dialog_133',
        "command": 'run_dialog',
        "args": [998, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_134',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_135',
        "command": 'run_dialog',
        "args": [1004, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_136',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_137',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_602_run_dialog_157']
    },
    {
        "identifier": 'EVENT_602_set_7000_to_object_coord_138',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.F, []]
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_139',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_602_run_dialog_162']
    },
    {
        "identifier": 'EVENT_602_set_7000_to_70A0_short_mem_140',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_602_dec_141',
        "command": 'dec',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_602_jmp_if_7000_equals_short_142',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_602_run_dialog_149']
    },
    {
        "identifier": 'EVENT_602_set_70A0_short_mem_to_7000_143',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70ac]
    },
    {
        "identifier": 'EVENT_602_run_dialog_144',
        "command": 'run_dialog',
        "args": [1019, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_action_queue_async_145',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [3, 55]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_602_action_queue_async_145_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_602_clear_bit_146',
        "command": 'clear_bit',
        "args": [0x704c, 2]
    },
    {
        "identifier": 'EVENT_602_run_background_event_147',
        "command": 'run_background_event',
        "args": [617, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_602_ret_148',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_149',
        "command": 'run_dialog',
        "args": [1020, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_clear_bit_150',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_602_clear_bit_151',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_602_clear_bit_152',
        "command": 'clear_bit',
        "args": [0x704c, 2]
    },
    {
        "identifier": 'EVENT_602_set_153',
        "command": 'set',
        "args": [0x70ac, 0]
    },
    {
        "identifier": 'EVENT_602_set_154',
        "command": 'set',
        "args": [0x70b8, 0]
    },
    {
        "identifier": 'EVENT_602_set_bit_155',
        "command": 'set_bit',
        "args": [0x704c, 3]
    },
    {
        "identifier": 'EVENT_602_ret_156',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_157',
        "command": 'run_dialog',
        "args": [1014, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_jmp_if_bit_set_158',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_602_run_background_event_159',
        "command": 'run_background_event',
        "args": [623, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_602_set_bit_160',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_602_ret_161',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_602_run_dialog_162',
        "command": 'run_dialog',
        "args": [1021, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_602_ret_163',
        "command": 'ret'
    }
]
