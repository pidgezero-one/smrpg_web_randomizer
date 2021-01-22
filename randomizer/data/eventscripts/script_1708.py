from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1708_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_1708_jmp_if_bit_clear_3']
    },
    {
        "identifier": 'EVENT_1708_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_1708_jmp_if_bit_clear_3']
    },
    {
        "identifier": 'EVENT_1708_set_short_2',
        "command": 'set_short',
        "args": [0x7022, 0x001e]
    },
    {
        "identifier": 'EVENT_1708_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x704d, 3, 'EVENT_1708_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_1708_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_sync_8_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_8_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_8_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 7, 'EVENT_1708_jmp_if_bit_clear_15']
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1708_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1708_run_event_as_subroutine_13',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1708_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1708_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7077, 4, 'EVENT_1708_set_bit_20']
    },
    {
        "identifier": 'EVENT_1708_run_event_as_subroutine_16',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1708_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1708_action_queue_async_37']
    },
    {
        "identifier": 'EVENT_1708_run_background_event_18',
        "command": 'run_background_event',
        "args": [1709, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1708_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1708_set_bit_20',
        "command": 'set_bit',
        "args": [0x7077, 4]
    },
    {
        "identifier": 'EVENT_1708_run_event_as_subroutine_21',
        "command": 'run_event_as_subroutine',
        "args": [14]
    },
    {
        "identifier": 'EVENT_1708_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_sync_22_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_pause_23',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_24_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_south_steps_8',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_northwest_steps_11',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_north_steps_12',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_13',
                "command": 'shift_northeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_25_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_walk_1_step_east_1',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_shift_north_steps_7',
                "command": 'shift_north_steps',
                "args": [13]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1708_action_queue_sync_26_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_stop_embedded_action_script_27',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1708_jmp_to_subroutine_28',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1708_action_queue_async_37']
    },
    {
        "identifier": 'EVENT_1708_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1708_run_background_event_35']
    },
    {
        "identifier": 'EVENT_1708_summon_to_current_level_at_marios_coords_30',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_31_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_31_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_31_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_run_dialog_32',
        "command": 'run_dialog',
        "args": [1068, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_33_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_33_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_33_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_33_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1708_run_background_event_35',
        "command": 'run_background_event',
        "args": [1709, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1708_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_37_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 90, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_37_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_38_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 102, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_38_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_set_bit_39',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1708_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_41_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 115, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_41_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_41_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1708_action_queue_async_42_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 98, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1708_action_queue_async_42_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1708_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 472]
    },
    {
        "identifier": 'EVENT_1708_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 472]
    },
    {
        "identifier": 'EVENT_1708_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 472]
    },
    {
        "identifier": 'EVENT_1708_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 469]
    },
    {
        "identifier": 'EVENT_1708_ret_47',
        "command": 'ret'
    }
]
