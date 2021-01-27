from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_811_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'ACTION_811_set_animation_speed_7']
    },
    {
        "identifier": 'ACTION_811_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_811_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_811_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_811_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_811_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_811_face_northwest_6',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_811_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_811_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_811_db_9',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_811_embedded_animation_routine_10',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_811_set_11',
        "command": 'set',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_811_shift_z_20_steps_12',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_811_turn_clockwise_45_degrees_n_times_13',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_811_pause_14',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_811_turn_clockwise_45_degrees_n_times_15',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_811_pause_16',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_811_jmp_if_random_above_128_17',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_811_jmp_19']
    },
    {
        "identifier": 'ACTION_811_pause_18',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_811_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_811_set_11']
    }
]
