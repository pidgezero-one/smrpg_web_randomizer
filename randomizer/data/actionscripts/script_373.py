from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_373_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_373_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_373_set_short_2',
        "command": 'set_short',
        "args": [0x7028, 0x0001]
    },
    {
        "identifier": 'ACTION_373_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_373_jmp_if_random_above_66_12']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_jmp_if_random_above_66_12']
    },
    {
        "identifier": 'ACTION_373_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x700c, 0x70c1]
    },
    {
        "identifier": 'ACTION_373_mem_compare_7',
        "command": 'mem_compare',
        "args": [0x700c, 5]
    },
    {
        "identifier": 'ACTION_373_jmp_if_comparison_result_is_greater_or_equal_8',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_373_jump_to_subroutine_17']
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_373_jump_to_subroutine_15']
    },
    {
        "identifier": 'ACTION_373_jump_to_subroutine_10',
        "command": 'jump_to_subroutine',
        "args": [0x44d1]
    },
    {
        "identifier": 'ACTION_373_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_373_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_66_12',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_373_jump_to_subroutine_15']
    },
    {
        "identifier": 'ACTION_373_jump_to_subroutine_13',
        "command": 'jump_to_subroutine',
        "args": [0x451e]
    },
    {
        "identifier": 'ACTION_373_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_373_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_373_jump_to_subroutine_15',
        "command": 'jump_to_subroutine',
        "args": [0x445e]
    },
    {
        "identifier": 'ACTION_373_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_373_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_373_jump_to_subroutine_17',
        "command": 'jump_to_subroutine',
        "args": [0x44d1]
    },
    {
        "identifier": 'ACTION_373_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_373_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_373_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 0, 'ACTION_373_jmp_if_var_equals_short_43']
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_373_jmp_if_var_equals_short_43']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_shift_northeast_steps_34']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_373_shift_northeast_steps_34']
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_128_23',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_373_clear_solidity_bits_28']
    },
    {
        "identifier": 'ACTION_373_turn_random_direction_24',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_373_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_373_turn_random_direction_26',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_373_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_373_clear_solidity_bits_28',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_373_clear_solidity_bits_29',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_373_set_object_memory_bits_30',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_373_set_bit_31',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_373_jump_to_height_silent_32',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_373_add_33',
        "command": 'add',
        "args": [0x70c1, 0x01]
    },
    {
        "identifier": 'ACTION_373_shift_northeast_steps_34',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_373_dec_short_35',
        "command": 'dec_short',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_373_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_373_db_37',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x89, 0x44]
    },
    {
        "identifier": 'ACTION_373_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_373_set_object_memory_bits_39',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[]]
    },
    {
        "identifier": 'ACTION_373_set_solidity_bits_40',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_373_set_solidity_bits_41',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_373_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_373_jmp_if_var_equals_short_43',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 3, 'ACTION_373_jmp_if_var_equals_short_19']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_shift_southwest_steps_57']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_373_shift_southwest_steps_57']
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_128_46',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_373_clear_solidity_bits_51']
    },
    {
        "identifier": 'ACTION_373_turn_random_direction_47',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_373_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_373_turn_random_direction_49',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_373_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_373_clear_solidity_bits_51',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_373_clear_solidity_bits_52',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_373_set_object_memory_bits_53',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[0, 1]]
    },
    {
        "identifier": 'ACTION_373_set_bit_54',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_373_jump_to_height_silent_55',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_373_add_56',
        "command": 'add',
        "args": [0x70c1, 0x01]
    },
    {
        "identifier": 'ACTION_373_shift_southwest_steps_57',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_373_add_short_58',
        "command": 'add_short',
        "args": [0x7028, 0x01]
    },
    {
        "identifier": 'ACTION_373_pause_59',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_373_db_60',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xc1, 0x44]
    },
    {
        "identifier": 'ACTION_373_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_373_set_object_memory_bits_62',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[]]
    },
    {
        "identifier": 'ACTION_373_set_solidity_bits_63',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_373_set_solidity_bits_64',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_373_ret_65',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_373_jmp_if_random_above_128_66',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_373_jmp_if_bit_set_82']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_clear_bit_75']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_373_ret_81']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_69',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_373_jmp_if_bit_set_97']
    },
    {
        "identifier": 'ACTION_373_set_bit_70',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_clear_bit_71',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_jmp_74',
        "command": 'jmp',
        "args": ['ACTION_373_shift_southeast_steps_79']
    },
    {
        "identifier": 'ACTION_373_clear_bit_75',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_set_bit_78',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_shift_southeast_steps_79',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_373_set_80',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'ACTION_373_ret_81',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_82',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_373_clear_bit_90']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_373_ret_96']
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_84',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_jmp_if_bit_set_97']
    },
    {
        "identifier": 'ACTION_373_clear_bit_85',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_clear_bit_86',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_set_bit_87',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_clear_bit_88',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_jmp_89',
        "command": 'jmp',
        "args": ['ACTION_373_shift_northwest_steps_94']
    },
    {
        "identifier": 'ACTION_373_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_set_bit_91',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_clear_bit_92',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_clear_bit_93',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_shift_northwest_steps_94',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_373_set_95',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'ACTION_373_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_373_jmp_if_bit_set_97',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_373_set_bit_104']
    },
    {
        "identifier": 'ACTION_373_clear_bit_98',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_set_bit_99',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_clear_bit_100',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_clear_bit_101',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_walk_1_step_southeast_102',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_373_ret_103',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_373_set_bit_104',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_373_clear_bit_105',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_373_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_373_clear_bit_107',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_373_walk_1_step_northwest_108',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_373_ret_109',
        "command": 'ret'
    }
]
