from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_810_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'ACTION_810_set_animation_speed_9']
    },
    {
        "identifier": 'ACTION_810_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_810_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_810_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_810_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_810_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_810_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_810_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_810_floating_on_8',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_810_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_810_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_810_db_11',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_810_embedded_animation_routine_12',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_810_set_13',
        "command": 'set',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_810_shift_z_20_steps_14',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_810_turn_clockwise_45_degrees_n_times_15',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_810_pause_16',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_810_turn_clockwise_45_degrees_n_times_17',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_810_pause_18',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_810_turn_clockwise_45_degrees_n_times_19',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_810_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_810_jmp_22']
    },
    {
        "identifier": 'ACTION_810_pause_21',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_810_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_810_set_13']
    }
]
