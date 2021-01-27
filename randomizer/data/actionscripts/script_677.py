from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_677_jmp_if_random_above_66_0',
        "command": 'jmp_if_random_above_66',
        "args": [0x7c56, 'ACTION_677_pause_3']
    },
    {
        "identifier": 'ACTION_677_pause_1',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_677_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_677_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_677_jump_to_height_silent_4',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_677_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_677_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'ACTION_677_pause_9']
    },
    {
        "identifier": 'ACTION_677_db_7',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x5d, 0x7c]
    },
    {
        "identifier": 'ACTION_677_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_677_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_677_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_677_db_10',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x6b, 0x7c]
    },
    {
        "identifier": 'ACTION_677_face_northeast_11',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_677_ret_12',
        "command": 'ret'
    }
]
