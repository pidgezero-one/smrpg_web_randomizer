from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_931_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 7, 'EVENT_931_run_event_as_subroutine_83']
    },
    {
        "identifier": 'EVENT_931_set_1',
        "command": 'set',
        "args": [0x70ba, 0]
    },
    {
        "identifier": 'EVENT_931_set_2',
        "command": 'set',
        "args": [0x70d6, 0]
    },
    {
        "identifier": 'EVENT_931_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_931_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_931_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_931_action_queue_sync_4_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 66]
            }
        ]
    },
    {
        "identifier": 'EVENT_931_run_dialog_5',
        "command": 'run_dialog',
        "args": [2356, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_remember_last_object_6',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_931_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_931_run_dialog_63']
    },
    {
        "identifier": 'EVENT_931_store_item_amount_7000_8',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_931_jmp_if_7000_equals_short_9',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_931_run_dialog_60']
    },
    {
        "identifier": 'EVENT_931_set_random_10',
        "command": 'set_random',
        "args": [0x7000, 43]
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_11',
        "command": 'mem_compare_val',
        "args": [42]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_12',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_27']
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_13',
        "command": 'mem_compare_val',
        "args": [40]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_14',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_29']
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_15',
        "command": 'mem_compare_val',
        "args": [37]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_16',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_31']
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_17',
        "command": 'mem_compare_val',
        "args": [32]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_18',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_33']
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_19',
        "command": 'mem_compare_val',
        "args": [24]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_20',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_25']
    },
    {
        "identifier": 'EVENT_931_mem_compare_val_21',
        "command": 'mem_compare_val',
        "args": [14]
    },
    {
        "identifier": 'EVENT_931_jmp_if_comparison_result_is_greater_or_equal_22',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_931_set_35']
    },
    {
        "identifier": 'EVENT_931_set_23',
        "command": 'set',
        "args": [0x70ba, 3]
    },
    {
        "identifier": 'EVENT_931_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_37']
    },
    {
        "identifier": 'EVENT_931_set_25',
        "command": 'set',
        "args": [0x70ba, 5]
    },
    {
        "identifier": 'EVENT_931_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_37']
    },
    {
        "identifier": 'EVENT_931_set_27',
        "command": 'set',
        "args": [0x70ba, 20]
    },
    {
        "identifier": 'EVENT_931_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_931_set_29',
        "command": 'set',
        "args": [0x70ba, 10]
    },
    {
        "identifier": 'EVENT_931_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_931_set_31',
        "command": 'set',
        "args": [0x70ba, 8]
    },
    {
        "identifier": 'EVENT_931_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_931_set_33',
        "command": 'set',
        "args": [0x70ba, 6]
    },
    {
        "identifier": 'EVENT_931_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_931_set_35',
        "command": 'set',
        "args": [0x70ba, 4]
    },
    {
        "identifier": 'EVENT_931_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_42']
    },
    {
        "identifier": 'EVENT_931_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ba]
    },
    {
        "identifier": 'EVENT_931_mem_7000_shift_left_38',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_931_run_dialog_39',
        "command": 'run_dialog',
        "args": [2358, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_jmp_if_dialog_option_b_40',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_931_set_bit_57']
    },
    {
        "identifier": 'EVENT_931_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_931_set_bit_47']
    },
    {
        "identifier": 'EVENT_931_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ba]
    },
    {
        "identifier": 'EVENT_931_mem_7000_shift_left_43',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_931_run_dialog_44',
        "command": 'run_dialog',
        "args": [2357, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_jmp_if_dialog_option_b_45',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_931_set_bit_57']
    },
    {
        "identifier": 'EVENT_931_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_931_set_bit_47']
    },
    {
        "identifier": 'EVENT_931_set_bit_47',
        "command": 'set_bit',
        "args": [0x705e, 0]
    },
    {
        "identifier": 'EVENT_931_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x705e, 1]
    },
    {
        "identifier": 'EVENT_931_run_dialog_49',
        "command": 'run_dialog',
        "args": [2359, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_store_item_amount_7000_50',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_931_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_931_jmp_to_subroutine_52',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_930_enable_controls_until_return_85']
    },
    {
        "identifier": 'EVENT_931_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_931_set_short_mem_54',
        "command": 'set_short_mem',
        "args": [0x70d6, 0x7000]
    },
    {
        "identifier": 'EVENT_931_run_dialog_55',
        "command": 'run_dialog',
        "args": [2361, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_931_set_short_mem_66']
    },
    {
        "identifier": 'EVENT_931_set_bit_57',
        "command": 'set_bit',
        "args": [0x705e, 1]
    },
    {
        "identifier": 'EVENT_931_clear_bit_58',
        "command": 'clear_bit',
        "args": [0x705e, 0]
    },
    {
        "identifier": 'EVENT_931_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_931_run_dialog_49']
    },
    {
        "identifier": 'EVENT_931_run_dialog_60',
        "command": 'run_dialog',
        "args": [2363, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_run_background_event_61',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_931_ret_62',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_931_run_dialog_63',
        "command": 'run_dialog',
        "args": [2360, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_931_run_background_event_64',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_931_ret_65',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_931_set_short_mem_66',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d6]
    },
    {
        "identifier": 'EVENT_931_set_short_mem_67',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_931_set_object_memory_to_68',
        "command": 'set_object_memory_to',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_931_remove_one_from_inventory_69',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_931_end_loop_70',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_931_set_bit_71',
        "command": 'set_bit',
        "args": [0x7061, 7]
    },
    {
        "identifier": 'EVENT_931_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_931_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_931_clear_bit_74',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_931_circle_mask_static_75',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 3]
    },
    {
        "identifier": 'EVENT_931_pause_script_until_effect_done_76',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_931_pause_action_script_77',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_931_pause_action_script_78',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_79',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_79_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 82, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_79_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_79_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_79_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_80',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_80_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 83, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_80_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_80_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_931_start_embedded_action_script_sync_F1_80_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_931_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_931_action_queue_async_81_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 80, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_931_action_queue_async_81_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_931_jmp_to_event_82',
        "command": 'jmp_to_event',
        "args": [458]
    },
    {
        "identifier": 'EVENT_931_run_event_as_subroutine_83',
        "command": 'run_event_as_subroutine',
        "args": [456]
    },
    {
        "identifier": 'EVENT_931_run_dialog_84',
        "command": 'run_dialog',
        "args": [2383, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_931_run_background_event_85',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_931_ret_86',
        "command": 'ret'
    }
]
