from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2603_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 6, 'EVENT_2603_ret_72']
    },
    {
        "identifier": 'EVENT_2603_set_bit_1',
        "command": 'set_bit',
        "args": [0x708f, 6]
    },
    {
        "identifier": 'EVENT_2603_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_2603_start_battle_15']
    },
    {
        "identifier": 'EVENT_2603_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_sync_3_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [5, 75]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_pause_5',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_6_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_6_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_6_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_7',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_8',
        "command": 'run_dialog',
        "args": [3231, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_9_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_9_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_9_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_10',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_11',
        "command": 'run_dialog',
        "args": [3232, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_12_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_13',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_14',
        "command": 'run_dialog',
        "args": [3233, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_start_battle_15',
        "command": 'start_battle',
        "args": [0x0095, 48]
    },
    {
        "identifier": 'EVENT_2603_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2603_restore_all_hp_18']
    },
    {
        "identifier": 'EVENT_2603_reset_and_choose_game_17',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2603_restore_all_hp_18',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2603_restore_all_fp_19',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2603_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2603_summon_to_current_level_28',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_15]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_29',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_35',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_remove_from_level_36',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_summon_to_level_37',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_15, Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_38_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [10, 91]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_38_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_38_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_38_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_38_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_fade_in_from_black_async_39',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2603_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2603_ret_72']
    },
    {
        "identifier": 'EVENT_2603_summon_to_current_level_at_marios_coords_41',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_42_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_42_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_43',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_44',
        "command": 'run_dialog',
        "args": [3261, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_45_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_45_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_45_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_46',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_47',
        "command": 'run_dialog',
        "args": [3266, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_sync_48_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_49_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 57]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_49_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [160]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_49_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [5, 75]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_pause_50',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2603_db_51',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_52',
        "command": 'run_dialog',
        "args": [3262, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_pause_script_resume_on_next_dialog_page_a_53',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2603_set_action_script_async_54',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_12, 854]
    },
    {
        "identifier": 'EVENT_2603_unsync_dialog_55',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_56_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_56_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_57',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_58',
        "command": 'run_dialog',
        "args": [3263, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_set_59',
        "command": 'set',
        "args": [0x70ae, 32]
    },
    {
        "identifier": 'EVENT_2603_set_action_script_async_60',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2603_pause_61',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2603_db_62',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_63',
        "command": 'run_dialog',
        "args": [3264, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2603_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_65',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_66',
        "command": 'run_dialog',
        "args": [3265, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_pause_67',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_68_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_db_69',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2603_run_dialog_70',
        "command": 'run_dialog',
        "args": [3212, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2603_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_2603_action_queue_async_71_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_71_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2603_action_queue_async_71_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2603_ret_72',
        "command": 'ret'
    }
]
