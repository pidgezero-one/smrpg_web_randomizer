from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3598_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 3, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [16, 30, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_2_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_3_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [12, 9]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_4',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_5',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_6_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_6_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_7_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_8',
        "command": 'run_dialog',
        "args": [555, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_join_party_9',
        "command": 'join_party',
        "args": [AreaObjects.TOADSTOOL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [18, 55, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_10_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_10_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_11_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_12_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_13',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_14',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_15_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_15_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_15_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_16',
        "command": 'run_dialog',
        "args": [556, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_18',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_20',
        "command": 'run_dialog',
        "args": [557, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_21_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_22_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_unsync_dialog_23',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_25_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_26',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_27',
        "command": 'run_dialog',
        "args": [558, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_freeze_camera_28',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_fade_out_music_to_volume_29',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_30',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_play_music_default_volume_31',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_set_action_script_async_33',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_34',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_visibility_off_22',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_visibility_on_24',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_visibility_off_27',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_visibility_on_29',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_reset_properties_32',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_transfer_to_xyzf_33',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_visibility_on_34',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_face_southwest_35',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_35_SUBSCRIPT_set_animation_speed_36',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [71]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_visibility_on_14',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_start_loop_n_times_22',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_36_SUBSCRIPT_end_loop_31',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_37_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_37_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_38',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 67],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 69],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 71],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 68],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 68],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 69],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_46_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_47_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_47_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_47_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [22, 48, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_48_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_summon_to_current_level_49',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 31, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._103_TOADSTOOL_CRYING, 6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_50_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_51_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_51_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [18, 55, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_51_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_51_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_52_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 31, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_52_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_52_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_52_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_53_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_54_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_54_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_54_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [22, 48, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_55_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_55_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_55_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_55_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [15, 31, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._103_TOADSTOOL_CRYING, 6]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_shift_northeast_pixels_11',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_stop_sound_16',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_56_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [18, 55, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_57_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [26, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_reset_properties_22',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_sequence_looping_off_23',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_58_SUBSCRIPT_face_northeast_24',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_add_z_coord_1_step_5',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_59_SUBSCRIPT_dec_z_coord_1_step_6',
                "command": 'dec_z_coord_1_step',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_60',
        "command": 'run_dialog',
        "args": [559, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_61_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_62',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_walk_1_step_southeast_4',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_63_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_64',
        "command": 'run_dialog',
        "args": [560, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_65',
        "command": 'run_dialog',
        "args": [561, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_66',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_bit_67',
        "command": 'set_bit',
        "args": [0x7049, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_async_68',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_69',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_70_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_70_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_70_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_70_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [28]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_walk_1_step_northeast_5',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_71_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_72',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_bit_73',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_74',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 72],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_75',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 74],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_76',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 71],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_77',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_78',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 73],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_79',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 73],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_80',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 75],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_81',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_82_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_82_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [22, 48, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_82_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [47]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=4, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_play_sound_13',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_83_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_84_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_84_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_84_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_84_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [23, 44, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_85',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_play_sound_29',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_86_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [39]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_floating_off_5',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [78]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_transfer_to_xyzf_8',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_walk_1_step_southwest_12',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_jump_to_height_silent_14',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northeast_pixels_16',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_jump_to_height_silent_18',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northeast_pixels_19',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_play_sound_22',
                "command": 'play_sound',
                "args": [Sounds._091_TUMBLING_BOULDERS, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northwest_pixels_23',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_start_loop_n_times_24',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_southeast_pixels_25',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northwest_pixels_26',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_end_loop_27',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_southeast_pixels_28',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_start_loop_n_times_29',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northwest_pixels_30',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_southeast_pixels_31',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_end_loop_32',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northwest_pixels_33',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_stop_sound_34',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_36',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_play_sound_37',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_38',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_clear_solidity_bits_39',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_db_40',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_db_41',
                "command": 'db',
                "args": [0x25, 0x00, 0x0a, 0x40, 0x00]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_animation_speed_42',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_walk_1_step_southwest_43',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_bpl_26_27_28_44',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_floating_off_45',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_transfer_to_xyzf_46',
                "command": 'transfer_to_xyzf',
                "args": [15, 32, 19, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_face_southwest_47',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_sprite_sequence_48',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_49',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_floating_on_50',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_set_solidity_bits_51',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_fixed_f_coord_on_52',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_shift_northeast_steps_53',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_54',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_jmp_if_mario_in_air_55',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_sync_87_SUBSCRIPT_pause_54']
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_87_SUBSCRIPT_play_sound_56',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.CHARACTER_IN_SLOT_2],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_floating_off_4',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._103_TOADSTOOL_CRYING, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_stop_sound_18',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_88_SUBSCRIPT_transfer_to_xyzf_19',
                "command": 'transfer_to_xyzf',
                "args": [20, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_89_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_89_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_89_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_89_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_90',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_mario_in_air_91',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3598_pause_90'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_92',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_92_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_92_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_93',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_async_94',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_95',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_96',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_fixed_f_coord_on_16',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_sequence_playback_on_17',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_jump_to_height_19',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_shift_south_pixels_21',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_jmp_if_mario_in_air_23',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_22']
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_jump_to_height_24',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_set_animation_speed_25',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_shift_west_pixels_26',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_jmp_if_mario_in_air_28',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_27']
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_end_loop_29',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_fixed_f_coord_off_31',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_96_SUBSCRIPT_face_northwest_32',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_97',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_async_98',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_99',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_100',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_100_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_100_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_100_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_unsync_action_script_101',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_fade_in_music_102',
        "command": 'fade_in_music',
        "args": [Music._02_MUSHROOM_KINGDOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_103',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_floating_on_1',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_dec_z_coord_1_step_5',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_add_z_coord_1_step_6',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_dec_z_coord_1_step_7',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_104_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_105',
        "command": 'run_dialog',
        "args": [562, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_106',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_floating_on_2',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_clear_solidity_bits_9',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_106_SUBSCRIPT_floating_off_10',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_107',
        "command": 'run_dialog',
        "args": [563, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_async_108',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_109',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_110',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_111',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_111_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_unfreeze_camera_113',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_bit_114',
        "command": 'set_bit',
        "args": [0x7081, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_leave_party_115',
        "command": 'leave_party',
        "args": [AreaObjects.TOADSTOOL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_store_character_equipment_7000_116',
        "command": 'store_character_equipment_7000',
        "args": [PlayableCharacters.MARIO, EquipSlots.WEAPON],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_var_equals_short_117',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 255, 'EVENT_3598_store_item_amount_7000_166'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_store_01_to_0248_118',
        "command": 'store_01_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_119',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_120',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_7000_to_pressed_button_121',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_7000_any_bits_set_122',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_3598_action_queue_sync_124'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_123',
        "command": 'jmp',
        "args": ['EVENT_3598_pause_120'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_124_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_124_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_124_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_124_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_125',
        "command": 'run_dialog',
        "args": [630, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_126',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_127',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_face_west_2',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_face_north_6',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_walk_to_xy_coords_8',
                "command": 'walk_to_xy_coords',
                "args": [16, 30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_127_SUBSCRIPT_face_northeast_9',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_128',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_129',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_129_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_130',
        "command": 'run_dialog',
        "args": [959, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_play_sound_131',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_132',
        "command": 'run_dialog',
        "args": [958, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_bit_133',
        "command": 'set_bit',
        "args": [0x7062, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_134',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_135',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_135_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3598_action_queue_async_135_SUBSCRIPT_pause_5']
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_136_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_136_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_136_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_137',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_138_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_139',
        "command": 'run_dialog',
        "args": [630, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_140',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_14',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [16, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_20',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_end_loop_21',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_23',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_25',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_141_SUBSCRIPT_shift_southwest_pixels_27',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_142',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_143',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_144',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_145',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_146',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_147',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_148',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 626],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_149',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_150_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_150_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_150_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_151',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_151_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_152',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_153_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_153_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_153_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_154',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_154_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_154_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_155',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_156',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_156_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_157',
        "command": 'run_dialog',
        "args": [965, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_158',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_159',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_159_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_160',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_161',
        "command": 'run_dialog',
        "args": [966, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_162',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_163',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_face_south_4',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_163_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_set_action_script_sync_164',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_ret_165',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_store_item_amount_7000_166',
        "command": 'store_item_amount_7000',
        "args": [items.Hammer],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_var_equals_short_167',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3598_store_01_to_0248_118'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_168',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_168_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_168_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_enable_controls_until_return_169',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_170',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_enable_controls_until_return_171',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_172',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_173',
        "command": 'run_dialog',
        "args": [880, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_174',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_174_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [16, 30]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_174_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_175',
        "command": 'run_dialog',
        "args": [881, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_176',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_177',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_177_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_178',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_178_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_178_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_178_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_178_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_async_178_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_179',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_179_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_179_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_179_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_179_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_179_SUBSCRIPT_jmp_4',
                "command": 'jmp',
                "args": ['EVENT_3598_action_queue_sync_179_SUBSCRIPT_set_sprite_sequence_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_180',
        "command": 'run_dialog',
        "args": [882, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_181',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_start_embedded_action_script_async_182',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_182_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_182_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_182_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_182_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_182_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_start_embedded_action_script_async_183',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_start_embedded_action_script_async_183_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_184_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_184_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_184_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_184_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_pause_185',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_186',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_unsync_dialog_187',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_188',
        "command": 'run_dialog',
        "args": [883, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_dialog_option_b_189',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3598_action_queue_sync_208'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_190',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_dialog_191',
        "command": 'run_dialog',
        "args": [884, AreaObjects.NPC_6, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_enable_controls_until_return_192',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_set_7000_to_tapped_button_193',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_if_7000_any_bits_set_194',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[4], 'EVENT_3598_close_dialog_197'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_195',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_196',
        "command": 'jmp',
        "args": ['EVENT_3598_set_7000_to_tapped_button_193'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_close_dialog_197',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_run_menu_tutorial_198',
        "command": 'run_menu_tutorial',
        "args": [Tutorials._00_HOW_TO_EQUIP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_199_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_199_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_199_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_199_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_199_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_fade_in_from_black_sync_200',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_201',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_script_until_effect_done_202',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_203_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_203_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_203_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_203_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_203_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_204',
        "command": 'run_dialog',
        "args": [885, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_205',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_async_206',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_async_206_SUBSCRIPT_face_south_0',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_jmp_207',
        "command": 'jmp',
        "args": ['EVENT_3598_store_01_to_0248_118'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_action_queue_sync_208',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3598_action_queue_sync_208_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_208_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_208_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_208_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3598_action_queue_sync_208_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3598_run_dialog_209',
        "command": 'run_dialog',
        "args": [886, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_pause_210',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_remember_last_object_211',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3598_jmp_212',
        "command": 'jmp',
        "args": ['EVENT_3598_action_queue_async_206'],
        "subscript": []
    }
]
