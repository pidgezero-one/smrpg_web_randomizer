from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_57_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_57_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_57_mem_700C_and_const_2',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_57_pause_8']
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_57_pause_9']
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_57_pause_10']
    },
    {
        "identifier": 'ACTION_57_pause_6',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_57_inc_short_7',
        "command": 'inc_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_pause_8',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_57_pause_9',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_57_pause_10',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_57_inc_short_11',
        "command": 'inc_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 1, 'ACTION_57_object_memory_modify_bits_64']
    },
    {
        "identifier": 'ACTION_57_set_700C_to_current_level_13',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_14',
        "command": 'jmp_if_700C_equals_short',
        "args": [57, 'ACTION_57_set_animation_speed_83']
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_15',
        "command": 'jmp_if_700C_equals_short',
        "args": [58, 'ACTION_57_set_animation_speed_83']
    },
    {
        "identifier": 'ACTION_57_set_700C_to_pressed_button_16',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_19',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_57_set_animation_speed_83']
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_57_turn_clockwise_45_degrees_n_times_21',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_bpl_26_27_28_22',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_57_clear_solidity_bits_23',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_26',
        "command": 'shift_f_direction_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_57_db_27',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x08, 0x51, 0x11]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_28',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_57_turn_clockwise_45_degrees_n_times_29',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_30',
        "command": 'shift_f_direction_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_57_turn_clockwise_45_degrees_n_times_31',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_57_bpl_26_27_28_22']
    },
    {
        "identifier": 'ACTION_57_set_solidity_bits_33',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_36',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_57_db_37',
        "command": 'db',
        "args": [0xc7, 0x87]
    },
    {
        "identifier": 'ACTION_57_set_700C_to_object_coord_38',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_57_add_39',
        "command": 'add',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_57_mem_700C_and_const_40',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_57_set_7000_short_mem_to_700C_41',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x702e]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_jump_to_height_silent_43',
        "command": 'jump_to_height_silent',
        "args": [160]
    },
    {
        "identifier": 'ACTION_57_walk_1_step_f_direction_44',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_57_set_priority_45',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_46',
        "command": 'shift_f_direction_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_jump_to_height_silent_47',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_57_turn_clockwise_45_degrees_n_times_48',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_49',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_57_jump_to_height_silent_50',
        "command": 'jump_to_height_silent',
        "args": [32]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_51',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_57_object_memory_modify_bits_52',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_57_move_7010_7012_7014_to_7016_7018_701A_53',
        "command": 'move_7010_7012_7014_to_7016_7018_701A'
    },
    {
        "identifier": 'ACTION_57_db_54',
        "command": 'db',
        "args": [0x98]
    },
    {
        "identifier": 'ACTION_57_set_700C_to_7000_short_mem_55',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x702e]
    },
    {
        "identifier": 'ACTION_57_face_east_7C_56',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_57_bpl_26_27_28_57',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_57_clear_solidity_bits_58',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_59',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_60',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_61',
        "command": 'shift_f_direction_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_57_turn_clockwise_45_degrees_n_times_62',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_57_jmp_63',
        "command": 'jmp',
        "args": ['ACTION_57_bpl_26_27_28_22']
    },
    {
        "identifier": 'ACTION_57_object_memory_modify_bits_64',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_57_clear_solidity_bits_65',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_66',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_fixed_f_coord_on_67',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_57_floating_on_68',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_57_jmp_if_random_above_128_69',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_57_set_sprite_sequence_72']
    },
    {
        "identifier": 'ACTION_57_set_sprite_sequence_70',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_57_jmp_71',
        "command": 'jmp',
        "args": ['ACTION_57_turn_random_direction_73']
    },
    {
        "identifier": 'ACTION_57_set_sprite_sequence_72',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_57_turn_random_direction_73',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_57_jmp_if_random_above_66_74',
        "command": 'jmp_if_random_above_66',
        "args": [0x11b5, 'ACTION_57_jump_to_height_79']
    },
    {
        "identifier": 'ACTION_57_jump_to_height_75',
        "command": 'jump_to_height',
        "args": [112]
    },
    {
        "identifier": 'ACTION_57_walk_1_step_f_direction_76',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_57_reset_properties_77',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_57_jmp_78',
        "command": 'jmp',
        "args": ['ACTION_57_walk_1_step_f_direction_80']
    },
    {
        "identifier": 'ACTION_57_jump_to_height_79',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_57_walk_1_step_f_direction_80',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_57_reset_properties_81',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_57_jmp_82',
        "command": 'jmp',
        "args": ['ACTION_57_object_memory_modify_bits_64']
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_83',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_inc_short_84',
        "command": 'inc_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_set_700C_to_7000_short_mem_85',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_mem_700C_and_const_86',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_87',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_57_shift_f_direction_steps_89']
    },
    {
        "identifier": 'ACTION_57_set_animation_speed_88',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_57_shift_f_direction_steps_89',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_57_inc_short_90',
        "command": 'inc_short',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_set_700C_to_7000_short_mem_91',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x702c]
    },
    {
        "identifier": 'ACTION_57_mem_700C_and_const_92',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_57_jmp_if_700C_equals_short_93',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_57_face_mario_96']
    },
    {
        "identifier": 'ACTION_57_turn_random_direction_94',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_57_jmp_95',
        "command": 'jmp',
        "args": ['ACTION_57_set_animation_speed_83']
    },
    {
        "identifier": 'ACTION_57_face_mario_96',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_57_jmp_97',
        "command": 'jmp',
        "args": ['ACTION_57_set_animation_speed_83']
    }
]
