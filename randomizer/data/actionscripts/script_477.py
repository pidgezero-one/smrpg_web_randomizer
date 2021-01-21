from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_477_db_0',
        "command": 'db',
        "args": [0x20, 0x00]
    },
    {
        "identifier": 'ACTION_477_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_477_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_477_pause_1']
    }
]
