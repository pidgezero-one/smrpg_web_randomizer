
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1393_stop_music_FDA2_0',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1393_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1393_set_bit_2',
        "command": 'set_bit',
        "args": [0x7052, 2]
    },
    {
        "identifier": 'EVENT_1393_set_bit_3',
        "command": 'set_bit',
        "args": [0x7065, 0]
    },
    {
        "identifier": 'EVENT_1393_set_bit_4',
        "command": 'set_bit',
        "args": [0x7065, 1]
    },
    {
        "identifier": 'EVENT_1393_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_5_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_5_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_5_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_5_SUBSCRIPT_ret_4',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_sync_6_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_6_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_7_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_8_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_8_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_fade_in_from_black_sync_duration_9',
        "command": 'fade_in_from_black_sync_duration',
        "args": [149]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._015_NIGHT_CRICKETS, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._015_NIGHT_CRICKETS, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._015_NIGHT_CRICKETS, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._015_NIGHT_CRICKETS, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_shift_northwest_steps_13',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_jump_to_height_15',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_10_SUBSCRIPT_ret_17',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_11_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_11_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shadow_on_6',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_north_pixels_10',
                "command": 'shift_north_pixels',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_start_loop_n_times_11',
                "command": 'start_loop_n_times',
                "args": [13]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_north_pixels_12',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_east_pixels_13',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_north_pixels_16',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_east_pixels_17',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_end_loop_18',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_start_loop_n_times_19',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_north_pixels_20',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_shift_east_pixels_21',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_end_loop_22',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_13_SUBSCRIPT_ret_23',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_15_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_15_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_16',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._028_PIPE_ENTRANCE, 4]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_17_SUBSCRIPT_ret_7',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_18',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1393_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._017_OPEN_FRONT_GATE, 6]
    },
    {
        "identifier": 'EVENT_1393_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_sync_20_SUBSCRIPT_ret_7',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_shift_northeast_steps_12',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_21_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._016_MARIOS_PAD, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1393_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_24_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_set_bit_25',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_1393_pause_26',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1393_stop_music_FDA2_27',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1393_enter_area_28',
        "command": 'enter_area',
        "args": [Rooms._189_MARIOS_PIPEHOUSE, RadialDirections.SOUTHEAST, 3, 13, 0, []]
    },
    {
        "identifier": 'EVENT_1393_palette_set_29',
        "command": 'palette_set',
        "args": [33, 7, [0]]
    },
    {
        "identifier": 'EVENT_1393_stop_music_FDA2_30',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 9, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_31_SUBSCRIPT_shadow_on_6',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_32_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_32_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_32_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 95]
    },
    {
        "identifier": 'EVENT_1393_freeze_camera_34',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_35_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_fade_in_from_black_async_36',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1393_pause_37',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [1, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._016_OPEN_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_sequence_playback_off_10',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._018_SUDDEN_STOP, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_shift_northeast_pixels_15',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_38_SUBSCRIPT_face_northwest_18',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_39',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1393_run_dialog_40',
        "command": 'run_dialog',
        "args": [2759, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1393_pause_41',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_42_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_play_music_default_volume_43',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": 'EVENT_1393_pause_44',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1393_play_sound_45',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1393_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1393_set_7000_to_tapped_button_47',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1393_pause_48',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1393_mem_7000_and_const_49',
        "command": 'mem_7000_and_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_1393_jmp_if_7000_equals_short_50',
        "command": 'jmp_if_7000_equals_short',
        "args": [128, 'EVENT_1393_pause_action_script_52']
    },
    {
        "identifier": 'EVENT_1393_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_1393_set_7000_to_tapped_button_47']
    },
    {
        "identifier": 'EVENT_1393_pause_action_script_52',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1393_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [69]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 6]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_stop_sound_15',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1393_action_queue_async_53_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1393_pause_54',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1393_ret_55',
        "command": 'ret'
    }
]
