from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1650_stop_music_0',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1650_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1650_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._338_MOLEVILLE_DYNA_AND_MITES_HOUSE, RadialDirections.SOUTHWEST, 4, 41, 0, []]
    },
    {
        "identifier": 'EVENT_1650_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_async_3_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_3_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_3_SUBSCRIPT_transfer_xyzf_steps_2',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 20, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_4_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_4_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [2, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_5_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1650_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_1650_fade_out_sound_to_volume_9']
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 650]
    },
    {
        "identifier": 'EVENT_1650_fade_out_sound_to_volume_9',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 64]
    },
    {
        "identifier": 'EVENT_1650_play_sound_balance_10',
        "command": 'play_sound_balance',
        "args": [Sounds._019_LONG_FALL, 32]
    },
    {
        "identifier": 'EVENT_1650_pause_11',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1650_fade_out_sound_to_volume_12',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 127]
    },
    {
        "identifier": 'EVENT_1650_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_14_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_10',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_11',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_13',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_15',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_start_loop_n_times_16',
                "command": 'start_loop_n_times',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_17',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_south_pixels_18',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_end_loop_19',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_15_SUBSCRIPT_shift_north_pixels_20',
                "command": 'shift_north_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 41, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_shadow_on_3',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x17, 0x7a]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [104]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_jump_to_height_silent_7',
                "command": 'jump_to_height_silent',
                "args": [104]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_walk_1_step_north_8',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_jmp_if_mario_in_air_10',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_9']
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_17_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_walk_1_step_northeast_6',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x16, 0xc3]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_jump_to_height_10',
                "command": 'jump_to_height',
                "args": [133]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_walk_1_step_northeast_11',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x16, 0xce]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_jump_to_height_14',
                "command": 'jump_to_height',
                "args": [125]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_shift_southeast_steps_15',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_db_17',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x16, 0xda]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_jump_to_height_18',
                "command": 'jump_to_height',
                "args": [116]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_clear_solidity_bits_20',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_pause_19',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1650_set_short_20',
        "command": 'set_short',
        "args": [0x7034, 0x0002]
    },
    {
        "identifier": 'EVENT_1650_set_short_21',
        "command": 'set_short',
        "args": [0x7010, 0x0900]
    },
    {
        "identifier": 'EVENT_1650_set_short_22',
        "command": 'set_short',
        "args": [0x7012, 0x1500]
    },
    {
        "identifier": 'EVENT_1650_set_short_23',
        "command": 'set_short',
        "args": [0x7014, 0x0100]
    },
    {
        "identifier": 'EVENT_1650_start_loop_n_times_24',
        "command": 'start_loop_n_times',
        "args": [23]
    },
    {
        "identifier": 'EVENT_1650_pause_25',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1650_create_packet_at_7010_coords_jmp_if_null_26',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1650_pause_25']
    },
    {
        "identifier": 'EVENT_1650_pause_27',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1650_add_short_28',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_1650_add_short_29',
        "command": 'add_short',
        "args": [0x7014, 0x0070]
    },
    {
        "identifier": 'EVENT_1650_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_31_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_31_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_31_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_31_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_32_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_32_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_32_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_32_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_sync_33_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_shift_east_steps_3',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1650_action_queue_async_34_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 650]
    },
    {
        "identifier": 'EVENT_1650_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1650_pause_script_until_effect_done_278']
    },
    {
        "identifier": 'EVENT_1650_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_43',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_44',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_45',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_46',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_47',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_48',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_49',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_50',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_51',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_52',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_53',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_54',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_55',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_56',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_57',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_58',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_59',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_60',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_61',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_62',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_63',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_64',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_65',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_66',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_67',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_68',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_69',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_70',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_71',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_72',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_73',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_74',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_75',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_76',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_77',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_78',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_79',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_80',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_81',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_82',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_83',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_84',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_85',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_86',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_87',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_88',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_89',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_90',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_91',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_92',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_93',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_94',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_95',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_96',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_97',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_98',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_99',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_100',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_101',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_102',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_103',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_104',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_105',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_106',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_107',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_108',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_109',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_110',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_111',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_112',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_113',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_114',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_115',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_116',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_117',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_118',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_119',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_120',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_121',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_122',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_123',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_124',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_125',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_126',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_127',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_128',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_129',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_130',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_131',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_132',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_133',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_134',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_135',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_136',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_137',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_138',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_139',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_140',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_141',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_142',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_143',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_144',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_145',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_146',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_147',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_148',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_149',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_150',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_151',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_152',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_153',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_154',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_155',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_156',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_157',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_158',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_159',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_160',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_161',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_162',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_163',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_164',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_165',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_166',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_167',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_168',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_169',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_170',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_171',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_172',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_173',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_174',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_175',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_176',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_177',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_178',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_179',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_180',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_181',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_182',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_183',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_184',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_185',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_186',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_187',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_188',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_189',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_190',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_191',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_192',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_193',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_194',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_195',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_196',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_197',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_198',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_199',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_200',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_201',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_202',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_203',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_204',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_205',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_206',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_207',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_208',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_209',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_210',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_211',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_212',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_213',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_214',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_215',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_216',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_217',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_218',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_219',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_220',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_221',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_222',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_223',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_224',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_225',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_226',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_227',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_228',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_229',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_230',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_231',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_232',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_233',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_234',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_235',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_236',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_237',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_238',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_239',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_240',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_241',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_242',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_243',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_244',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_245',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_246',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_247',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_248',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_249',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_250',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_251',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_252',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_253',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_254',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_255',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_256',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_257',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_258',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_259',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_260',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_261',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_262',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_263',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_264',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_265',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_266',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_267',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_268',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_269',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_270',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_271',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_272',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_273',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_274',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_275',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_276',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_stop_sound_277',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1650_pause_script_until_effect_done_278',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_1650_set_bit_279',
        "command": 'set_bit',
        "args": [0x707a, 5]
    },
    {
        "identifier": 'EVENT_1650_set_bit_280',
        "command": 'set_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_1650_set_bit_281',
        "command": 'set_bit',
        "args": [0x707b, 2]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_282',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 160]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_283',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 160]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_284',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 160]
    },
    {
        "identifier": 'EVENT_1650_ret_285',
        "command": 'ret'
    }
]
