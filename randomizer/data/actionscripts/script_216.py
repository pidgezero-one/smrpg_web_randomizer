from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_216_jmp_if_random_above_128_0',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_216_set_animation_speed_3']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_set_6',
        "command": 'set',
        "args": [0x700c, 3]
    },
    {
        "identifier": 'ACTION_216_shift_z_20_steps_7',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_216_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_216_jmp_if_bit_set_21']
    },
    {
        "identifier": 'ACTION_216_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_216_turn_clockwise_45_degrees_n_times_12']
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_10',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_216_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_216_pause_13']
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_12',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_216_pause_13',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_216_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_216_set_animation_speed_17']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_216_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_216_turn_clockwise_45_degrees_n_times_28']
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_22',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_216_pause_23',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_24',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_216_pause_25',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_216_set_bit_26',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_216_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_28',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_216_pause_29',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_216_turn_clockwise_45_degrees_n_times_30',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_216_pause_31',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_216_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_216_jmp_33',
        "command": 'jmp',
        "args": ['ACTION_216_set_6']
    }
]
