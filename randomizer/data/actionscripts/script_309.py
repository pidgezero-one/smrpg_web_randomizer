from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_309_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_309_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_309_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_309_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_309_mem_700C_and_const_4',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_309_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_309_jmp_if_random_above_128_11']
    },
    {
        "identifier": 'ACTION_309_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_309_pause_10']
    },
    {
        "identifier": 'ACTION_309_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_309_pause_9']
    },
    {
        "identifier": 'ACTION_309_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_pause_9',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_pause_10',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_309_add_z_coord_1_step_15']
    },
    {
        "identifier": 'ACTION_309_dec_z_coord_1_step_12',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_309_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_309_dec_z_coord_1_step_12']
    },
    {
        "identifier": 'ACTION_309_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_309_set_700C_to_object_coord_17']
    },
    {
        "identifier": 'ACTION_309_add_z_coord_1_step_15',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_309_jmp_if_random_above_128_16',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_309_add_z_coord_1_step_15']
    },
    {
        "identifier": 'ACTION_309_set_700C_to_object_coord_17',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_309_mem_compare_18',
        "command": 'mem_compare',
        "args": [0x700c, 8]
    },
    {
        "identifier": 'ACTION_309_jmp_if_comparison_result_is_greater_or_equal_19',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_309_visibility_off_0']
    },
    {
        "identifier": 'ACTION_309_face_mario_20',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_309_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._044_GHOST_FLOAT, 4]
    },
    {
        "identifier": 'ACTION_309_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_visibility_on_23',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_309_pause_24',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_309_visibility_off_25',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_309_pause_26',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_309_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_309_object_memory_clear_bit_28',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_309_set_solidity_bits_29',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_309_visibility_on_30',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_309_sequence_looping_on_31',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_309_shift_f_direction_steps_32',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_309_jmp_if_random_above_128_33',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_309_sequence_looping_on_31']
    },
    {
        "identifier": 'ACTION_309_start_loop_n_times_34',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_turn_random_direction_35',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_309_pause_36',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_309_end_loop_37',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_309_object_memory_set_bit_38',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_309_clear_solidity_bits_39',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_309_start_loop_n_times_40',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_309_visibility_off_41',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_309_pause_42',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_309_visibility_on_43',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_309_pause_44',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_309_end_loop_45',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_309_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_309_visibility_off_0']
    }
]
