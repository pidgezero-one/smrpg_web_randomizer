from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_336_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_336_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_336_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_336_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_336_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_336_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_336_jmp_if_var_equals_byte_6',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 2, 'ACTION_336_pause_5']
    },
    {
        "identifier": 'ACTION_336_db_7',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x01, 0xb4, 0x3d]
    },
    {
        "identifier": 'ACTION_336_db_8',
        "command": 'db',
        "args": [0x3a, 0x14, 0xd0, 0x00, 0xb4, 0x3d]
    },
    {
        "identifier": 'ACTION_336_dec_9',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_336_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_336_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_336_object_memory_clear_bit_12',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_336_set_vram_priority_13',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_336_set_solidity_bits_14',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_336_ret_15',
        "command": 'ret'
    }
]
