from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_888_inc_palette_row_by_0',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_888_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_888_db_2',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x02, 0xf7, 0xa8]
    },
    {
        "identifier": 'ACTION_888_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_888_pause_1']
    },
    {
        "identifier": 'ACTION_888_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_888_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_888_inc_palette_row_by_6',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_888_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_881_set_solidity_bits_0']
    }
]
