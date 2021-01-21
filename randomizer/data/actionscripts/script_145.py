from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_145_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_145_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_145_shift_northwest_steps_2',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_145_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_145_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_145_pause_5',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_145_face_northwest_6',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_145_pause_7',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_145_shift_southeast_steps_8',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_145_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_145_face_southwest_10',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_145_pause_11',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_145_face_southeast_12',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_145_pause_13',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_145_shift_northwest_steps_14',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_145_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_145_set_animation_speed_0']
    }
]
