from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_975_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_975_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_975_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_975_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_975_shift_southwest_steps_4',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_975_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_975_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_975_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_975_face_northwest_8',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_975_jump_to_height_9',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_975_pause_10',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_975_sequence_looping_off_11',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_975_ret_12',
        "command": 'ret'
    }
]
