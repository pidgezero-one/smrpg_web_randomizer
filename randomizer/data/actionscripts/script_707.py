from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_707_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_object_memory_clear_bit_4',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_707_set_solidity_bits_5',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_707_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_707_sequence_looping_on_7',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_707_fixed_f_coord_on_8',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_707_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_707_set_animation_speed_43']
    },
    {
        "identifier": 'ACTION_707_set_random_10',
        "command": 'set_random',
        "args": [0x700c, 60]
    },
    {
        "identifier": 'ACTION_707_mem_compare_val_11',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'ACTION_707_jmp_if_comparison_result_is_lesser_12',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_707_jmp_if_bit_set_24']
    },
    {
        "identifier": 'ACTION_707_load_mem_13',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_707_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_707_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_707_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'ACTION_707_jmp_if_bit_set_24']
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_shift_northwest_pixels_20',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_707_shift_southeast_pixels_21',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_707_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_707_set_animation_speed_43']
    },
    {
        "identifier": 'ACTION_707_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_707_set_random_10']
    },
    {
        "identifier": 'ACTION_707_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_707_set_animation_speed_43']
    },
    {
        "identifier": 'ACTION_707_jmp_if_var_equals_byte_25',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'ACTION_707_load_mem_13']
    },
    {
        "identifier": 'ACTION_707_inc_26',
        "command": 'inc',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_27',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_play_sound_29',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_707_jump_to_height_30',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_707_set_sprite_sequence_31',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_pause_32',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_707_set_sprite_sequence_33',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_shift_northwest_steps_35',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_707_set_sprite_sequence_36',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_shift_southeast_steps_37',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_707_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_707_shift_southeast_steps_42']
    },
    {
        "identifier": 'ACTION_707_dec_39',
        "command": 'dec',
        "args": [0x70ae]
    },
    {
        "identifier": 'ACTION_707_shift_southeast_steps_40',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_707_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_707_set_random_10']
    },
    {
        "identifier": 'ACTION_707_shift_southeast_steps_42',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_43',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_707_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_707_clear_solidity_bits_45',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_707_walk_1_step_southeast_46',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_707_set_700C_to_object_coord_47',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.X, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_707_mem_compare_val_48',
        "command": 'mem_compare_val',
        "args": [5888]
    },
    {
        "identifier": 'ACTION_707_jmp_if_comparison_result_is_lesser_49',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_707_walk_1_step_southeast_46']
    },
    {
        "identifier": 'ACTION_707_ret_50',
        "command": 'ret'
    }
]
