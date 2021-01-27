from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_880_db_0',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_880_embedded_animation_routine_1',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80]
    },
    {
        "identifier": 'ACTION_880_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_880_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_880_pause_2']
    }
]
