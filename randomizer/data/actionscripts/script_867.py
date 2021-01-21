from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_867_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_867_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_867_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_867_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_867_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_867_ret_5',
        "command": 'ret'
    }
]
