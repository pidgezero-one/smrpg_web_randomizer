from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_492_db_0',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x06, 0xaf, 0x5e]
    },
    {
        "identifier": 'ACTION_492_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_492_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_492_db_0']
    },
    {
        "identifier": 'ACTION_492_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_492_ret_4',
        "command": 'ret'
    }
]
