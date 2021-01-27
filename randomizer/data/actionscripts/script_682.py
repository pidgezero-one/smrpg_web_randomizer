from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_682_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [1]]
    },
    {
        "identifier": 'ACTION_682_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_682_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_682_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_682_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_682_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_682_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_682_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_682_face_northeast_8',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_682_pause_9',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_682_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_656_set_object_memory_bits_0']
    }
]
