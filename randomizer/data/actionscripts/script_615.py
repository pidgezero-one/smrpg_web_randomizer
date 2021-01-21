from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_615_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 2, 'ACTION_615_visibility_off_3']
    },
    {
        "identifier": 'ACTION_615_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'ACTION_615_visibility_off_3']
    },
    {
        "identifier": 'ACTION_615_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_5_turn_random_direction_0']
    },
    {
        "identifier": 'ACTION_615_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_615_object_memory_set_bit_4',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_615_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_615_ret_6',
        "command": 'ret'
    }
]
