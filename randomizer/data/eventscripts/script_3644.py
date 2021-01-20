from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3644_set_0',
        "command": 'set',
        "args": [0x70ae, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_short_1',
        "command": 'set_short',
        "args": [0x7024, 0x001e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_3644_run_dialog_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_3644_run_dialog_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_3644_run_dialog_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_3644_run_dialog_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_3644_run_dialog_186'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_7',
        "command": 'run_dialog',
        "args": [3729, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_dialog_option_b_8',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3644_pause_171'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_event_as_subroutine_11',
        "command": 'run_event_as_subroutine',
        "args": [274],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_3644_clear_bit_175'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_dec_coins_14',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_15',
        "command": 'set_bit',
        "args": [0x7090, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_16',
        "command": 'run_dialog',
        "args": [3730, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_dialog_option_b_17',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3644_pause_181'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_18',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_event_as_subroutine_20',
        "command": 'run_event_as_subroutine',
        "args": [274],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_3644_clear_bit_178'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_dec_coins_23',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_24',
        "command": 'run_dialog',
        "args": [3775, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_music_to_volume_25',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_circle_mask_static_26',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 18, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_27',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_29',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_pause_31',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_circle_mask_static_32',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_33',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3747_jmp_if_bit_clear_1'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_mem_compare_35',
        "command": 'mem_compare',
        "args": [0x7000, 45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_comparison_result_is_greater_or_equal_36',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3644_jmp_if_bit_set_54'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_mem_compare_37',
        "command": 'mem_compare',
        "args": [0x7000, 41],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_comparison_result_is_greater_or_equal_38',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3644_set_bit_161'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_mem_compare_39',
        "command": 'mem_compare',
        "args": [0x7000, 34],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_comparison_result_is_greater_or_equal_40',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3644_set_bit_145'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_mem_compare_41',
        "command": 'mem_compare',
        "args": [0x7000, 17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_comparison_result_is_greater_or_equal_42',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3644_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_43',
        "command": 'set_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_enter_area_44',
        "command": 'enter_area',
        "args": [Rooms._504_NIMBUS_LAND_DREAM_CUSHION_DREAM_TORTES_ARE_SEASONING_MARIO, RadialDirections.SOUTH, 26, 84, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_45_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_45_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_45_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 6, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_46_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_47_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_48',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_49',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_50',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_51',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_52',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_53',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_54',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 6, 'EVENT_3644_set_bit_161'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_55',
        "command": 'set_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_enter_area_56',
        "command": 'enter_area',
        "args": [Rooms._502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, RadialDirections.SOUTH, 23, 20, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_57_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_57_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 248, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_58_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_58_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_58_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_summon_to_current_level_59',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_61',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_62',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_63',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_64',
        "command": 'run_dialog',
        "args": [3800, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_65',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_66',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_67',
        "command": 'run_dialog',
        "args": [3801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_end_loop_11',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_end_loop_17',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_68_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_end_loop_7',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_start_loop_n_times_8',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._044_GHOST_FLOAT, 4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_on_16',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_off_18',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_end_loop_20',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_69_SUBSCRIPT_visibility_on_21',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_remember_last_object_70',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_71',
        "command": 'run_dialog',
        "args": [3802, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_72',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_73',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_74',
        "command": 'set_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_75',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70e1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_mem_compare_77',
        "command": 'mem_compare',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_comparison_result_is_greater_or_equal_78',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3644_set_bit_161'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_79',
        "command": 'set_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_enter_area_80',
        "command": 'enter_area',
        "args": [Rooms._502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, RadialDirections.SOUTH, 23, 20, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_81_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_81_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 248, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_82_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_82_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_82_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_set_random_83',
        "command": 'set_random',
        "args": [0x7000, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_var_equals_short_84',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_3644_jmp_if_bit_set_101'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_var_equals_short_85',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_3644_jmp_if_bit_set_114'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_var_equals_short_86',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3644_jmp_if_bit_set_128'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_87',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 2, 'EVENT_3644_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_88',
        "command": 'set_bit',
        "args": [0x7098, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_add_89',
        "command": 'add',
        "args": [0x70e1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_summon_to_current_level_90',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_91',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_92',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_93',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_async_94',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_0, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_95',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_96',
        "command": 'run_dialog',
        "args": [3803, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_97',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_98',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_99',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_100',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_101',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 3, 'EVENT_3644_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_102',
        "command": 'set_bit',
        "args": [0x7098, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_add_103',
        "command": 'add',
        "args": [0x70e1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_summon_to_current_level_104',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_105',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_106',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_107',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [20, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_108_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._063_YOSHI_TALK, 4]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_108_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_108_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_run_dialog_109',
        "command": 'run_dialog',
        "args": [3804, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_110',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_111',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_112',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_113',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_114',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 4, 'EVENT_3644_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_115',
        "command": 'set_bit',
        "args": [0x7098, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_add_116',
        "command": 'add',
        "args": [0x70e1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_summon_to_current_level_117',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_119',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_120',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_121',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_122',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_122_SUBSCRIPT_end_loop_7',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_run_dialog_123',
        "command": 'run_dialog',
        "args": [3805, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_124',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_125',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_126',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_127',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_128',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 5, 'EVENT_3644_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_129',
        "command": 'set_bit',
        "args": [0x7098, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_add_130',
        "command": 'add',
        "args": [0x70e1, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_summon_to_current_level_131',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_sync_132',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 99],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_133',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_134',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_135',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_136',
        "command": 'run_dialog',
        "args": [3806, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_137',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_138',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_sync_139',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_140',
        "command": 'run_dialog',
        "args": [3807, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_141',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_142',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_143',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_144',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_145',
        "command": 'set_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_enter_area_146',
        "command": 'enter_area',
        "args": [Rooms._502_NIMBUS_LAND_DREAM_CUSHION_DREAM_SMALL_CLOUD_PERSON_CHEERS_ON_MARIOBED_FLOATS, RadialDirections.SOUTH, 22, 19, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_freeze_camera_147',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_148_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_148_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_149_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [30, 19, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_149_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_149_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_remember_last_object_150',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_151',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_152',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_shift_east_steps_3',
                "command": 'shift_east_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_shift_east_pixels_4',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_153_SUBSCRIPT_bpl_26_27_28_5',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_154',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_embedded_animation_routine_5',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_shift_west_steps_6',
                "command": 'shift_west_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_154_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_pause_155',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_156_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_156_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_156_SUBSCRIPT_shift_east_steps_2',
                "command": 'shift_east_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_156_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_async_157',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_async_157_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_157_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_157_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3644_action_queue_async_157_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_158',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_159',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_160',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_bit_161',
        "command": 'set_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_enter_area_162',
        "command": 'enter_area',
        "args": [Rooms._503_NIMBUS_LAND_DREAM_CUSHION_DREAM_HEAVY_TROOPA_LAYING_ON_MARIO, RadialDirections.SOUTH, 25, 52, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [25, 52, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_transfer_xyzf_pixels_5',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_163_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3644_action_queue_sync_164_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3644_fade_in_from_black_sync_duration_165',
        "command": 'fade_in_from_black_sync_duration',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_166',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_167',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_fade_out_to_black_sync_duration_168',
        "command": 'fade_out_to_black_sync_duration',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_script_until_effect_done_169',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_170',
        "command": 'jmp_to_event',
        "args": [736],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_171',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_async_172',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_173',
        "command": 'run_dialog',
        "args": [3772, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_ret_174',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_175',
        "command": 'clear_bit',
        "args": [0x7049, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_176',
        "command": 'run_dialog',
        "args": [3731, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_ret_177',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_178',
        "command": 'clear_bit',
        "args": [0x7049, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_179',
        "command": 'run_dialog',
        "args": [3774, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_180',
        "command": 'jmp_to_event',
        "args": [280],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_pause_181',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_set_action_script_async_182',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_to_event_183',
        "command": 'jmp_to_event',
        "args": [280],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_event_as_subroutine_184',
        "command": 'run_event_as_subroutine',
        "args": [3660],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_ret_185',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_186',
        "command": 'run_dialog',
        "args": [3767, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_187',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_3644_run_dialog_192'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_188',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 6, 'EVENT_3644_run_dialog_194'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_if_bit_set_189',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_3644_run_dialog_196'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_190',
        "command": 'run_dialog',
        "args": [3769, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_191',
        "command": 'jmp',
        "args": ['EVENT_3644_clear_bit_197'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_192',
        "command": 'run_dialog',
        "args": [3768, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_193',
        "command": 'jmp',
        "args": ['EVENT_3644_clear_bit_197'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_194',
        "command": 'run_dialog',
        "args": [3770, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_jmp_195',
        "command": 'jmp',
        "args": ['EVENT_3644_clear_bit_197'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_run_dialog_196',
        "command": 'run_dialog',
        "args": [3771, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_197',
        "command": 'clear_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_198',
        "command": 'clear_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_199',
        "command": 'clear_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_200',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_clear_bit_201',
        "command": 'clear_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3644_ret_202',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
