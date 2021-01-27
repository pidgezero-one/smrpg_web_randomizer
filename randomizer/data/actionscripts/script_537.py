from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_537_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_537_face_southeast_1',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_537_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_537_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_537_pause_6',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_537_fixed_f_coord_off_7',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_537_shift_southeast_steps_8',
        "command": 'shift_southeast_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_537_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_537_shift_southeast_steps_14',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_537_pause_15',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_537_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_537_shift_northwest_steps_18',
        "command": 'shift_northwest_steps',
        "args": [11]
    },
    {
        "identifier": 'ACTION_537_shift_northeast_steps_19',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_537_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_537_ret_21',
        "command": 'ret'
    }
]