from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_920_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._117_SPINNING_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_920_set_700C_to_object_coord_1',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F]
    },
    {
        "identifier": 'ACTION_920_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 7, 'ACTION_920_set_sprite_sequence_14']
    },
    {
        "identifier": 'ACTION_920_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_920_set_sprite_sequence_14']
    },
    {
        "identifier": 'ACTION_920_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_920_object_memory_set_bit_5',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_920_clear_solidity_bits_6',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_920_pause_7',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'ACTION_920_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._117_SPINNING_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_920_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_920_pause_10',
        "command": 'pause',
        "args": [36]
    },
    {
        "identifier": 'ACTION_920_object_memory_clear_bit_11',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_920_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_920_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_920_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_920_object_memory_set_bit_15',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_920_clear_solidity_bits_16',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_920_pause_17',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_920_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_920_pause_19',
        "command": 'pause',
        "args": [36]
    },
    {
        "identifier": 'ACTION_920_object_memory_clear_bit_20',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_920_set_solidity_bits_21',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_920_ret_22',
        "command": 'ret'
    }
]
