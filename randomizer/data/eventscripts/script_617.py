from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_617_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_5, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 63, 'EVENT_617_enable_controls_until_return_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_2_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_async_2_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_617_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_random_above_128_5',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_617_set_7000_to_object_coord_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_random_above_66_6',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_617_action_queue_sync_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_7_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_7_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_617_set_8',
        "command": 'set',
        "args": [0x70a9, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_9',
        "command": 'set',
        "args": [0x70b8, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_617_pause_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_shift_northwest_pixels_11',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_off_16',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_19',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_11_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_617_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [6, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_shift_northwest_pixels_10',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_shift_southeast_pixels_11',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_off_14',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_shift_northwest_steps_17',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_shift_north_steps_18',
                "command": 'shift_north_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_617_action_queue_sync_12_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_617_remember_last_object_13',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_14',
        "command": 'set',
        "args": [0x70a9, 28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_15',
        "command": 'set',
        "args": [0x70b8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_617_pause_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_17_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_617_set_18',
        "command": 'set',
        "args": [0x70a9, 26],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_19',
        "command": 'set',
        "args": [0x70b8, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_pause_20',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_random_above_128_21',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_617_action_queue_async_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 28, 'EVENT_617_set_action_script_sync_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MEM_70A9, 324],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_617_set_7000_to_object_coord_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 325],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_async_27',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 326],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_617_set_7000_to_object_coord_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_async_29_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_617_pause_30',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_run_dialog_31',
        "command": 'run_dialog',
        "args": [1005, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_617_action_queue_async_33_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_617_action_queue_async_33_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_617_action_queue_async_33_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_617_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_enable_controls_until_return_37',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_var_equals_short_39',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_617_set_action_script_sync_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_jmp_if_var_equals_short_40',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_617_set_action_script_sync_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 321],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 321],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 321],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 321],
        "subscript": []
    },
    {
        "identifier": 'EVENT_617_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
