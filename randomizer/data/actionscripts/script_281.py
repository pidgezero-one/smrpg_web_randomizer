from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_281_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_281_add_1',
        "command": 'add',
        "args": [0x700c, 65515]
    },
    {
        "identifier": 'ACTION_281_set_short_2',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'ACTION_281_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_281_set_short_mem_7']
    },
    {
        "identifier": 'ACTION_281_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_281_mem_700C_shift_left_5',
        "command": 'mem_700C_shift_left',
        "args": [0x7032, 255]
    },
    {
        "identifier": 'ACTION_281_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_281_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x700c, 0x703e]
    },
    {
        "identifier": 'ACTION_281_mem_700C_and_var_8',
        "command": 'mem_700C_and_var',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_281_mem_compare_9',
        "command": 'mem_compare',
        "args": [0x700c, 0]
    },
    {
        "identifier": 'ACTION_281_jmp_if_loaded_memory_is_not_0_10',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['ACTION_281_jump_to_subroutine_18']
    },
    {
        "identifier": 'ACTION_281_jump_to_subroutine_11',
        "command": 'jump_to_subroutine',
        "args": [0x33fd]
    },
    {
        "identifier": 'ACTION_281_set_vram_priority_12',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_281_set_solidity_bits_13',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_281_object_memory_clear_bit_14',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_281_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_281_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_281_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_281_jump_to_subroutine_18',
        "command": 'jump_to_subroutine',
        "args": [0x33fd]
    },
    {
        "identifier": 'ACTION_281_set_vram_priority_19',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_281_clear_solidity_bits_20',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_281_object_memory_set_bit_21',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_281_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_281_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_281_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_281_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x700c, 0x703c]
    },
    {
        "identifier": 'ACTION_281_mem_700C_and_var_26',
        "command": 'mem_700C_and_var',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_281_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7028, 0x700c]
    },
    {
        "identifier": 'ACTION_281_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x700c, 0x703e]
    },
    {
        "identifier": 'ACTION_281_mem_700C_and_var_29',
        "command": 'mem_700C_and_var',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_281_mem_compare_30',
        "command": 'mem_compare',
        "args": [0x700c, 0x7028]
    },
    {
        "identifier": 'ACTION_281_jmp_if_loaded_memory_is_0_31',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['ACTION_281_ret_33']
    },
    {
        "identifier": 'ACTION_281_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 4]
    },
    {
        "identifier": 'ACTION_281_ret_33',
        "command": 'ret'
    }
]
