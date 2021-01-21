from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_79_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_79_floating_on_1',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_79_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_79_jump_to_height_silent_3',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_79_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_79_db_5',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x14, 0x16]
    },
    {
        "identifier": 'ACTION_79_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_79_jump_to_height_silent_3']
    }
]
