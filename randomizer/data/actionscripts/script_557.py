from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_557_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_557_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_557_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_557_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_557_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_northwest_steps_8']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_northwest_steps_8']
    },
    {
        "identifier": 'ACTION_557_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_northwest_steps_8',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_northeast_steps_12']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_10',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_northeast_steps_12']
    },
    {
        "identifier": 'ACTION_557_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_northeast_steps_16']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_northeast_steps_16']
    },
    {
        "identifier": 'ACTION_557_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_northeast_steps_20']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_18',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_northeast_steps_20']
    },
    {
        "identifier": 'ACTION_557_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_northeast_steps_20',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_557_shift_southeast_steps_21',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_southeast_steps_25']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_23',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_southeast_steps_25']
    },
    {
        "identifier": 'ACTION_557_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_southeast_steps_25',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_southwest_steps_29']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_27',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_southwest_steps_29']
    },
    {
        "identifier": 'ACTION_557_set_bit_28',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_southwest_steps_29',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_southwest_steps_33']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_31',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_southwest_steps_33']
    },
    {
        "identifier": 'ACTION_557_set_bit_32',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_southwest_steps_33',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_34',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_shift_southwest_steps_37']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_35',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_shift_southwest_steps_37']
    },
    {
        "identifier": 'ACTION_557_set_bit_36',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_shift_southwest_steps_37',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_557_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_557_jmp_41']
    },
    {
        "identifier": 'ACTION_557_jmp_if_random_above_128_39',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_557_jmp_41']
    },
    {
        "identifier": 'ACTION_557_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_557_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_557_shift_northwest_steps_4']
    }
]
