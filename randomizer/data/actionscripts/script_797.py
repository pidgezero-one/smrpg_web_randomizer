from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_797_set_random_0',
        "command": 'set_random',
        "args": [0x700c, 80]
    },
    {
        "identifier": 'ACTION_797_mem_compare_address_1',
        "command": 'mem_compare_address',
        "args": [0x7038]
    },
    {
        "identifier": 'ACTION_797_jmp_if_comparison_result_is_greater_or_equal_2',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_797_jump_to_subroutine_9']
    },
    {
        "identifier": 'ACTION_797_mem_compare_address_3',
        "command": 'mem_compare_address',
        "args": [0x703a]
    },
    {
        "identifier": 'ACTION_797_jmp_if_comparison_result_is_greater_or_equal_4',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_797_jump_to_subroutine_13']
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x994e]
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0x9984]
    },
    {
        "identifier": 'ACTION_797_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7014, 1, 'ACTION_797_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_797_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_797_set_random_0']
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_9',
        "command": 'jump_to_subroutine',
        "args": [0x995a]
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_10',
        "command": 'jump_to_subroutine',
        "args": [0x9984]
    },
    {
        "identifier": 'ACTION_797_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7014, 1, 'ACTION_797_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_797_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_797_set_random_0']
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_13',
        "command": 'jump_to_subroutine',
        "args": [0x9954]
    },
    {
        "identifier": 'ACTION_797_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x9984]
    },
    {
        "identifier": 'ACTION_797_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7014, 1, 'ACTION_797_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_797_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_797_set_random_0']
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_797_walk_1_step_northeast_19',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_797_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_797_walk_1_step_northeast_23',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_797_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_797_walk_1_step_northeast_27',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_797_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_797_shift_northeast_pixels_29',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_797_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'ACTION_797_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_797_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_797_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_797_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_797_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_797_set_bit_33',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_797_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7085, 4]
    },
    {
        "identifier": 'ACTION_797_shift_northeast_pixels_35',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_797_set_short_37',
        "command": 'set_short',
        "args": [0x7014, 0x0000]
    },
    {
        "identifier": 'ACTION_797_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_797_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_797_shift_northeast_pixels_40',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_797_set_short_41',
        "command": 'set_short',
        "args": [0x7014, 0x0000]
    },
    {
        "identifier": 'ACTION_797_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_797_dec_short_43',
        "command": 'dec_short',
        "args": [0x7014]
    },
    {
        "identifier": 'ACTION_797_ret_44',
        "command": 'ret'
    }
]
