from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_683_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_683_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_683_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_683_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_683_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_683_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_683_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_683_face_northeast_7',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_683_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_683_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_676_set_object_memory_bits_0']
    }
]
