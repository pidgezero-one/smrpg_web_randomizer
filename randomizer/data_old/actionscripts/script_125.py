
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_125_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'ACTION_125_set_var_to_random_1',
        "command": 'set_var_to_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_125_inc_2',
        "command": 'inc',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_125_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_125_jmp_to_subroutine_4',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_103_clear_solidity_bits_0']
    },
    {
        "identifier": 'ACTION_125_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_125_jmp_to_subroutine_6',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_104_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_125_jmp_to_subroutine_7',
        "command": 'jmp_to_subroutine',
        "args": ['ACTION_106_set_animation_speed_0']
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
