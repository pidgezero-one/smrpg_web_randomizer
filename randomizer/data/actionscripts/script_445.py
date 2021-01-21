from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_445_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x700c, 33]
    },
    {
        "identifier": 'ACTION_445_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_445_set_object_memory_bits_51']
    },
    {
        "identifier": 'ACTION_445_pause_4',
        "command": 'pause',
        "args": [91]
    },
    {
        "identifier": 'ACTION_445_jmp_if_random_above_128_5',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_445_pause_4']
    },
    {
        "identifier": 'ACTION_445_pause_6',
        "command": 'pause',
        "args": [55]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_byte_7',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70af, 0, 'ACTION_445_pause_4']
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_8',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x70af, 0x700c]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 30, 'ACTION_445_set_short_15']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 31, 'ACTION_445_set_short_17']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 32, 'ACTION_445_set_short_19']
    },
    {
        "identifier": 'ACTION_445_set_short_13',
        "command": 'set_short',
        "args": [0x7038, 0x0001]
    },
    {
        "identifier": 'ACTION_445_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_445_pause_20']
    },
    {
        "identifier": 'ACTION_445_set_short_15',
        "command": 'set_short',
        "args": [0x703a, 0x0001]
    },
    {
        "identifier": 'ACTION_445_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_445_pause_20']
    },
    {
        "identifier": 'ACTION_445_set_short_17',
        "command": 'set_short',
        "args": [0x703c, 0x0001]
    },
    {
        "identifier": 'ACTION_445_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_445_pause_20']
    },
    {
        "identifier": 'ACTION_445_set_short_19',
        "command": 'set_short',
        "args": [0x703e, 0x0001]
    },
    {
        "identifier": 'ACTION_445_pause_20',
        "command": 'pause',
        "args": [328]
    },
    {
        "identifier": 'ACTION_445_shift_z_up_steps_21',
        "command": 'shift_z_up_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_445_db_22',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_445_embedded_animation_routine_23',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_445_embedded_animation_routine_24',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_445_pause_25',
        "command": 'pause',
        "args": [512]
    },
    {
        "identifier": 'ACTION_445_embedded_animation_routine_26',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_445_embedded_animation_routine_27',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_445_pause_28',
        "command": 'pause',
        "args": [512]
    },
    {
        "identifier": 'ACTION_445_bpl_26_27_28_29',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_30',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x70af, 0x700c]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_32',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 30, 'ACTION_445_set_short_39']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_33',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 31, 'ACTION_445_set_short_43']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_34',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 32, 'ACTION_445_set_short_47']
    },
    {
        "identifier": 'ACTION_445_set_short_35',
        "command": 'set_short',
        "args": [0x7038, 0x0002]
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_36',
        "command": 'bounce_to_xy_with_height',
        "args": [8, 40, 0]
    },
    {
        "identifier": 'ACTION_445_set_short_37',
        "command": 'set_short',
        "args": [0x7038, 0x0000]
    },
    {
        "identifier": 'ACTION_445_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_445_set_priority_0']
    },
    {
        "identifier": 'ACTION_445_set_short_39',
        "command": 'set_short',
        "args": [0x703a, 0x0002]
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_40',
        "command": 'bounce_to_xy_with_height',
        "args": [17, 42, 0]
    },
    {
        "identifier": 'ACTION_445_set_short_41',
        "command": 'set_short',
        "args": [0x703a, 0x0000]
    },
    {
        "identifier": 'ACTION_445_jmp_42',
        "command": 'jmp',
        "args": ['ACTION_445_set_priority_0']
    },
    {
        "identifier": 'ACTION_445_set_short_43',
        "command": 'set_short',
        "args": [0x703c, 0x0002]
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_44',
        "command": 'bounce_to_xy_with_height',
        "args": [14, 26, 0]
    },
    {
        "identifier": 'ACTION_445_set_short_45',
        "command": 'set_short',
        "args": [0x703c, 0x0000]
    },
    {
        "identifier": 'ACTION_445_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_445_set_priority_0']
    },
    {
        "identifier": 'ACTION_445_set_short_47',
        "command": 'set_short',
        "args": [0x703e, 0x0002]
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_48',
        "command": 'bounce_to_xy_with_height',
        "args": [23, 38, 0]
    },
    {
        "identifier": 'ACTION_445_set_short_49',
        "command": 'set_short',
        "args": [0x703e, 0x0000]
    },
    {
        "identifier": 'ACTION_445_jmp_50',
        "command": 'jmp',
        "args": ['ACTION_445_set_priority_0']
    },
    {
        "identifier": 'ACTION_445_set_object_memory_bits_51',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[2]]
    },
    {
        "identifier": 'ACTION_445_inc_palette_row_by_52',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_53',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_set_priority_54',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_445_pause_55',
        "command": 'pause',
        "args": [55]
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_56',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_57',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 34, 'ACTION_445_pause_63']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_58',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 35, 'ACTION_445_pause_66']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_59',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 36, 'ACTION_445_pause_69']
    },
    {
        "identifier": 'ACTION_445_pause_60',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_61',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7038, 1, 'ACTION_445_pause_60']
    },
    {
        "identifier": 'ACTION_445_jmp_62',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_71']
    },
    {
        "identifier": 'ACTION_445_pause_63',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_64',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703a, 1, 'ACTION_445_pause_63']
    },
    {
        "identifier": 'ACTION_445_jmp_65',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_71']
    },
    {
        "identifier": 'ACTION_445_pause_66',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_67',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703c, 1, 'ACTION_445_pause_66']
    },
    {
        "identifier": 'ACTION_445_jmp_68',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_71']
    },
    {
        "identifier": 'ACTION_445_pause_69',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_70',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703e, 1, 'ACTION_445_pause_69']
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_71',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_72',
        "command": 'pause',
        "args": [256]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_73',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_74',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_75',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_76',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_77',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_78',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_79',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_80',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_81',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_pause_82',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_445_create_packet_at_object_coords_jmp_if_null_83',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._030_WATER_SPLASH_DROPS_SFX, AreaObjects.DUMMY_0X07, 'ACTION_445_set_sprite_sequence_84']
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_84',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_set_priority_85',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_445_inc_palette_row_by_86',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_87',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_88',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 34, 'ACTION_445_pause_94']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_89',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 35, 'ACTION_445_pause_97']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_90',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 36, 'ACTION_445_pause_100']
    },
    {
        "identifier": 'ACTION_445_pause_91',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_92',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7038, 2, 'ACTION_445_pause_91']
    },
    {
        "identifier": 'ACTION_445_jmp_93',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_102']
    },
    {
        "identifier": 'ACTION_445_pause_94',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_95',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703a, 2, 'ACTION_445_pause_94']
    },
    {
        "identifier": 'ACTION_445_jmp_96',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_102']
    },
    {
        "identifier": 'ACTION_445_pause_97',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_98',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703c, 2, 'ACTION_445_pause_97']
    },
    {
        "identifier": 'ACTION_445_jmp_99',
        "command": 'jmp',
        "args": ['ACTION_445_set_sprite_sequence_102']
    },
    {
        "identifier": 'ACTION_445_pause_100',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_not_equals_short_101',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703e, 2, 'ACTION_445_pause_100']
    },
    {
        "identifier": 'ACTION_445_set_sprite_sequence_102',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_445_set_object_memory_bits_103',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[]]
    },
    {
        "identifier": 'ACTION_445_set_700C_to_pressed_button_104',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_105',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 34, 'ACTION_445_bounce_to_xy_with_height_110']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_106',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 35, 'ACTION_445_bounce_to_xy_with_height_112']
    },
    {
        "identifier": 'ACTION_445_jmp_if_var_equals_short_107',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 36, 'ACTION_445_bounce_to_xy_with_height_114']
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_108',
        "command": 'bounce_to_xy_with_height',
        "args": [8, 40, 0]
    },
    {
        "identifier": 'ACTION_445_jmp_109',
        "command": 'jmp',
        "args": ['ACTION_445_create_packet_at_object_coords_jmp_if_null_115']
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_110',
        "command": 'bounce_to_xy_with_height',
        "args": [17, 42, 0]
    },
    {
        "identifier": 'ACTION_445_jmp_111',
        "command": 'jmp',
        "args": ['ACTION_445_create_packet_at_object_coords_jmp_if_null_115']
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_112',
        "command": 'bounce_to_xy_with_height',
        "args": [14, 26, 0]
    },
    {
        "identifier": 'ACTION_445_jmp_113',
        "command": 'jmp',
        "args": ['ACTION_445_create_packet_at_object_coords_jmp_if_null_115']
    },
    {
        "identifier": 'ACTION_445_bounce_to_xy_with_height_114',
        "command": 'bounce_to_xy_with_height',
        "args": [23, 38, 0]
    },
    {
        "identifier": 'ACTION_445_create_packet_at_object_coords_jmp_if_null_115',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._030_WATER_SPLASH_DROPS_SFX, AreaObjects.DUMMY_0X07, 'ACTION_445_jmp_116']
    },
    {
        "identifier": 'ACTION_445_jmp_116',
        "command": 'jmp',
        "args": ['ACTION_445_set_object_memory_bits_51']
    }
]
