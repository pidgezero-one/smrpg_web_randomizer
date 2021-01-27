from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_332_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_332_pause_1',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_332_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_332_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_332_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_332_pause_5',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_332_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_332_pause_7',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_332_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_332_set_sprite_sequence_0']
    }
]
