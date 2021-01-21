from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_282_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_282_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_282_inc_palette_row_by_2',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_282_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_282_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_282_shift_southwest_pixels_5',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_282_object_memory_set_bit_6',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_282_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_282_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_282_ret_9',
        "command": 'ret'
    }
]
