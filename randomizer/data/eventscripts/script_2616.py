from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2616_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_set_bit_1',
        "command": 'set_bit',
        "args": [0x7091, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_2_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._009_GREEN_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_2_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_3_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 82]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 391],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 61]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_2616_pause_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_14, 944],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 3, 'EVENT_2616_pause_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_12_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [3, 66]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_pause_13',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 4, 'EVENT_2616_pause_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_15_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_15_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_pause_16',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_dec_z_coord_1_step_0',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_17_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_floating_off_8',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_18_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_pause_19',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_unfreeze_camera_20',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_shift_z_up_steps_0',
                "command": 'shift_z_up_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_21_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shadow_off_7',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_22_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_23_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_freeze_camera_24',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_pause_25',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_async_26_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_27_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0xd0, 0xfd, 0xb0, 0x01]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0xa0, 0xff]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [27]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._019_LONG_FALL, 4]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x24, 0x40, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0x24, 0x00, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_set_vram_priority_11',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_set_priority_13',
                "command": 'set_priority',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_28_SUBSCRIPT_bpl_26_27_28_15',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2616_action_queue_sync_29_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [37]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_29_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_29_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x00, 0x00, 0xd0, 0xff]
            },
            {
                "identifier": 'EVENT_2616_action_queue_sync_29_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [59]
            }
        ]
    },
    {
        "identifier": 'EVENT_2616_pause_30',
        "command": 'pause',
        "args": [88],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_fade_out_to_black_async_duration_31',
        "command": 'fade_out_to_black_async_duration',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_pause_32',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_jmp_to_event_33',
        "command": 'jmp_to_event',
        "args": [3791],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2616_ret_34',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
