from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_883_inc_palette_row_by_0',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_883_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_883_db_2',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x02, 0x18, 0xa8]
    },
    {
        "identifier": 'ACTION_883_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_883_pause_1']
    },
    {
        "identifier": 'ACTION_883_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_883_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_883_inc_palette_row_by_6',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_883_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_881_set_solidity_bits_0']
    }
]
