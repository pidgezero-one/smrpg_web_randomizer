from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_141_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_141_walk_1_step_west_1',
        "command": 'walk_1_step_west'
    },
    {
        "identifier": 'ACTION_141_face_southeast_2',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_141_ret_3',
        "command": 'ret'
    }
]
