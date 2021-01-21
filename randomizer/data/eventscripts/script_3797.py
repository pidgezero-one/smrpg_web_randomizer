from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3797_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1]
    },
    {
        "identifier": 'EVENT_3797_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_3',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_4',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_5',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3797_start_battle_17',
        "command": 'start_battle',
        "args": [0x00b9, 44]
    },
    {
        "identifier": 'EVENT_3797_set_bit_18',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_3797_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [1011]
    },
    {
        "identifier": 'EVENT_3797_freeze_camera_20',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3797_set_bit_7_offset_21',
        "command": 'set_bit_7_offset',
        "args": [0x0258]
    },
    {
        "identifier": 'EVENT_3797_play_music_current_volume_22',
        "command": 'play_music_current_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_3797_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_stop_music_24',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_25_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_3],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_26_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_26_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_27_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 50, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_28_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 53, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_28_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_29_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [1, 54, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_29_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_29_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_30_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [2, 59, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_30_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_30_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_30_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_31_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 58, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_31_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_31_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_23],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_32_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [1, 57, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_32_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_32_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_33',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 120]
    },
    {
        "identifier": 'EVENT_3797_fade_in_from_colour_duration_35',
        "command": 'fade_in_from_colour_duration',
        "args": [90, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_36',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_pause_37',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_38',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_add_z_coord_1_step_7',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_39_SUBSCRIPT_shift_z_up_steps_9',
                "command": 'shift_z_up_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [6, 50, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_shift_z_up_steps_6',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_40_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_41_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_41_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_42',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_44',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_46_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_46_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_46_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_46_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_23],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_50',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [13, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [14, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_53',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_async_55',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3797_pause_56',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_58_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_23],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_59_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_60_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_61',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_pause_62',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_63_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_63_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_63_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_63_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_65',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_3797_play_music_default_volume_66',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_67',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_pause_68',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_69',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_70_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_70_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_70_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [6, 50, 10]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_70_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_71',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_72_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 54, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_72_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_73',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 248]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_74_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_74_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [0, 1, 2]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_75_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_75_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0xf0, 0xff, 0xc0, 0xff]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_75_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_75_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_turn_clockwise_45_degrees_n_times_4',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_76_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x24, 0x80, 0x00, 0xe0, 0xff]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [140]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_77_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x24, 0x30, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_78_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_db_79',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x16, 0x0a, 0x0b]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_80',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_unsync_action_script_81',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_82_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_83',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_84',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_85',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_86',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_add_z_coord_1_step_6',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_86_SUBSCRIPT_shift_z_up_steps_8',
                "command": 'shift_z_up_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [4, 46, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_add_z_coord_1_step_7',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_87_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_88',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_90',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_91',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_92',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [62]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_92_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_93',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_play_music_default_volume_94',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_3797_pause_95',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_96',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_96_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_96_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_96_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_96_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_97_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_97_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_98',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_99_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_99_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_99_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_99_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_99_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_100_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_100_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_100_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_100_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_100_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_101',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_3797_db_102',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0a, 0x0a]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_103',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_104',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_105',
        "command": 'pause',
        "args": [98]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_106',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_107_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_107_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_107_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_108_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 38, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_108_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [250, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_108_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_108_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_108_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_109',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_run_star_piece_sequence_110',
        "command": 'run_star_piece_sequence',
        "args": [7]
    },
    {
        "identifier": 'EVENT_3797_db_111',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x72, 0x00, 0x00]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_112',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_112_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_112_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 16, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_bit_113',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_3797_run_event_as_subroutine_114',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_3797_freeze_camera_115',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_116',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_116_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 51, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_117',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_117_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_117_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_117_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x80, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [88]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_118_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_clear_bit_7_offset_119',
        "command": 'clear_bit_7_offset',
        "args": [0x0258]
    },
    {
        "identifier": 'EVENT_3797_fade_in_from_black_sync_duration_120',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_121',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_122',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_123',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_123_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_123_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_123_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_123_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_123_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_124',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_125_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_126',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3797_pause_127',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_128_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_128_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_128_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_129_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_129_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_129_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_23],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_130_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_130_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_131',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_pause_132',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_133',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_133_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_133_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_play_music_default_volume_134',
        "command": 'play_music_default_volume',
        "args": [Music._70_ENDING_PART_1]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_135',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_135_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_136',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_20],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_137_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_23],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_138_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_19],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_139_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [92]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_140_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_141_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_141_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_141_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 49, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_141_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [246, 8, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_141_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_142',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_142_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_142_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_142_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 53, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_142_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_142_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_143',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_143_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_143_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_143_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 56, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_143_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [12, 246, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_143_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_144',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_144_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_144_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_144_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 56, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_144_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_144_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_145',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_145_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_145_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_145_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 54, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_145_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_145_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_146',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_146_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_146_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_146_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 52, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_146_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [250, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_146_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_147',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_147_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_147_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_147_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 50, 20, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_147_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [238, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_147_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_148',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_db_149',
        "command": 'db',
        "args": [0x5e]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_150',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_151',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_152',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_153',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_154',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_155',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 120]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_156',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_14, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_157',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_158',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 251]
    },
    {
        "identifier": 'EVENT_3797_pause_159',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_160',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 252]
    },
    {
        "identifier": 'EVENT_3797_pause_161',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_162',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 253]
    },
    {
        "identifier": 'EVENT_3797_pause_163',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_164',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 254]
    },
    {
        "identifier": 'EVENT_3797_pause_165',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_166',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 255]
    },
    {
        "identifier": 'EVENT_3797_pause_167',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_168',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 224]
    },
    {
        "identifier": 'EVENT_3797_pause_169',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_170',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 225]
    },
    {
        "identifier": 'EVENT_3797_pause_171',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_172',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_173',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_174',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_175',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_176',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_177',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_178',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_179',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_180',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_181',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_14, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_182',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_183',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_184',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 226]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_185',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 226]
    },
    {
        "identifier": 'EVENT_3797_pause_short_186',
        "command": 'pause_short',
        "args": [420]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_187',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_21, 227]
    },
    {
        "identifier": 'EVENT_3797_pause_188',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_189',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3797_action_queue_sync_191']
    },
    {
        "identifier": 'EVENT_3797_jmp_190',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_188']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_191',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 42, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_191_SUBSCRIPT_set_object_memory_bits_8',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_192',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_193',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3797_action_queue_sync_195']
    },
    {
        "identifier": 'EVENT_3797_jmp_194',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_192']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_195',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 41, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_195_SUBSCRIPT_set_object_memory_bits_7',
                "command": 'set_object_memory_bits',
                "args": [0x0e, []]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_196',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_197',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3797_action_queue_sync_199']
    },
    {
        "identifier": 'EVENT_3797_jmp_198',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_196']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 43, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [250, 12, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x24, 0x00, 0xfa, 0x00, 0xfa]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_199_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_200',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_201',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3797_action_queue_sync_203']
    },
    {
        "identifier": 'EVENT_3797_jmp_202',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_200']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_203',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_18],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 46, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 244, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x24, 0x20, 0xfc, 0xe0, 0xfb]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_203_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_204',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_205',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3797_action_queue_sync_207']
    },
    {
        "identifier": 'EVENT_3797_jmp_206',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_204']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_207',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [2, 45, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 6, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x24, 0xe0, 0x05, 0xe0, 0xf8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_207_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_208',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_209',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3797_action_queue_sync_211']
    },
    {
        "identifier": 'EVENT_3797_jmp_210',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_208']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_211',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 49, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x00, 0xfe, 0x00, 0xf8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_211_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_212',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_jmp_if_bit_set_213',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3797_action_queue_sync_215']
    },
    {
        "identifier": 'EVENT_3797_jmp_214',
        "command": 'jmp',
        "args": ['EVENT_3797_pause_212']
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_215',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 45, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [232, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x24, 0x00, 0xfe, 0x00, 0xf8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_215_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_216',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_217',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_3],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_217_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_217_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_218',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3797_fade_out_to_colour_duration_219',
        "command": 'fade_out_to_colour_duration',
        "args": [120, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_220',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_pause_221',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_enter_area_222',
        "command": 'enter_area',
        "args": [Rooms._088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, RadialDirections.SOUTHWEST, 4, 51, 0, []]
    },
    {
        "identifier": 'EVENT_3797_freeze_camera_223',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_224',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_224_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 50, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_224_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_224_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_225',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 57, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [240, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_225_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_226',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_226_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 56, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_226_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [240, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_226_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_227',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_227_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 53, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_227_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [242, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_227_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_228',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_228_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 50, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_228_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [240, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_fade_in_from_colour_duration_229',
        "command": 'fade_in_from_colour_duration',
        "args": [40, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_230',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_231',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_231_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_231_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_231_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_231_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_231_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [12, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_232',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_233',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_233_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_234',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_234_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_235',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_235_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_236',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_pause_237',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_238',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 56, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 220, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_start_loop_n_times_8',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_shift_z_up_pixels_10',
                "command": 'shift_z_up_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_shift_z_down_pixels_11',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_visibility_off_16',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_priority_17',
                "command": 'set_priority',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_transfer_xyzf_pixels_18',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 216, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_visibility_on_20',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_priority_21',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_238_SUBSCRIPT_set_vram_priority_22',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_239',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_239_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_239_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_239_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [150]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_239_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_240',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_240_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_240_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_240_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_240_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_241',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_241_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_242',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_242_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_243',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_244',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120]
    },
    {
        "identifier": 'EVENT_3797_pause_245',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_246',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_247',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_bpl_26_27_28_1',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x25, 0x00, 0x07, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x24, 0x98, 0xff, 0xc8, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_247_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_248',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_249',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_249_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_250',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_250_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_251',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_251_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_252',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_252_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_253',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_254',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_255',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_255_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_255_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_255_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x80, 0x06, 0xa0, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_255_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x90, 0xff, 0x00, 0x01]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_255_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_256',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_257',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_257_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_258',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_258_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_259',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_259_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_260',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_261',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_262',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_262_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_262_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_262_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x88, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_262_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x78, 0x01, 0x00, 0x00]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_262_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [28]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_263',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_264',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_264_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_265',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_265_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_265_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_265_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_265_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0xc3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_265_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_266',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_267',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3797_start_embedded_action_script_async_268',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_268_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_268_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_268_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0x80, 0x06, 0x90, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_268_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x20, 0x00, 0x30, 0xff]
            },
            {
                "identifier": 'EVENT_3797_start_embedded_action_script_async_268_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_269',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 120]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_270',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_270_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_271',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_272',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_272_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 52, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_272_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [242, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_273',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 228]
    },
    {
        "identifier": 'EVENT_3797_pause_274',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3797_pause_action_script_275',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_276',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_276_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_276_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_277',
        "command": 'pause',
        "args": [230]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_278',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_278_SUBSCRIPT_shift_north_steps_5',
                "command": 'shift_north_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_279',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'EVENT_3797_enter_area_280',
        "command": 'enter_area',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, RadialDirections.NORTHWEST, 4, 48, 0, []]
    },
    {
        "identifier": 'EVENT_3797_run_star_piece_sequence_281',
        "command": 'run_star_piece_sequence',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3797_palette_set_282',
        "command": 'palette_set',
        "args": [163, 1]
    },
    {
        "identifier": 'EVENT_3797_palette_set_283',
        "command": 'palette_set',
        "args": [164, 1]
    },
    {
        "identifier": 'EVENT_3797_palette_set_284',
        "command": 'palette_set',
        "args": [166, 1]
    },
    {
        "identifier": 'EVENT_3797_palette_set_285',
        "command": 'palette_set',
        "args": [167, 1]
    },
    {
        "identifier": 'EVENT_3797_palette_set_286',
        "command": 'palette_set',
        "args": [165, 1]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_287',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_287_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_287_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_287_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_288',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_288_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_288_SUBSCRIPT_walk_1_step_west_1',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_288_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_289',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_289_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 90, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_289_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_289_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_289_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_290',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_290_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_290_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_291',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_291_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_291_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_292',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_292_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_292_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_293',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_293_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_293_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_293_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_action_queue_async_294',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_async_294_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 208, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3797_action_queue_async_294_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_295',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3797_fade_in_from_colour_duration_296',
        "command": 'fade_in_from_colour_duration',
        "args": [60, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_297',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_pause_298',
        "command": 'pause',
        "args": [170]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_299',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_299_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_short_300',
        "command": 'pause_short',
        "args": [328]
    },
    {
        "identifier": 'EVENT_3797_action_queue_sync_301',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3797_action_queue_sync_301_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3797_action_queue_sync_301_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3797_pause_302',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_303',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 229]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_304',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 229]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_305',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 229]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_306',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 229]
    },
    {
        "identifier": 'EVENT_3797_set_action_script_sync_307',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 229]
    },
    {
        "identifier": 'EVENT_3797_remember_last_object_308',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3797_apply_tile_mod_309',
        "command": 'apply_tile_mod',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3797_pause_310',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3797_apply_tile_mod_311',
        "command": 'apply_tile_mod',
        "args": [Rooms._375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3797_pause_312',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3797_db_313',
        "command": 'db',
        "args": [0x5f]
    },
    {
        "identifier": 'EVENT_3797_pause_short_314',
        "command": 'pause_short',
        "args": [404]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_315',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 161, 1]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_316',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 162, 5]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_317',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 84, 8]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_318',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 85, 10]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_319',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 86, 11]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_320',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 141, 9]
    },
    {
        "identifier": 'EVENT_3797_palette_set_morphs_321',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 12, 140, 13]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_322',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_pause_323',
        "command": 'pause',
        "args": [216]
    },
    {
        "identifier": 'EVENT_3797_apply_tile_mod_324',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3797_apply_tile_mod_325',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3797_apply_tile_mod_326',
        "command": 'apply_tile_mod',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3797_fade_out_to_black_sync_duration_327',
        "command": 'fade_out_to_black_sync_duration',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3797_pause_script_until_effect_done_328',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3797_pause_329',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3797_play_music_default_volume_330',
        "command": 'play_music_default_volume',
        "args": [Music._71_ENDING_PART_2]
    },
    {
        "identifier": 'EVENT_3797_pause_331',
        "command": 'pause',
        "args": [130]
    },
    {
        "identifier": 'EVENT_3797_run_event_sequence_332',
        "command": 'run_event_sequence',
        "args": [EventSequences._13_RUN_STAR_PIECE_END_SEQUENCE, 0x00]
    },
    {
        "identifier": 'EVENT_3797_pause_333',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3797_enter_area_334',
        "command": 'enter_area',
        "args": [Rooms._269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, RadialDirections.SOUTHWEST, 17, 40, 2, []]
    },
    {
        "identifier": 'EVENT_3797_jmp_to_event_335',
        "command": 'jmp_to_event',
        "args": [3804]
    }
]
