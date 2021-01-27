from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_308_set_movement_bits_0',
        "command": 'set_movement_bits',
        "args": [[_0x0AFlags.BIT_0, _0x0AFlags.CANT_WALK_UNDER]]
    },
    {
        "identifier": 'ACTION_308_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_308_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_308_db_3',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_308_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x80, 0x00, 0x80]
    },
    {
        "identifier": 'ACTION_308_turn_random_direction_5',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_308_shift_f_direction_steps_6',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_308_face_mario_7',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_308_walk_1_step_f_direction_8',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_308_turn_random_direction_9',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_308_shift_f_direction_steps_10',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_308_db_11',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x04, 0xf1, 0x38]
    },
    {
        "identifier": 'ACTION_308_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_308_turn_random_direction_5']
    },
    {
        "identifier": 'ACTION_308_face_mario_13',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_308_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_308_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_308_walk_1_step_f_direction_16',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_308_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_308_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_308_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_308_turn_random_direction_5']
    }
]
