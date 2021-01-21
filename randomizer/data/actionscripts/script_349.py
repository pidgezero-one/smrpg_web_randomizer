from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_349_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_349_face_mario_1',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_349_pause_2',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_349_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_349_sequence_looping_on_0']
    }
]
