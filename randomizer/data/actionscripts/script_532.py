from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_532_db_0',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_532_embedded_animation_routine_1',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_southwest_steps_4',
        "command": 'shift_southwest_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_532_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_532_face_southeast_12',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_532_pause_13',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_532_face_northeast_14',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_532_pause_15',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_northeast_steps_18',
        "command": 'shift_northeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_northeast_steps_21',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_532_set_animation_speed_23',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_532_shift_northeast_steps_24',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_532_pause_25',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_532_face_northwest_26',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_532_pause_27',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_532_face_southwest_28',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_532_pause_29',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_532_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_532_set_animation_speed_2']
    }
]
