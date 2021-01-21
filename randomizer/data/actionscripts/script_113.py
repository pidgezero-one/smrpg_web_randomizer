from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_113_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_113_shift_west_pixels_4']
    },
    {
        "identifier": 'ACTION_113_face_northeast_1',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_113_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_113_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_113_shift_west_pixels_4',
        "command": 'shift_west_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_113_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_113_shift_east_pixels_6',
        "command": 'shift_east_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_113_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_113_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_113_shift_west_pixels_4']
    }
]
