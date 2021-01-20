from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3639_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3639_jmp_if_bit_set_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 3, 'EVENT_3639_run_dialog_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 2, 'EVENT_3639_action_queue_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_4',
        "command": 'run_dialog',
        "args": [2444, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_6_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 18]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_6_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_7_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_pause_8',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_9',
        "command": 'run_dialog',
        "args": [2439, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_if_dialog_option_b_10',
        "command": 'jmp_if_dialog_option_b',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_pause_13',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_14_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_run_dialog_15',
        "command": 'run_dialog',
        "args": [2442, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x705f, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_walk_1_step_east_2',
                "command": 'walk_1_step_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_face_north_5',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_17_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_pause_18',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_19',
        "command": 'run_dialog',
        "args": [2443, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_20',
        "command": 'jmp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_21',
        "command": 'run_dialog',
        "args": [3672, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 2, 'EVENT_3639_run_dialog_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_set_bit_24',
        "command": 'set_bit',
        "args": [0x7084, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_25_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_25_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 22]
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_sync_26_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_sync_27_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_sync_27_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_28_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_run_dialog_29',
        "command": 'run_dialog',
        "args": [3783, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_pause_30',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_31',
        "command": 'run_dialog',
        "args": [3784, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_33',
        "command": 'run_dialog',
        "args": [3785, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_34_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_34_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_pause_35',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_36',
        "command": 'run_dialog',
        "args": [3786, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_pause_37',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_38_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_38_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_38_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_pause_39',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3639_action_queue_async_40_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [28, 85, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3639_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_run_dialog_43',
        "command": 'run_dialog',
        "args": [3787, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3639_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
