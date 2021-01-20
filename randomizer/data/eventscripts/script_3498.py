from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3498_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 7, 'EVENT_3498_action_queue_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_3498_action_queue_async_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_5_SUBSCRIPT_floating_off_6',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_sync_6_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_6_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_6_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 4]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_east_pixels_5',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_west_pixels_6',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_east_pixels_7',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_shift_west_pixels_8',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_7_SUBSCRIPT_face_southeast_9',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_set_short_8',
        "command": 'set_short',
        "args": [0x700c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_create_packet_at_object_coords_jmp_if_null_10',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._017_SMALL_COIN_NOT_MOVING, AreaObjects.NPC_1, 'EVENT_3498_pause_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_add_short_12',
        "command": 'add_short',
        "args": [0x700c, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_end_loop_13',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_pause_14',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3498_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3498_action_queue_async_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_18_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_18_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_18_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_18_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_18_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_pause_19',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_20_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_20_SUBSCRIPT_floating_off_2',
                "command": 'floating_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_sync_21_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 4]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_sync_22_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 90, 9]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_set_short_23',
        "command": 'set_short',
        "args": [0x700c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_start_loop_n_times_24',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_create_packet_at_object_coords_jmp_if_null_25',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._017_SMALL_COIN_NOT_MOVING, AreaObjects.NPC_3, 'EVENT_3498_pause_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_pause_26',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_add_short_27',
        "command": 'add_short',
        "args": [0x700c, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_end_loop_28',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_pause_29',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3498_jmp_if_bit_set_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_31_SUBSCRIPT_shift_west_steps_5',
                "command": 'shift_west_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_sync_32_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 90, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3498_action_queue_sync_32_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [88]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_shift_east_steps_6',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._065_THWOMP_STOMP, 4]
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3498_action_queue_async_33_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3498_action_queue_async_34_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3498_set_bit_35',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_3498_action_queue_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_jmp_if_bit_set_37',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 7, 'EVENT_3498_ret_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_set_38',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_add_max_FP_7000_39',
        "command": 'add_max_FP_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_set_bit_40',
        "command": 'set_bit',
        "args": [0x7078, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3498_ret_41',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
