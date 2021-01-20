from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3479_set_0',
        "command": 'set',
        "args": [0x70ae, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 1, 'EVENT_3479_run_dialog_134'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3479_run_dialog_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_not_equals_short_3',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 0, 'EVENT_3479_set_short_mem_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_4',
        "command": 'run_dialog',
        "args": [1086, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_3479_run_dialog_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_not_equals_short_7',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 100, 'EVENT_3479_jmp_if_bit_clear_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3479_set_short_mem_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_10',
        "command": 'set',
        "args": [0x70ca, 60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_11',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3479_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_14',
        "command": 'set',
        "args": [0x70ca, 80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_15',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_16',
        "command": 'mem_compare',
        "args": [0x7000, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_17',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_18',
        "command": 'set',
        "args": [0x70ca, 75],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_19',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_20',
        "command": 'mem_compare',
        "args": [0x7000, 80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_21',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_22',
        "command": 'set',
        "args": [0x70ca, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_23',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_24',
        "command": 'mem_compare',
        "args": [0x7000, 90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_25',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_26',
        "command": 'set',
        "args": [0x70ca, 60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_27',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_28',
        "command": 'mem_compare',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_29',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_short_mem_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_30',
        "command": 'set',
        "args": [0x70ca, 50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_31',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ca],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_35',
        "command": 'run_dialog',
        "args": [1076, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_36',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3479_set_short_mem_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_38',
        "command": 'mem_compare',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_39',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_set_short_mem_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_40',
        "command": 'run_dialog',
        "args": [1087, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_41',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x70b3, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_43',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3479_run_dialog_duration_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_45',
        "command": 'run_dialog_duration',
        "args": [1043, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_3479_set_short_mem_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_47',
        "command": 'run_dialog_duration',
        "args": [1037, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_equals_byte_49',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70d4, 0, 'EVENT_3479_mem_compare_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_50',
        "command": 'run_dialog_duration',
        "args": [1044, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_51',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_short_mem_52',
        "command": 'add_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_53',
        "command": 'mem_compare',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_54',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_set_short_mem_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_55',
        "command": 'run_dialog_duration',
        "args": [1045, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_56',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_short_57',
        "command": 'add_short',
        "args": [0x7028, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_dec_short_mem_58',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_59',
        "command": 'mem_compare',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_60',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_add_short_57'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x70d4, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_62',
        "command": 'set',
        "args": [0x7000, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_object_memory_to_63',
        "command": 'set_object_memory_to',
        "args": [0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_short_mem_64',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_end_loop_65',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_66',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_67',
        "command": 'run_dialog_duration',
        "args": [1046, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_68',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3479_jmp_to_subroutine_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_69',
        "command": 'run_dialog',
        "args": [1039, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_70',
        "command": 'add',
        "args": [0x7000, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_71',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_to_subroutine_72',
        "command": 'jmp_to_subroutine',
        "args": [0x605e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_73',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x70d4, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_77',
        "command": 'run_dialog_duration',
        "args": [1042, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_play_sound_78',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_clear_79',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_80',
        "command": 'run_dialog',
        "args": [1038, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_81',
        "command": 'set_short',
        "args": [0x7028, 0x0005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_to_subroutine_82',
        "command": 'jmp_to_subroutine',
        "args": [0x605e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 0, 'EVENT_3479_jmp_if_bit_set_85'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_var_not_equals_short_84',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 0, 'EVENT_3479_set_88'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_85',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_action_queue_async_94'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_ret_86',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_ret_87',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_88',
        "command": 'set',
        "args": [0x70a7, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_89',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_event_as_subroutine_90',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_bit_91',
        "command": 'set_bit',
        "args": [0x704e, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_92',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_action_queue_async_94'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_ret_93',
        "command": 'ret',
        "args": [],
        "subscript": []
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
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_94_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3479_clear_bit_95',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_ret_96',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_97',
        "command": 'run_dialog',
        "args": [1077, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_bit_set_98',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3479_run_dialog_duration_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_99',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_100',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_101',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_102',
        "command": 'run_dialog_duration',
        "args": [1075, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_103',
        "command": 'run_dialog_duration',
        "args": [1082, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_dialog_option_b_104',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3479_pause_130'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_pause_105',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_106',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_store_coin_amount_7000_107',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_108',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_greater_or_equal_109',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3479_set_123'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_110',
        "command": 'run_dialog',
        "args": [1081, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_111',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_mem_compare_112',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_comparison_result_is_lesser_113',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3479_run_dialog_duration_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_114',
        "command": 'run_dialog_duration',
        "args": [1040, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_if_dialog_option_b_115',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3479_pause_130'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_116',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_117',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_118',
        "command": 'add',
        "args": [0x7000, 65506],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_short_mem_119',
        "command": 'set_short_mem',
        "args": [0x70d4, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_120',
        "command": 'jmp',
        "args": ['EVENT_3479_run_dialog_125'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_duration_121',
        "command": 'run_dialog_duration',
        "args": [1079, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_122',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_123',
        "command": 'set',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_dec_coins_124',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_125',
        "command": 'run_dialog',
        "args": [1078, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_play_sound_126',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_bit_127',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_bit_128',
        "command": 'set_bit',
        "args": [0x7079, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_pause_130',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_action_script_async_131',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_132',
        "command": 'run_dialog',
        "args": [1079, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_3479_jmp_if_bit_set_83'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_run_dialog_134',
        "command": 'run_dialog',
        "args": [1080, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_set_bit_135',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_ret_136',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_sync_137_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3479_set_object_memory_to_138',
        "command": 'set_object_memory_to',
        "args": [0x7028],
        "subscript": []
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
                "command": 'shadow_off',
                "args": []
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
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
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
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_floating_off_10',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_jump_to_height_silent_11',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_walk_1_step_northeast_12',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3479_action_queue_async_139_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3479_set_140',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_add_frog_coins_141',
        "command": 'add_frog_coins',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_end_loop_142',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3479_action_queue_sync_143',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3479_action_queue_sync_143_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3479_ret_144',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
