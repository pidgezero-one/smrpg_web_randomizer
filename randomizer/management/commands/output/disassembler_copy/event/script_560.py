
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'EVENT_560_jmp_if_random_above_128_191']
    },
    {
        "identifier": 'EVENT_560_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 7, 'EVENT_560_jmp_if_random_above_128_191']
    },
    {
        "identifier": 'EVENT_560_set_bit_2',
        "command": 'set_bit',
        "args": [0x7085, 7]
    },
    {
        "identifier": 'EVENT_560_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 16, 0]
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_4_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [0, 1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_5_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 17, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_6_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_7_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_7_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_7_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_7_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_7_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_8_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_8_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_9',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 99]
    },
    {
        "identifier": 'EVENT_560_run_dialog_12',
        "command": 'run_dialog',
        "args": [823, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_unsync_dialog_13',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_14_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_run_dialog_16',
        "command": 'run_dialog',
        "args": [857, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_18_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_18_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_18_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_22_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_22_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_23',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_24_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_25_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_25_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_26_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_26_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_27_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_27_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_28_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_28_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_29',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_30_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_31',
        "command": 'run_dialog',
        "args": [824, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_33_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_33_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_34',
        "command": 'run_dialog',
        "args": [825, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_35',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_pause_36',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_37_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_38',
        "command": 'run_dialog',
        "args": [826, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_40_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 99]
    },
    {
        "identifier": 'EVENT_560_run_dialog_42',
        "command": 'run_dialog',
        "args": [827, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_43',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_45',
        "command": 'run_dialog',
        "args": [828, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_46_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_bit_47',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_560_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_unsync_action_script_49',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_560_run_dialog_50',
        "command": 'run_dialog',
        "args": [829, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_run_dialog_52',
        "command": 'run_dialog',
        "args": [830, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_53_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [70]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_54_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_54_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_54_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_54_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_55_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_56',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_560_fade_out_music_to_volume_57',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_58',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_play_music_default_volume_59',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_60_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_60_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_60_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_60_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_60_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_61_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_61_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_61_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_62_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_62_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_62_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_63',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_run_dialog_64',
        "command": 'run_dialog',
        "args": [831, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_65',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [3, 19, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._080_BEEPING, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_shift_northwest_pixels_10',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_66_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [3, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [5, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [6, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [5, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_floating_on_19',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_face_northeast_23',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_jump_to_height_24',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_67_SUBSCRIPT_floating_off_26',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_68_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_68_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_68_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_69',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_560_pause_71',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_72_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._087_CORRECT_SIGNAL, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 17, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._081_STAR, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_shift_z_down_pixels_6',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_74_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_75',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_76_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_76_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_76_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_76_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_560_action_queue_async_76_SUBSCRIPT_pause_2']
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_77_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_77_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_79_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_79_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_80',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_run_dialog_81',
        "command": 'run_dialog',
        "args": [841, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_82',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_83_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_walk_1_step_south_0',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_floating_off_6',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [1, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [5, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [6, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [5, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_reset_properties_21',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_floating_on_23',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_set_animation_speed_25',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_shift_northwest_steps_26',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_face_northeast_27',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_jump_to_height_28',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_pause_29',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_84_SUBSCRIPT_floating_off_30',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [42]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 19, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._080_BEEPING, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_shift_northwest_steps_8',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_85_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_87',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_88',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_560_pause_89',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_90',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_90_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_91',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_92',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._088_WRONG_SIGNAL, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_93',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_94',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_94_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_95',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_96',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._088_WRONG_SIGNAL, 4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_96_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_97',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [9, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_end_loop_20',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_99',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_100',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_560_pause_101',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_102_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_103',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_104_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_104_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_105_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_105_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_105_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_105_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_560_action_queue_async_105_SUBSCRIPT_pause_2']
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_106_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_106_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_106_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_107_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_107_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_107_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_107_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_108_SUBSCRIPT_walk_1_step_south_0',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_108_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_109',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_run_dialog_110',
        "command": 'run_dialog',
        "args": [842, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_111',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_run_dialog_112',
        "command": 'run_dialog',
        "args": [843, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_113',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_113_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_113_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_113_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_113_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_113_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_114',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_114_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_114_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_114_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_114_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_115_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_115_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_116',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_fade_out_music_to_volume_117',
        "command": 'fade_out_music_to_volume',
        "args": [1, 0]
    },
    {
        "identifier": 'EVENT_560_pause_118',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_119',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_fade_in_music_120',
        "command": 'fade_in_music',
        "args": [Music._18_ROSE_TOWN]
    },
    {
        "identifier": 'EVENT_560_fade_out_music_to_volume_121',
        "command": 'fade_out_music_to_volume',
        "args": [0, 97]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_122_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_123',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_123_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_124_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_125',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_run_dialog_126',
        "command": 'run_dialog',
        "args": [844, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_127',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_bit_128',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_129',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 99]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_130',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_130_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_131',
        "command": 'run_dialog',
        "args": [845, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_132',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_133',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 507]
    },
    {
        "identifier": 'EVENT_560_pause_134',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_560_run_dialog_135',
        "command": 'run_dialog',
        "args": [846, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_136',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_unsync_dialog_137',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_560_pause_action_script_138',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_139_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_140',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_560_run_dialog_141',
        "command": 'run_dialog',
        "args": [847, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_142',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_143',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_143_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_143_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_143_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_143_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_144',
        "command": 'run_dialog',
        "args": [848, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_145',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_146',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_146_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_146_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_147',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 4, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_147_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_560_action_queue_sync_147_SUBSCRIPT_set_sprite_sequence_3']
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_148_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_149',
        "command": 'run_dialog',
        "args": [849, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_150',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 507]
    },
    {
        "identifier": 'EVENT_560_pause_151',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_560_pause_action_script_152',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_run_dialog_153',
        "command": 'run_dialog',
        "args": [850, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_154',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_154_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_154_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_155',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_155_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_155_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_155_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_155_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_155_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_156',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_action_script_async_157',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 99]
    },
    {
        "identifier": 'EVENT_560_run_dialog_158',
        "command": 'run_dialog',
        "args": [851, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_159',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_160',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [13, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_160_SUBSCRIPT_face_northeast_14',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_161',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_161_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [26]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [18]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_end_loop_20',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_162_SUBSCRIPT_reset_properties_21',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_pause_163',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_164',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 99]
    },
    {
        "identifier": 'EVENT_560_run_dialog_165',
        "command": 'run_dialog',
        "args": [852, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_action_queue_async_166',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_walk_1_step_east_4',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_shift_northwest_steps_9',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_shift_west_steps_11',
                "command": 'shift_west_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_560_action_queue_async_166_SUBSCRIPT_set_solidity_bits_14',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_167',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_167_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_167_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_167_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_168',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_168_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_168_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_168_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_169',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_169_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_169_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_start_embedded_action_script_sync_F1_169_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_run_dialog_170',
        "command": 'run_dialog',
        "args": [853, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_171',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_172',
        "command": 'set',
        "args": [0x70a7, 9]
    },
    {
        "identifier": 'EVENT_560_set_173',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_560_run_event_as_subroutine_174',
        "command": 'run_event_as_subroutine',
        "args": [3827]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_175',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 507]
    },
    {
        "identifier": 'EVENT_560_pause_176',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_560_pause_action_script_177',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_560_pause_178',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_run_dialog_179',
        "command": 'run_dialog',
        "args": [856, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_pause_180',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_181',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_181_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_182',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_182_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_action_queue_sync_183',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_sync_183_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_183_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_183_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_560_action_queue_sync_183_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_560_remember_last_object_184',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_560_action_queue_async_185',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_560_action_queue_async_185_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_186',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 128]
    },
    {
        "identifier": 'EVENT_560_pause_187',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_560_set_action_script_sync_188',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_560_set_bit_189',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_560_ret_190',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_jmp_if_random_above_128_191',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_560_run_dialog_194']
    },
    {
        "identifier": 'EVENT_560_run_dialog_192',
        "command": 'run_dialog',
        "args": [854, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_193',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_560_run_dialog_194',
        "command": 'run_dialog',
        "args": [855, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_560_ret_195',
        "command": 'ret'
    }
]
