from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3738_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, RadialDirections.SOUTH, 15, 46, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3738_fade_in_from_black_sync_1',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3738_set_bit_2',
        "command": 'set_bit',
        "args": [0x705e, 5]
    },
    {
        "identifier": 'EVENT_3738_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_3738_remove_from_level_211']
    },
    {
        "identifier": 'EVENT_3738_stop_sound_4',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_5',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_fade_in_from_black_sync_duration_20',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_23',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_freeze_camera_24',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_26_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_27_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_28',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_29',
        "command": 'run_dialog',
        "args": [3683, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_31_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_33',
        "command": 'run_dialog',
        "args": [3684, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_34_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_walk_1_step_south_7',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_walk_1_step_southwest_6',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_36_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 55, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_37_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_38',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_39',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_39_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_40_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_41',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_42_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_43',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_44',
        "command": 'run_dialog',
        "args": [3685, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_46_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_46_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_48',
        "command": 'run_dialog',
        "args": [3679, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_49_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_49_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_49_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_49_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_49_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_51_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_52',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_53',
        "command": 'run_dialog',
        "args": [3686, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_55_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_55_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_55_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_57',
        "command": 'run_dialog',
        "args": [3687, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_58',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_59_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_60',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_61_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_62',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_63',
        "command": 'run_dialog',
        "args": [3688, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_64',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_65_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_65_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_66',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_67',
        "command": 'run_dialog',
        "args": [3689, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_68',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_69_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_69_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_69_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_69_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_69_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_70_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_71',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_72',
        "command": 'run_dialog',
        "args": [3711, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_73',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_74_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_74_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_75',
        "command": 'run_dialog',
        "args": [3712, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_76',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_77_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_78',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_79',
        "command": 'run_dialog',
        "args": [3713, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_80',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_82',
        "command": 'run_dialog',
        "args": [3714, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_83',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_84',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3738_pause_85',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_86',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_pause_87',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_88',
        "command": 'run_dialog',
        "args": [3715, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_89',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_90',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_90_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_90_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_90_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_90_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_90_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_91',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_92',
        "command": 'run_dialog',
        "args": [3716, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_94',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_95',
        "command": 'run_dialog',
        "args": [3717, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_96',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_97_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_98_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_100',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_pause_101',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_start_loop_n_times_102',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_pause_103',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_run_event_as_subroutine_104',
        "command": 'run_event_as_subroutine',
        "args": [275]
    },
    {
        "identifier": 'EVENT_3738_jmp_if_var_equals_short_105',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_3738_end_loop_106',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_107',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_floating_off_4',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_107_SUBSCRIPT_floating_on_9',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_108',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_jmp_if_mario_in_air_109',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3502_open_location_119']
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_110',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_face_east_5',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_110_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_111',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_112',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_112_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_112_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_112_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_113',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_113_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_113_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_114',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_114_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_114_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_115_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_116',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_117_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_117_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_117_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_117_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_117_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_119_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_119_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_119_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_120_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_121_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_122',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_123',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_pause_124',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_125_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_126',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_127',
        "command": 'run_dialog',
        "args": [3690, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_128',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_129',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_129_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_130',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_131',
        "command": 'run_dialog',
        "args": [3691, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_132',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_133',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_133_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_133_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_133_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_133_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_133_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_134',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_135',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_136_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_137',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_138',
        "command": 'run_dialog',
        "args": [3692, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_139',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_140_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_140_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_141',
        "command": 'run_dialog',
        "args": [3693, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_142',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_142_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_142_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_142_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_143',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_144',
        "command": 'run_dialog',
        "args": [3694, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_145',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_145_SUBSCRIPT_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_146',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_147',
        "command": 'run_dialog',
        "args": [3695, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_148',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_149_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_150',
        "command": 'run_dialog',
        "args": [3696, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_151',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_152',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_152_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_152_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_152_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_153',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_154',
        "command": 'run_dialog',
        "args": [3697, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_155',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_156',
        "command": 'run_dialog',
        "args": [3698, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_157',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_158',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_158_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_158_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_159',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_159_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_160',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_161',
        "command": 'run_dialog',
        "args": [3699, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_162',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_163_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_163_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_164_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_165',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_165_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_165_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_166',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_166_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_166_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_167',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_167_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_167_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_168',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_169',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_170',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_171',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_171_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_172',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_172_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_173_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_174',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_174_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_175',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_pause_176',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_177',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_177_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_178',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_179',
        "command": 'run_dialog',
        "args": [3700, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_180',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_181',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_182',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_183',
        "command": 'run_dialog',
        "args": [3701, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_185',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_186',
        "command": 'run_dialog',
        "args": [3702, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_187',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_188',
        "command": 'run_dialog',
        "args": [3703, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_189',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_190',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_190_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_190_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_190_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_191',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_191_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_192',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_pause_193',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_stop_sound_194',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_195',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_195_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_195_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_195_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_195_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_196',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_197',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_197_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_197_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_198',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_198_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_198_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_198_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_199_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_199_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_199_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_200',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_200_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_200_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_200_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_201',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_201_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_201_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_202',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_202_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_203',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_204',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_205',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_205_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_205_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_206',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_207',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_207_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_208',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_209',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_209_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_209_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_209_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_unfreeze_camera_210',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3738_remove_from_level_211',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA]
    },
    {
        "identifier": 'EVENT_3738_set_short_212',
        "command": 'set_short',
        "args": [0x700a, 0x00dd]
    },
    {
        "identifier": 'EVENT_3738_jmp_to_event_213',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_3738_ret_214',
        "command": 'ret'
    }
]
