from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_211_face_northwest_0',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_211_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_211_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_211_set_short_3',
        "command": 'set_short',
        "args": [0x703e, 0x0005]
    },
    {
        "identifier": 'ACTION_211_ret_4',
        "command": 'ret'
    }
]
