from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_744_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 3, 'EVENT_744_run_dialog_54']
    },
    {
        "identifier": 'EVENT_744_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_744_set_37']
    },
    {
        "identifier": 'EVENT_744_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_744_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_744_run_dialog_4',
        "command": 'run_dialog',
        "args": [52, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [28, 52]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_5_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_6_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_6_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [27, 53, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_7_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_8_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_8_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_9_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_11_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_12',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_run_dialog_13',
        "command": 'run_dialog',
        "args": [54, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_15_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_15_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_15_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_run_dialog_16',
        "command": 'run_dialog',
        "args": [55, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_remember_last_object_17',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_744_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_18_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_18_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_18_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_run_dialog_20',
        "command": 'run_dialog',
        "args": [56, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_22_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_run_dialog_23',
        "command": 'run_dialog',
        "args": [57, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_pause_24',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_run_dialog_25',
        "command": 'run_dialog',
        "args": [58, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_pause_26',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_27_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_28_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_29',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_744_run_dialog_30',
        "command": 'run_dialog',
        "args": [59, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_remember_last_object_31',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_744_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_32_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_32_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_32_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_34_SUBSCRIPT_face_southeast_13',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_35',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_744_run_dialog_36',
        "command": 'run_dialog',
        "args": [60, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_set_37',
        "command": 'set',
        "args": [0x70a7, 116]
    },
    {
        "identifier": 'EVENT_744_set_38',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_744_run_event_as_subroutine_39',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_744_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_744_set_bit_50']
    },
    {
        "identifier": 'EVENT_744_pause_41',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_42_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_744_action_queue_async_42_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_pause_43',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_44_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_45_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_744_action_queue_sync_45_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [37, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_744_remember_last_object_46',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_744_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_744_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_744_action_queue_async_48_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_744_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_744_set_bit_50',
        "command": 'set_bit',
        "args": [0x709f, 3]
    },
    {
        "identifier": 'EVENT_744_resume_action_script_51',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_744_resume_action_script_52',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_744_ret_53',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_744_run_dialog_54',
        "command": 'run_dialog',
        "args": [61, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_744_ret_55',
        "command": 'ret'
    }
]
