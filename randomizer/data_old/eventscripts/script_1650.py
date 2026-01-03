
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
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
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, False],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
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
        "identifier": 'EVENT_1650_set_action_script_async__35',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_1, False, 650]
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.SCREEN_FOCUS, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
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
                "command": 'jmp_if_object_in_air',
                "args": [AreaObjects.NPC_3, 'EVENT_1650_action_queue_sync_16_SUBSCRIPT_pause_6']
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
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_2, True],
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
                "command": 'jmp_if_object_in_air',
                "args": [AreaObjects.NPC_2, 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_8']
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
                "command": 'jmp_if_object_in_air',
                "args": [AreaObjects.NPC_2, 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_12']
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
                "command": 'jmp_if_object_in_air',
                "args": [AreaObjects.NPC_2, 'EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_16']
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
        "command": "set_var_to_const",
        "args": [0x7034, 0x0002]
    },
    {
        "identifier": 'EVENT_1650_set_short_21',
        "command": "set_var_to_const",
        "args": [0x7010, 0x0900]
    },
    {
        "identifier": 'EVENT_1650_set_short_22',
        "command": "set_var_to_const",
        "args": [0x7012, 0x1500]
    },
    {
        "identifier": 'EVENT_1650_set_short_23',
        "command": "set_var_to_const",
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
        "identifier": 'EVENT_1650_create_packet_at_7010_26',
        "command": 'create_packet_at_7010',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1650_pause_25']
    },
    {
        "identifier": 'EVENT_1650_pause_27',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1650_add_short_28',
        "command": "add_const_to_var",
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_1650_add_short_29',
        "command": "add_const_to_var",
        "args": [0x7014, 0x0070]
    },
    {
        "identifier": 'EVENT_1650_end_loop_30',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1650_action_queue_sync_31',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_2, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_0, True],
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
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, False],
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
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_2, False, 650]
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
        "identifier": 'EVENT_1650_set_action_script_sync_282',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_0, True, 160]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_283',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_1, True, 160]
    },
    {
        "identifier": 'EVENT_1650_set_action_script_sync_284',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_2, True, 160]
    },
    {
        "identifier": 'EVENT_1650_ret_285',
        "command": 'ret'
    }
]
