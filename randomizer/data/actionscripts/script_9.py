from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_9_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7055, 2, 'ACTION_9_visibility_on_4']
    },
    {
        "identifier": 'ACTION_9_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_9_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_9_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_9_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_9_sequence_looping_off_5',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_9_ret_6',
        "command": 'ret'
    }
]
