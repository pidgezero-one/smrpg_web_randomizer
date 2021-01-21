from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_30_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_30_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_30_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_30_walk_1_step_southeast_3',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_30_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_30_pause_8']
    },
    {
        "identifier": 'ACTION_30_walk_1_step_northwest_5',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_30_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_30_pause_14']
    },
    {
        "identifier": 'ACTION_30_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_30_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_30_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_face_northeast_9',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_30_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_face_southwest_11',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_30_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_30_walk_1_step_northwest_5']
    },
    {
        "identifier": 'ACTION_30_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_face_southwest_15',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_30_pause_16',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_face_northeast_17',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_30_pause_18',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_30_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_30_set_animation_speed_0']
    }
]
