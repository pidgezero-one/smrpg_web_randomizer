from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_374_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_374_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_374_set_short_2',
        "command": 'set_short',
        "args": [0x702a, 0x0005]
    },
    {
        "identifier": 'ACTION_374_fixed_f_coord_off_3',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_374_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_374_jmp_if_random_above_66_13']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_jmp_if_random_above_66_13']
    },
    {
        "identifier": 'ACTION_374_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x700c, 0x70c2]
    },
    {
        "identifier": 'ACTION_374_mem_compare_8',
        "command": 'mem_compare',
        "args": [0x700c, 5]
    },
    {
        "identifier": 'ACTION_374_jmp_if_comparison_result_is_greater_or_equal_9',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_374_jump_to_subroutine_18']
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_128_10',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_374_jump_to_subroutine_16']
    },
    {
        "identifier": 'ACTION_374_jump_to_subroutine_11',
        "command": 'jump_to_subroutine',
        "args": [0x45e4]
    },
    {
        "identifier": 'ACTION_374_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_374_jmp_if_bit_set_5']
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_66_13',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_374_jump_to_subroutine_16']
    },
    {
        "identifier": 'ACTION_374_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x4631]
    },
    {
        "identifier": 'ACTION_374_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_374_jmp_if_bit_set_5']
    },
    {
        "identifier": 'ACTION_374_jump_to_subroutine_16',
        "command": 'jump_to_subroutine',
        "args": [0x4571]
    },
    {
        "identifier": 'ACTION_374_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_374_jmp_if_bit_set_5']
    },
    {
        "identifier": 'ACTION_374_jump_to_subroutine_18',
        "command": 'jump_to_subroutine',
        "args": [0x45e4]
    },
    {
        "identifier": 'ACTION_374_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_374_jmp_if_bit_set_5']
    },
    {
        "identifier": 'ACTION_374_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 4, 'ACTION_374_jmp_if_var_equals_short_44']
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_128_21',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_374_jmp_if_var_equals_short_44']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_shift_northeast_steps_35']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_374_shift_northeast_steps_35']
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_128_24',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_374_clear_solidity_bits_29']
    },
    {
        "identifier": 'ACTION_374_turn_random_direction_25',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_374_pause_26',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_374_turn_random_direction_27',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_374_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_374_clear_solidity_bits_29',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_374_clear_solidity_bits_30',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_374_set_object_memory_bits_31',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_374_set_bit_32',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_374_jump_to_height_silent_33',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_374_add_34',
        "command": 'add',
        "args": [0x70c2, 0x01]
    },
    {
        "identifier": 'ACTION_374_shift_northeast_steps_35',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_374_dec_short_36',
        "command": 'dec_short',
        "args": [0x702a]
    },
    {
        "identifier": 'ACTION_374_pause_37',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_374_db_38',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x9c, 0x45]
    },
    {
        "identifier": 'ACTION_374_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_374_set_object_memory_bits_40',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[]]
    },
    {
        "identifier": 'ACTION_374_set_solidity_bits_41',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_374_set_solidity_bits_42',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_374_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_374_jmp_if_var_equals_short_44',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 7, 'ACTION_374_jmp_if_var_equals_short_20']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_shift_southwest_steps_58']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_374_shift_southwest_steps_58']
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_128_47',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_374_clear_solidity_bits_52']
    },
    {
        "identifier": 'ACTION_374_turn_random_direction_48',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_374_pause_49',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_374_turn_random_direction_50',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_374_pause_51',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_374_clear_solidity_bits_52',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_374_clear_solidity_bits_53',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_374_set_object_memory_bits_54',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_374_set_bit_55',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_374_jump_to_height_silent_56',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_374_add_57',
        "command": 'add',
        "args": [0x70c2, 0x01]
    },
    {
        "identifier": 'ACTION_374_shift_southwest_steps_58',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_374_add_short_59',
        "command": 'add_short',
        "args": [0x702a, 0x01]
    },
    {
        "identifier": 'ACTION_374_pause_60',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_374_db_61',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xd4, 0x45]
    },
    {
        "identifier": 'ACTION_374_clear_bit_62',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_374_set_object_memory_bits_63',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[]]
    },
    {
        "identifier": 'ACTION_374_set_solidity_bits_64',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_374_set_solidity_bits_65',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_374_ret_66',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_374_jmp_if_random_above_128_67',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_374_jmp_if_bit_set_83']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_clear_bit_76']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_69',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_374_ret_82']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_70',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'ACTION_374_jmp_if_bit_set_98']
    },
    {
        "identifier": 'ACTION_374_set_bit_71',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_clear_bit_74',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_jmp_75',
        "command": 'jmp',
        "args": ['ACTION_374_shift_southeast_steps_80']
    },
    {
        "identifier": 'ACTION_374_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_set_bit_79',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_shift_southeast_steps_80',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_374_set_81',
        "command": 'set',
        "args": [0x70c2, 0]
    },
    {
        "identifier": 'ACTION_374_ret_82',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_374_clear_bit_91']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_84',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'ACTION_374_ret_97']
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_85',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_jmp_if_bit_set_98']
    },
    {
        "identifier": 'ACTION_374_clear_bit_86',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_clear_bit_87',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_set_bit_88',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_clear_bit_89',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_jmp_90',
        "command": 'jmp',
        "args": ['ACTION_374_shift_northwest_steps_95']
    },
    {
        "identifier": 'ACTION_374_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_set_bit_92',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_clear_bit_93',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_clear_bit_94',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_shift_northwest_steps_95',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_374_set_96',
        "command": 'set',
        "args": [0x70c2, 0]
    },
    {
        "identifier": 'ACTION_374_ret_97',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_374_jmp_if_bit_set_98',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'ACTION_374_set_bit_105']
    },
    {
        "identifier": 'ACTION_374_clear_bit_99',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_set_bit_100',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_clear_bit_101',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_clear_bit_102',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_walk_1_step_southeast_103',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_374_ret_104',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_374_set_bit_105',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_374_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_374_clear_bit_107',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_374_clear_bit_108',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_374_walk_1_step_northwest_109',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_374_ret_110',
        "command": 'ret'
    }
]
