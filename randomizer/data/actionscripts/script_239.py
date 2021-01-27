from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_239_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_239_pause_1',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'ACTION_239_reset_properties_2',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_239_pause_3',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_239_face_southeast_4',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_239_pause_5',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_239_face_northeast_6',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_239_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_239_shift_northeast_steps_8',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_239_shift_northeast_pixels_9',
        "command": 'shift_northeast_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_239_face_northwest_10',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_239_pause_11',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_239_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_239_ret_13',
        "command": 'ret'
    }
]
