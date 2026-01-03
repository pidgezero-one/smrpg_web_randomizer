
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_492_db_0',
        "command": 'jmp_if_object_within_range_same_z',
        "args": [AreaObjects.MARIO, 0, 6, 'ACTION_492_set_bit_3']
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
