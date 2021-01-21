from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_833_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_833_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_833_walk_to_xy_coords_2',
        "command": 'walk_to_xy_coords',
        "args": [20, 36]
    },
    {
        "identifier": 'ACTION_833_walk_to_xy_coords_3',
        "command": 'walk_to_xy_coords',
        "args": [11, 53]
    },
    {
        "identifier": 'ACTION_833_ret_4',
        "command": 'ret'
    }
]
