from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_973_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_973_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_973_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_973_walk_1_step_northeast_3',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_973_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_973_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_973_shift_southeast_steps_6',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_973_shift_southeast_pixels_7',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_973_shift_northeast_steps_8',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_973_walk_1_step_northwest_9',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_973_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_973_shift_southwest_steps_11',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_973_face_northwest_12',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_973_jump_to_height_13',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_973_pause_14',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_973_sequence_looping_off_15',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_973_ret_16',
        "command": 'ret'
    }
]
