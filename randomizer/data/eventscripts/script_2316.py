from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2316_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_0_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_1_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_1_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 0, 'EVENT_2316_freeze_camera_28']
    },
    {
        "identifier": 'EVENT_2316_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 1, 'EVENT_2316_freeze_camera_6']
    },
    {
        "identifier": 'EVENT_2316_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2316_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2316_freeze_camera_6',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2316_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x708e, 1]
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_overwrite_solidity_4',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_shift_z_up_steps_8',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x24, 0x20, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_shift_z_up_steps_12',
                "command": 'shift_z_up_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_8_SUBSCRIPT_bpl_26_27_28_13',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_9_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2316_pause_11',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'EVENT_2316_fade_out_to_black_async_duration_12',
        "command": 'fade_out_to_black_async_duration',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2316_enter_area_13',
        "command": 'enter_area',
        "args": [Rooms._419_LAZY_SHELL_CLOUD, RadialDirections.SOUTH, 4, 109, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2316_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 0, 'EVENT_2316_jmp_if_bit_clear_16']
    },
    {
        "identifier": 'EVENT_2316_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 690]
    },
    {
        "identifier": 'EVENT_2316_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 1, 'EVENT_2316_freeze_camera_18']
    },
    {
        "identifier": 'EVENT_2316_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 690]
    },
    {
        "identifier": 'EVENT_2316_freeze_camera_18',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_19_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 76]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_19_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_19_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [4, 111]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_shift_z_down_steps_4',
                "command": 'shift_z_down_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_20_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_async_21_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_21_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_21_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_set_bit_22',
        "command": 'set_bit',
        "args": [0x708e, 0]
    },
    {
        "identifier": 'EVENT_2316_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2316_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0x1c, 0x00, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [14, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_overwrite_solidity_10',
                "command": 'overwrite_solidity',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_24_SUBSCRIPT_shift_northeast_pixels_11',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_set_action_script_async_25',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2316_unfreeze_camera_26',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2316_ret_27',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2316_freeze_camera_28',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_overwrite_solidity_4',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_29_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [9, 88, 24, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_30_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 67]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_fade_in_from_black_async_31',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2316_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x24, 0xe3, 0xff, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [14, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_32_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x40, 0x00, 0x30, 0x01]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [37]
            },
            {
                "identifier": 'EVENT_2316_action_queue_sync_33_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2316_action_queue_async_34_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2316_action_queue_async_34_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2316_unfreeze_camera_35',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2316_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x708e, 0]
    },
    {
        "identifier": 'EVENT_2316_set_action_script_async_37',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2316_ret_38',
        "command": 'ret'
    }
]
