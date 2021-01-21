from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_865_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_865_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_865_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_865_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_865_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_865_ret_5',
        "command": 'ret'
    }
]
