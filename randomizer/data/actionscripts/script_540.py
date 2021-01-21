from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_540_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_540_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_540_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_540_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_540_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_540_jump_to_height_5',
        "command": 'jump_to_height',
        "args": [144]
    },
    {
        "identifier": 'ACTION_540_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_540_pause_7',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_540_fixed_f_coord_on_8',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_540_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_540_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_540_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_540_ret_12',
        "command": 'ret'
    }
]
