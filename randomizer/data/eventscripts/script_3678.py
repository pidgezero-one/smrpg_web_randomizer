from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3678_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d5, 6, 'EVENT_3678_run_event_as_subroutine_2']
    },
    {
        "identifier": 'EVENT_3678_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3678_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [3375]
    },
    {
        "identifier": 'EVENT_3678_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._476_BOWSERS_KEEP_2ND_TIME_AREA_01, RadialDirections.NORTHEAST, 4, 37, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3678_set_bit_4',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_3678_set_bit_5',
        "command": 'set_bit',
        "args": [0x7070, 7]
    },
    {
        "identifier": 'EVENT_3678_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_7',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_8',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_9',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_10',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_11',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_12',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_13',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_14',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_15',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_16',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_17',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_18',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3678_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 1, 'EVENT_3678_action_queue_async_117']
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 1, 'EVENT_3678_action_queue_sync_29']
    },
    {
        "identifier": 'EVENT_3678_run_dialog_28',
        "command": 'run_dialog',
        "args": [3725, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_29_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_remember_last_object_30',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_dec_z_coord_1_step_5',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_31_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_32',
        "command": 'run_dialog',
        "args": [3810, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_34',
        "command": 'run_dialog',
        "args": [3811, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_35',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_36',
        "command": 'run_dialog',
        "args": [3812, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_37_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._059_HOVERING_FROGFUCIUS, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3678_action_queue_sync_41']
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_39_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_39_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_39_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_39_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_39_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_40',
        "command": 'run_dialog',
        "args": [3808, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_41_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_41_SUBSCRIPT_fade_out_sound_to_volume_4',
                "command": 'fade_out_sound_to_volume',
                "args": [2, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_42_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_42_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_42_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_42_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_43_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_43_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_43_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [270]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_43_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_44_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_44_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_44_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [270]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_44_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_45_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_45_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_45_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [270]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_45_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [280]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_46_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_46_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_remember_last_object_47',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3678_pause_48',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 0, 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_face_northeast_8']
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_3678_action_queue_sync_50']
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_49_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_50_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_50_SUBSCRIPT_face_west_1',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_50_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_50_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_clear_51',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3678_action_queue_async_55']
    },
    {
        "identifier": 'EVENT_3678_remember_last_object_52',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3678_pause_53',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3678_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_3678_action_queue_async_78']
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_55_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_55_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_55_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_55_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_57',
        "command": 'run_dialog',
        "args": [3813, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_58',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_60',
        "command": 'run_dialog',
        "args": [3814, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_61_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_62',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_63',
        "command": 'run_dialog',
        "args": [3815, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_64',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_65_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_66',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_67',
        "command": 'run_dialog',
        "args": [3816, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_68_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_69',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_70_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_71',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_72_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_72_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_72_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_73',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_74_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_74_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_74_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_remember_last_object_75',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3678_pause_76',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_walk_1_step_west_5',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_77_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 0, 'EVENT_3678_action_queue_async_78_SUBSCRIPT_walk_1_step_southwest_4']
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_3678_action_queue_async_78_SUBSCRIPT_face_west_5']
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_face_west_5',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_78_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_79',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3678_action_queue_async_84']
    },
    {
        "identifier": 'EVENT_3678_pause_80',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [5, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [5, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_jump_to_height_silent_16',
                "command": 'jump_to_height_silent',
                "args": [94]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_shift_northwest_steps_17',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_shift_northwest_pixels_18',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_shift_northwest_pixels_20',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_shadow_off_21',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_81_SUBSCRIPT_floating_off_22',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_set_action_script_sync_82',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 976]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_83_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_83_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_83_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_walk_1_step_north_0',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [94]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_shadow_off_10',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_84_SUBSCRIPT_floating_off_11',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 976]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_86_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_87',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_88_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_88_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_88_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_88_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_89',
        "command": 'run_dialog',
        "args": [3817, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_90',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_91_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_92',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_93',
        "command": 'run_dialog',
        "args": [3818, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3678_pause_94',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_95',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3678_action_queue_async_97']
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_96',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_96_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_97',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_97_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_98',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3678_freeze_camera_99',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_100_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_100_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_100_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_101_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_101_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_102_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_103_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._059_HOVERING_FROGFUCIUS, 4]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3678_action_queue_sync_104_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_pause_105',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'EVENT_3678_set_bit_106',
        "command": 'set_bit',
        "args": [0x7070, 2]
    },
    {
        "identifier": 'EVENT_3678_set_bit_107',
        "command": 'set_bit',
        "args": [0x7070, 7]
    },
    {
        "identifier": 'EVENT_3678_fade_out_to_black_sync_duration_108',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3678_pause_script_until_effect_done_109',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3678_run_event_sequence_110',
        "command": 'run_event_sequence',
        "args": [EventSequences._16_RUN_WORLD_MAP_EVENT_SEQUENCE, OverworldSequences._02_MARIO_TAKES_NIMBUS_BUS]
    },
    {
        "identifier": 'EVENT_3678_fade_out_sound_to_volume_111',
        "command": 'fade_out_sound_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_bit_set_112',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 1, 'EVENT_3678_open_location_115']
    },
    {
        "identifier": 'EVENT_3678_set_bit_113',
        "command": 'set_bit',
        "args": [0x7098, 1]
    },
    {
        "identifier": 'EVENT_3678_jmp_to_event_114',
        "command": 'jmp_to_event',
        "args": [2277]
    },
    {
        "identifier": 'EVENT_3678_open_location_115',
        "command": 'open_location',
        "args": [Locations._004_BOWSERS_KEEP, [6, 7]]
    },
    {
        "identifier": 'EVENT_3678_ret_116',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_117',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_117_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_117_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 38]
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_117_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3678_action_queue_async_117_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3678_action_queue_async_118_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3678_set_119',
        "command": 'set',
        "args": [0x70ae, 16]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_120',
        "command": 'run_dialog',
        "args": [3872, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3678_jmp_if_dialog_option_b_121',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3678_pause_127']
    },
    {
        "identifier": 'EVENT_3678_pause_122',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_set_action_script_async_123',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_124',
        "command": 'run_dialog',
        "args": [3873, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3678_set_bit_125',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3678_jmp_126',
        "command": 'jmp',
        "args": ['EVENT_3678_action_queue_async_37']
    },
    {
        "identifier": 'EVENT_3678_pause_127',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3678_set_action_script_async_128',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3678_run_dialog_129',
        "command": 'run_dialog',
        "args": [3874, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3678_clear_bit_130',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3678_ret_131',
        "command": 'ret'
    }
]
