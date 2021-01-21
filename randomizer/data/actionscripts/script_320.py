from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_320_set_bit_0',
        "command": 'set_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'ACTION_320_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_320_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_320_walk_1_step_northeast_3',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_320_face_southwest_4',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_320_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_320_ret_6',
        "command": 'ret'
    }
]
