from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_124_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_124_set_random_1',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_124_add_2',
        "command": 'add',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_124_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_124_jump_to_subroutine_4',
        "command": 'jump_to_subroutine',
        "args": [0x18ea]
    },
    {
        "identifier": 'ACTION_124_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_124_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0x195e]
    },
    {
        "identifier": 'ACTION_124_jump_to_subroutine_7',
        "command": 'jump_to_subroutine',
        "args": [0x193a]
    },
    {
        "identifier": 'ACTION_124_face_southeast_8',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_124_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_124_set_bit_0']
    }
]
