from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_56_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_56_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [302, 'ACTION_56_set_vram_priority_9']
    },
    {
        "identifier": 'ACTION_56_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [303, 'ACTION_56_set_vram_priority_9']
    },
    {
        "identifier": 'ACTION_56_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_56_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7055, 1, 'ACTION_56_set_700C_to_current_level_0']
    },
    {
        "identifier": 'ACTION_56_set_vram_priority_5',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_56_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_56_clear_solidity_bits_7',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_56_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_56_set_vram_priority_9',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_56_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 2, 'ACTION_56_set_solidity_bits_14']
    },
    {
        "identifier": 'ACTION_56_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_56_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_56_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_56_set_vram_priority_9']
    },
    {
        "identifier": 'ACTION_56_set_solidity_bits_14',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_56_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_56_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_56_ret_17',
        "command": 'ret'
    }
]
