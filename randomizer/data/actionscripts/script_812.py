from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_812_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'ACTION_812_set_priority_9']
    },
    {
        "identifier": 'ACTION_812_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_812_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_812_db_3',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_812_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_812_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_812_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_812_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_812_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_812_set_priority_9',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_812_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_812_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_812_db_12',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_812_embedded_animation_routine_13',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_812_set_14',
        "command": 'set',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_812_shift_z_20_steps_15',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_812_turn_clockwise_45_degrees_n_times_16',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_812_pause_17',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_812_turn_clockwise_45_degrees_n_times_18',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_812_pause_19',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_812_turn_clockwise_45_degrees_n_times_20',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_812_jmp_if_random_above_128_21',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_812_pause_23']
    },
    {
        "identifier": 'ACTION_812_pause_22',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_812_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_812_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_812_set_14']
    }
]
