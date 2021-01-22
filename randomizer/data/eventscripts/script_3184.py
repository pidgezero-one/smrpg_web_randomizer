from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3184_set_0',
        "command": 'set',
        "args": [0x70df, 54]
    },
    {
        "identifier": 'EVENT_3184_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3184_set_bit_3']
    },
    {
        "identifier": 'EVENT_3184_jmp_to_subroutine_2',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3183_jmp_if_bit_set_4']
    },
    {
        "identifier": 'EVENT_3184_set_bit_3',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_3184_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 1, 'EVENT_3184_jmp_if_bit_set_57']
    },
    {
        "identifier": 'EVENT_3184_play_music_default_volume_5',
        "command": 'play_music_default_volume',
        "args": [Music._27_DUNGEON_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_6_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_event_as_subroutine_7',
        "command": 'run_event_as_subroutine',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_8',
        "command": 'run_dialog',
        "args": [1616, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_9_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_9_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_10',
        "command": 'run_dialog',
        "args": [1617, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_11',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [18, 30]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_walk_1_step_southwest_11',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_walk_1_step_southwest_13',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_fixed_f_coord_off_15',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_face_southwest_16',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_shift_southwest_steps_18',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_object_memory_set_bit_20',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_db_21',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_clear_solidity_bits_22',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_11_SUBSCRIPT_end_all_23',
                "command": 'end_all'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_set_bit_12',
        "command": 'set_bit',
        "args": [0x7056, 1]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_13',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_13_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_14',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_14_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_pause_15',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_16',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_16_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [19, 29]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_17',
        "command": 'run_dialog',
        "args": [1618, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_18',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_18_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [18, 26]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_19',
        "command": 'run_dialog',
        "args": [1619, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_20',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_20_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_20_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [29]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_21',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_21_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_21_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_22',
        "command": 'run_dialog',
        "args": [1620, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_23',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [29]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_23_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_24',
        "command": 'run_dialog',
        "args": [1621, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_25',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_25_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_25_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [29]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_26',
        "command": 'run_dialog',
        "args": [1622, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_27',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_27_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_28',
        "command": 'run_dialog',
        "args": [1623, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_start_embedded_action_script_async_29',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_set_bit_5',
                "command": 'set_bit',
                "args": [0x7043, 3]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [29]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_walk_1_step_southwest_10',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_sequence_looping_on_13',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3184_start_embedded_action_script_async_29_SUBSCRIPT_set_bit_15',
                "command": 'set_bit',
                "args": [0x7043, 2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3184_jmp_if_bit_clear_31',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3184_pause_30']
    },
    {
        "identifier": 'EVENT_3184_run_dialog_32',
        "command": 'run_dialog',
        "args": [1624, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_set_33',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3184_set_temp_action_script_sync_34',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_35',
        "command": 'run_dialog',
        "args": [1625, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_jmp_if_dialog_option_b_36',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3184_set_48']
    },
    {
        "identifier": 'EVENT_3184_set_37',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3184_set_temp_action_script_sync_38',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_39',
        "command": 'run_dialog',
        "args": [1628, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_jmp_if_dialog_option_b_40',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3184_set_53']
    },
    {
        "identifier": 'EVENT_3184_set_41',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3184_set_temp_action_script_sync_42',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_43',
        "command": 'run_dialog',
        "args": [1630, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_44_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_44_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [1]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_44_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [19, 27]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_44_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_45_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_45_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [1]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_45_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [19, 26]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_45_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_46',
        "command": 'run_dialog',
        "args": [1631, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_ret_47',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3184_set_48',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3184_set_temp_action_script_sync_49',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_50',
        "command": 'run_dialog',
        "args": [1626, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_51',
        "command": 'run_dialog',
        "args": [1627, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_jmp_52',
        "command": 'jmp',
        "args": ['EVENT_3184_run_dialog_39']
    },
    {
        "identifier": 'EVENT_3184_set_53',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3184_set_temp_action_script_sync_54',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3184_run_dialog_55',
        "command": 'run_dialog',
        "args": [1629, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3184_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_3184_run_dialog_39']
    },
    {
        "identifier": 'EVENT_3184_jmp_if_bit_set_57',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'EVENT_3184_remove_from_current_level_62']
    },
    {
        "identifier": 'EVENT_3184_play_music_default_volume_58',
        "command": 'play_music_default_volume',
        "args": [Music._27_DUNGEON_IS_FULL_OF_MONSTERS]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_59_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [1]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_59_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [19, 27]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_59_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3184_action_queue_sync_60_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [1]]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_60_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [19, 26]
            },
            {
                "identifier": 'EVENT_3184_action_queue_sync_60_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3184_jmp_to_event_61',
        "command": 'jmp_to_event',
        "args": [15]
    },
    {
        "identifier": 'EVENT_3184_remove_from_current_level_62',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3184_remove_from_current_level_63',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3184_disable_trigger_64',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3184_disable_trigger_65',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3184_jmp_to_event_66',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
