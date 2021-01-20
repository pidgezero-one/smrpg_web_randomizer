from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_512_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 7, 'EVENT_512_jmp_to_subroutine_201'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_bit_2',
        "command": 'set_bit',
        "args": [0x7084, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_play_music_current_volume_3',
        "command": 'play_music_current_volume',
        "args": [Music._28_LETS_PLAY_GENO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_5_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 20, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_8_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_8_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_8_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_8_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_freeze_camera_9',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_12_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_13_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_13_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_14',
        "command": 'run_dialog',
        "args": [736, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_15',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_16_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_16_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_17',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_18_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_18_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_18_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_18_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [46]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_19_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_19_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_20',
        "command": 'run_dialog',
        "args": [737, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0x2d]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_21_SUBSCRIPT_jump_to_height_silent_12',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [79]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_22_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_22_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1a, 0x3e]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_22_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_23',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_24',
        "command": 'run_dialog',
        "args": [738, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_25',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0xf0, 0xfe, 0x68, 0x00]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x05, 0x78, 0xff]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_26_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0xf0, 0xfe, 0x68, 0x00]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x05, 0x78, 0xff]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_floating_on_5',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_27_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_28',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_29_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [21]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_shift_southwest_pixels_11',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_shift_northeast_pixels_14',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_30_SUBSCRIPT_fixed_f_coord_off_15',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [94]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x60, 0xff]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_32_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_33',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_34_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_34_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_35_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_35_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_36_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_37',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_38',
        "command": 'run_dialog',
        "args": [739, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_39_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_39_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_39_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_39_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_40_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_40_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_41',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_42',
        "command": 'run_dialog',
        "args": [740, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_43_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_44_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_45',
        "command": 'run_dialog',
        "args": [741, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_46_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_46_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_47_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_48',
        "command": 'run_dialog',
        "args": [742, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_49',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_50_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_51',
        "command": 'run_dialog',
        "args": [743, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_unsync_dialog_52',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_53',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_54_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_54_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_54_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_54_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_55',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_56_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_56_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_56_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_56_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_56_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_57',
        "command": 'run_dialog',
        "args": [744, AreaObjects.NPC_1, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_58',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_59_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_59_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_59_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_59_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_59_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_60',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_61_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_62',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_63_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_63_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_63_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_63_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_63_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_64_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_64_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_65',
        "command": 'run_dialog',
        "args": [745, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_66',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_67_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_68_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_68_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_68_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_68_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_69_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_69_SUBSCRIPT_face_east_1',
                "command": 'face_east',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_70',
        "command": 'run_dialog',
        "args": [746, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_71',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_72_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_73_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_74',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_75',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_76_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_76_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_77_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_77_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_77_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0xd0]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_78',
        "command": 'run_dialog',
        "args": [747, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_79_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_79_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_80_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_northwest_pixels_8',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_walk_1_step_west_13',
                "command": 'walk_1_step_west',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_west_pixels_14',
                "command": 'shift_west_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_southwest_steps_15',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_81_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_82_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_82_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_82_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_walk_1_step_west_6',
                "command": 'walk_1_step_west',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_83_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_84',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_85',
        "command": 'run_dialog',
        "args": [749, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_if_dialog_option_b_86',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_512_pause_98'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_87',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_event_as_subroutine_88',
        "command": 'run_event_as_subroutine',
        "args": [3587],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_89',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_90',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_91',
        "command": 'run_dialog',
        "args": [750, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_event_as_subroutine_92',
        "command": 'run_event_as_subroutine',
        "args": [286],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_93_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_93_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_93_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_512_action_queue_async_93_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_94',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_95_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_95_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_95_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0x58]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_96',
        "command": 'run_dialog',
        "args": [751, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_97',
        "command": 'jmp',
        "args": ['EVENT_512_action_queue_async_102'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_98',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_99',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_100',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_101',
        "command": 'run_dialog',
        "args": [752, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_102_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_102_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_103',
        "command": 'run_dialog',
        "args": [756, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_104',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_105_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_106',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_107',
        "command": 'run_dialog',
        "args": [757, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_108_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_108_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_109',
        "command": 'run_dialog',
        "args": [758, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_110',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_111',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_111_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_112',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_113',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_114',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0xa1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_walk_1_step_south_6',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_bounce_to_xy_with_height_7',
                "command": 'bounce_to_xy_with_height',
                "args": [2, 19, 0]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_115_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_116',
        "command": 'run_dialog',
        "args": [753, AreaObjects.NPC_1, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_remember_last_object_117',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_118_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_119',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_119_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_119_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_119_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_119_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_119_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_unsync_dialog_120',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_close_dialog_121',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_122_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_123',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_123_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_123_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_124',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_124_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_124_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_124_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_124_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_125',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_126',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_126_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_127',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_127_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_127_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_127_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_127_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_127_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_128',
        "command": 'run_dialog',
        "args": [754, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_129',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_130_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_130_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_130_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0x04]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_131',
        "command": 'run_dialog',
        "args": [759, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_132',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_512_action_queue_sync_133_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_jmp_if_mario_in_air_9',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_512_action_queue_sync_133_SUBSCRIPT_pause_8']
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_133_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x19, 0x35]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_134_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x19, 0x3f]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_135',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_start_loop_n_times_136',
        "command": 'start_loop_n_times',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_bit_137',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_138',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_end_loop_139',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_140_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_141',
        "command": 'run_dialog',
        "args": [755, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_142',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_142_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_142_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_143',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_143_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_143_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_143_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_run_dialog_144',
        "command": 'run_dialog',
        "args": [760, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_sync_145',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_146',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_147',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_147_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_148',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_148_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_play_sound_149',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_150_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_151_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_152',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_152_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_153',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_153_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_153_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_154',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_155',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_sync_156',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_action_script_async_157',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_158',
        "command": 'run_dialog',
        "args": [761, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_159',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_160',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_walk_1_step_northeast_9',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_shift_northeast_pixels_11',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_sequence_looping_off_12',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_160_SUBSCRIPT_fixed_f_coord_off_13',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_161',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_161_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_161_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_161_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_161_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_161_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_162_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_163_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_164',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_164_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_165',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_166',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_166_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_167',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_167_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_167_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_167_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_167_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_167_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_168',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_169',
        "command": 'run_dialog',
        "args": [762, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_170',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_170_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_170_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_170_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_170_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_170_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_171',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_171_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_172',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_173',
        "command": 'run_dialog',
        "args": [763, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_async_174',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_174_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_174_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 15, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_174_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_174_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_175',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_175_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_175_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_176',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._075_ROCKETING_BLAST, 6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_9',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_transfer_xyzf_pixels_10',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_13',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_transfer_xyzf_pixels_14',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_transfer_xyzf_pixels_17',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_19',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_transfer_xyzf_pixels_20',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_22',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_transfer_xyzf_pixels_23',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_25',
                "command": 'shift_southwest_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_177',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x04, 0x80, 0x00]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_177_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_178',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x00, 0x04, 0x80, 0x00]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_178_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_async_179',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_southeast_pixels_8',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_async_179_SUBSCRIPT_end_loop_10',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_180',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_181',
        "command": 'run_dialog',
        "args": [764, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_182',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_dec_z_coord_1_step_1',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_32',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_34',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_36',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_38',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_40',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_pause_41',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_42',
                "command": 'set_sprite_sequence',
                "args": [25, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_183',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0x5a]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_183_SUBSCRIPT_walk_1_step_southeast_7',
                "command": 'walk_1_step_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_184_SUBSCRIPT_floating_on_9',
                "command": 'floating_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_pause_185',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_186',
        "command": 'run_dialog',
        "args": [765, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_187',
        "command": 'pause',
        "args": [100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_slow_down_music_188',
        "command": 'slow_down_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pixelate_layers_189',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 15, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pixelate_layers_190',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 0, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_191',
        "command": 'pause',
        "args": [19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_192',
        "command": 'pause',
        "args": [19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pixelate_layers_193',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 15, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pixelate_layers_194',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 0, 196],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_195',
        "command": 'pause',
        "args": [25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_out_to_black_sync_duration_196',
        "command": 'fade_out_to_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pixelate_layers_197',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 15, 71],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_pause_script_until_effect_done_198',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_out_music_to_volume_199',
        "command": 'fade_out_music_to_volume',
        "args": [2, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_to_event_200',
        "command": 'jmp_to_event',
        "args": [513],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_to_subroutine_201',
        "command": 'jmp_to_subroutine',
        "args": [0x57c0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_if_bit_clear_202',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 0, 'EVENT_512_fade_in_from_black_async_221'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_set_7010_to_object_xyz_203',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_mem_compare_204',
        "command": 'mem_compare',
        "args": [0x7010, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_if_comparison_result_is_lesser_205',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_512_fade_out_music_to_volume_207'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_to_event_206',
        "command": 'jmp_to_event',
        "args": [261],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_out_music_to_volume_207',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_in_from_black_async_208',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_run_dialog_209',
        "command": 'run_dialog',
        "args": [0, AreaObjects.NPC_12, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_ret_210',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_211',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_211_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 21, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_212',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_212_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 20, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_213',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_213_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_213_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_jmp_if_bit_clear_214',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 0, 'EVENT_512_action_queue_sync_218'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_215',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_215_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_215_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_215_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_512_set_action_script_sync_216',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_217',
        "command": 'jmp',
        "args": ['EVENT_512_remember_last_object_219'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_action_queue_sync_218',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_512_action_queue_sync_218_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [1, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_218_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_512_action_queue_sync_218_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_512_remember_last_object_219',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_ret_220',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_fade_in_from_black_async_221',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_512_jmp_to_event_222',
        "command": 'jmp_to_event',
        "args": [515],
        "subscript": []
    }
]
