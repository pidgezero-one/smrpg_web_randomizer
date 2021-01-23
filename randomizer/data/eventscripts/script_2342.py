from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2342_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_2342_set_action_script_sync_49']
    },
    {
        "identifier": 'EVENT_2342_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7048, 0, 'EVENT_2342_set_action_script_sync_49']
    },
    {
        "identifier": 'EVENT_2342_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2342_freeze_camera_3',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 738]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x0f, 0xe1, 0xff]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [199]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_5_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [127]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_db_18',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_db_19',
                "command": 'db',
                "args": [0x25, 0x50, 0x0f, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [74]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_bpl_26_27_28_21',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_shirt_to_xy_coords_22',
                "command": 'shirt_to_xy_coords',
                "args": [18, 121]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [248]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_7_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_7_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [19]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_pause_8',
        "command": 'pause',
        "args": [255]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 739]
    },
    {
        "identifier": 'EVENT_2342_pause_10',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 7]
    },
    {
        "identifier": 'EVENT_2342_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_13_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_14_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_14_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_14_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_14_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_14_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_stop_embedded_action_script_15',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2342_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 14]
    },
    {
        "identifier": 'EVENT_2342_pause_18',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 738]
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_20_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [28]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_21_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 739]
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_25_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_25_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_pause_26',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2342_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2342_set_29',
        "command": 'set',
        "args": [0x70a7, 12]
    },
    {
        "identifier": 'EVENT_2342_set_30',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2342_run_event_as_subroutine_31',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_2342_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2342_set_action_script_async_41']
    },
    {
        "identifier": 'EVENT_2342_pause_action_script_33',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [18, 123]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [104]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_34_SUBSCRIPT_shift_z_down_steps_8',
                "command": 'shift_z_down_steps',
                "args": [19]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 6]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_async_36',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2342_pause_37',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0x80, 0x00, 0x80, 0x00]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2342_action_queue_sync_38_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._012_DIZZINESS, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_east_4',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_north_8',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_west_10',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_south_13',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_end_loop_15',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_shift_south_pixels_18',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [1, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_play_sound_20',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_shift_north_pixels_23',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_39_SUBSCRIPT_face_southwest_24',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_async_41',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2342_set_bit_42',
        "command": 'set_bit',
        "args": [0x7048, 0]
    },
    {
        "identifier": 'EVENT_2342_clear_bit_43',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2342_disable_trigger_in_level_44',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    },
    {
        "identifier": 'EVENT_2342_remove_from_current_level_45',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2342_enable_controls_46',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2342_unfreeze_camera_47',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2342_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2342_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 738]
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_50_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_50_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2342_action_queue_async_50_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [28]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_sync_51_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_pause_52',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2342_set_action_script_async_53',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 739]
    },
    {
        "identifier": 'EVENT_2342_set_7000_to_object_coord_54',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2342_jmp_if_7000_equals_short_55',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_2342_freeze_camera_58']
    },
    {
        "identifier": 'EVENT_2342_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2342_ret_57',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2342_freeze_camera_58',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2342_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2342_action_queue_async_59_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_2342_unfreeze_camera_60',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2342_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2342_ret_62',
        "command": 'ret'
    }
]
