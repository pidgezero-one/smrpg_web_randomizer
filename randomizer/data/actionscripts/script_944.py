from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_944_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_944_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_944_db_2',
        "command": 'db',
        "args": [0xc8, 0x87]
    },
    {
        "identifier": 'ACTION_944_set_short_3',
        "command": 'set_short',
        "args": [0x701a, 0x000d]
    },
    {
        "identifier": 'ACTION_944_db_4',
        "command": 'db',
        "args": [0x98]
    },
    {
        "identifier": 'ACTION_944_walk_to_xy_coords_5',
        "command": 'walk_to_xy_coords',
        "args": [3, 82]
    },
    {
        "identifier": 'ACTION_944_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_944_walk_to_xy_coords_7',
        "command": 'walk_to_xy_coords',
        "args": [6, 81]
    },
    {
        "identifier": 'ACTION_944_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_944_walk_to_xy_coords_9',
        "command": 'walk_to_xy_coords',
        "args": [7, 82]
    },
    {
        "identifier": 'ACTION_944_ret_10',
        "command": 'ret'
    }
]
