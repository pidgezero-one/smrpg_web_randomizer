from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_813_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 7, 'ACTION_813_set_animation_speed_6']
    },
    {
        "identifier": 'ACTION_813_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_813_db_2',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_813_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_813_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_813_face_northeast_5',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_813_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_813_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_813_db_8',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_813_embedded_animation_routine_9',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_813_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_813_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_813_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_128_set_object_memory_bits_0']
    }
]
