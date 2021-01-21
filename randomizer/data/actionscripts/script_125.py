from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_125_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_125_set_random_1',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_125_add_2',
        "command": 'add',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_125_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_125_jump_to_subroutine_4',
        "command": 'jump_to_subroutine',
        "args": [0x18ea]
    },
    {
        "identifier": 'ACTION_125_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_125_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0x1928]
    },
    {
        "identifier": 'ACTION_125_jump_to_subroutine_7',
        "command": 'jump_to_subroutine',
        "args": [0x194c]
    },
    {
        "identifier": 'ACTION_125_face_southwest_8',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_125_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_125_set_bit_0']
    }
]
