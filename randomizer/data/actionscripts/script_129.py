from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_129_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_129_shift_southwest_pixels_1',
        "command": 'shift_southwest_pixels',
        "args": [22]
    },
    {
        "identifier": 'ACTION_129_walk_1_step_southwest_2',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_129_walk_1_step_southeast_3',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_129_walk_1_step_southeast_4',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_129_shift_southeast_pixels_5',
        "command": 'shift_southeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_129_shift_northeast_steps_6',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_129_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [22]
    },
    {
        "identifier": 'ACTION_129_shift_northwest_pixels_8',
        "command": 'shift_northwest_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_129_shift_northwest_steps_9',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_129_walk_1_step_southwest_10',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_129_face_southeast_11',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_129_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_129_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'ACTION_129_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_129_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_129_pause_12']
    }
]
