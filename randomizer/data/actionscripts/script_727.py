from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_727_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70df, 50, 'ACTION_727_set_animation_speed_11']
    },
    {
        "identifier": 'ACTION_727_pause_1',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_727_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_727_pause_1']
    },
    {
        "identifier": 'ACTION_727_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_727_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_727_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_727_pause_1']
    },
    {
        "identifier": 'ACTION_727_walk_1_step_f_direction_6',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_727_face_mario_7',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_727_walk_1_step_f_direction_8',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_727_face_mario_9',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_727_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_727_pause_1']
    },
    {
        "identifier": 'ACTION_727_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_727_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_727_walk_1_step_f_direction_13',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_727_jump_to_height_silent_14',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_727_face_mario_15',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_727_jmp_if_random_above_66_16',
        "command": 'jmp_if_random_above_66',
        "args": [0x8778, 'ACTION_727_turn_clockwise_45_degrees_n_times_20']
    },
    {
        "identifier": 'ACTION_727_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_727_pause_1']
    },
    {
        "identifier": 'ACTION_727_turn_clockwise_45_degrees_n_times_18',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_727_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_727_pause_1']
    },
    {
        "identifier": 'ACTION_727_turn_clockwise_45_degrees_n_times_20',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_727_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_727_pause_1']
    }
]
