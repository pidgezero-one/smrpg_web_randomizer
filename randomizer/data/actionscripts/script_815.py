from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_815_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'ACTION_815_set_animation_speed_6']
    },
    {
        "identifier": 'ACTION_815_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_815_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_815_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_815_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_815_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_815_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_815_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_815_db_8',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_815_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_815_set_10',
        "command": 'set',
        "args": [0x700c, 6]
    },
    {
        "identifier": 'ACTION_815_shift_z_20_steps_11',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_815_turn_clockwise_45_degrees_n_times_12',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_815_pause_13',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_815_turn_clockwise_45_degrees_n_times_14',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_815_pause_15',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_815_jmp_if_random_above_128_16',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_815_jmp_18']
    },
    {
        "identifier": 'ACTION_815_pause_17',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_815_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_815_set_10']
    }
]
