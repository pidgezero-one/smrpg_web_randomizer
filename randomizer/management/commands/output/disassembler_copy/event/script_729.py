
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_729_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_729_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_729_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_729_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_3_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [7, 86]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_3_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_3_SUBSCRIPT_face_west_2',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_729_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'EVENT_729_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_729_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_729_pause_4']
    },
    {
        "identifier": 'EVENT_729_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_7_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_7_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_8_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_run_dialog_10',
        "command": 'run_dialog',
        "args": [2314, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_13',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_14_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_14_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_run_dialog_16',
        "command": 'run_dialog',
        "args": [2315, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_17_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_729_action_queue_async_19_SUBSCRIPT_pause_4']
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_19_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_run_dialog_20',
        "command": 'run_dialog',
        "args": [2316, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_run_dialog_22',
        "command": 'run_dialog',
        "args": [2317, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_run_dialog_24',
        "command": 'run_dialog',
        "args": [2188, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_729_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [7, 85, 12, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_26_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_27_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_27_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_remember_last_object_29',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_729_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_run_dialog_31',
        "command": 'run_dialog',
        "args": [2310, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._087_CORRECT_SIGNAL, 4]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_34_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_35',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_36_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_36_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_36_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_36_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_37_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_run_dialog_38',
        "command": 'run_dialog',
        "args": [2311, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_remember_last_object_39',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_40_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_40_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_40_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_42',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_44',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_run_dialog_45',
        "command": 'run_dialog',
        "args": [2312, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_46_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_46_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_46_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_47_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_remember_last_object_49',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_729_set_action_script_async_50',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_729_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_52_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_run_dialog_53',
        "command": 'run_dialog',
        "args": [2313, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_729_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_sync_54_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_729_action_queue_sync_54_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_55_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_55_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_55_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_55_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [1, 42, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_57_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_57_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_58',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_59_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_59_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [1, 42, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_729_pause_60',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_61_SUBSCRIPT_face_east_0',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_61_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_61_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_729_action_queue_async_61_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_61_SUBSCRIPT_face_south_4',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_set_bit_62',
        "command": 'set_bit',
        "args": [0x7049, 2]
    },
    {
        "identifier": 'EVENT_729_run_event_as_subroutine_63',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_729_run_dialog_64',
        "command": 'run_dialog',
        "args": [2303, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_729_fade_out_music_to_volume_65',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_729_pause_66',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_729_play_music_default_volume_67',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER]
    },
    {
        "identifier": 'EVENT_729_pause_68',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_69_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_69_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_729_action_queue_async_69_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 510]
    },
    {
        "identifier": 'EVENT_729_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_729_action_queue_async_71_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_729_set_action_script_sync_72',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_729_play_music_default_volume_73',
        "command": 'play_music_default_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_729_join_party_74',
        "command": 'join_party',
        "args": [AreaObjects.TOADSTOOL]
    },
    {
        "identifier": 'EVENT_729_set_bit_75',
        "command": 'set_bit',
        "args": [0x705d, 5]
    },
    {
        "identifier": 'EVENT_729_ret_76',
        "command": 'ret'
    }
]
