from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_584_face_northeast_0',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_584_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_584_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_584_pause_3',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_584_pause_4',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_584_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_584_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_584_jump_to_height_silent_7',
        "command": 'jump_to_height_silent',
        "args": [32]
    },
    {
        "identifier": 'ACTION_584_shift_northwest_steps_8',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_584_shift_southwest_steps_9',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_584_visibility_off_10',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_584_ret_11',
        "command": 'ret'
    }
]
