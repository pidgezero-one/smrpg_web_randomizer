from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1331_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1331_action_queue_async_2']
    },
    {
        "identifier": 'EVENT_1331_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_2_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_stop_sound_3',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [2, 121, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_4_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_5',
        "command": 'run_dialog',
        "args": [2812, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_pause_6',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_7',
        "command": 'run_dialog',
        "args": [2810, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_8_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_9_SUBSCRIPT_shift_north_pixels_8',
                "command": 'shift_north_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_face_east_3',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [101]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_6',
                "command": 'walk_to_xy_coords',
                "args": [4, 114]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_10_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_fixed_f_coord_on_16',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_11_SUBSCRIPT_shift_northeast_steps_17',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_pause_13',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1331_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1331_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1331_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1331_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._202_BOOSTER_TOWER_ENTRANCE]
    },
    {
        "identifier": 'EVENT_1331_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_20_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 115]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_21_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_21_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_22',
        "command": 'run_dialog',
        "args": [2813, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_pause_script_resume_on_next_dialog_page_a_23',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1331_pause_script_resume_on_next_dialog_page_a_24',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_25_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_unsync_dialog_26',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1331_close_dialog_27',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_28_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_29',
        "command": 'run_dialog',
        "args": [2814, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_30_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [34]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_30_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_pause_31',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_32_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_33',
        "command": 'run_dialog',
        "args": [2815, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_fade_out_music_to_volume_34',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_1331_pause_35',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1331_play_music_default_volume_36',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER]
    },
    {
        "identifier": 'EVENT_1331_pause_37',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_38_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_38_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_38_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_38_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_39_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [8, 111, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_40_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_pause_41',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1331_close_dialog_42',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1331_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_sync_43_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1331_action_queue_sync_43_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1331_action_queue_async_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_44_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1331_action_queue_async_44_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_45',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1331_remove_from_level_46',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._202_BOOSTER_TOWER_ENTRANCE]
    },
    {
        "identifier": 'EVENT_1331_remove_from_current_level_47',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1331_set_bit_48',
        "command": 'set_bit',
        "args": [0x7062, 2]
    },
    {
        "identifier": 'EVENT_1331_set_bit_49',
        "command": 'set_bit',
        "args": [0x7053, 6]
    },
    {
        "identifier": 'EVENT_1331_join_party_50',
        "command": 'join_party',
        "args": [AreaObjects.BOWSER]
    },
    {
        "identifier": 'EVENT_1331_clear_bit_51',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1331_play_music_default_volume_52',
        "command": 'play_music_default_volume',
        "args": [Music._13_ROAD_IS_FULL_OF_DANGERS]
    },
    {
        "identifier": 'EVENT_1331_pause_53',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1331_run_dialog_54',
        "command": 'run_dialog',
        "args": [2940, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1331_jmp_if_dialog_option_b_55',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1331_ret_58']
    },
    {
        "identifier": 'EVENT_1331_run_menu_tutorial_56',
        "command": 'run_menu_tutorial',
        "args": [Tutorials._02_HOW_TO_SWITCH_ALLIES]
    },
    {
        "identifier": 'EVENT_1331_fade_in_from_black_async_57',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1331_ret_58',
        "command": 'ret'
    }
]
