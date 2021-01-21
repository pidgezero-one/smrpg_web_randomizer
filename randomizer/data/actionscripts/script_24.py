from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_24_shift_southwest_steps_0',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_24_face_northwest_1',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_24_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_24_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_24_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_24_walk_1_step_northeast_8']
    },
    {
        "identifier": 'ACTION_24_face_northwest_5',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_24_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_24_jmp_if_random_above_128_7',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_24_shift_southwest_steps_12']
    },
    {
        "identifier": 'ACTION_24_walk_1_step_northeast_8',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_24_pause_9',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_24_walk_1_step_southwest_10',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_24_jmp_if_random_above_128_11',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_24_face_northwest_5']
    },
    {
        "identifier": 'ACTION_24_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_24_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_24_face_northwest_1']
    }
]
