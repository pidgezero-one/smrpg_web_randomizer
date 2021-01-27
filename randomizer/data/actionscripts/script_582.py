from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_582_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_582_pause_1',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_582_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_582_pause_3',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_582_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_582_ret_5',
        "command": 'ret'
    }
]
