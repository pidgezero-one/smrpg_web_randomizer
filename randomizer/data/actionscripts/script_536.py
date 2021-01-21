from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_536_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_536_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_536_face_northwest_2',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_536_pause_3',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_536_face_northeast_4',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_536_pause_5',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_536_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_536_pause_7',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_536_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_536_pause_9',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_536_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_536_set_animation_speed_0']
    }
]
