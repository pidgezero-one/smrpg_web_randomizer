from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_573_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_573_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_573_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_573_ret_3',
        "command": 'ret'
    }
]
