from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_381_pause_0',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_381_face_southeast_1',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_381_pause_2',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_381_face_northwest_3',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_381_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_381_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_381_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_381_add_z_coord_1_step_7',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_381_dec_z_coord_1_step_8',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_381_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_381_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_381_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_381_floating_on_12',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_381_shift_southwest_steps_13',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_381_ret_14',
        "command": 'ret'
    }
]
