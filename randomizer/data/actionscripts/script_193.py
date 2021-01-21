from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_193_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_193_pause_1',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_193_db_2',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0xce, 0x26]
    },
    {
        "identifier": 'ACTION_193_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_193_pause_1']
    },
    {
        "identifier": 'ACTION_193_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_193_pause_5',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_193_db_6',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0xd1, 0x26]
    },
    {
        "identifier": 'ACTION_193_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_193_set_sprite_sequence_0']
    }
]
