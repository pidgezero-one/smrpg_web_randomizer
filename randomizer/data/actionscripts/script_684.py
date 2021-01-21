from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_684_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_684_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_684_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_684_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_684_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_684_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_684_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_684_shift_southwest_pixels_7',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_684_face_southeast_8',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_684_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_684_ret_10',
        "command": 'ret'
    }
]
