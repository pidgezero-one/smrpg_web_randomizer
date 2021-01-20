from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3280_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 1, 'EVENT_3280_jmp_to_event_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_async_2_SUBSCRIPT_transfer_xyzf_steps_0',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 25, RadialDirections.NORTHEAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_4_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_5_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_6_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_6_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_6_SUBSCRIPT_face_mario_3',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_7_SUBSCRIPT_face_mario_0',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_async_8_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_8_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 5, 'EVENT_3280_action_queue_sync_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_10_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_10_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_10_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_11_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [3, 125]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_11_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_12_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [4, 122]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_12_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_12_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [3, 123]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_13_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [2, 123]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_13_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_14_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [3, 122]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_14_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [255]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [255]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_5',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_9',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_13',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [255]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_15_SUBSCRIPT_turn_clockwise_45_degrees_n_times_15',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [255]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 5, 'EVENT_3280_set_action_script_sync_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 5, 'EVENT_3280_start_battle_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_19_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_19_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_20_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_face_north_1',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_face_east_5',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_21_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_22_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_start_battle_23',
        "command": 'start_battle',
        "args": [0x0044, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_set_bit_24',
        "command": 'set_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_run_event_as_subroutine_27',
        "command": 'run_event_as_subroutine',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3280_set_bit_84'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_fade_in_from_black_async_29',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_30_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_31_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_32_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_33_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_33_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_33_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_34_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_34_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_34_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_34_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_35_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_35_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_36_SUBSCRIPT_face_north_0',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_36_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_36_SUBSCRIPT_face_north_2',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_36_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [13]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_37_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_jump_to_height_silent_5',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_walk_1_step_southeast_8',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_38_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_39_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3280_action_queue_async_40_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_remove_from_level_41',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_remove_from_level_43',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_remove_from_level_44',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_set_bit_45',
        "command": 'set_bit',
        "args": [0x7058, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_clear_bit_46',
        "command": 'clear_bit',
        "args": [0x7058, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_48_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_48_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3280_action_queue_sync_49_SUBSCRIPT_stop_sound_0',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_49_SUBSCRIPT_stop_sound_1',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_49_SUBSCRIPT_stop_sound_2',
                "command": 'stop_sound',
                "args": []
            },
            {
                "identifier": 'EVENT_3280_action_queue_sync_49_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3280_fade_in_from_black_sync_50',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_3142_action_queue_sync_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_52',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_53',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_54',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_55',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_56',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_57',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_58',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_59',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_60',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_61',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_62',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_63',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_64',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_65',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_66',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_67',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_68',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_69',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_70',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_71',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_72',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_73',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_74',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_75',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_76',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_77',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_78',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_79',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_80',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_stop_sound_81',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_ret_82',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_jmp_to_event_83',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_set_bit_84',
        "command": 'set_bit',
        "args": [0x7058, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_run_event_at_return_85',
        "command": 'run_event_at_return',
        "args": [3306],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3280_ret_86',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
