
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3778_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x707d, 7, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3778_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 1, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_2_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [2, 39]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_3_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [4, 57]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_3_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 57, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_4_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_6',
        "command": 'run_dialog',
        "args": [3791, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_8_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_10',
        "command": 'run_dialog',
        "args": [3792, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_12_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_12_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_13',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_14',
        "command": 'run_dialog',
        "args": [3793, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_15_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_15_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_15_SUBSCRIPT_fixed_f_coord_off_2',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_15_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_16_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_remember_last_object_17',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3778_run_dialog_18',
        "command": 'run_dialog',
        "args": [3794, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_21',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_22_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_24',
        "command": 'run_dialog',
        "args": [3795, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_26_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_28',
        "command": 'run_dialog',
        "args": [3854, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_29',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_30_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_31_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_33',
        "command": 'run_dialog',
        "args": [3855, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_34',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_35_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_35_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_35_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_35_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_35_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_36_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_37_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_remember_last_object_38',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3778_run_dialog_39',
        "command": 'run_dialog',
        "args": [3856, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_40',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_41',
        "command": 'run_dialog',
        "args": [3857, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_42',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_set_action_script_async_43',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 382]
    },
    {
        "identifier": 'EVENT_3778_pause_44',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_45',
        "command": 'run_dialog',
        "args": [3858, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_47_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_48_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_remember_last_object_49',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3778_run_dialog_50',
        "command": 'run_dialog',
        "args": [3859, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_51_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_52_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_remember_last_object_53',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3778_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_55',
        "command": 'run_dialog',
        "args": [3860, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_57_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_58',
        "command": 'run_dialog',
        "args": [3861, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_59',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_60_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_60_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_61',
        "command": 'run_dialog',
        "args": [3862, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_62',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_63_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_64',
        "command": 'run_dialog',
        "args": [3863, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_65',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_66',
        "command": 'run_dialog',
        "args": [3864, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_67',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_68_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_68_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_68_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_68_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_69',
        "command": 'run_dialog',
        "args": [3865, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_70',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_71_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3778_action_queue_sync_71_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_72_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_73_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_74',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_run_dialog_75',
        "command": 'run_dialog',
        "args": [3866, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3778_pause_76',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_remember_last_object_77',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3778_set_action_script_async_78',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3778_pause_79',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3778_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_sync_80_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_81_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_81_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3778_action_queue_async_81_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [6, 83, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_pause_82',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3778_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3778_action_queue_async_83_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3778_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3778_set_bit_85',
        "command": 'set_bit',
        "args": [0x7099, 1]
    },
    {
        "identifier": 'EVENT_3778_ret_86',
        "command": 'ret'
    }
]
