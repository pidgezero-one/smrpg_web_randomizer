from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_996_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_996_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_996_shift_southwest_steps_2',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_996_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_996_shift_northeast_steps_4',
        "command": 'shift_northeast_steps',
        "args": [11]
    },
    {
        "identifier": 'ACTION_996_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_996_shift_southwest_steps_6',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_996_face_northeast_7',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_996_fixed_f_coord_on_8',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_996_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_996_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_996_shift_southwest_steps_11',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_996_fixed_f_coord_off_12',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_996_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_996_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_996_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_996_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_996_set_animation_speed_0']
    }
]
