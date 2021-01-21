from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_994_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_994_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_994_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_994_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_994_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_994_face_southeast_8',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_994_fixed_f_coord_on_9',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_994_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_994_fixed_f_coord_off_13',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_994_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_994_shift_southwest_steps_16',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_994_shift_northwest_steps_17',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_994_shift_northeast_steps_18',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_994_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_994_set_animation_speed_0']
    }
]
