from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_21_set_0',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'ACTION_21_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_21_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_21_inc_3',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_inc_4',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_21_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_21_turn_random_direction_9']
    },
    {
        "identifier": 'ACTION_21_walk_1_step_northwest_7',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_21_dec_8',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_turn_random_direction_9',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_21_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_21_walk_1_step_southeast_11',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_21_inc_12',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_jmp_if_random_above_66_13',
        "command": 'jmp_if_random_above_66',
        "args": [0x0a86, 'ACTION_21_set_animation_speed_29']
    },
    {
        "identifier": 'ACTION_21_pause_14',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_21_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_21_shift_southeast_steps_16',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_21_inc_17',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_inc_18',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_inc_19',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_jump_to_subroutine_20',
        "command": 'jump_to_subroutine',
        "args": [0x0acd]
    },
    {
        "identifier": 'ACTION_21_jmp_if_var_equals_byte_21',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 1, 'ACTION_21_pause_32']
    },
    {
        "identifier": 'ACTION_21_turn_random_direction_22',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_21_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_21_shift_northwest_steps_24',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_21_dec_25',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_dec_26',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_jmp_if_random_above_128_27',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_21_pause_32']
    },
    {
        "identifier": 'ACTION_21_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_21_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_21_walk_1_step_northwest_30',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_21_dec_31',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_pause_32',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_21_shift_northwest_steps_33',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_21_dec_34',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_dec_35',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_dec_36',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_jump_to_subroutine_37',
        "command": 'jump_to_subroutine',
        "args": [0x0acd]
    },
    {
        "identifier": 'ACTION_21_jmp_if_var_equals_byte_38',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 2, 'ACTION_21_pause_14']
    },
    {
        "identifier": 'ACTION_21_jmp_39',
        "command": 'jmp',
        "args": ['ACTION_21_set_0']
    },
    {
        "identifier": 'ACTION_21_set_700C_to_70A0_short_mem_40',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_21_set_7000_short_mem_to_700C_41',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_21_mem_compare_42',
        "command": 'mem_compare',
        "args": [0x702c, 28]
    },
    {
        "identifier": 'ACTION_21_jmp_if_comparison_result_is_greater_or_equal_43',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_21_set_48']
    },
    {
        "identifier": 'ACTION_21_mem_compare_44',
        "command": 'mem_compare',
        "args": [0x702c, 13]
    },
    {
        "identifier": 'ACTION_21_jmp_if_comparison_result_is_lesser_45',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_21_set_51']
    },
    {
        "identifier": 'ACTION_21_set_46',
        "command": 'set',
        "args": [0x70af, 0]
    },
    {
        "identifier": 'ACTION_21_ret_47',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_21_set_48',
        "command": 'set',
        "args": [0x70af, 1]
    },
    {
        "identifier": 'ACTION_21_set_49',
        "command": 'set',
        "args": [0x70ae, 23]
    },
    {
        "identifier": 'ACTION_21_ret_50',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_21_set_51',
        "command": 'set',
        "args": [0x70af, 2]
    },
    {
        "identifier": 'ACTION_21_set_52',
        "command": 'set',
        "args": [0x70ae, 17]
    },
    {
        "identifier": 'ACTION_21_ret_53',
        "command": 'ret'
    }
]
