from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_312_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_312_inc_palette_row_by_1',
        "command": 'inc_palette_row_by',
        "args": [3]
    },
    {
        "identifier": 'ACTION_312_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_312_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_312_db_4',
        "command": 'db',
        "args": [0x3a, 0x14, 0x30, 0x00, 0xe7, 0x39]
    },
    {
        "identifier": 'ACTION_312_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_312_pause_3']
    },
    {
        "identifier": 'ACTION_312_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_0, Coords.F, []]
    },
    {
        "identifier": 'ACTION_312_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 1, 'ACTION_312_jmp_if_700C_not_equals_short_11']
    },
    {
        "identifier": 'ACTION_312_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 2, 'ACTION_312_jmp_if_700C_not_equals_short_20']
    },
    {
        "identifier": 'ACTION_312_jmp_if_var_equals_byte_9',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'ACTION_312_jmp_if_700C_not_equals_short_35']
    },
    {
        "identifier": 'ACTION_312_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 4, 'ACTION_312_jmp_if_700C_not_equals_short_49']
    },
    {
        "identifier": 'ACTION_312_jmp_if_700C_not_equals_short_11',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [1, 'ACTION_312_pause_3']
    },
    {
        "identifier": 'ACTION_312_fixed_f_coord_on_12',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_312_floating_on_13',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_312_walk_1_step_southeast_14',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_312_jump_to_height_silent_15',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_312_pause_16',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_312_floating_off_17',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_312_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_312_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_312_jmp_if_700C_not_equals_short_20',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [7, 'ACTION_312_pause_3']
    },
    {
        "identifier": 'ACTION_312_fixed_f_coord_on_21',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_312_floating_on_22',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_312_walk_1_step_northeast_23',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_312_object_memory_modify_bits_24',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_312_clear_solidity_bits_25',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_312_jump_to_height_silent_26',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_312_pause_27',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_312_set_bit_28',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_312_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_312_db_30',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x24, 0x3a]
    },
    {
        "identifier": 'ACTION_312_shift_northeast_steps_31',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_312_visibility_off_32',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_312_object_memory_set_bit_33',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_312_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_312_jmp_if_700C_not_equals_short_35',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [3, 'ACTION_312_pause_3']
    },
    {
        "identifier": 'ACTION_312_fixed_f_coord_on_36',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_312_floating_on_37',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_312_walk_1_step_southwest_38',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_312_clear_solidity_bits_39',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_312_jump_to_height_silent_40',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_312_pause_41',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_312_set_bit_42',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_312_pause_43',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_312_db_44',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x43, 0x3a]
    },
    {
        "identifier": 'ACTION_312_shift_southwest_steps_45',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_312_visibility_off_46',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_312_object_memory_set_bit_47',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_312_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_312_jmp_if_700C_not_equals_short_49',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [5, 'ACTION_312_pause_3']
    },
    {
        "identifier": 'ACTION_312_fixed_f_coord_on_50',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_312_floating_on_51',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_312_walk_1_step_northwest_52',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_312_object_memory_modify_bits_53',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_312_clear_solidity_bits_54',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_312_jump_to_height_silent_55',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_312_pause_56',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_312_set_bit_57',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_312_pause_58',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_312_db_59',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x64, 0x3a]
    },
    {
        "identifier": 'ACTION_312_shift_northwest_steps_60',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_312_visibility_off_61',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_312_object_memory_set_bit_62',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_312_ret_63',
        "command": 'ret'
    }
]
