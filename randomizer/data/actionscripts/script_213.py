from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_213_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_213_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_213_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_213_set_short_3',
        "command": 'set_short',
        "args": [0x703e, 0x0003]
    },
    {
        "identifier": 'ACTION_213_ret_4',
        "command": 'ret'
    }
]
