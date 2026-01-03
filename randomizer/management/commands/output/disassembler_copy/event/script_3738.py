
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3738_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, RadialDirections.NORTHEAST, 2, 62, 0, []]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 262]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 263]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 262]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 263]
    },
    {
        "identifier": 'EVENT_3738_set_bit_5',
        "command": 'set_bit',
        "args": [0x705e, 5]
    },
    {
        "identifier": 'EVENT_3738_fade_in_from_black_sync_duration_6',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_7_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_7_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_7_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_8_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_9',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_freeze_camera_10',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_12_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_13_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_15',
        "command": 'run_dialog',
        "args": [3683, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_17_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_19',
        "command": 'run_dialog',
        "args": [3684, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_20_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_walk_1_step_south_7',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_21_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_walk_1_step_southwest_6',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_22_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 55, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_23_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_24',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_25_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_26_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_27',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_28_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_29',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_30',
        "command": 'run_dialog',
        "args": [3685, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_31',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_32_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_34',
        "command": 'run_dialog',
        "args": [3679, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_35_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_36',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_37_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_39',
        "command": 'run_dialog',
        "args": [3686, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_40',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_41_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_41_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_41_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_42',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_43',
        "command": 'run_dialog',
        "args": [3687, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_44',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_45_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_47_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_49',
        "command": 'run_dialog',
        "args": [3688, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_51_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_51_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
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
        "args": [3689, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_55_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_55_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_55_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_55_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_55_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_56_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_57',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_58',
        "command": 'run_dialog',
        "args": [3711, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_59',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_60_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_60_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_61',
        "command": 'run_dialog',
        "args": [3712, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_62',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_63_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_64',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_65',
        "command": 'run_dialog',
        "args": [3713, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_66',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_68',
        "command": 'run_dialog',
        "args": [3714, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_69',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3738_pause_71',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_72',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_pause_73',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_74',
        "command": 'run_dialog',
        "args": [3715, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_75',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_76_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_76_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_76_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_76_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_76_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_77',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_78',
        "command": 'run_dialog',
        "args": [3716, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_79',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_79_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_80',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_81',
        "command": 'run_dialog',
        "args": [3717, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_82',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_83_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_84_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_85_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_86',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_pause_87',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_start_loop_n_times_88',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_pause_89',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_run_event_as_subroutine_90',
        "command": 'run_event_as_subroutine',
        "args": [275]
    },
    {
        "identifier": 'EVENT_3738_jmp_if_7000_equals_short_91',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_3738_action_queue_async_93']
    },
    {
        "identifier": 'EVENT_3738_end_loop_92',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [7, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_93_SUBSCRIPT_floating_on_10',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_94',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3738_jmp_if_mario_in_air_95',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3738_pause_94']
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_96',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_face_east_5',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_97',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_98_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_98_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_98_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_99_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_100_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_100_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_101_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_101_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_102',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_103_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_103_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_103_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_103_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_103_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_104_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_105_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_105_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_105_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_106_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_107_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_108',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_109',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_pause_110',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_111',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_111_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_112',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_113',
        "command": 'run_dialog',
        "args": [3690, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_114',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_115',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_115_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_116',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_117',
        "command": 'run_dialog',
        "args": [3691, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_118',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_119',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_119_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_119_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._026_LAUGHING_BOWSER, 4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_119_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_119_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_119_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_120',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_async_121',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_122',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_123',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_124',
        "command": 'run_dialog',
        "args": [3692, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_125',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_126_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_126_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_127',
        "command": 'run_dialog',
        "args": [3693, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_128',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_128_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_128_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_128_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_129',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_130',
        "command": 'run_dialog',
        "args": [3694, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_131',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_131_SUBSCRIPT_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_132',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_133',
        "command": 'run_dialog',
        "args": [3695, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_134',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_136',
        "command": 'run_dialog',
        "args": [3696, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_137',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_138_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_138_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_138_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_139',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_140',
        "command": 'run_dialog',
        "args": [3697, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_141',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_142',
        "command": 'run_dialog',
        "args": [3698, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_143',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_144',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_144_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_144_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_145',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_145_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
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
        "args": [3699, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_148',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_149_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_149_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_150',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_150_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_150_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_151_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_151_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_152',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_152_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_152_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_153_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_153_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_154',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_155',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_156_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_157',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_157_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_158',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_158_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_159',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_159_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_160',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_160_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_161',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_pause_162',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_163',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_163_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_164',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_165',
        "command": 'run_dialog',
        "args": [3700, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_166',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_167',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_167_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_167_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_167_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_168',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_169',
        "command": 'run_dialog',
        "args": [3701, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_170',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_170_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_171',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_172',
        "command": 'run_dialog',
        "args": [3702, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_173_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_173_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_173_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_173_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_run_dialog_174',
        "command": 'run_dialog',
        "args": [3703, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_175',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_176',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_176_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_176_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_176_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_177',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_177_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
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
        "args": [3704, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_pause_180',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_181',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_181_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
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
        "args": [3720, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_184',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_184_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_185',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_185_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_185_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_185_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_186',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_186_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_186_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_186_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_187',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_187_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_188',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_188_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_188_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_189',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_189_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_190',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_remember_last_object_191',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_192',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3738_action_queue_async_192_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [21, 118, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_pause_193',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3738_action_queue_async_194',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_async_194_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_set_action_script_sync_195',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3738_action_queue_sync_196',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3738_action_queue_sync_196_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_196_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3738_action_queue_sync_196_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3738_unfreeze_camera_197',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3738_remove_from_level_198',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA]
    },
    {
        "identifier": 'EVENT_3738_ret_199',
        "command": 'ret'
    }
]
