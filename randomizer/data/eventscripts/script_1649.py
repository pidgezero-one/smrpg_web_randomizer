from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1649_set_0',
        "command": 'set',
        "args": [0x70df, 24]
    },
    {
        "identifier": 'EVENT_1649_fade_out_music_to_volume_1',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_2_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 1, 'EVENT_1649_jmp_if_bit_set_5']
    },
    {
        "identifier": 'EVENT_1649_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1649_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 6, 'EVENT_1649_clear_bit_11']
    },
    {
        "identifier": 'EVENT_1649_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 2, 'EVENT_1649_run_event_at_return_9']
    },
    {
        "identifier": 'EVENT_1649_fade_in_from_black_async_7',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1649_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1649_run_event_at_return_9',
        "command": 'run_event_at_return',
        "args": [257]
    },
    {
        "identifier": 'EVENT_1649_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1649_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x707a, 6]
    },
    {
        "identifier": 'EVENT_1649_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 5, 'EVENT_1649_fade_out_music_to_volume_34']
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_16',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_18',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_19',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1649_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1649_freeze_camera_22',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_23_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_23_SUBSCRIPT_transfer_xyzf_steps_1',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 20, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x97, 0x00]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_24_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_fade_in_from_black_sync_25',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1649_play_sound_balance_26',
        "command": 'play_sound_balance',
        "args": [Sounds._019_LONG_FALL, 255]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_27_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_27_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_27_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [19]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x25, 0x01, 0x00, 0xe0, 0xff]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_walk_1_step_southwest_9',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_walk_1_step_southwest_10',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_28_SUBSCRIPT_shadow_off_11',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_fade_out_music_to_volume_29',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'EVENT_1649_fade_out_to_black_sync_duration_30',
        "command": 'fade_out_to_black_sync_duration',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_31_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_31_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_31_SUBSCRIPT_bpl_26_27_28_2',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_run_event_at_return_32',
        "command": 'run_event_at_return',
        "args": [1650]
    },
    {
        "identifier": 'EVENT_1649_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1649_fade_out_music_to_volume_34',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_1649_freeze_camera_35',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_36_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_36_SUBSCRIPT_transfer_xyzf_steps_1',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 18, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x97, 0x00]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_37_SUBSCRIPT_set_object_memory_bits_6',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_fade_in_from_black_sync_38',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_39_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_39_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_39_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_40_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_41_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_42_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_43_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._021_RUMBLING, 4]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_walk_1_step_southwest_6',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_walk_1_step_southwest_8',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_44_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [104]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_jmp_if_mario_in_air_6',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1649_action_queue_sync_45_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1649_action_queue_sync_45_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_set_short_46',
        "command": 'set_short',
        "args": [0x7034, 0x0006]
    },
    {
        "identifier": 'EVENT_1649_set_short_47',
        "command": 'set_short',
        "args": [0x7010, 0x3400]
    },
    {
        "identifier": 'EVENT_1649_set_short_48',
        "command": 'set_short',
        "args": [0x7012, 0x1600]
    },
    {
        "identifier": 'EVENT_1649_set_short_49',
        "command": 'set_short',
        "args": [0x7014, 0x0400]
    },
    {
        "identifier": 'EVENT_1649_start_loop_n_times_50',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'EVENT_1649_pause_51',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1649_create_packet_at_7010_coords_jmp_if_null_52',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1649_pause_51']
    },
    {
        "identifier": 'EVENT_1649_pause_53',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1649_add_short_54',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_1649_add_short_55',
        "command": 'add_short',
        "args": [0x7014, 0x0080]
    },
    {
        "identifier": 'EVENT_1649_end_loop_56',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1649_unfreeze_camera_57',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1649_stop_music_58',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1649_pause_59',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1649_play_music_default_volume_60',
        "command": 'play_music_default_volume',
        "args": [Music._33_MOLEVILLE]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_61_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_62_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1649_run_dialog_64',
        "command": 'run_dialog',
        "args": [1100, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1649_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1649_run_dialog_duration_66',
        "command": 'run_dialog_duration',
        "args": [1101, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1649_set_short_mem_67',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1649_mem_compare_address_68',
        "command": 'mem_compare_address',
        "args": [0x702e]
    },
    {
        "identifier": 'EVENT_1649_jmp_if_comparison_result_is_lesser_69',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1649_run_dialog_duration_72']
    },
    {
        "identifier": 'EVENT_1649_run_dialog_duration_70',
        "command": 'run_dialog_duration',
        "args": [1102, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1649_jmp_71',
        "command": 'jmp',
        "args": ['EVENT_1649_clear_bit_90']
    },
    {
        "identifier": 'EVENT_1649_run_dialog_duration_72',
        "command": 'run_dialog_duration',
        "args": [1103, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1649_jmp_if_bit_clear_73',
        "command": 'jmp_if_bit_clear',
        "args": [0x707b, 0, 'EVENT_1649_clear_bit_90']
    },
    {
        "identifier": 'EVENT_1649_set_action_script_sync_74',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 650]
    },
    {
        "identifier": 'EVENT_1649_run_dialog_75',
        "command": 'run_dialog',
        "args": [1116, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1649_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_sync_76_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_start_loop_n_times_78',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1649_add_coins_79',
        "command": 'add_coins',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1649_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_1649_pause_81',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1649_set_7010_to_object_xyz_82',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_1649_add_short_83',
        "command": 'add_short',
        "args": [0x7010, 0x00a0]
    },
    {
        "identifier": 'EVENT_1649_add_short_84',
        "command": 'add_short',
        "args": [0x7014, 0x0160]
    },
    {
        "identifier": 'EVENT_1649_create_packet_at_7010_coords_jmp_if_null_85',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._016_BIG_COIN, 'EVENT_1649_pause_81']
    },
    {
        "identifier": 'EVENT_1649_pause_86',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1649_end_loop_87',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_88_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [10, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1649_action_queue_async_89_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1649_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x707b, 0]
    },
    {
        "identifier": 'EVENT_1649_ret_91',
        "command": 'ret'
    }
]
