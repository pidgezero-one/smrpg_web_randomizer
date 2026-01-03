
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x705f, 2, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3640_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x705f, 2]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 18]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_2_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_3_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_5',
        "command": 'run_dialog',
        "args": [2439, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3640_pause_205']
    },
    {
        "identifier": 'EVENT_3640_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3640_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_10',
        "command": 'run_dialog',
        "args": [2438, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_set_bit_11',
        "command": 'set_bit',
        "args": [0x705f, 3]
    },
    {
        "identifier": 'EVENT_3640_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_southeast_12',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_14',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_15',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_south_pixels_16',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_17',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_northeast_18',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_19',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_south_pixels_20',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_21',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_23',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_east_pixels_24',
                "command": 'shift_east_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_25',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_northwest_26',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_27',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_east_pixels_28',
                "command": 'shift_east_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_29',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_31',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_set_animation_speed_32',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_west_pixels_33',
                "command": 'shift_west_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_34',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_northeast_35',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_36',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_west_pixels_37',
                "command": 'shift_west_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_38',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_on_40',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_north_pixels_41',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_42',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_face_southeast_43',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_44',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_shift_north_pixels_45',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_sequence_looping_off_46',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_pause_47',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_13_SUBSCRIPT_visibility_off_48',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [6, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_16_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_17',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_18_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_18_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_18_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_19',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [5]
    },
    {
        "identifier": 'EVENT_3640_pause_22',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_23_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_23_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_23_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_24',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_25_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_25_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_25_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_26',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_27_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_27_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_28',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3640_palette_set_morphs_30',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 111, 8]
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [9]
    },
    {
        "identifier": 'EVENT_3640_pause_32',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_33_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_33_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_34',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_35_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_35_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_36',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_37_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_37_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_37_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_38',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_end_loop_39',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_40_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_41',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_42',
        "command": 'run_dialog',
        "args": [2428, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_pause_43',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_44_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_45_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_45_SUBSCRIPT_dec_z_coord_1_step_3',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_46',
        "command": 'run_dialog',
        "args": [2429, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_48_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_48_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_48_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_48_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_48_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_49',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_50',
        "command": 'run_dialog',
        "args": [2430, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3640_action_queue_async_52_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_52_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3640_action_queue_async_52_SUBSCRIPT_pause_4']
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_53',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_54',
        "command": 'run_dialog',
        "args": [2431, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_pause_55',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_56_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_walk_1_step_southeast_9',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_57_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_58_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_58_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_59_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_60_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_60_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_60_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_60_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_60_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_61',
        "command": 'pause',
        "args": [126]
    },
    {
        "identifier": 'EVENT_3640_fade_out_to_black_sync_duration_62',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_63',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_64',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._341_NIMBUS_LAND_GARROS_HOUSE]
    },
    {
        "identifier": 'EVENT_3640_set_bit_65',
        "command": 'set_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3640_enter_area_66',
        "command": 'enter_area',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, RadialDirections.SOUTHEAST, 13, 36, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3640_apply_solidity_mod_67',
        "command": 'apply_solidity_mod',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3640_palette_set_68',
        "command": 'palette_set',
        "args": [111, 1, [3]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_69_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_69_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_69_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_walk_1_step_east_5',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_70_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 37, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_sequence_playback_off_3',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_shift_east_steps_6',
                "command": 'shift_east_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_walk_1_step_northeast_8',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 38, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_walk_1_step_east_6',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_72_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_fade_in_from_black_sync_duration_73',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_74',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_75',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_run_dialog_76',
        "command": 'run_dialog',
        "args": [2445, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_77',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_78',
        "command": 'run_dialog',
        "args": [2446, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_79_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_80_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_80_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_81_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_82_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_83_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_84',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_run_dialog_85',
        "command": 'run_dialog',
        "args": [2064, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_86_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_87',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_87_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_87_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_88',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_89',
        "command": 'run_dialog',
        "args": [2447, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_90',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_91_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_walk_1_step_west_5',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_92_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_93',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_run_dialog_94',
        "command": 'run_dialog',
        "args": [2448, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_95_SUBSCRIPT_face_northeast_9',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_96',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_97',
        "command": 'run_dialog',
        "args": [2449, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_98_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_98_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_walk_1_step_east_3',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_99_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_100_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_100_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_100_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_101_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_101_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_101_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_102',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3640_fade_out_to_black_sync_duration_103',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_104',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3640_fade_out_music_to_volume_105',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_3640_pause_106',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_3640_enter_area_107',
        "command": 'enter_area',
        "args": [Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, RadialDirections.NORTHEAST, 3, 31, 2, []]
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_108',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA]
    },
    {
        "identifier": 'EVENT_3640_palette_set_109',
        "command": 'palette_set',
        "args": [111, 1, [3]]
    },
    {
        "identifier": 'EVENT_3640_freeze_camera_110',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_111',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_111_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_111_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_112',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_fixed_f_coord_on_5',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_walk_1_step_south_7',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_walk_1_step_southwest_10',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_112_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_113',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_113_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_114',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_face_east_4',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_114_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_fade_in_from_black_sync_duration_115',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_116',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_117',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3640_run_dialog_118',
        "command": 'run_dialog',
        "args": [2450, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_119',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_sequence_playback_on_5',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_120_SUBSCRIPT_walk_1_step_northeast_9',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_121_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_122',
        "command": 'run_dialog',
        "args": [2465, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_123',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_124_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_124_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_apply_tile_mod_125',
        "command": 'apply_tile_mod',
        "args": [Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3640_play_sound_126',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_127',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_127_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_127_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [11, 16, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_128',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_129_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_129_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_129_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_130_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_130_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_130_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_131',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_132',
        "command": 'run_dialog',
        "args": [2451, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_133',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_run_dialog_134',
        "command": 'run_dialog',
        "args": [2452, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_135_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_135_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_135_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_135_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_135_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_136_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_137',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_138',
        "command": 'run_dialog',
        "args": [2453, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_139',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_140_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_140_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_140_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_141',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_141_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_141_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_142',
        "command": 'run_dialog',
        "args": [2454, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_143',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_143_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_144',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_fixed_f_coord_off_9',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_sequence_playback_on_10',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_face_southeast_11',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_face_southeast_15',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_144_SUBSCRIPT_face_northeast_17',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_145',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_146',
        "command": 'run_dialog',
        "args": [2456, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_147',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_148_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_148_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_148_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_149',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_149_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_149_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_150',
        "command": 'run_dialog',
        "args": [2457, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_151',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_151_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_151_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_151_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_151_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_151_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_152',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_152_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_152_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_152_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_152_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_153',
        "command": 'run_dialog',
        "args": [2458, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_154',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_154_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_155',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_155_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_155_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_155_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_155_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_156',
        "command": 'run_dialog',
        "args": [2459, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_157',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_158',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_158_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_159',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_160',
        "command": 'run_dialog',
        "args": [2460, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_161',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_161_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_162',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_163',
        "command": 'run_dialog',
        "args": [2461, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_164',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_165',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_165_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_165_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_165_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_166',
        "command": 'run_dialog',
        "args": [2452, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_167',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_168',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_walk_1_step_northwest_4',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_shift_southwest_pixels_11',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_fixed_f_coord_off_14',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_face_southeast_15',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_floating_on_17',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_set_solidity_bits_18',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_168_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remove_from_current_level_169',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_170',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_171',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_171_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_171_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_171_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_172',
        "command": 'run_dialog',
        "args": [2466, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_173',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_174',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_174_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_175',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_176',
        "command": 'run_dialog',
        "args": [2462, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_177',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_178',
        "command": 'run_dialog',
        "args": [2463, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_179',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_180',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [11, 16, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_180_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_181',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_181_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_181_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_181_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_181_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_182',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_182_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_182_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_183',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_184',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_185',
        "command": 'run_dialog',
        "args": [2464, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3640_pause_186',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_187',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_shift_z_down_pixels_6',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_sequence_playback_on_7',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_187_SUBSCRIPT_shift_northeast_steps_10',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_188',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_188_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_189',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_190',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [84]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_190_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_191',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [26, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_24',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_26',
                "command": 'set_sprite_sequence',
                "args": [26, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_191_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_192',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [17]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._145_BLACKSMITH_HAMMER_STRIKE, 4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_11',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._145_BLACKSMITH_HAMMER_STRIKE, 4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_14',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_15',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_end_loop_16',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_17',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_19',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_play_sound_20',
                "command": 'play_sound',
                "args": [Sounds._145_BLACKSMITH_HAMMER_STRIKE, 4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_start_loop_n_times_21',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_22',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_southeast_pixels_23',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_end_loop_24',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_192_SUBSCRIPT_shift_northwest_pixels_25',
                "command": 'shift_northwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_remember_last_object_193',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_194',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [84]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_walk_1_step_southwest_11',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_194_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_195',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_195_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_195_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_196',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_196_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_196_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_197',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_197_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_197_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_197_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_198',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3640_fade_out_to_black_sync_duration_199',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_200',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_201',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_202',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3640_enter_area_203',
        "command": 'enter_area',
        "args": [Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, RadialDirections.NORTHEAST, 5, 69, 1, []]
    },
    {
        "identifier": 'EVENT_3640_jmp_to_event_204',
        "command": 'jmp_to_event',
        "args": [2112]
    },
    {
        "identifier": 'EVENT_3640_pause_205',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_set_action_script_async_206',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3640_pause_207',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3640_run_dialog_208',
        "command": 'run_dialog',
        "args": [2440, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3640_set_action_script_sync_209',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3640_ret_210',
        "command": 'ret'
    }
]
