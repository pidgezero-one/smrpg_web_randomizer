from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_611_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 96]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_611_action_queue_sync_92']
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_611_jmp_if_bit_clear_23']
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_611_action_queue_async_19']
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_611_jmp_if_bit_set_11']
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_611_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_611_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_611_jmp_if_bit_set_16']
    },
    {
        "identifier": 'EVENT_611_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_611_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_611_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_611_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_611_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 2, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_611_run_background_event_17',
        "command": 'run_background_event',
        "args": [623, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_611_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_19_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 62, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_19_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_611_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_611_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 5, 'EVENT_611_jmp_if_bit_clear_25']
    },
    {
        "identifier": 'EVENT_611_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_24_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 62, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_24_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_clear_25',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_611_jmp_if_bit_clear_27']
    },
    {
        "identifier": 'EVENT_611_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_26_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_26_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_clear_27',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 5, 'EVENT_611_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_async_28',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_611_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_29_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_611_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac]
    },
    {
        "identifier": 'EVENT_611_add_32',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 6, 'EVENT_611_run_dialog_76']
    },
    {
        "identifier": 'EVENT_611_run_dialog_34',
        "command": 'run_dialog',
        "args": [2509, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_611_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_611_dec_short_36',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_611_set_short_37',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_611_set_object_memory_to_38',
        "command": 'set_object_memory_to',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_611_store_coin_amount_7000_39',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_611_mem_compare_40',
        "command": 'mem_compare',
        "args": [0x7000, 100]
    },
    {
        "identifier": 'EVENT_611_jmp_if_comparison_result_is_lesser_41',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_611_set_bit_58']
    },
    {
        "identifier": 'EVENT_611_set_42',
        "command": 'set',
        "args": [0x7000, 100]
    },
    {
        "identifier": 'EVENT_611_dec_coins_43',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_611_add_short_44',
        "command": 'add_short',
        "args": [0x7026, 0x01]
    },
    {
        "identifier": 'EVENT_611_play_sound_45',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_611_pause_46',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_611_end_loop_47',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_611_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_48_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_48_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_611_run_dialog_50',
        "command": 'run_dialog',
        "args": [1003, AreaObjects.BOWSER, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_611_remember_last_object_51',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_611_set_bit_52',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_611_clear_bit_53',
        "command": 'clear_bit',
        "args": [0x7042, 6]
    },
    {
        "identifier": 'EVENT_611_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 323]
    },
    {
        "identifier": 'EVENT_611_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 891]
    },
    {
        "identifier": 'EVENT_611_set_56',
        "command": 'set',
        "args": [0x70ac, 0]
    },
    {
        "identifier": 'EVENT_611_ret_57',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_set_bit_58',
        "command": 'set_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_611_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7042, 6]
    },
    {
        "identifier": 'EVENT_611_run_dialog_60',
        "command": 'run_dialog',
        "args": [1002, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_611_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_611_dec_short_mem_62',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_611_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000]
    },
    {
        "identifier": 'EVENT_611_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_611_set_action_script_sync_65',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 322]
    },
    {
        "identifier": 'EVENT_611_fade_out_to_black_sync_duration_66',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90]
    },
    {
        "identifier": 'EVENT_611_pause_script_until_effect_done_67',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_611_enter_area_68',
        "command": 'enter_area',
        "args": [Rooms._007_MARRYMORE_INN_1F, RadialDirections.SOUTHEAST, 3, 55, 0, []]
    },
    {
        "identifier": 'EVENT_611_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_sync_69_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_69_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_69_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_611_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_sync_70_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_70_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_sync_duration_71',
        "command": 'fade_in_from_black_sync_duration',
        "args": [90]
    },
    {
        "identifier": 'EVENT_611_pause_script_until_effect_done_72',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_611_pause_73',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_611_run_background_event_74',
        "command": 'run_background_event',
        "args": [617, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_611_ret_75',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_611_run_dialog_76',
        "command": 'run_dialog',
        "args": [2479, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_611_run_dialog_77',
        "command": 'run_dialog',
        "args": [2480, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_611_store_coin_amount_7000_78',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_611_dec_coins_79',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_611_store_frog_coin_amount_7000_80',
        "command": 'store_frog_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_611_dec_frog_coins_7000_81',
        "command": 'dec_frog_coins_7000'
    },
    {
        "identifier": 'EVENT_611_play_sound_82',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_611_pause_83',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_611_play_sound_84',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_611_pause_85',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_611_run_dialog_86',
        "command": 'run_dialog',
        "args": [2478, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_611_set_bit_87',
        "command": 'set_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_611_clear_bit_88',
        "command": 'clear_bit',
        "args": [0x7042, 6]
    },
    {
        "identifier": 'EVENT_611_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_611_set_90',
        "command": 'set',
        "args": [0x70ac, 200]
    },
    {
        "identifier": 'EVENT_611_jmp_91',
        "command": 'jmp',
        "args": ['EVENT_611_set_action_script_sync_65']
    },
    {
        "identifier": 'EVENT_611_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_sync_92_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_92_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_93',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_611_jmp_if_bit_set_104']
    },
    {
        "identifier": 'EVENT_611_set_short_mem_94',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_611_jmp_if_var_equals_short_95',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_611_jmp_if_bit_set_104']
    },
    {
        "identifier": 'EVENT_611_jmp_if_var_equals_short_96',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_611_action_queue_sync_100']
    },
    {
        "identifier": 'EVENT_611_jmp_if_var_equals_short_97',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_611_action_queue_async_103']
    },
    {
        "identifier": 'EVENT_611_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_98_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 60, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_98_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_99',
        "command": 'jmp',
        "args": ['EVENT_611_jmp_if_bit_set_104']
    },
    {
        "identifier": 'EVENT_611_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_sync_100_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 60, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_sync_100_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_action_queue_async_101',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_101_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 59, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_101_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_102',
        "command": 'jmp',
        "args": ['EVENT_611_jmp_if_bit_set_104']
    },
    {
        "identifier": 'EVENT_611_action_queue_async_103',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_611_action_queue_async_103_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 60, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_611_action_queue_async_103_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_611_jmp_if_bit_set_104',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_611_run_event_as_subroutine_8']
    },
    {
        "identifier": 'EVENT_611_fade_in_from_black_async_105',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_611_ret_106',
        "command": 'ret'
    }
]
