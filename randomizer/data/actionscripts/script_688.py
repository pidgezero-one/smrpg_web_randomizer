from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_688_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_688_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_688_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_688_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_688_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_southeast_steps_8']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_6',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_southeast_steps_8']
    },
    {
        "identifier": 'ACTION_688_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_southeast_steps_8',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_southwest_steps_12']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_10',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_southwest_steps_12']
    },
    {
        "identifier": 'ACTION_688_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_southwest_steps_16']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_14',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_southwest_steps_16']
    },
    {
        "identifier": 'ACTION_688_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_southwest_steps_16',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northwest_steps_20']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_18',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northwest_steps_20']
    },
    {
        "identifier": 'ACTION_688_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northwest_steps_20',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_688_shift_southwest_steps_21',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_southwest_steps_25']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_23',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_southwest_steps_25']
    },
    {
        "identifier": 'ACTION_688_set_bit_24',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_southwest_steps_25',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_688_shift_northeast_steps_26',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northeast_steps_30']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_28',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northeast_steps_30']
    },
    {
        "identifier": 'ACTION_688_set_bit_29',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northeast_steps_30',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_southeast_steps_34']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_32',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_southeast_steps_34']
    },
    {
        "identifier": 'ACTION_688_set_bit_33',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_southeast_steps_34',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_35',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northeast_steps_38']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_36',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northeast_steps_38']
    },
    {
        "identifier": 'ACTION_688_set_bit_37',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northeast_steps_38',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northeast_steps_42']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_40',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northeast_steps_42']
    },
    {
        "identifier": 'ACTION_688_set_bit_41',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northeast_steps_42',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northwest_steps_46']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_44',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northwest_steps_46']
    },
    {
        "identifier": 'ACTION_688_set_bit_45',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northwest_steps_46',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_shift_northwest_steps_50']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_48',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_shift_northwest_steps_50']
    },
    {
        "identifier": 'ACTION_688_set_bit_49',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_shift_northwest_steps_50',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_688_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'ACTION_688_jmp_54']
    },
    {
        "identifier": 'ACTION_688_jmp_if_random_above_66_52',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_688_jmp_54']
    },
    {
        "identifier": 'ACTION_688_set_bit_53',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_688_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_688_shift_southeast_steps_4']
    }
]
