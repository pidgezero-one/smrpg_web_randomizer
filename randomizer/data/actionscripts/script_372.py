from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_372_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_372_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_372_set_short_2',
        "command": 'set_short',
        "args": [0x7026, 0x0003]
    },
    {
        "identifier": 'ACTION_372_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_372_jmp_if_random_above_66_12']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_jmp_if_random_above_66_12']
    },
    {
        "identifier": 'ACTION_372_set_700C_to_70A0_short_mem_6',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70c0]
    },
    {
        "identifier": 'ACTION_372_mem_compare_val_7',
        "command": 'mem_compare_val',
        "args": [5]
    },
    {
        "identifier": 'ACTION_372_jmp_if_comparison_result_is_greater_or_equal_8',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_372_jump_to_subroutine_17']
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_372_jump_to_subroutine_15']
    },
    {
        "identifier": 'ACTION_372_jump_to_subroutine_10',
        "command": 'jump_to_subroutine',
        "args": [0x43bf]
    },
    {
        "identifier": 'ACTION_372_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_372_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_66_12',
        "command": 'jmp_if_random_above_66',
        "args": [0x4340, 'ACTION_372_jump_to_subroutine_17']
    },
    {
        "identifier": 'ACTION_372_jump_to_subroutine_13',
        "command": 'jump_to_subroutine',
        "args": [0x440c]
    },
    {
        "identifier": 'ACTION_372_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_372_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_372_jump_to_subroutine_15',
        "command": 'jump_to_subroutine',
        "args": [0x434c]
    },
    {
        "identifier": 'ACTION_372_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_372_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_372_jump_to_subroutine_17',
        "command": 'jump_to_subroutine',
        "args": [0x43bf]
    },
    {
        "identifier": 'ACTION_372_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_372_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_372_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'ACTION_372_jmp_if_var_equals_short_43']
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_372_jmp_if_var_equals_short_43']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_shift_northeast_steps_34']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_372_shift_northeast_steps_34']
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_128_23',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_372_clear_solidity_bits_28']
    },
    {
        "identifier": 'ACTION_372_turn_random_direction_24',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_372_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_372_turn_random_direction_26',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_372_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_372_clear_solidity_bits_28',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_372_clear_solidity_bits_29',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_372_set_object_memory_bits_30',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [0, 1]]
    },
    {
        "identifier": 'ACTION_372_set_bit_31',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_372_jump_to_height_silent_32',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_372_inc_33',
        "command": 'inc',
        "args": [0x70c0]
    },
    {
        "identifier": 'ACTION_372_shift_northeast_steps_34',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_372_dec_short_35',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_372_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_372_db_37',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x77, 0x43]
    },
    {
        "identifier": 'ACTION_372_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_372_set_object_memory_bits_39',
        "command": 'set_object_memory_bits',
        "args": [0x0b, []]
    },
    {
        "identifier": 'ACTION_372_set_solidity_bits_40',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_372_set_solidity_bits_41',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_372_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_372_jmp_if_var_equals_short_43',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 5, 'ACTION_372_jmp_if_var_equals_short_19']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_shift_southwest_steps_57']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_372_shift_southwest_steps_57']
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_128_46',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_372_clear_solidity_bits_51']
    },
    {
        "identifier": 'ACTION_372_turn_random_direction_47',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_372_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_372_turn_random_direction_49',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_372_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_372_clear_solidity_bits_51',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_372_clear_solidity_bits_52',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_372_set_object_memory_bits_53',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [0, 1]]
    },
    {
        "identifier": 'ACTION_372_set_bit_54',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_372_jump_to_height_silent_55',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_372_inc_56',
        "command": 'inc',
        "args": [0x70c0]
    },
    {
        "identifier": 'ACTION_372_shift_southwest_steps_57',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_372_inc_short_58',
        "command": 'inc_short',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_372_pause_59',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_372_db_60',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xaf, 0x43]
    },
    {
        "identifier": 'ACTION_372_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_372_set_object_memory_bits_62',
        "command": 'set_object_memory_bits',
        "args": [0x0b, []]
    },
    {
        "identifier": 'ACTION_372_set_solidity_bits_63',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_372_set_solidity_bits_64',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_372_ret_65',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_372_jmp_if_random_above_128_66',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_372_jmp_if_bit_set_82']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_clear_bit_75']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_372_ret_81']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_69',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_372_jmp_if_bit_set_97']
    },
    {
        "identifier": 'ACTION_372_set_bit_70',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_clear_bit_71',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_jmp_74',
        "command": 'jmp',
        "args": ['ACTION_372_shift_southeast_steps_79']
    },
    {
        "identifier": 'ACTION_372_clear_bit_75',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_set_bit_78',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_shift_southeast_steps_79',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_372_set_80',
        "command": 'set',
        "args": [0x70c0, 0]
    },
    {
        "identifier": 'ACTION_372_ret_81',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_82',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'ACTION_372_clear_bit_90']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_83',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_372_ret_96']
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_84',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_jmp_if_bit_set_97']
    },
    {
        "identifier": 'ACTION_372_clear_bit_85',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_clear_bit_86',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_set_bit_87',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_clear_bit_88',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_jmp_89',
        "command": 'jmp',
        "args": ['ACTION_372_shift_northwest_steps_94']
    },
    {
        "identifier": 'ACTION_372_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_set_bit_91',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_clear_bit_92',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_clear_bit_93',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_shift_northwest_steps_94',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_372_set_95',
        "command": 'set',
        "args": [0x70c0, 0]
    },
    {
        "identifier": 'ACTION_372_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_372_jmp_if_bit_set_97',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_372_set_bit_104']
    },
    {
        "identifier": 'ACTION_372_clear_bit_98',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_set_bit_99',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_clear_bit_100',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_clear_bit_101',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_walk_1_step_southeast_102',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_372_ret_103',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_372_set_bit_104',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_372_clear_bit_105',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_372_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_372_clear_bit_107',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_372_walk_1_step_northwest_108',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_372_ret_109',
        "command": 'ret'
    }
]
