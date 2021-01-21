from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_379_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_379_jump_to_height_silent_1',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_379_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_379_db_3',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x9c, 0x46]
    },
    {
        "identifier": 'ACTION_379_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_379_face_southeast_6']
    },
    {
        "identifier": 'ACTION_379_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_379_face_southwest_0']
    },
    {
        "identifier": 'ACTION_379_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_379_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_379_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_379_face_southwest_0']
    },
    {
        "identifier": 'ACTION_379_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_379_pause_7']
    }
]
