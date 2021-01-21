from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_271_reset_properties_0',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_271_pause_3',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_271_turn_clockwise_45_degrees_n_times_4',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_271_jmp_if_random_above_66_5',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_271_face_mario_8']
    },
    {
        "identifier": 'ACTION_271_walk_1_step_f_direction_6',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_271_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_271_pause_3']
    },
    {
        "identifier": 'ACTION_271_face_mario_8',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_271_walk_1_step_f_direction_11',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_271_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_271_face_mario_8']
    },
    {
        "identifier": 'ACTION_271_pause_13',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_271_jmp_if_random_above_128_14',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_271_face_mario_18']
    },
    {
        "identifier": 'ACTION_271_pause_15',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_271_turn_clockwise_45_degrees_n_times_16',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_271_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_271_face_mario_8']
    },
    {
        "identifier": 'ACTION_271_face_mario_18',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_271_walk_1_step_f_direction_19',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_271_db_20',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x03, 0x11, 0x31]
    },
    {
        "identifier": 'ACTION_271_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_271_reset_properties_0']
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_271_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_271_face_mario_24',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_271_walk_1_step_f_direction_25',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_271_jmp_if_random_above_128_26',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_271_face_mario_18']
    },
    {
        "identifier": 'ACTION_271_pause_27',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_271_db_28',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x02, 0x25, 0x31]
    },
    {
        "identifier": 'ACTION_271_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_271_face_mario_18']
    },
    {
        "identifier": 'ACTION_271_jump_to_height_30',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_271_jmp_31',
        "command": 'jmp',
        "args": ['ACTION_271_set_animation_speed_22']
    }
]
