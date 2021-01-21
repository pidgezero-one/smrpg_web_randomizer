from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_320_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x015c]
    },
    {
        "identifier": 'EVENT_320_set_bit_7_offset_1',
        "command": 'set_bit_7_offset',
        "args": [0x015e]
    },
    {
        "identifier": 'EVENT_320_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7042, 7]
    },
    {
        "identifier": 'EVENT_320_jmp_if_object_trigger_disabled_3',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, 'EVENT_320_stop_sound_5']
    },
    {
        "identifier": 'EVENT_320_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_4_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_stop_sound_5',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 5, 'EVENT_320_summon_to_current_level_31']
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 4, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_320_remove_from_current_level_42']
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 1, 'EVENT_320_jmp_if_bit_set_28']
    },
    {
        "identifier": 'EVENT_320_set_bit_11',
        "command": 'set_bit',
        "args": [0x7081, 1]
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7052, 5, 'EVENT_320_action_queue_async_20']
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_13_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_13_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_fade_in_from_black_sync_14',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_320_remember_last_object_15',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_320_run_dialog_16',
        "command": 'run_dialog',
        "args": [550, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_run_background_event_17',
        "command": 'run_background_event',
        "args": [343, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_320_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 65]
    },
    {
        "identifier": 'EVENT_320_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_320_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_20_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [2, 36, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_20_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_20_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_fade_in_from_black_sync_21',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_320_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_22_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_22_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_22_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_22_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_script_until_effect_done_23',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_320_run_dialog_24',
        "command": 'run_dialog',
        "args": [667, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_run_background_event_25',
        "command": 'run_background_event',
        "args": [343, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_320_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 65]
    },
    {
        "identifier": 'EVENT_320_ret_27',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_320_summon_to_current_level_31']
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_320_summon_to_current_level_31']
    },
    {
        "identifier": 'EVENT_320_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_320_summon_to_current_level_31',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_320_summon_to_current_level_32',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_320_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 128]
    },
    {
        "identifier": 'EVENT_320_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 128]
    },
    {
        "identifier": 'EVENT_320_fade_in_from_black_async_35',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_320_run_event_as_subroutine_36',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_320_jmp_if_bit_clear_37',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_320_jmp_if_object_trigger_disabled_38',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_4, Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_320_play_sound_39',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_320_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_320_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_320_remove_from_current_level_42',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_320_remove_from_current_level_43',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_44_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_44_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_44_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_fade_in_from_black_sync_45',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_320_remember_last_object_46',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_320_pause_script_until_effect_done_47',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_320_run_dialog_48',
        "command": 'run_dialog',
        "args": [2244, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_pause_49',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [2, 34, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_50_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_51',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_52_SUBSCRIPT_face_east_0',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_add_z_coord_1_step_5',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_53_SUBSCRIPT_dec_z_coord_1_step_6',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_54',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_run_dialog_55',
        "command": 'run_dialog',
        "args": [2245, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_pause_56',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_57_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_58_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_58_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_run_dialog_59',
        "command": 'run_dialog',
        "args": [2246, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_60_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_60_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_61',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_run_dialog_62',
        "command": 'run_dialog',
        "args": [2247, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_pause_63',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_320_action_queue_sync_64_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_65_SUBSCRIPT_add_z_coord_1_step_0',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_65_SUBSCRIPT_dec_z_coord_1_step_1',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_66',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_run_dialog_67',
        "command": 'run_dialog',
        "args": [2248, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_pause_68',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_sync_69_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_70_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_70_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_70_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_run_dialog_71',
        "command": 'run_dialog',
        "args": [2249, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_72',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_72_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_72_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_72_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_320_action_queue_async_72_SUBSCRIPT_set_object_memory_bits_3',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_set_action_script_sync_73',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 65]
    },
    {
        "identifier": 'EVENT_320_run_background_event_74',
        "command": 'run_background_event',
        "args": [343, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_75_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_320_pause_76',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_320_run_dialog_77',
        "command": 'run_dialog',
        "args": [2250, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_320_pause_78',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_320_set_action_script_async_79',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_320_pause_80',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_320_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_320_action_queue_async_81_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_320_action_queue_async_81_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_320_set_bit_82',
        "command": 'set_bit',
        "args": [0x705d, 4]
    },
    {
        "identifier": 'EVENT_320_ret_83',
        "command": 'ret'
    }
]
