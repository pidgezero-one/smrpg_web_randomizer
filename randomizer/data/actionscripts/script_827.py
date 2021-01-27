from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_827_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_827_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_827_set_700C_to_current_level_3',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_827_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [473, 'ACTION_827_floating_off_72']
    },
    {
        "identifier": 'ACTION_827_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_827_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [29, 'ACTION_827_shadow_off_53']
    },
    {
        "identifier": 'ACTION_827_mem_compare_val_7',
        "command": 'mem_compare_val',
        "args": [24]
    },
    {
        "identifier": 'ACTION_827_jmp_if_comparison_result_is_greater_or_equal_8',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_827_set_700C_to_pressed_button_33']
    },
    {
        "identifier": 'ACTION_827_set_700C_to_pressed_button_9',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_827_add_10',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_827_load_mem_11',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_827_pause_12',
        "command": 'pause',
        "args": [49]
    },
    {
        "identifier": 'ACTION_827_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_827_db_14',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_827_transfer_to_xyzf_15',
        "command": 'transfer_to_xyzf',
        "args": [1, 71, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_visibility_on_17',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_827_object_memory_clear_bit_18',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_19',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_dec_z_coord_1_step_21',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_walk_1_step_southeast_23',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_dec_z_coord_1_step_25',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_27',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_827_object_memory_set_bit_28',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_pause_29',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_visibility_off_30',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_pause_31',
        "command": 'pause',
        "args": [49]
    },
    {
        "identifier": 'ACTION_827_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_827_db_14']
    },
    {
        "identifier": 'ACTION_827_set_700C_to_pressed_button_33',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_827_add_34',
        "command": 'add',
        "args": [0x700c, 65513]
    },
    {
        "identifier": 'ACTION_827_load_mem_35',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_827_pause_36',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'ACTION_827_end_loop_37',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_827_db_38',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_827_transfer_to_xyzf_39',
        "command": 'transfer_to_xyzf',
        "args": [7, 70, 4, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_visibility_on_41',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_827_object_memory_clear_bit_42',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_43',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_dec_z_coord_1_step_45',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_46',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_47',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_827_object_memory_set_bit_48',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_pause_49',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_visibility_off_50',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_pause_51',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'ACTION_827_jmp_52',
        "command": 'jmp',
        "args": ['ACTION_827_db_38']
    },
    {
        "identifier": 'ACTION_827_shadow_off_53',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_827_transfer_to_xyzf_54',
        "command": 'transfer_to_xyzf',
        "args": [11, 58, 6, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_55',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_visibility_on_56',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_827_object_memory_clear_bit_57',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_58',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_827_shadow_on_59',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_60',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_61',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_dec_z_coord_1_step_62',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_827_play_sound_63',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_827_set_animation_speed_64',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_827_shadow_off_65',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_827_shift_southeast_steps_66',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_827_object_memory_set_bit_67',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_pause_68',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_visibility_off_69',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_pause_70',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_827_jmp_71',
        "command": 'jmp',
        "args": ['ACTION_827_shadow_off_53']
    },
    {
        "identifier": 'ACTION_827_floating_off_72',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_827_clear_solidity_bits_73',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_827_jmp_if_bit_set_74',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_827_jmp_if_bit_clear_100']
    },
    {
        "identifier": 'ACTION_827_transfer_to_xyzf_75',
        "command": 'transfer_to_xyzf',
        "args": [7, 101, 28, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_827_pause_76',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'ACTION_827_jump_to_height_77',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_827_shadow_on_78',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_827_shift_southeast_pixels_79',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_827_pause_80',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_827_visibility_on_81',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_827_object_memory_clear_bit_82',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_set_solidity_bits_83',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_827_floating_on_84',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_827_pause_85',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_db_86',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x1a, 0xdf, 0xa1]
    },
    {
        "identifier": 'ACTION_827_play_sound_87',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_827_pause_88',
        "command": 'pause',
        "args": [218]
    },
    {
        "identifier": 'ACTION_827_jmp_if_bit_set_89',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 0, 'ACTION_827_clear_bit_91']
    },
    {
        "identifier": 'ACTION_827_play_sound_90',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_827_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x704d, 0]
    },
    {
        "identifier": 'ACTION_827_shadow_off_92',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_827_floating_off_93',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_827_clear_solidity_bits_94',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_827_shift_northwest_steps_95',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_827_object_memory_set_bit_96',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_pause_97',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_visibility_off_98',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_jmp_99',
        "command": 'jmp',
        "args": ['ACTION_827_jmp_if_bit_set_74']
    },
    {
        "identifier": 'ACTION_827_jmp_if_bit_clear_100',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'ACTION_827_jmp_if_bit_set_74']
    },
    {
        "identifier": 'ACTION_827_transfer_to_xyzf_101',
        "command": 'transfer_to_xyzf',
        "args": [8, 58, 12, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_827_pause_102',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_827_jump_to_height_103',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_827_shadow_on_104',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_827_shift_southeast_pixels_105',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_827_pause_106',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_827_visibility_on_107',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_827_object_memory_clear_bit_108',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_set_solidity_bits_109',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_827_floating_on_110',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_827_pause_111',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_db_112',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x1a, 0x1e, 0xa2]
    },
    {
        "identifier": 'ACTION_827_play_sound_113',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_827_pause_short_114',
        "command": 'pause_short',
        "args": [258]
    },
    {
        "identifier": 'ACTION_827_jmp_if_bit_set_115',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 0, 'ACTION_827_clear_bit_117']
    },
    {
        "identifier": 'ACTION_827_play_sound_116',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_827_clear_bit_117',
        "command": 'clear_bit',
        "args": [0x704d, 0]
    },
    {
        "identifier": 'ACTION_827_shadow_off_118',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_827_floating_off_119',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_827_clear_solidity_bits_120',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_827_shift_northwest_steps_121',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_827_object_memory_set_bit_122',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_827_pause_123',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_827_visibility_off_124',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_827_jmp_125',
        "command": 'jmp',
        "args": ['ACTION_827_jmp_if_bit_clear_100']
    }
]
