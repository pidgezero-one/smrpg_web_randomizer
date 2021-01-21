from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_217_face_southeast_0',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_217_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_217_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_217_set_short_3',
        "command": 'set_short',
        "args": [0x703e, 0x0001]
    },
    {
        "identifier": 'ACTION_217_ret_4',
        "command": 'ret'
    }
]
