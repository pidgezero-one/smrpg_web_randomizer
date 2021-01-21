from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_993_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_993_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_993_face_southwest_3',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_993_fixed_f_coord_on_4',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_993_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_993_fixed_f_coord_off_8',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_993_face_northeast_9',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_993_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_993_shift_northeast_steps_15',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_993_shift_southeast_steps_16',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_993_shift_southwest_steps_17',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_993_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_993_shift_southwest_steps_20',
        "command": 'shift_southwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_993_shift_northwest_steps_21',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_993_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_993_shift_northeast_steps_2']
    }
]
