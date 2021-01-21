from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_995_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_995_shift_southwest_steps_2',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_995_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_995_shift_southwest_steps_8',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_995_shift_northwest_steps_9',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_995_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_995_shift_northeast_steps_13',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_995_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_995_shift_northeast_steps_16',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_995_shift_southeast_steps_17',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_995_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_995_shift_southwest_steps_2']
    }
]
