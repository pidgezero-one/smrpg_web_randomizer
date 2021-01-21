from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_58_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_58_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_58_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_58_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_58_set_short_4',
        "command": 'set_short',
        "args": [0x702c, 0x0014]
    },
    {
        "identifier": 'ACTION_58_dec_short_mem_5',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x702c]
    },
    {
        "identifier": 'ACTION_58_mem_700C_and_const_6',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_58_pause_15']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_58_pause_16']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 3, 'ACTION_58_pause_17']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 4, 'ACTION_58_pause_18']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 5, 'ACTION_58_pause_19']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 6, 'ACTION_58_pause_20']
    },
    {
        "identifier": 'ACTION_58_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 7, 'ACTION_58_pause_21']
    },
    {
        "identifier": 'ACTION_58_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_58_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_58_pause_23',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_58_db_24',
        "command": 'db',
        "args": [0x3b, 0x00, 0xc0, 0x02, 0x34, 0x12]
    },
    {
        "identifier": 'ACTION_58_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_58_visibility_off_22']
    },
    {
        "identifier": 'ACTION_58_visibility_on_26',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_58_set_animation_speed_27',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_58_shift_southwest_steps_28',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_58_pause_29',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_58_shift_northwest_steps_30',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_58_pause_31',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_58_walk_1_step_northeast_32',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_58_pause_33',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_58_shift_southeast_steps_34',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_58_pause_35',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_58_shift_southwest_steps_36',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_58_pause_37',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_58_shift_northwest_steps_38',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_58_shift_northeast_steps_39',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_58_jmp_40',
        "command": 'jmp',
        "args": ['ACTION_58_visibility_off_22']
    }
]
