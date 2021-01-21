from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_534_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_534_pause_1',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_534_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_534_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_534_pause_4',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_534_sequence_looping_off_5',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_534_pause_6',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_534_face_southeast_7',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_534_pause_8',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_534_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_534_face_southwest_0']
    },
    {
        "identifier": 'ACTION_534_ret_10',
        "command": 'ret'
    }
]
