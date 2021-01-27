from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_726_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_726_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_726_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_726_pause_3',
        "command": 'pause',
        "args": [23]
    },
    {
        "identifier": 'ACTION_726_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_726_visibility_off_0']
    },
    {
        "identifier": 'ACTION_726_pause_5',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_726_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_726_visibility_off_0']
    },
    {
        "identifier": 'ACTION_726_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_726_visibility_off_0']
    },
    {
        "identifier": 'ACTION_726_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_726_visibility_on_26']
    },
    {
        "identifier": 'ACTION_726_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_726_object_memory_set_bit_10',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_726_clear_solidity_bits_11',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_726_turn_random_direction_12',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_726_walk_1_step_f_direction_13',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_726_set_700C_to_pressed_button_14',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_726_mem_700C_and_const_15',
        "command": 'mem_700C_and_const',
        "args": [0x0003]
    },
    {
        "identifier": 'ACTION_726_jmp_if_700C_equals_short_16',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_726_pause_21']
    },
    {
        "identifier": 'ACTION_726_jmp_if_700C_equals_short_17',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_726_pause_22']
    },
    {
        "identifier": 'ACTION_726_jmp_if_700C_equals_short_18',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_726_pause_23']
    },
    {
        "identifier": 'ACTION_726_turn_random_direction_19',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_726_pause_20',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_726_pause_21',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_726_pause_22',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_726_pause_23',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_726_jmp_if_random_above_128_24',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_726_turn_random_direction_12']
    },
    {
        "identifier": 'ACTION_726_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_726_visibility_off_9']
    },
    {
        "identifier": 'ACTION_726_visibility_on_26',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_726_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 4]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_28',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_29',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_30',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_31',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_32',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_33',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_34',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_35',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_start_loop_n_times_36',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_37',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_38',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_39',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_40',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_41',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_42',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_end_loop_43',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_726_start_loop_n_times_44',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_45',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_46',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_47',
        "command": 'set_sprite_sequence',
        "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_48',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_49',
        "command": 'set_sprite_sequence',
        "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_50',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_end_loop_51',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_52',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_53',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_54',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_55',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_56',
        "command": 'set_sprite_sequence',
        "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_57',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_reset_properties_58',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_726_object_memory_clear_bit_59',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_726_set_solidity_bits_60',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_726_sequence_looping_on_61',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_726_sequence_playback_on_62',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_726_db_63',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_726_db_64',
        "command": 'db',
        "args": [0x29, 0x00]
    },
    {
        "identifier": 'ACTION_726_bpl_26_27_65',
        "command": 'bpl_26_27'
    },
    {
        "identifier": 'ACTION_726_set_animation_speed_66',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_726_visibility_on_67',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_726_visibility_off_68',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_726_db_69',
        "command": 'db',
        "args": [0x2b, 0x08, 0x20, 0x80, 0x00]
    },
    {
        "identifier": 'ACTION_726_embedded_animation_routine_70',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_726_jmp_if_bit_set_71',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_726_object_memory_set_bit_84']
    },
    {
        "identifier": 'ACTION_726_face_mario_72',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_726_pause_73',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_726_set_700C_to_object_coord_74',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_726_mem_compare_val_75',
        "command": 'mem_compare_val',
        "args": [10]
    },
    {
        "identifier": 'ACTION_726_jmp_if_comparison_result_is_greater_or_equal_76',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_726_object_memory_set_bit_84']
    },
    {
        "identifier": 'ACTION_726_jmp_if_random_above_128_77',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_726_jmp_if_bit_set_71']
    },
    {
        "identifier": 'ACTION_726_pause_78',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_726_set_700C_to_object_coord_79',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_726_mem_compare_val_80',
        "command": 'mem_compare_val',
        "args": [10]
    },
    {
        "identifier": 'ACTION_726_jmp_if_comparison_result_is_greater_or_equal_81',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_726_object_memory_set_bit_84']
    },
    {
        "identifier": 'ACTION_726_jmp_if_random_above_128_82',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_726_jmp_if_bit_set_71']
    },
    {
        "identifier": 'ACTION_726_bpl_26_27_28_83',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_726_object_memory_set_bit_84',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_726_clear_solidity_bits_85',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_86',
        "command": 'set_sprite_sequence',
        "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_87',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_88',
        "command": 'set_sprite_sequence',
        "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_89',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_90',
        "command": 'set_sprite_sequence',
        "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_91',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_start_loop_n_times_92',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_93',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_94',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_95',
        "command": 'set_sprite_sequence',
        "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_96',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_97',
        "command": 'set_sprite_sequence',
        "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_98',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_end_loop_99',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_726_start_loop_n_times_100',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_101',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_102',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_103',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_104',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_105',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_106',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_end_loop_107',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_108',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_109',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_110',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_111',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_112',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_113',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_set_sprite_sequence_114',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_726_pause_115',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_726_jmp_116',
        "command": 'jmp',
        "args": ['ACTION_726_visibility_off_9']
    }
]
