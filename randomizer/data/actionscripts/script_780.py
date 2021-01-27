from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_780_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_780_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_780_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_780_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_780_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_780_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'ACTION_780_pause_5']
    },
    {
        "identifier": 'ACTION_780_set_priority_7',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_780_set_700C_to_current_level_8',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_780_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [319, 'ACTION_780_object_memory_modify_bits_44']
    },
    {
        "identifier": 'ACTION_780_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [403, 'ACTION_780_object_memory_modify_bits_44']
    },
    {
        "identifier": 'ACTION_780_set_700C_to_pressed_button_11',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_780_dec_short_mem_12',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_780_jmp_if_700C_equals_short_13',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_780_face_south_19']
    },
    {
        "identifier": 'ACTION_780_jmp_if_700C_equals_short_14',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_780_face_southwest_17']
    },
    {
        "identifier": 'ACTION_780_face_north_15',
        "command": 'face_north'
    },
    {
        "identifier": 'ACTION_780_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_780_jmp_if_bit_clear_39']
    },
    {
        "identifier": 'ACTION_780_face_southwest_17',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_780_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_780_jmp_if_bit_clear_30']
    },
    {
        "identifier": 'ACTION_780_face_south_19',
        "command": 'face_south'
    },
    {
        "identifier": 'ACTION_780_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_780_set_animation_speed_24']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_clear_solidity_bits_22',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_780_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_780_walk_1_step_f_direction_26']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_set_solidity_bits_25',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_26',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_27',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_780_shift_f_direction_steps_28',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_29',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_780_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_780_set_animation_speed_34']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_clear_solidity_bits_32',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_780_jmp_33',
        "command": 'jmp',
        "args": ['ACTION_780_shift_f_direction_steps_36']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_set_solidity_bits_35',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_780_shift_f_direction_steps_36',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_37',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_38',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_jmp_if_bit_clear_39',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'ACTION_780_pause_42']
    },
    {
        "identifier": 'ACTION_780_pause_40',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_780_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_780_jmp_if_bit_clear_20']
    },
    {
        "identifier": 'ACTION_780_pause_42',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_780_jmp_43',
        "command": 'jmp',
        "args": ['ACTION_780_jmp_if_bit_clear_20']
    },
    {
        "identifier": 'ACTION_780_object_memory_modify_bits_44',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_780_set_solidity_bits_45',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_780_set_700C_to_pressed_button_46',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_780_mem_compare_address_47',
        "command": 'mem_compare_address',
        "args": [0x7026]
    },
    {
        "identifier": 'ACTION_780_jmp_if_loaded_memory_is_0_48',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['ACTION_780_set_animation_speed_53']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_49',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_50',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_51',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_jmp_52',
        "command": 'jmp',
        "args": ['ACTION_780_object_memory_modify_bits_44']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_53',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_face_mario_54',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_780_db_55',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x04, 0xf1, 0x94]
    },
    {
        "identifier": 'ACTION_780_jmp_if_random_above_66_56',
        "command": 'jmp_if_random_above_66',
        "args": [0x94e2, 'ACTION_780_turn_clockwise_45_degrees_n_times_63']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_57',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_780_pause_58',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_780_jmp_59',
        "command": 'jmp',
        "args": ['ACTION_780_walk_1_step_f_direction_65']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_60',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_780_pause_61',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_780_jmp_62',
        "command": 'jmp',
        "args": ['ACTION_780_walk_1_step_f_direction_65']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_63',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [6]
    },
    {
        "identifier": 'ACTION_780_pause_64',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_65',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_jmp_66',
        "command": 'jmp',
        "args": ['ACTION_780_object_memory_modify_bits_44']
    },
    {
        "identifier": 'ACTION_780_set_animation_speed_67',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_68',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_69',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_70',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_780_pause_71',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_780_jmp_if_random_above_66_72',
        "command": 'jmp_if_random_above_66',
        "args": [0x9504, 'ACTION_780_turn_clockwise_45_degrees_n_times_77']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_73',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_780_jmp_74',
        "command": 'jmp',
        "args": ['ACTION_780_walk_1_step_f_direction_78']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_75',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_780_jmp_76',
        "command": 'jmp',
        "args": ['ACTION_780_walk_1_step_f_direction_78']
    },
    {
        "identifier": 'ACTION_780_turn_clockwise_45_degrees_n_times_77',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [5]
    },
    {
        "identifier": 'ACTION_780_walk_1_step_f_direction_78',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_780_jmp_79',
        "command": 'jmp',
        "args": ['ACTION_780_object_memory_modify_bits_44']
    }
]
