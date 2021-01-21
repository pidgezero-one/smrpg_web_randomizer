from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_685_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_685_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_685_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_685_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_685_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_685_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_685_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_685_shift_southwest_pixels_7',
        "command": 'shift_southwest_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_685_walk_1_step_northwest_8',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_685_face_southeast_9',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_685_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_685_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_685_ret_12',
        "command": 'ret'
    }
]
