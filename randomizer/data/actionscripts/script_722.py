from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_722_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 1, 'ACTION_722_ret_4']
    },
    {
        "identifier": 'ACTION_722_face_southwest_1',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_722_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_722_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_722_jmp_if_bit_set_0']
    },
    {
        "identifier": 'ACTION_722_ret_4',
        "command": 'ret'
    }
]
