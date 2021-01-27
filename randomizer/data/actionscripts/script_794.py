from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_794_set_random_0',
        "command": 'set_random',
        "args": [0x700c, 80]
    },
    {
        "identifier": 'ACTION_794_mem_compare_address_1',
        "command": 'mem_compare_address',
        "args": [0x7016]
    },
    {
        "identifier": 'ACTION_794_jmp_if_comparison_result_is_greater_or_equal_2',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_794_jump_to_subroutine_9']
    },
    {
        "identifier": 'ACTION_794_mem_compare_address_3',
        "command": 'mem_compare_address',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_794_jmp_if_comparison_result_is_greater_or_equal_4',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_794_jump_to_subroutine_13']
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x97fe]
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0x9831]
    },
    {
        "identifier": 'ACTION_794_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'ACTION_794_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_794_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_794_set_random_0']
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_9',
        "command": 'jump_to_subroutine',
        "args": [0x980a]
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_10',
        "command": 'jump_to_subroutine',
        "args": [0x9831]
    },
    {
        "identifier": 'ACTION_794_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'ACTION_794_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_794_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_794_set_random_0']
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_13',
        "command": 'jump_to_subroutine',
        "args": [0x9804]
    },
    {
        "identifier": 'ACTION_794_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x9831]
    },
    {
        "identifier": 'ACTION_794_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'ACTION_794_shift_northeast_pixels_29']
    },
    {
        "identifier": 'ACTION_794_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_794_set_random_0']
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_794_walk_1_step_northeast_19',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_794_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_794_walk_1_step_northeast_23',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_794_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_794_walk_1_step_northeast_27',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_794_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_794_shift_northeast_pixels_29',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_794_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 4, 'ACTION_794_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_794_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_794_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_794_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_794_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_794_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_794_set_animation_speed_39']
    },
    {
        "identifier": 'ACTION_794_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_794_shift_northeast_pixels_35',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_794_face_southwest_37',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_794_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_677_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_794_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_794_shift_northeast_pixels_40',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_794_ret_41',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_794_dec_short_42',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_794_ret_43',
        "command": 'ret'
    }
]