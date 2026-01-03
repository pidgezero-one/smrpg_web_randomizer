
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_373_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_375_play_music_default_volume_0']
    },
    {
        "identifier": 'EVENT_373_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_373_jmp_if_mario_in_air_2',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_373_pause_1']
    },
    {
        "identifier": 'EVENT_373_set_7016_to_object_xyz_3',
        "command": 'set_7016_to_object_xyz',
        "args": [0x80]
    },
    {
        "identifier": 'EVENT_373_jmp_if_var_not_equals_short_4',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x701a, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_bounce_to_xy_with_height_3',
                "command": 'bounce_to_xy_with_height',
                "args": [16, 29, 4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_6_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [12, 9]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_9_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_11_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_13_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_15_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_16_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_16_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._086_BIG_BOUNCE, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x00, 0x0a, 0xe0, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_transfer_to_xyzf_6',
                "command": 'transfer_to_xyzf',
                "args": [18, 26, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_17_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [13]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_18_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_18_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [150]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_18_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_18_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_373_pause_20',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_373_set_bit_21',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_action_script_22',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 103]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 103]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 103]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 103]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 103]
    },
    {
        "identifier": 'EVENT_373_jmp_if_bit_clear_28',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 4, 'EVENT_373_action_queue_sync_32']
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 103]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 103]
    },
    {
        "identifier": 'EVENT_373_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_373_play_sound_34']
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_33_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_35_SUBSCRIPT_shift_north_pixels_9',
                "command": 'shift_north_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_36',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_373_clear_bit_37',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 113]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_39_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 636]
    },
    {
        "identifier": 'EVENT_373_play_sound_41',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 6]
    },
    {
        "identifier": 'EVENT_373_run_dialog_42',
        "command": 'run_dialog',
        "args": [625, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_43',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_44_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_45_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_46_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_46_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_47_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_47_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_48_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_48_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_49_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_49_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_51',
        "command": 'run_event_as_subroutine',
        "args": [272]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_52_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_53_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_53_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_54_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_54_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_55_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_55_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_56_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_57_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_57_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_unsync_dialog_58',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_373_pause_59',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [72]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_60_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_61',
        "command": 'set',
        "args": [0x70a9, 24]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_62',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_63_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_64',
        "command": 'run_dialog',
        "args": [626, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_65_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_66',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_67',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_68_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_68_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_69_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_70',
        "command": 'run_dialog',
        "args": [627, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_walk_1_step_northwest_6',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_71_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_72',
        "command": 'set',
        "args": [0x70a9, 26]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_73',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_74_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_74_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_75_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_75_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_76',
        "command": 'run_dialog',
        "args": [628, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_77',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_78_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_78_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_78_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [72]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_78_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_79',
        "command": 'set',
        "args": [0x70a9, 26]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_80',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_81_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_82',
        "command": 'run_dialog',
        "args": [629, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_83_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_83_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_83_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_play_sound_84',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
    },
    {
        "identifier": 'EVENT_373_xor_3105_with_01_85',
        "command": 'xor_3105_with_01'
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x84, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_walk_1_step_southeast_7',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_86_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x84, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_87_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x84, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_walk_1_step_northeast_9',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_88_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x84, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_walk_1_step_northwest_7',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_89_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x40, 0x08, 0x84, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_90_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_play_sound_91',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_92',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_set_bit_93',
        "command": 'set_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_373_clear_bit_94',
        "command": 'clear_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_373_clear_bit_95',
        "command": 'clear_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_373_fade_out_music_to_volume_96',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1]
    },
    {
        "identifier": 'EVENT_373_start_battle_97',
        "command": 'start_battle',
        "args": [0x00b3, 15]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_98',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_373_xor_3105_with_01_99',
        "command": 'xor_3105_with_01'
    },
    {
        "identifier": 'EVENT_373_set_bit_100',
        "command": 'set_bit',
        "args": [0x7082, 0]
    },
    {
        "identifier": 'EVENT_373_restore_all_hp_101',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_373_restore_all_fp_102',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_373_play_music_current_volume_103',
        "command": 'play_music_current_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_373_pause_104',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_373_stop_music_FDA2_105',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_106',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_107',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_108',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_109',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_110',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_111',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_111_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_112',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_112_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_fade_in_from_black_async_113',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_373_pause_114',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_115_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_115_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_store_02_to_0248_116',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_373_db_117',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x99, 0x07, 0x0f]
    },
    {
        "identifier": 'EVENT_373_pause_118',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_373_store_00_to_0248_119',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_373_pause_action_script_120',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_pixels_10',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_shift_z_up_pixels_12',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_121_SUBSCRIPT_set_priority_13',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_122_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_122_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_122_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_122_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_123',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_124',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_pause_125',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_373_start_embedded_action_script_async_F1_126',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_start_embedded_action_script_async_F1_126_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_127',
        "command": 'pause',
        "args": [69]
    },
    {
        "identifier": 'EVENT_373_play_music_default_volume_128',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_373_pause_129',
        "command": 'pause',
        "args": [51]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_130',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 634]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_131_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_131_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_walk_1_step_west_4',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_132_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_unsync_action_script_133',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_134_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_134_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_134_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_135',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_136',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 120]
    },
    {
        "identifier": 'EVENT_373_pause_137',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_373_pause_action_script_138',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_139',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_139_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_10',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_12',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_140_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [90]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 13, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_141_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_142',
        "command": 'pause',
        "args": [232]
    },
    {
        "identifier": 'EVENT_373_play_music_default_volume_143',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_144',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_145',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_145_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_145_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_146',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_146_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_146_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_146_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_146_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_147',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_147_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_147_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_pause_148',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_149_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_149_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_149_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_149_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 29, 9, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [42]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_150_SUBSCRIPT_shift_z_up_pixels_8',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_151_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_151_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_151_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_151_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_151_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_152',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_db_153',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0a, 0x06]
    },
    {
        "identifier": 'EVENT_373_set_bit_154',
        "command": 'set_bit',
        "args": [0x7062, 1]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_155',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 120]
    },
    {
        "identifier": 'EVENT_373_pause_156',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_373_pause_action_script_157',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_158',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_158_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_159',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_159_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_159_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_160',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_160_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_160_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_remember_last_object_161',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_373_run_star_piece_sequence_162',
        "command": 'run_star_piece_sequence',
        "args": [1]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_163',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_373_remove_from_current_level_164',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_165',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_165_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_165_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_db_166',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x72, 0x00, 0x06]
    },
    {
        "identifier": 'EVENT_373_fade_out_music_to_volume_167',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1]
    },
    {
        "identifier": 'EVENT_373_play_music_current_volume_168',
        "command": 'play_music_current_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_373_pause_169',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_373_stop_music_FDA2_170',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_373_set_bit_171',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_172',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_373_fade_in_from_black_async_173',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_373_pause_174',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_175',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 135]
    },
    {
        "identifier": 'EVENT_373_pause_176',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_177',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_177_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_177_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [11, 15, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_178',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_178_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_179',
        "command": 'run_dialog',
        "args": [708, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_180',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_181',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_182',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_183',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 135]
    },
    {
        "identifier": 'EVENT_373_pause_184',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_185',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_185_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_186',
        "command": 'run_dialog',
        "args": [708, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_187',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_188',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_189',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_190',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 135]
    },
    {
        "identifier": 'EVENT_373_pause_191',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_192',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_192_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_193',
        "command": 'run_dialog',
        "args": [709, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_194',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_195',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_196',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_197',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 135]
    },
    {
        "identifier": 'EVENT_373_pause_198',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_199',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_199_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_200',
        "command": 'run_dialog',
        "args": [710, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_201',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_202',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_203',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_204',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 135]
    },
    {
        "identifier": 'EVENT_373_pause_205',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_206',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_206_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_207',
        "command": 'run_dialog',
        "args": [711, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_208',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_209',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_210',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_211',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 135]
    },
    {
        "identifier": 'EVENT_373_pause_212',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_213',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_213_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_run_dialog_214',
        "command": 'run_dialog',
        "args": [712, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_373_set_bit_215',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_pause_216',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_clear_bit_217',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_373_action_queue_sync_218',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_shift_southwest_steps_14',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_shift_southwest_pixels_15',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_bpl_26_27_28_16',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_373_action_queue_sync_218_SUBSCRIPT_visibility_off_17',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_action_queue_async_219',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_db_10',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_bpl_26_27_28_13',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_373_action_queue_async_219_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_373_remove_from_level_220',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    },
    {
        "identifier": 'EVENT_373_remove_from_level_221',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    },
    {
        "identifier": 'EVENT_373_pause_222',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_373_set_bit_223',
        "command": 'set_bit',
        "args": [0x7049, 2]
    },
    {
        "identifier": 'EVENT_373_run_event_as_subroutine_224',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_373_set_action_script_sync_225',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_373_ret_226',
        "command": 'ret'
    }
]
