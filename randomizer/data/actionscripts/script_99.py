from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_99_floating_on_0',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_99_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_99_jump_to_height_silent_2',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_99_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_99_db_4',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x83, 0x18]
    },
    {
        "identifier": 'ACTION_99_floating_off_5',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_99_clear_solidity_bits_6',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_99_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_99_ret_9']
    },
    {
        "identifier": 'ACTION_99_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_99_floating_on_0']
    },
    {
        "identifier": 'ACTION_99_ret_9',
        "command": 'ret'
    }
]
