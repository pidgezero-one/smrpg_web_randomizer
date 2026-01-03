
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2448_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'EVENT_2448_ret_255']
    },
    {
        "identifier": 'EVENT_2448_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 6]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 7]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7046, 0]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7046, 1]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_11_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_12_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_12_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_13',
        "command": 'run_dialog',
        "args": [3184, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_summon_to_current_level_at_marios_coords_14',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_15_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_15_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_15_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_15_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_16',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_17',
        "command": 'run_dialog',
        "args": [3185, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_18_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_unsync_dialog_19',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_20_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_20_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_21_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_22_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_25',
        "command": 'run_dialog',
        "args": [3186, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 487]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 487]
    },
    {
        "identifier": 'EVENT_2448_run_background_event_36',
        "command": 'run_background_event',
        "args": [2446, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_37',
        "command": 'run_dialog',
        "args": [3187, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_38_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_38_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_bit_39',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2448_stop_all_background_events_40',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_2448_pause_41',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_42',
        "command": 'run_dialog',
        "args": [3188, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_43',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_44_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_45',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_46_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_46_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_47',
        "command": 'run_dialog',
        "args": [3189, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_freeze_camera_48',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_49_SUBSCRIPT_end_loop_7',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_background_event_50',
        "command": 'run_background_event',
        "args": [2465, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_51_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 4, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_51_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_51_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [5, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_53',
        "command": 'run_dialog',
        "args": [3190, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_54',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_2448_set_bit_55',
        "command": 'set_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_56_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_56_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_56_SUBSCRIPT_face_west_2',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_56_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_56_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_57_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_57_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_57_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_58',
        "command": 'run_dialog',
        "args": [3192, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_59_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_60_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_60_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_61_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_62',
        "command": 'run_dialog',
        "args": [3191, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [14, 37]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_63_SUBSCRIPT_sequence_looping_off_11',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [15, 35]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_64_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_65',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_unfreeze_camera_66',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_67_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [17, 40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_67_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [17]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_67_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_68_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_68_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [17, 40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_68_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [13]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_68_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_69_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_69_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_69_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_69_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_69_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_72',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_73',
        "command": 'run_dialog',
        "args": [3193, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_74',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_17]
    },
    {
        "identifier": 'EVENT_2448_unsync_dialog_75',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_76_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_76_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_77',
        "command": 'run_dialog',
        "args": [3194, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_78',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_79',
        "command": 'run_dialog',
        "args": [3195, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_81_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_82',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 29, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [20, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x21, 0xe2, 0xc4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 6]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_sequence_playback_on_10',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [17, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_84',
        "command": 'run_dialog',
        "args": [3196, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_85_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [17, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_86_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_86_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_87',
        "command": 'run_dialog',
        "args": [3197, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_join_party_88',
        "command": 'join_party',
        "args": [AreaObjects.GENO]
    },
    {
        "identifier": 'EVENT_2448_start_battle_89',
        "command": 'start_battle',
        "args": [0x00b5, 1]
    },
    {
        "identifier": 'EVENT_2448_jmp_if_bit_clear_90',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2448_set_bit_92']
    },
    {
        "identifier": 'EVENT_2448_reset_and_choose_game_91',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2448_set_bit_92',
        "command": 'set_bit',
        "args": [0x7083, 6]
    },
    {
        "identifier": 'EVENT_2448_set_bit_93',
        "command": 'set_bit',
        "args": [0x706e, 4]
    },
    {
        "identifier": 'EVENT_2448_set_bit_94',
        "command": 'set_bit',
        "args": [0x7066, 4]
    },
    {
        "identifier": 'EVENT_2448_set_bit_95',
        "command": 'set_bit',
        "args": [0x7066, 5]
    },
    {
        "identifier": 'EVENT_2448_set_bit_96',
        "command": 'set_bit',
        "args": [0x7066, 6]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_97',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_98',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_99',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_100',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_101',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_102',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_103',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_104',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_105',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_106',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_17]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_107',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_108',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_109',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_110',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_111',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_112',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_113',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_114',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_115',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_116',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_117',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_118',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_119',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_120',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_17, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_121',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09]
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_122',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._228_FOREST_MAZE_AREA_04]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_123',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_123_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_123_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [12, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_124_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_125',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_125_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 31]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_126',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_126_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 34]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_126_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_126_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_127',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_127_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_127_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [11, 26]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_127_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_127_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_128_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [9, 16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_128_SUBSCRIPT_object_memory_modify_bits_1',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_129',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_129_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_129_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [8, 17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_fade_in_from_black_async_130',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_131_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_132',
        "command": 'run_dialog',
        "args": [3198, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_134',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_135_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_136_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_137_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_137_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_137_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_138',
        "command": 'run_dialog',
        "args": [3199, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_140',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_freeze_camera_141',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_142',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_142_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_143',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_async_143_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_143_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_144',
        "command": 'run_dialog',
        "args": [3200, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_145',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_146',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_146_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_146_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_147',
        "command": 'run_dialog',
        "args": [3201, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_148_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_149',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_150_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_150_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_150_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_151',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_151_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_151_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_151_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_152',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_154',
        "command": 'run_dialog',
        "args": [3202, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_155',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_157',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_157_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_158',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_159',
        "command": 'run_dialog',
        "args": [3203, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_160',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_161',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_161_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_163',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_164_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_165',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_async_165_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_shift_northwest_steps_12',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_166',
        "command": 'run_dialog',
        "args": [3204, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_167',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_168',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_168_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_169',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_169_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_170',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_170_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_171',
        "command": 'run_dialog',
        "args": [3205, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_172',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 7, 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_1']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_174',
        "command": 'run_dialog',
        "args": [3206, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_set_bit_175',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_176',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_177',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_11, 395]
    },
    {
        "identifier": 'EVENT_2448_pause_178',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_179',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_180',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 6, 'EVENT_2448_run_dialog_181']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_180_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_2448_action_queue_sync_180_SUBSCRIPT_set_sprite_sequence_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_181',
        "command": 'run_dialog',
        "args": [3207, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_set_bit_182',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_2448_pause_183',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [62]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [27, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_184_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_185',
        "command": 'run_dialog',
        "args": [3208, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_186',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_186_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_187',
        "command": 'run_dialog',
        "args": [3210, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_fade_out_music_FDA3_188',
        "command": 'fade_out_music_FDA3'
    },
    {
        "identifier": 'EVENT_2448_pause_189',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_190',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_2448_pause_191',
        "command": 'pause',
        "args": [74]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_192',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_192_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_192_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_192_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_193',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_193_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_194',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 393]
    },
    {
        "identifier": 'EVENT_2448_pause_195',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_196',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_196_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [1, 2]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_197',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2448_pause_short_198',
        "command": 'pause_short',
        "args": [448]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_pause_short_3',
                "command": 'pause_short',
                "args": [384]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [31, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_200',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_200_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_201',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_15]
    },
    {
        "identifier": 'EVENT_2448_pause_202',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_shift_z_down_pixels_12',
                "command": 'shift_z_down_pixels',
                "args": [44]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_shift_west_pixels_14',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_shift_z_down_pixels_15',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_204',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_205',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_2448_pause_206',
        "command": 'pause',
        "args": [256]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_207',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_207_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_207_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_207_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_207_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_207_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_208',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_208_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [67]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_208_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_208_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_209',
        "command": 'pause',
        "args": [73]
    },
    {
        "identifier": 'EVENT_2448_fade_out_to_black_async_duration_210',
        "command": 'fade_out_to_black_async_duration',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_211',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_212',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15]
    },
    {
        "identifier": 'EVENT_2448_run_star_piece_sequence_213',
        "command": 'run_star_piece_sequence',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_214',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_214_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [8, 17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_215',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_216',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_216_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_216_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_216_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_217',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_13, 395]
    },
    {
        "identifier": 'EVENT_2448_fade_in_from_black_async_218',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2448_run_dialog_219',
        "command": 'run_dialog',
        "args": [3212, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_220',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_220_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_221',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_221_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_222',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_223',
        "command": 'run_dialog',
        "args": [3209, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_224',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER]
    },
    {
        "identifier": 'EVENT_2448_pause_225',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_226',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_227',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2448_pause_228',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_229',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_229_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_229_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_230',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_231',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_bpl_26_27_28_14',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_231_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_232',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 484]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_233',
        "command": 'run_dialog',
        "args": [3211, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_set_bit_234',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2448_pause_235',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_236',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_236_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_237',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_238',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_238_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_238_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_238_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_restore_all_hp_239',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2448_restore_all_fp_240',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2448_db_241',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_2448_pause_script_until_effect_done_242',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_2448_run_dialog_243',
        "command": 'run_dialog',
        "args": [3440, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2448_pause_244',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_245',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2448_pause_246',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'EVENT_2448_play_sound_247',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_2448_pause_248',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_db_249',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_2448_pause_script_until_effect_done_250',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_251',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2448_pause_252',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_253',
        "command": 'play_music_default_volume',
        "args": [Music._26_FOREST_MAZE]
    },
    {
        "identifier": 'EVENT_2448_unfreeze_camera_254',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2448_ret_255',
        "command": 'ret'
    }
]
