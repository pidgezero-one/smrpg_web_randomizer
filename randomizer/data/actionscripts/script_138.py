from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_138_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_138_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_138_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_138_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_138_shift_northwest_pixels_4',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_138_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_138_pause_6',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_138_walk_1_step_southeast_7',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_138_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_138_pause_9',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_138_walk_1_step_northwest_10',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_138_face_southwest_11',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_138_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_138_pause_6']
    }
]
