from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_662_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_662_transfer_to_xyzf_1',
        "command": 'transfer_to_xyzf',
        "args": [15, 55, 2, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_662_face_southeast_2',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_662_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_662_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_662_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_662_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_662_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_662_walk_1_step_northeast_8',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_662_face_southwest_9',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_662_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_662_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_662_ret_12',
        "command": 'ret'
    }
]
