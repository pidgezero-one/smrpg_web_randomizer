from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3507_set_0',
        "command": 'set',
        "args": [0x70ae, 26]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_1_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 67, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_2_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_4_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 4, 'EVENT_3507_run_dialog_26']
    },
    {
        "identifier": 'EVENT_3507_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 3, 'EVENT_3507_run_dialog_23']
    },
    {
        "identifier": 'EVENT_3507_jmp_if_var_not_equals_byte_7',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70b2, 0, 'EVENT_3507_run_dialog_20']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_8',
        "command": 'run_dialog',
        "args": [1205, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_9',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_pause_16']
    },
    {
        "identifier": 'EVENT_3507_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_12_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_12_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_13_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_set_bit_14',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_3507_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3508_action_queue_async_14']
    },
    {
        "identifier": 'EVENT_3507_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3507_run_dialog_18',
        "command": 'run_dialog',
        "args": [1206, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_3507_play_sound_31']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_20',
        "command": 'run_dialog',
        "args": [1204, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_21',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_set_short_mem_36']
    },
    {
        "identifier": 'EVENT_3507_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3507_pause_28']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_23',
        "command": 'run_dialog',
        "args": [1207, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_24',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_set_short_mem_36']
    },
    {
        "identifier": 'EVENT_3507_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3507_pause_28']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_26',
        "command": 'run_dialog',
        "args": [1199, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_27',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_set_short_mem_36']
    },
    {
        "identifier": 'EVENT_3507_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3507_run_dialog_30',
        "command": 'run_dialog',
        "args": [1200, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3507_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_sync_32_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3507_action_queue_sync_32_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_33_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_33_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_run_event_at_return_34',
        "command": 'run_event_at_return',
        "args": [3510]
    },
    {
        "identifier": 'EVENT_3507_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3507_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b1]
    },
    {
        "identifier": 'EVENT_3507_mem_compare_37',
        "command": 'mem_compare',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_comparison_result_is_lesser_38',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3507_pause_48']
    },
    {
        "identifier": 'EVENT_3507_pause_39',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_bit_set_41',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 2, 'EVENT_3507_run_dialog_45']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_42',
        "command": 'run_dialog',
        "args": [1203, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_43',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_pause_48']
    },
    {
        "identifier": 'EVENT_3507_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_3507_pause_28']
    },
    {
        "identifier": 'EVENT_3507_run_dialog_45',
        "command": 'run_dialog',
        "args": [1202, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_jmp_if_dialog_option_b_46',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3507_pause_48']
    },
    {
        "identifier": 'EVENT_3507_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_3507_pause_28']
    },
    {
        "identifier": 'EVENT_3507_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_async_49',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3507_run_dialog_50',
        "command": 'run_dialog',
        "args": [1201, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3507_play_sound_51',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_52_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_52_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3507_action_queue_async_53_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_53_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_53_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3507_action_queue_async_53_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3507_run_background_event_54',
        "command": 'run_background_event',
        "args": [3511, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_1, 704]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 655]
    },
    {
        "identifier": 'EVENT_3507_set_action_script_sync_57',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_3, 705]
    },
    {
        "identifier": 'EVENT_3507_set_bit_58',
        "command": 'set_bit',
        "args": [0x707b, 4]
    },
    {
        "identifier": 'EVENT_3507_run_event_at_return_59',
        "command": 'run_event_at_return',
        "args": [3502]
    },
    {
        "identifier": 'EVENT_3507_ret_60',
        "command": 'ret'
    }
]
