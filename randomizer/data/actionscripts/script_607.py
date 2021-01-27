from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_607_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_607_add_1',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_607_load_mem_2',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_607_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_607_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_607_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_607_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_607_jmp_if_random_above_128_7',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_607_pause_12']
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_8',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_607_walk_1_step_f_direction_9',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_607_pause_10',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_607_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_607_jmp_if_random_above_128_7']
    },
    {
        "identifier": 'ACTION_607_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_607_jmp_if_random_above_66_13',
        "command": 'jmp_if_random_above_66',
        "args": [0x6e99, 'ACTION_607_set_700C_to_pressed_button_25']
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_14',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_607_pause_15',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_16',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_607_pause_17',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_18',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_607_pause_19',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_20',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_21',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_607_walk_1_step_f_direction_22',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_607_pause_23',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_607_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_607_jmp_if_random_above_128_7']
    },
    {
        "identifier": 'ACTION_607_set_700C_to_pressed_button_25',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_607_mem_compare_val_26',
        "command": 'mem_compare_val',
        "args": [25]
    },
    {
        "identifier": 'ACTION_607_jmp_if_comparison_result_is_lesser_27',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_607_start_loop_n_times_31']
    },
    {
        "identifier": 'ACTION_607_set_sprite_sequence_28',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_607_pause_29',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_607_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_607_jmp_if_random_above_128_7']
    },
    {
        "identifier": 'ACTION_607_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_607_turn_clockwise_45_degrees_n_times_32',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_607_pause_33',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_607_end_loop_34',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_607_jmp_35',
        "command": 'jmp',
        "args": ['ACTION_607_jmp_if_random_above_128_7']
    }
]
