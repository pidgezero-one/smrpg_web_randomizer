from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_34_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'ACTION_34_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_34_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_34_face_northeast_29']
    },
    {
        "identifier": 'ACTION_34_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_34_face_northeast_20']
    },
    {
        "identifier": 'ACTION_34_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_34_face_northeast_11']
    },
    {
        "identifier": 'ACTION_34_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_34_jump_to_subroutine_5',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_34_set_priority_6',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_set_priority_8',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_shift_southwest_steps_9',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_34_face_northeast_11',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_34_jump_to_subroutine_12',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_13',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northwest_14',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_34_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_34_set_priority_16',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_southeast_17',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_18',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_34_face_northeast_20',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_34_jump_to_subroutine_21',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_22',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_southeast_23',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_34_set_priority_24',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_shift_southwest_steps_25',
        "command": 'shift_southwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northwest_26',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_27',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_34_face_northeast_29',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_34_jump_to_subroutine_30',
        "command": 'jump_to_subroutine',
        "args": [0x0cc4]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_31',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northwest_32',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_34_shift_southwest_steps_33',
        "command": 'shift_southwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northwest_34',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_34_shift_northeast_steps_35',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_southeast_36',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_37',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_set_priority_38',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_start_loop_n_times_39',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_southeast_40',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northeast_41',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_34_end_loop_42',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_34_shift_northeast_steps_43',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_set_priority_44',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_walk_1_step_northwest_45',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_southwest_46',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_34_jmp_47',
        "command": 'jmp',
        "args": ['ACTION_32_shift_z_up_steps_20']
    },
    {
        "identifier": 'ACTION_34_clear_solidity_bits_48',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_34_set_short_49',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'ACTION_34_set_animation_speed_50',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_34_set_700C_to_pressed_button_51',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_34_dec_short_mem_52',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_34_mem_700C_and_const_53',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_34_jmp_if_var_not_equals_short_54',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 0, 'ACTION_34_load_mem_60']
    },
    {
        "identifier": 'ACTION_34_db_55',
        "command": 'db',
        "args": [0xc8, 0x07]
    },
    {
        "identifier": 'ACTION_34_add_short_56',
        "command": 'add_short',
        "args": [0x701a, 0x0080]
    },
    {
        "identifier": 'ACTION_34_add_short_57',
        "command": 'add_short',
        "args": [0x7016, 0x0040]
    },
    {
        "identifier": 'ACTION_34_db_58',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_34_jmp_59',
        "command": 'jmp',
        "args": ['ACTION_34_visibility_on_65']
    },
    {
        "identifier": 'ACTION_34_load_mem_60',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_34_pause_61',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_34_end_loop_62',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_34_pause_63',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_34_set_animation_speed_64',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_34_visibility_on_65',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_34_set_priority_66',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_add_z_coord_1_step_67',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_34_walk_1_step_f_direction_68',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_34_set_700C_to_object_coord_69',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_34_mem_compare_70',
        "command": 'mem_compare',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_34_jmp_if_comparison_result_is_lesser_71',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_34_set_priority_74']
    },
    {
        "identifier": 'ACTION_34_set_priority_72',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_34_jmp_73',
        "command": 'jmp',
        "args": ['ACTION_34_dec_z_coord_1_step_75']
    },
    {
        "identifier": 'ACTION_34_set_priority_74',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_34_dec_z_coord_1_step_75',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_34_set_solidity_bits_76',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_34_dec_z_coord_1_step_77',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_34_ret_78',
        "command": 'ret'
    }
]
