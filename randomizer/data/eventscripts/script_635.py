from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_635_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 2, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_635_set_bit_1',
        "command": 'set_bit',
        "args": [0x7063, 2]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_2_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_635_action_queue_async_2_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_635_action_queue_async_15']
    },
    {
        "identifier": 'EVENT_635_run_dialog_4',
        "command": 'run_dialog',
        "args": [2064, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_635_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_635_action_queue_sync_5_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [7, 34, 4]
            },
            {
                "identifier": 'EVENT_635_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_sync_6_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [2, 16, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_635_remember_last_object_7',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_635_run_dialog_8',
        "command": 'run_dialog',
        "args": [2065, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_635_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [286]
    },
    {
        "identifier": 'EVENT_635_close_dialog_10',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_635_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_11_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_11_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_11_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_635_action_queue_async_11_SUBSCRIPT_pause_1']
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_12_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_635_action_queue_async_12_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_run_dialog_13',
        "command": 'run_dialog',
        "args": [2066, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_635_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_sync_14_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_635_action_queue_sync_14_SUBSCRIPT_face_west_1',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_15_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_15_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [4, 32]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_15_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_set_bit_16',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_635_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 333]
    },
    {
        "identifier": 'EVENT_635_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_sync_18_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_635_action_queue_sync_18_SUBSCRIPT_face_west_1',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_unsync_action_script_19',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_635_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_635_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_635_action_queue_async_38']
    },
    {
        "identifier": 'EVENT_635_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_22_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_run_dialog_23',
        "command": 'run_dialog',
        "args": [2067, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_635_pause_24',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_25_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_26_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_27_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_635_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_3',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_635_action_queue_async_37']
    },
    {
        "identifier": 'EVENT_635_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_635_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_37_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_635_action_queue_async_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_635_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_635_action_queue_async_38_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_635_pause_39',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_635_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 333]
    },
    {
        "identifier": 'EVENT_635_apply_solidity_mod_41',
        "command": 'apply_solidity_mod',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_635_remove_from_level_42',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_12, Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_635_remove_from_level_43',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_635_ret_44',
        "command": 'ret'
    }
]
