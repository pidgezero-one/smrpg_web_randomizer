from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_809_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_809_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [117, 'ACTION_809_db_6']
    },
    {
        "identifier": 'ACTION_809_db_2',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_809_db_3',
        "command": 'db',
        "args": [0x24, 0x00, 0xfe, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_809_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_809_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_809_pause_4']
    },
    {
        "identifier": 'ACTION_809_db_6',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_809_db_7',
        "command": 'db',
        "args": [0x24, 0x00, 0x02, 0x00, 0x01]
    },
    {
        "identifier": 'ACTION_809_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_809_pause_4']
    }
]
