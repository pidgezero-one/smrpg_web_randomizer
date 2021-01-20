from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3486_set_0',
        "command": 'set',
        "args": [0x70df, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_1_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_adjust_music_tempo_3',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_4_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7096, 5, 'EVENT_3486_action_queue_sync_5']
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_4_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_5_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_6_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0, 1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7096, 5, 'EVENT_3486_jmp_if_bit_set_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3486_remove_from_current_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3486_action_queue_async_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_short_13',
        "command": 'set_short',
        "args": [0x702a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_15_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 15, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_15_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_fade_in_from_black_sync_16',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_play_sound_balance_17',
        "command": 'play_sound_balance',
        "args": [Sounds._048_MINECART_START, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_18_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_18_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_18_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_19_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_19_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_19_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_19_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 5, 'EVENT_3486_action_queue_sync_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_jmp_if_bit_set_2',
                "command": 'jmp_if_bit_set',
                "args": [0x704e, 5, 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_5']
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_jmp_4',
                "command": 'jmp',
                "args": ['EVENT_3486_action_queue_sync_22']
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_22_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_22_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_22_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_22_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3486_action_queue_sync_23_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_jump_to_height_silent_10',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_shift_southwest_steps_11',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_jmp_if_mario_in_air_13',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_12']
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_24_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 5, 'EVENT_3486_ret_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 0, 'EVENT_3486_jmp_if_bit_set_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_28',
        "command": 'set_bit',
        "args": [0x7065, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_29',
        "command": 'set_bit',
        "args": [0x7065, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_30',
        "command": 'set_bit',
        "args": [0x706d, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_31',
        "command": 'set_bit',
        "args": [0x706d, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_32',
        "command": 'set_bit',
        "args": [0x7079, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_mem_compare_34',
        "command": 'mem_compare',
        "args": [0x7000, 32768],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_comparison_result_is_lesser_35',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3486_set_short_mem_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_36',
        "command": 'set',
        "args": [0x7000, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x70b3, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_set_bit_38',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 5, 'EVENT_3486_jmp_to_event_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._034_SQUIRM_WRITHE, 4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_shift_east_pixels_8',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_end_loop_9',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_shift_west_pixels_10',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_walk_1_step_southwest_11',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_fixed_f_coord_off_12',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_40_SUBSCRIPT_face_northeast_13',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3486_action_queue_async_41_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_41_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_41_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3486_action_queue_async_41_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3486_action_queue_async_41_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3486_set_bit_42',
        "command": 'set_bit',
        "args": [0x704e, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_jmp_to_event_43',
        "command": 'jmp_to_event',
        "args": [3479],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3486_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
