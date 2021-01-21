from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_668_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_668_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_668_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_668_stop_background_event_3',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_668_stop_background_event_4',
        "command": 'stop_background_event',
        "args": [0x701e]
    },
    {
        "identifier": 'EVENT_668_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_668_start_battle_59']
    },
    {
        "identifier": 'EVENT_668_run_dialog_6',
        "command": 'run_dialog',
        "args": [2100, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_8_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_15],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_9_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_10_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [9, 97, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_11_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 8, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [9, 98, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_12_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 95, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_13_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [254, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_14_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 85]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_remember_last_object_15',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_668_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 636]
    },
    {
        "identifier": 'EVENT_668_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 636]
    },
    {
        "identifier": 'EVENT_668_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_store_01_to_0248_22',
        "command": 'store_01_to_0248'
    },
    {
        "identifier": 'EVENT_668_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_14],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_23_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [1, 3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_24_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [19]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [19]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_27_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [22]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_27_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_28',
        "command": 'run_dialog',
        "args": [2110, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_668_run_dialog_30',
        "command": 'run_dialog',
        "args": [2140, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_set_bit_31',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_668_pause_32',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_668_clear_bit_33',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 376]
    },
    {
        "identifier": 'EVENT_668_pause_35',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_668_run_dialog_36',
        "command": 'run_dialog',
        "args": [2141, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_action_script_37',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_668_start_embedded_action_script_async_38',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_38_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_pause_39',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_40_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 75, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_40_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_40_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_40_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_pause_41',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_668_run_dialog_43',
        "command": 'run_dialog',
        "args": [2142, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_set_bit_44',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_668_pause_45',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_668_clear_bit_46',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_47_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_run_dialog_49',
        "command": 'run_dialog',
        "args": [2143, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_51_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_52',
        "command": 'run_dialog',
        "args": [2144, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_53',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_start_embedded_action_script_async_54',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_54_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_54_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_54_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_start_embedded_action_script_async_55',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_55_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_55_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_start_embedded_action_script_async_55_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_57_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_58',
        "command": 'run_dialog',
        "args": [2060, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_start_battle_59',
        "command": 'start_battle',
        "args": [0x00b0, 35]
    },
    {
        "identifier": 'EVENT_668_jmp_if_bit_set_60',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_287_reset_and_choose_game_0']
    },
    {
        "identifier": 'EVENT_668_restore_all_hp_61',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_668_restore_all_fp_62',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_63',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_64',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_65',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_668_run_event_as_subroutine_66',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_668_remember_last_object_67',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_68',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_69',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_70',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_71',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_15]
    },
    {
        "identifier": 'EVENT_668_remove_from_current_level_72',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_73',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_74',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_75',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_76',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_15, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_77',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_13, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_remove_from_level_78',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_79_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_fade_in_from_black_async_80',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_668_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_668_stop_sound_115']
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_82_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_82_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_82_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_83_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_84',
        "command": 'run_dialog',
        "args": [2103, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_85',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_face_south_8',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_86_SUBSCRIPT_face_southeast_10',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_87',
        "command": 'run_dialog',
        "args": [2104, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_88',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_set_action_script_async_89',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_668_pause_90',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_91_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_91_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_91_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_92_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_92_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_92_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_92_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_93',
        "command": 'run_dialog',
        "args": [2149, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_94',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_95',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_95_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_96',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_96_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_96_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_97',
        "command": 'run_dialog',
        "args": [2150, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_pause_98',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_668_freeze_camera_99',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_668_action_queue_async_100',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_668_action_queue_async_100_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_668_action_queue_async_100_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_101_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_101_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_101_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_101_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_668_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_sync_102_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_668_action_queue_sync_102_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_remember_last_object_103',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_668_unfreeze_camera_104',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_668_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_105_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_run_dialog_106',
        "command": 'run_dialog',
        "args": [2302, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_668_fade_out_music_to_volume_107',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_668_pause_108',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_668_play_music_default_volume_109',
        "command": 'play_music_default_volume',
        "args": [Music._40_NEW_PARTNER]
    },
    {
        "identifier": 'EVENT_668_pause_110',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_111',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_111_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_111_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_111_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_668_action_queue_async_111_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_set_action_script_async_112',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 510]
    },
    {
        "identifier": 'EVENT_668_action_queue_async_113',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_668_action_queue_async_113_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_668_play_music_default_volume_114',
        "command": 'play_music_default_volume',
        "args": [Music._39_MARRYMORE]
    },
    {
        "identifier": 'EVENT_668_stop_sound_115',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_stop_sound_116',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_stop_sound_117',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_stop_sound_118',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_clear_bit_119',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_668_set_bit_120',
        "command": 'set_bit',
        "args": [0x704c, 6]
    },
    {
        "identifier": 'EVENT_668_set_bit_121',
        "command": 'set_bit',
        "args": [0x7067, 2]
    },
    {
        "identifier": 'EVENT_668_set_bit_122',
        "command": 'set_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_668_clear_bit_123',
        "command": 'clear_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_668_clear_bit_124',
        "command": 'clear_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_125',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_126',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_127',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_128',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 3, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_129',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 4, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_130',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 5, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_131',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 6, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_apply_tile_mod_132',
        "command": 'apply_tile_mod',
        "args": [Rooms._065_MARRYMORE_CHAPEL_SANCTUARY, 7, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_668_stop_sound_133',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_stop_sound_134',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_668_summon_to_level_135',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL]
    },
    {
        "identifier": 'EVENT_668_enable_controls_136',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_668_set_bit_137',
        "command": 'set_bit',
        "args": [0x7062, 2]
    },
    {
        "identifier": 'EVENT_668_set_short_138',
        "command": 'set_short',
        "args": [0x700a, 0x00d1]
    },
    {
        "identifier": 'EVENT_668_jmp_to_event_139',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_668_ret_140',
        "command": 'ret'
    }
]
