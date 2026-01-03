
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1618_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1618_mem_compare_val_2',
        "command": 'mem_compare_val',
        "args": [7424]
    },
    {
        "identifier": 'EVENT_1618_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1618_pause_0']
    },
    {
        "identifier": 'EVENT_1618_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1618_mem_compare_val_5',
        "command": 'mem_compare_val',
        "args": [7936]
    },
    {
        "identifier": 'EVENT_1618_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1618_pause_0']
    },
    {
        "identifier": 'EVENT_1618_enable_controls_until_return_7',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1618_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x707a, 3, 'EVENT_1618_set_bit_10']
    },
    {
        "identifier": 'EVENT_1618_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1618_set_bit_10',
        "command": 'set_bit',
        "args": [0x707a, 3]
    },
    {
        "identifier": 'EVENT_1618_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6]
    },
    {
        "identifier": 'EVENT_1618_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_jmp_if_mario_in_air_13',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1618_pause_12']
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_14_SUBSCRIPT_face_southwest_7D_9',
                "command": 'face_southwest_7D',
                "args": [0x1a]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_15_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 16, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_walk_1_step_southeast_8',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_walk_1_step_northeast_10',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_reset_properties_18',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_face_southeast_19',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_set_solidity_bits_21',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_play_sound_22',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_jump_to_height_23',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_17_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_freeze_all_npcs_until_return_18',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_19_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_19_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_19_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 42]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_20_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [26, 44]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_21_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 43]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_22_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [26, 45]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_23_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [28, 44]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_sync_F1_24_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [27, 46]
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_start_embedded_action_script_async_F1_25_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_26_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_26_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_26_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_26_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1a, 0xd8, 0x1d]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_26_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_27_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_28_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_28_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_29_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_29_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_29_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_29_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [100]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_30_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_30_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_30_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_run_dialog_32',
        "command": 'run_dialog',
        "args": [1092, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_33_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_33_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_33_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_33_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_34_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_run_dialog_35',
        "command": 'run_dialog',
        "args": [1093, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_36_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_37_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_37_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_37_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_async_38_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_38_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1618_action_queue_async_38_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_39_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_39_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_run_dialog_40',
        "command": 'run_dialog',
        "args": [1094, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_41_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_42_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_43_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_44_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_45_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_46_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1618_action_queue_sync_47_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1618_pause_48',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_49',
        "command": 'start_loop_n_times',
        "args": [17]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_50',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 130]
    },
    {
        "identifier": 'EVENT_1618_pause_51',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_52',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_53',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 96]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_54',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_55',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 110]
    },
    {
        "identifier": 'EVENT_1618_pause_56',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_57',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_58',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 80]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_59',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_60',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 90]
    },
    {
        "identifier": 'EVENT_1618_pause_61',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_62',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_63',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 64]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_64',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_65',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 70]
    },
    {
        "identifier": 'EVENT_1618_pause_66',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_67',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_68',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 48]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_69',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_70',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 50]
    },
    {
        "identifier": 'EVENT_1618_pause_71',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_72',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_73',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 32]
    },
    {
        "identifier": 'EVENT_1618_start_loop_n_times_74',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1618_play_sound_balance_75',
        "command": 'play_sound_balance',
        "args": [Sounds._046_CRUMBLING_NOISE, 30]
    },
    {
        "identifier": 'EVENT_1618_pause_76',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1618_end_loop_77',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1618_stop_sound_78',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1618_fade_out_sound_to_volume_79',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 127]
    },
    {
        "identifier": 'EVENT_1618_set_80',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1618_run_event_as_subroutine_81',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1618_enable_controls_until_return_82',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1618_ret_83',
        "command": 'ret'
    }
]
