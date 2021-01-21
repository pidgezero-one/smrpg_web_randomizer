from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_487_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_487_add_1',
        "command": 'add',
        "args": [0x700c, 65516]
    },
    {
        "identifier": 'ACTION_487_load_mem_2',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_487_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_487_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_487_jump_to_height_5',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_487_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_487_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_487_jump_to_height_5']
    },
    {
        "identifier": 'ACTION_487_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_487_set_700C_to_pressed_button_0']
    },
    {
        "identifier": 'ACTION_487_ret_9',
        "command": 'ret'
    }
]
