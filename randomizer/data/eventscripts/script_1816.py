from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1816_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1816_ret_84']
    },
    {
        "identifier": 'EVENT_1816_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1816_ret_84']
    },
    {
        "identifier": 'EVENT_1816_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1816_stop_all_background_events_3',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1816_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1816_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1816_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1816_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_1816_fade_out_music_to_volume_9',
        "command": 'fade_out_music_to_volume',
        "args": [2, 127]
    },
    {
        "identifier": 'EVENT_1816_set_10',
        "command": 'set',
        "args": [0x70ab, 21]
    },
    {
        "identifier": 'EVENT_1816_run_event_as_subroutine_11',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1816_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_12_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [25, 112]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_12_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_13_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_13_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._133_CLOSE_HIT_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_13_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1816_run_dialog_15',
        "command": 'run_dialog',
        "args": [1263, AreaObjects.MARIO, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_16_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1816_mem_compare_18',
        "command": 'mem_compare',
        "args": [0x7000, 1800]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_comparison_result_is_lesser_19',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1816_mem_compare_22']
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_20',
        "command": 'run_dialog_duration',
        "args": [1271, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_mem_compare_22',
        "command": 'mem_compare',
        "args": [0x7000, 840]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_comparison_result_is_lesser_23',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1816_mem_compare_26']
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_24',
        "command": 'run_dialog_duration',
        "args": [1264, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_mem_compare_26',
        "command": 'mem_compare',
        "args": [0x7000, 720]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_comparison_result_is_lesser_27',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1816_mem_compare_32']
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_28',
        "command": 'run_dialog_duration',
        "args": [1265, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_random_above_66_29',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_1816_run_dialog_duration_83']
    },
    {
        "identifier": 'EVENT_1816_set_short_30',
        "command": 'set_short',
        "args": [0x7028, 0x0001]
    },
    {
        "identifier": 'EVENT_1816_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1816_run_dialog_duration_73']
    },
    {
        "identifier": 'EVENT_1816_mem_compare_32',
        "command": 'mem_compare',
        "args": [0x7000, 660]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_comparison_result_is_lesser_33',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1816_run_dialog_duration_70']
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_34',
        "command": 'run_dialog_duration',
        "args": [1266, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_bit_set_35',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 7, 'EVENT_1816_set_short_64']
    },
    {
        "identifier": 'EVENT_1816_set_bit_36',
        "command": 'set_bit',
        "args": [0x7094, 7]
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_37',
        "command": 'run_dialog_duration',
        "args": [1268, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_set_38',
        "command": 'set',
        "args": [0x70a7, 92]
    },
    {
        "identifier": 'EVENT_1816_set_39',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1816_run_event_as_subroutine_40',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_1816_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_43',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_44',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_45',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_46',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_47',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_48',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_stop_sound_49',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1816_ret_50',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_sync_51_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_51_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_51_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_51_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1816_action_queue_sync_51_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_z_down_steps_5',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._057_FINGER_SNAP, 4]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._134_SWIPE, 4]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_east_pixels_13',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_fixed_f_coord_off_14',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_face_northwest_15',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_fixed_f_coord_on_16',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_east_pixels_17',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_play_sound_19',
                "command": 'play_sound',
                "args": [Sounds._057_FINGER_SNAP, 4]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_southeast_pixels_20',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_northwest_pixels_21',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_end_loop_23',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_shift_z_up_steps_25',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_fixed_f_coord_off_26',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_walk_1_step_north_27',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_dec_z_coord_1_step_28',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_52_SUBSCRIPT_face_southwest_29',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_53_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_53_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_53_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_53_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_play_sound_54',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1816_set_bit_55',
        "command": 'set_bit',
        "args": [0x704b, 6]
    },
    {
        "identifier": 'EVENT_1816_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 510]
    },
    {
        "identifier": 'EVENT_1816_set_57',
        "command": 'set',
        "args": [0x70a7, 92]
    },
    {
        "identifier": 'EVENT_1816_set_58',
        "command": 'set',
        "args": [0x7000, 1219]
    },
    {
        "identifier": 'EVENT_1816_run_dialog_59',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE]]
    },
    {
        "identifier": 'EVENT_1816_equip_item_to_character_60',
        "command": 'equip_item_to_character',
        "args": [PlayableCharacters.MARIO, items.TroopaPin]
    },
    {
        "identifier": 'EVENT_1816_unsync_action_script_61',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1816_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1816_ret_63',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_set_short_64',
        "command": 'set_short',
        "args": [0x7028, 0x0001]
    },
    {
        "identifier": 'EVENT_1816_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1816_mem_compare_66',
        "command": 'mem_compare',
        "args": [0x7000, 690]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_comparison_result_is_lesser_67',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1816_jmp_69']
    },
    {
        "identifier": 'EVENT_1816_jmp_if_random_above_128_68',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_1816_run_dialog_duration_83']
    },
    {
        "identifier": 'EVENT_1816_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_1816_run_dialog_duration_73']
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_70',
        "command": 'run_dialog_duration',
        "args": [1267, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_jmp_if_bit_clear_71',
        "command": 'jmp_if_bit_clear',
        "args": [0x7094, 7, 'EVENT_1816_set_bit_36']
    },
    {
        "identifier": 'EVENT_1816_set_short_72',
        "command": 'set_short',
        "args": [0x7028, 0x0005]
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_73',
        "command": 'run_dialog_duration',
        "args": [1269, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_set_object_memory_to_75',
        "command": 'set_object_memory_to',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 4]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x97, 0x15]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_floating_off_10',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_walk_1_step_southwest_12',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1816_action_queue_async_76_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_set_77',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_1816_add_frog_coins_78',
        "command": 'add_frog_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1816_end_loop_79',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1816_pause_80',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1816_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1816_action_queue_async_81_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1816_ret_82',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1816_run_dialog_duration_83',
        "command": 'run_dialog_duration',
        "args": [1270, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1816_ret_84',
        "command": 'ret'
    }
]
