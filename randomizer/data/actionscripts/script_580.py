from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_580_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_580_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_580_face_southwest_2',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_580_pause_3',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_580_face_northwest_4',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_580_pause_5',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'ACTION_580_face_southwest_6',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_580_pause_7',
        "command": 'pause',
        "args": [31]
    },
    {
        "identifier": 'ACTION_580_face_northwest_8',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_580_pause_9',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'ACTION_580_face_southwest_10',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_580_pause_11',
        "command": 'pause',
        "args": [37]
    },
    {
        "identifier": 'ACTION_580_face_northwest_12',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_580_pause_13',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'ACTION_580_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_580_set_animation_speed_0']
    }
]
