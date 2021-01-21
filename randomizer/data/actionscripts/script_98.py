from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_98_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_98_walk_1_step_southwest_1',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_98_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_98_pause_6']
    },
    {
        "identifier": 'ACTION_98_walk_1_step_northeast_3',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_98_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_98_pause_12']
    },
    {
        "identifier": 'ACTION_98_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_98_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_98_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_face_northwest_7',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_98_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_face_southeast_9',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_98_pause_10',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_98_walk_1_step_northeast_3']
    },
    {
        "identifier": 'ACTION_98_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_face_southeast_13',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_98_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_face_northwest_15',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_98_pause_16',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_98_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_98_set_animation_speed_0']
    }
]
