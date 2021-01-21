from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_474_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_474_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_474_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 78, 'ACTION_474_set_priority_27']
    },
    {
        "identifier": 'ACTION_474_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_474_add_4',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_474_load_mem_5',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_474_pause_6',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_474_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_474_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_474_shift_f_direction_steps_9',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_pause_10',
        "command": 'pause',
        "args": [21]
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_11',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_walk_1_step_f_direction_12',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_13',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_shift_f_direction_steps_14',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_pause_15',
        "command": 'pause',
        "args": [37]
    },
    {
        "identifier": 'ACTION_474_start_loop_n_times_16',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_17',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_474_walk_1_step_f_direction_18',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_19',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_474_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_pause_21',
        "command": 'pause',
        "args": [21]
    },
    {
        "identifier": 'ACTION_474_end_loop_22',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_23',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_walk_1_step_f_direction_24',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_474_turn_clockwise_45_degrees_n_times_25',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_474_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_474_set_animation_speed_8']
    },
    {
        "identifier": 'ACTION_474_set_priority_27',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_474_clear_solidity_bits_28',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_474_set_solidity_bits_29',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_474_visibility_on_30',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_474_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_474_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_474_set_700C_to_pressed_button_33',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_474_add_34',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_474_load_mem_35',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_474_pause_36',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_474_end_loop_37',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_474_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_714_turn_clockwise_45_degrees_12']
    }
]
