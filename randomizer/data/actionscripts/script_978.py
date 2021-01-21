from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_978_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_978_pause_1',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_978_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_978_face_southwest_0']
    },
    {
        "identifier": 'ACTION_978_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_978_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_978_face_southwest_0']
    }
]
