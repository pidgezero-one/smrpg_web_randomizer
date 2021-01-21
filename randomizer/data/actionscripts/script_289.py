from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_289_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_289_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[]]
    },
    {
        "identifier": 'ACTION_289_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_289_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_289_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_289_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'ACTION_289_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_289_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_289_pause_8',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_289_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_289_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_289_sequence_looping_on_11',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_289_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_289_clear_solidity_bits_13',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_289_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x700c, 0x703e]
    },
    {
        "identifier": 'ACTION_289_face_east_15',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_289_ret_16',
        "command": 'ret'
    }
]
