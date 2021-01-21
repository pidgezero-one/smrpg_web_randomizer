from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_100_transfer_to_xyzf_0',
        "command": 'transfer_to_xyzf',
        "args": [20, 118, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_100_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_100_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_100_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_100_face_northwest_4',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_100_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_99_floating_on_0']
    }
]
