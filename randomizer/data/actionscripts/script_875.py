from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_875_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_875_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_875_shift_southeast_pixels_2',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_875_face_northwest_3',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_875_fixed_f_coord_off_4',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_875_ret_5',
        "command": 'ret'
    }
]
