from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3479_set_0',
        "command": 'set',
        "args": [0x70ae, 23]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 1, 'EVENT_3479_run_dialog_134']
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3479_run_dialog_97']
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_not_equals_short_3',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 0, 'EVENT_3479_set_7000_to_7000_short_mem_6']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_4',
        "command": 'run_dialog',
        "args": [1086, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3479_run_dialog_97']
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_7000_short_mem_6',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_7000_not_equals_short_7',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [100, 'EVENT_3479_jmp_if_bit_clear_9']
    },
    {
        "identifier": 'EVENT_3479_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3479_set_7000_to_70A0_short_mem_13']
    },
    {
        "identifier": 'EVENT_3479_set_10',
        "command": 'set',
        "args": [0x70ca, 60]
    },
    {
        "identifier": 'EVENT_3479_set_short_11',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3479_set_7000_to_70A0_short_mem_32']
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_13',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b3]
    },
    {
        "identifier": 'EVENT_3479_set_14',
        "command": 'set',
        "args": [0x70ca, 80]
    },
    {
        "identifier": 'EVENT_3479_set_short_15',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_16',
        "command": 'mem_compare_val',
        "args": [70]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_17',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_7000_to_70A0_short_mem_32']
    },
    {
        "identifier": 'EVENT_3479_set_18',
        "command": 'set',
        "args": [0x70ca, 75]
    },
    {
        "identifier": 'EVENT_3479_set_short_19',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_20',
        "command": 'mem_compare_val',
        "args": [80]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_21',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_7000_to_70A0_short_mem_32']
    },
    {
        "identifier": 'EVENT_3479_set_22',
        "command": 'set',
        "args": [0x70ca, 70]
    },
    {
        "identifier": 'EVENT_3479_set_short_23',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_24',
        "command": 'mem_compare_val',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_25',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_7000_to_70A0_short_mem_32']
    },
    {
        "identifier": 'EVENT_3479_set_26',
        "command": 'set',
        "args": [0x70ca, 60]
    },
    {
        "identifier": 'EVENT_3479_set_short_27',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_28',
        "command": 'mem_compare_val',
        "args": [100]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_29',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_7000_to_70A0_short_mem_32']
    },
    {
        "identifier": 'EVENT_3479_set_30',
        "command": 'set',
        "args": [0x70ca, 50]
    },
    {
        "identifier": 'EVENT_3479_set_short_31',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_32',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ca]
    },
    {
        "identifier": 'EVENT_3479_set_7000_short_mem_to_7000_33',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_7000_short_mem_34',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_35',
        "command": 'run_dialog',
        "args": [1076, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_36',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3479_set_7000_to_7000_short_mem_43']
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_37',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b3]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_address_38',
        "command": 'mem_compare_address',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_39',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_set_7000_to_7000_short_mem_43']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_40',
        "command": 'run_dialog',
        "args": [1087, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_7000_short_mem_41',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_3479_set_70A0_short_mem_to_7000_42',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70b3]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_7000_short_mem_43',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3479_run_dialog_duration_47']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_45',
        "command": 'run_dialog_duration',
        "args": [1043, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_3479_set_7000_to_7000_short_mem_48']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_47',
        "command": 'run_dialog_duration',
        "args": [1037, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_7000_short_mem_48',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_equals_byte_49',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d4, 0, 'EVENT_3479_mem_compare_address_53']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_50',
        "command": 'run_dialog_duration',
        "args": [1044, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_51',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_add_short_mem_52',
        "command": 'add_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_address_53',
        "command": 'mem_compare_address',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_54',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_70A0_short_mem_to_7000_76']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_55',
        "command": 'run_dialog_duration',
        "args": [1045, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_set_short_56',
        "command": 'set_short',
        "args": [0x7028, 0x0000]
    },
    {
        "identifier": 'EVENT_3479_inc_short_57',
        "command": 'inc_short',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_3479_dec_short_mem_58',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_address_59',
        "command": 'mem_compare_address',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_60',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_inc_short_57']
    },
    {
        "identifier": 'EVENT_3479_set_70A0_short_mem_to_7000_61',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_set_62',
        "command": 'set',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_3479_set_object_memory_to_63',
        "command": 'set_object_memory_to',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_3479_add_short_mem_64',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3479_end_loop_65',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3479_set_7000_short_mem_to_7000_66',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_67',
        "command": 'run_dialog_duration',
        "args": [1046, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_68',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3479_jmp_to_subroutine_72']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_69',
        "command": 'run_dialog',
        "args": [1039, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_add_70',
        "command": 'add',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_3479_set_7000_short_mem_to_7000_71',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_3479_jmp_to_subroutine_72',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3479_action_queue_sync_137']
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_73',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_7000_equals_short_74',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_set_70A0_short_mem_to_7000_76',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_77',
        "command": 'run_dialog_duration',
        "args": [1042, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_play_sound_78',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_79',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_80',
        "command": 'run_dialog',
        "args": [1038, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_set_short_81',
        "command": 'set_short',
        "args": [0x7028, 0x0005]
    },
    {
        "identifier": 'EVENT_3479_jmp_to_subroutine_82',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3479_action_queue_sync_137']
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 0, 'EVENT_3479_jmp_if_bit_set_85']
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_not_equals_short_84',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 0, 'EVENT_3479_set_88']
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_85',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_action_queue_async_94']
    },
    {
        "identifier": 'EVENT_3479_ret_86',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3479_ret_87',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3479_set_88',
        "command": 'set',
        "args": [0x70a7, 7]
    },
    {
        "identifier": 'EVENT_3479_set_89',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_3479_run_event_as_subroutine_90',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_3479_set_bit_91',
        "command": 'set_bit',
        "args": [0x704e, 0]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_92',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_action_queue_async_94']
    },
    {
        "identifier": 'EVENT_3479_ret_93',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3479_action_queue_async_94',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_async_94_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_94_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_94_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_94_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3479_clear_bit_95',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3479_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3479_run_dialog_97',
        "command": 'run_dialog',
        "args": [1077, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_98',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_run_dialog_duration_103']
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_99',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_set_7000_short_mem_to_7000_100',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_101',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70b3]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_102',
        "command": 'run_dialog_duration',
        "args": [1075, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_103',
        "command": 'run_dialog_duration',
        "args": [1082, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_dialog_option_b_104',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3479_pause_130']
    },
    {
        "identifier": 'EVENT_3479_pause_105',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_106',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3479_store_coin_amount_7000_107',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_108',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_109',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_set_123']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_110',
        "command": 'run_dialog',
        "args": [1081, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_111',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_mem_compare_val_112',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_113',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_run_dialog_duration_121']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_114',
        "command": 'run_dialog_duration',
        "args": [1040, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_jmp_if_dialog_option_b_115',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3479_pause_130']
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_116',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3479_set_7000_to_70A0_short_mem_117',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_add_118',
        "command": 'add',
        "args": [0x7000, 65506]
    },
    {
        "identifier": 'EVENT_3479_set_70A0_short_mem_to_7000_119',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70d4]
    },
    {
        "identifier": 'EVENT_3479_jmp_120',
        "command": 'jmp',
        "args": ['EVENT_3479_run_dialog_125']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_121',
        "command": 'run_dialog_duration',
        "args": [1079, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3479_jmp_122',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_set_123',
        "command": 'set',
        "args": [0x7000, 30]
    },
    {
        "identifier": 'EVENT_3479_dec_coins_124',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_3479_run_dialog_125',
        "command": 'run_dialog',
        "args": [1078, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_play_sound_126',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_3479_set_bit_127',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3479_set_bit_128',
        "command": 'set_bit',
        "args": [0x7079, 1]
    },
    {
        "identifier": 'EVENT_3479_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_pause_130',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_131',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3479_run_dialog_132',
        "command": 'run_dialog',
        "args": [1079, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83']
    },
    {
        "identifier": 'EVENT_3479_run_dialog_134',
        "command": 'run_dialog',
        "args": [1080, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3479_set_bit_135',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3479_ret_136',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3479_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3479_set_object_memory_to_138',
        "command": 'set_object_memory_to',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_3479_action_queue_async_139',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 4]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x97, 0x17]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_floating_off_10',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_walk_1_step_northeast_12',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3479_set_140',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3479_add_frog_coins_141',
        "command": 'add_frog_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_3479_end_loop_142',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3479_action_queue_sync_143',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_sync_143_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3479_ret_144',
        "command": 'ret'
    }
]
