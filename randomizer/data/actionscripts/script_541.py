from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_541_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_541_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_541_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_541_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_541_shift_southwest_steps_9',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_541_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_541_pause_13',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_541_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_541_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_541_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_541_ret_18',
        "command": 'ret'
    }
]
