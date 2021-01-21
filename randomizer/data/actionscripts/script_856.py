from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_856_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_856_walk_1_step_southeast_1',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_856_shift_southwest_steps_2',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_856_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_856_shift_northeast_steps_4',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_856_walk_1_step_southeast_5',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_856_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_856_face_northeast_8']
    },
    {
        "identifier": 'ACTION_856_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_856_walk_1_step_southeast_1']
    },
    {
        "identifier": 'ACTION_856_face_northeast_8',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_856_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_856_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_856_ret_11',
        "command": 'ret'
    }
]
