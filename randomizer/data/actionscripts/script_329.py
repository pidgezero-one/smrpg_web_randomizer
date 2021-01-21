from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_329_set_solidity_bits_0',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_329_floating_on_1',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_329_face_southwest_2',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_329_transfer_to_xyzf_3',
        "command": 'transfer_to_xyzf',
        "args": [7, 59, 3, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_329_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_329_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_329_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_329_walk_1_step_southwest_7',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_329_walk_1_step_southeast_8',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_329_transfer_to_xyzf_9',
        "command": 'transfer_to_xyzf',
        "args": [6, 88, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_329_clear_solidity_bits_10',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_329_floating_off_11',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_329_set_bit_12',
        "command": 'set_bit',
        "args": [0x704c, 2]
    },
    {
        "identifier": 'ACTION_329_ret_13',
        "command": 'ret'
    }
]
