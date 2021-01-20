from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2448_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 6, 'EVENT_2448_ret_272'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7046, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7046, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_2448_stop_sound_89'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_13_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_13_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_14',
        "command": 'run_dialog',
        "args": [3184, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_summon_to_current_level_at_marios_coords_15',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_16_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_16_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_16_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_17',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_18',
        "command": 'run_dialog',
        "args": [3185, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_19_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_unsync_dialog_20',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_21_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_21_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_21_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_22_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_22_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_23_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_24_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_26',
        "command": 'run_dialog',
        "args": [3186, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 487],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_background_event_37',
        "command": 'run_background_event',
        "args": [2446, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_38',
        "command": 'run_dialog',
        "args": [3187, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_39_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_39_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_all_background_events_41',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_42',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_43',
        "command": 'run_dialog',
        "args": [3188, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_44',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_45_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_46',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_47_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_47_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_48',
        "command": 'run_dialog',
        "args": [3189, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_freeze_camera_49',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_50_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_50_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_50_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_50_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_50_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_background_event_51',
        "command": 'run_background_event',
        "args": [2465, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=4, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_52_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_52_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_54',
        "command": 'run_dialog',
        "args": [3190, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_55',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_56',
        "command": 'set_bit',
        "args": [0x7045, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_57_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_57_SUBSCRIPT_face_west_2',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_57_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_57_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_58_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_58_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_58_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_58_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_59',
        "command": 'run_dialog',
        "args": [3192, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_60_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_61_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_61_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_62_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_63',
        "command": 'run_dialog',
        "args": [3191, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [14, 37]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_64_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [15, 35]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_65_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_66',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_unfreeze_camera_67',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_68_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [17, 40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_68_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [17]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_68_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_69_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_69_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_70_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_71_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_72_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_72_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_73',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_74',
        "command": 'run_dialog',
        "args": [3193, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_75',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_unsync_dialog_76',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_77_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_78',
        "command": 'run_dialog',
        "args": [3194, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_79',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_80',
        "command": 'run_dialog',
        "args": [3195, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_sound_81',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_82_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_83',
        "command": 'pause',
        "args": [112],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 29, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x21, 0xc9]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 6]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_sequence_playback_on_10',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_84_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_85',
        "command": 'run_dialog',
        "args": [3196, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_87_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_87_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_88',
        "command": 'run_dialog',
        "args": [3197, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_89',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_90',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_start_battle_91',
        "command": 'start_battle',
        "args": [0x00b5, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_jmp_if_bit_clear_92',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2448_set_bit_94'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_reset_and_choose_game_93',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_94',
        "command": 'set_bit',
        "args": [0x7083, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_95',
        "command": 'set_bit',
        "args": [0x706e, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_96',
        "command": 'set_bit',
        "args": [0x7066, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_97',
        "command": 'set_bit',
        "args": [0x7066, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_98',
        "command": 'set_bit',
        "args": [0x7066, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_99',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_100',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_101',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_102',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_103',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_104',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_105',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_106',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_107',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_108',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_109',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_110',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_111',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_112',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_113',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_114',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_115',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_116',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_117',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_118',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_119',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_120',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_121',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_122',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_17, Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_123',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_level_124',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._228_FOREST_MAZE_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_jmp_125',
        "command": 'jmp',
        "args": ['EVENT_2448_fade_in_from_black_async_254'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_126',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_126_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_126_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [12, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_127',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_127_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_128_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 31]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_129_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [11, 34]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_129_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_129_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_130_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_130_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [11, 26]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_130_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_131_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [9, 16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_131_SUBSCRIPT_object_memory_modify_bits_1',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_132',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_132_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_132_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [8, 17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_fade_in_from_black_async_133',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_134',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_134_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_135',
        "command": 'run_dialog',
        "args": [3198, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_136_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_137',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_138_SUBSCRIPT_end_loop_9',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_139',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_139_SUBSCRIPT_end_loop_10',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_140_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_140_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_140_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_140_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_140_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_141',
        "command": 'run_dialog',
        "args": [3199, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_142',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_142_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_143',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_freeze_camera_144',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_145',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_146',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_jmp_if_mario_in_air_8',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_async_146_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_146_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_147',
        "command": 'run_dialog',
        "args": [3200, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_148_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_148_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_149_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_149_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_150',
        "command": 'run_dialog',
        "args": [3201, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_151_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_152',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_154',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_154_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_154_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_154_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_155',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_156_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_157',
        "command": 'run_dialog',
        "args": [3202, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_158',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_159',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_159_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_160',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_160_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_161',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_162',
        "command": 'run_dialog',
        "args": [3203, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_163',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_165',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_165_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_166',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_167',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_sync_167_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_168',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2448_action_queue_async_168_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_shift_northwest_steps_12',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_168_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_169',
        "command": 'run_dialog',
        "args": [3204, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_170',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_171',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_171_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_172',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_172_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_173_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_174',
        "command": 'run_dialog',
        "args": [3205, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_175',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_176',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 7, 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_sprite_sequence_7']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_sprite_sequence_1']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_176_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_177',
        "command": 'run_dialog',
        "args": [3206, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_178',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_179',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_180',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_11, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_181',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_182',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_183',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7044, 6, 'EVENT_2448_run_dialog_184']
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_183_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_2448_action_queue_sync_183_SUBSCRIPT_set_sprite_sequence_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_184',
        "command": 'run_dialog',
        "args": [3207, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_185',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_186',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_187',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [62]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [27, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_187_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_188',
        "command": 'run_dialog',
        "args": [3208, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_189',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_189_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_run_dialog_190',
        "command": 'run_dialog',
        "args": [3210, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_fade_out_music_191',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_192',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_193',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_194',
        "command": 'pause',
        "args": [74],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_195',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_195_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_195_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_195_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_196',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_196_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_197',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 393],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_198',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_199_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[1, 2]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_200',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_short_201',
        "command": 'pause_short',
        "args": [448],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_202',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_202_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_202_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_202_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_202_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [384]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_202_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_stop_embedded_action_script_204',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_205',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_206',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_shift_z_down_pixels_12',
                "command": 'shift_z_down_pixels',
                "args": [44]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_shift_west_pixels_14',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_shift_z_down_pixels_15',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_206_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_207',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_208',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_209',
        "command": 'pause',
        "args": [256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_210',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_210_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_210_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_210_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_210_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_210_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_211',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_211_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [67]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_211_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_211_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_212',
        "command": 'pause',
        "args": [73],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_fade_out_to_black_async_duration_213',
        "command": 'fade_out_to_black_async_duration',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_214',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_215',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_star_piece_sequence_216',
        "command": 'run_star_piece_sequence',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_217',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_217_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [8, 17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_218',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_219',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_219_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_219_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_219_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_220',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_13, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_fade_in_from_black_async_221',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_222',
        "command": 'run_dialog',
        "args": [3212, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_sync_223',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_sync_223_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_224',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_overwrite_solidity_1',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_224_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_225',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_226',
        "command": 'run_dialog',
        "args": [3209, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_227',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_228',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_229',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 385],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_async_230',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_231',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_232',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_232_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_232_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_clear_bit_233',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_234',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x24, 0x18, 0xff, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_bpl_26_27_28_14',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_234_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._077_EXOTIC_BIRD_CALLS, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_235',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 484],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_236',
        "command": 'run_dialog',
        "args": [3211, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_237',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_238',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_239',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_239_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_pause_240',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_action_queue_async_241',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2448_action_queue_async_241_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_241_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2448_action_queue_async_241_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2448_db_242',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_script_until_effect_done_243',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_run_dialog_244',
        "command": 'run_dialog',
        "args": [3440, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_245',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_action_script_sync_246',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_247',
        "command": 'pause',
        "args": [52],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_sound_248',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_249',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_db_250',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_pause_script_until_effect_done_251',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_252',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_253',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_fade_in_from_black_async_254',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_255',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_256',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_257',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_stop_sound_258',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_restore_all_hp_259',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_restore_all_fp_260',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_play_music_default_volume_261',
        "command": 'play_music_default_volume',
        "args": [Music._26_FOREST_MAZE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_unfreeze_camera_262',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_263',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_264',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_265',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_266',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_267',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_remove_from_current_level_268',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_bit_269',
        "command": 'set_bit',
        "args": [0x7062, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_set_short_270',
        "command": 'set_short',
        "args": [0x700a, 0x00cc],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_jmp_to_event_271',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2448_ret_272',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
