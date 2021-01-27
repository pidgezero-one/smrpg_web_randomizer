from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3723_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3723_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [107, 'EVENT_3723_run_dialog_87']
    },
    {
        "identifier": 'EVENT_3723_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_3723_run_dialog_33']
    },
    {
        "identifier": 'EVENT_3723_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 6, 'EVENT_3723_run_dialog_85']
    },
    {
        "identifier": 'EVENT_3723_set_4',
        "command": 'set',
        "args": [0x70ae, 16]
    },
    {
        "identifier": 'EVENT_3723_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3723_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3723_set_7',
        "command": 'set',
        "args": [0x70a7, 132]
    },
    {
        "identifier": 'EVENT_3723_set_8',
        "command": 'set',
        "args": [0x7000, 3660]
    },
    {
        "identifier": 'EVENT_3723_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_3723_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3723_set_bit_29',
        "command": 'set_bit',
        "args": [0x705f, 6]
    },
    {
        "identifier": 'EVENT_3723_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3723_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_3723_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3723_run_dialog_33',
        "command": 'run_dialog',
        "args": [3652, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3723_jmp_if_bit_set_34',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_3723_run_dialog_39']
    },
    {
        "identifier": 'EVENT_3723_inc_35',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_3723_set_7000_to_70A0_short_mem_36',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_3723_mem_compare_val_37',
        "command": 'mem_compare_val',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3723_jmp_if_comparison_result_is_lesser_38',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3723_run_dialog_39',
        "command": 'run_dialog',
        "args": [3653, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_40_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_40_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [27, 80]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_40_SUBSCRIPT_face_west_2',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [27, 80, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_shift_northwest_pixels_8',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_41_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_42_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_43',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 25]
    },
    {
        "identifier": 'EVENT_3723_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_46',
        "command": 'run_dialog',
        "args": [3654, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_pause_action_script_48',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_49_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_50',
        "command": 'run_dialog',
        "args": [3655, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_52_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_52_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_52_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_53',
        "command": 'run_dialog',
        "args": [3656, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_55_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_56_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_57',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_58',
        "command": 'run_dialog',
        "args": [3657, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_59',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_60_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_61_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_east_4',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_east_10',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_north_14',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_62_SUBSCRIPT_face_northwest_16',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_63',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_64_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_65_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_66',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_67',
        "command": 'run_dialog',
        "args": [3658, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_68',
        "command": 'run_dialog',
        "args": [3650, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_69',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_70_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3723_action_queue_sync_70_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3723_action_queue_sync_70_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3723_action_queue_sync_70_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_71_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_72',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_73',
        "command": 'run_dialog',
        "args": [3659, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3723_pause_74',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_sync_75_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3723_action_queue_async_76_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3723_action_queue_async_76_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [26, 16, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3723_pause_77',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_3723_set_7']
    },
    {
        "identifier": 'EVENT_3723_pause_79',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_set_action_script_async_80',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3723_pause_81',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3723_run_dialog_82',
        "command": 'run_dialog',
        "args": [3651, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3723_set_bit_83',
        "command": 'set_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3723_ret_84',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3723_run_dialog_85',
        "command": 'run_dialog',
        "args": [3648, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3723_ret_86',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3723_run_dialog_87',
        "command": 'run_dialog',
        "args": [3761, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3723_ret_88',
        "command": 'ret'
    }
]
