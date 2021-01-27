from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_194_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_194_pause_1',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_194_db_2',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x04, 0xea, 0x26]
    },
    {
        "identifier": 'ACTION_194_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_194_pause_1']
    },
    {
        "identifier": 'ACTION_194_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_194_pause_5',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_194_db_6',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x04, 0xed, 0x26]
    },
    {
        "identifier": 'ACTION_194_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_194_set_sprite_sequence_0']
    }
]
