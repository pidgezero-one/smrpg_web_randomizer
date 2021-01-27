from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_354_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_354_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_354_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_354_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_354_face_northeast_20']
    },
    {
        "identifier": 'ACTION_354_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_354_set_solidity_bits_30']
    },
    {
        "identifier": 'ACTION_354_set_solidity_bits_5',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
    },
    {
        "identifier": 'ACTION_354_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_354_set_object_memory_bits_7',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [1]]
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_354_add_z_coord_1_step_9',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_354_start_loop_n_times_10',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_354_turn_clockwise_45_degrees_n_times_11',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_354_walk_1_step_f_direction_12',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_354_pause_13',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_354_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_354_end_loop_16']
    },
    {
        "identifier": 'ACTION_354_pause_15',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_354_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_354_dec_z_coord_1_step_17',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_354_pause_18',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_354_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_354_set_object_memory_bits_7']
    },
    {
        "identifier": 'ACTION_354_face_northeast_20',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_354_shift_z_up_steps_22',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_354_shift_z_down_steps_23',
        "command": 'shift_z_down_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_354_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_354_set_solidity_bits_30']
    },
    {
        "identifier": 'ACTION_354_dec_z_coord_1_step_25',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_354_shift_f_direction_steps_27',
        "command": 'shift_f_direction_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_354_turn_clockwise_45_degrees_n_times_28',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_354_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_354_set_animation_speed_21']
    },
    {
        "identifier": 'ACTION_354_set_solidity_bits_30',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_354_set_solidity_bits_31',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_354_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_354_turn_clockwise_45_degrees_34',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_354_shift_f_direction_steps_35',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_354_set_700C_to_object_coord_36',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_354_mem_compare_val_37',
        "command": 'mem_compare_val',
        "args": [3072]
    },
    {
        "identifier": 'ACTION_354_jmp_if_comparison_result_is_lesser_38',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_354_set_animation_speed_42']
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_354_end_loop_40',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_354_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_354_set_animation_speed_32']
    },
    {
        "identifier": 'ACTION_354_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_354_shift_southeast_steps_43',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_354_shift_northeast_steps_44',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_354_jmp_45',
        "command": 'jmp',
        "args": ['ACTION_354_set_animation_speed_32']
    }
]
