from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_500_db_0',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_500_db_1',
        "command": 'db',
        "args": [0x24, 0x20, 0x00, 0xf0, 0xff]
    },
    {
        "identifier": 'ACTION_500_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_500_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_500_pause_2']
    }
]
