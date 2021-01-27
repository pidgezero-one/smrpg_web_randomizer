from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_273_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_273_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_273_set_sprite_sequence_8']
    },
    {
        "identifier": 'ACTION_273_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_273_set_sprite_sequence_8']
    },
    {
        "identifier": 'ACTION_273_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_273_object_memory_set_bit_4',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_273_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_273_pause_short_6',
        "command": 'pause_short',
        "args": [360]
    },
    {
        "identifier": 'ACTION_273_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_272_play_sound_17']
    },
    {
        "identifier": 'ACTION_273_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_273_object_memory_set_bit_9',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_273_clear_solidity_bits_10',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_273_pause_short_11',
        "command": 'pause_short',
        "args": [360]
    },
    {
        "identifier": 'ACTION_273_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_272_play_sound_42']
    }
]
