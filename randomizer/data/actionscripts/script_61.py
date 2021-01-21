from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_61_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_61_set_priority_1',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_61_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_61_mem_700C_and_const_3',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_61_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_61_pause_8']
    },
    {
        "identifier": 'ACTION_61_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_61_pause_9']
    },
    {
        "identifier": 'ACTION_61_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 3, 'ACTION_61_pause_10']
    },
    {
        "identifier": 'ACTION_61_pause_7',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_61_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_61_pause_9',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_61_pause_10',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_61_shift_f_direction_steps_11',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_61_pause_12',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_61_turn_clockwise_45_degrees_n_times_13',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_61_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_61_object_memory_set_bit_0']
    },
    {
        "identifier": 'ACTION_61_pause_15',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_61_turn_clockwise_45_degrees_n_times_16',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_61_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_61_object_memory_set_bit_0']
    }
]
