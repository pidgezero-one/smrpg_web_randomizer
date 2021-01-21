from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_176_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_176_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_176_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_176_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_176_db_5',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_176_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_176_embedded_animation_routine_7',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_176_embedded_animation_routine_8',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_set_700C_to_pressed_button_10',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_176_shadow_off_17']
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_176_shadow_off_29']
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_176_shadow_off_52']
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_176_jmp_if_bit_set_65']
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 25, 'ACTION_176_jmp_if_bit_set_77']
    },
    {
        "identifier": 'ACTION_176_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 26, 'ACTION_176_jmp_if_bit_set_120']
    },
    {
        "identifier": 'ACTION_176_shadow_off_17',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_shift_z_down_steps_24']
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_19',
        "command": 'shift_z_down_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_20',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_dec_z_coord_1_step_21',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_176_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_24',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_25',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_dec_z_coord_1_step_26',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_176_visibility_off_27',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_shadow_off_29',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_set_animation_speed_44']
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_shift_northwest_pixels_32',
        "command": 'shift_northwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_north_pixels_33',
        "command": 'shift_north_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_southeast_pixels_34',
        "command": 'shift_southeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_southwest_pixels_35',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_37',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_38',
        "command": 'shift_z_down_steps',
        "args": [13]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_39',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_40',
        "command": 'shift_z_down_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_41',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_visibility_off_42',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_shift_southeast_pixels_45',
        "command": 'shift_southeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_southwest_pixels_46',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_47',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_48',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_49',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_visibility_off_50',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_51',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_shadow_off_52',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_53',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_pause_59']
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_54',
        "command": 'shift_z_down_steps',
        "args": [13]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_55',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_dec_z_coord_1_step_56',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_176_visibility_off_57',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_58',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_pause_59',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_60',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_61',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_dec_z_coord_1_step_62',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_176_visibility_off_63',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_176_ret_64',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_65',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_shift_z_down_steps_75']
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_66',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_67',
        "command": 'shift_z_down_steps',
        "args": [20]
    },
    {
        "identifier": 'ACTION_176_pause_68',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_bpl_26_27_28_69',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_176_shadow_off_70',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_object_memory_clear_bit_71',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_176_set_solidity_bits_72',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_176_pause_73',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_jmp_74',
        "command": 'jmp',
        "args": ['ACTION_737_sequence_looping_on_0']
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_75',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_jmp_76',
        "command": 'jmp',
        "args": ['ACTION_176_pause_68']
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_77',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_shift_south_pixels_116']
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_78',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_shift_northwest_pixels_79',
        "command": 'shift_northwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_176_shift_north_pixels_80',
        "command": 'shift_north_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_southeast_pixels_81',
        "command": 'shift_southeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_shift_southwest_pixels_82',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_176_set_animation_speed_83',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_84',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_shadow_off_85',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_86',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_87',
        "command": 'shift_z_down_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_shadow_on_88',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_176_set_vram_priority_89',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_90',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_set_solidity_bits_91',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_92',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_176_bpl_26_27_28_93',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_176_object_memory_clear_bit_94',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_176_set_solidity_bits_95',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_clear_96',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 0, 'ACTION_176_db_99']
    },
    {
        "identifier": 'ACTION_176_pause_97',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_jmp_98',
        "command": 'jmp',
        "args": ['ACTION_176_face_northeast_107']
    },
    {
        "identifier": 'ACTION_176_db_99',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_176_embedded_animation_routine_100',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_176_embedded_animation_routine_101',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_on_102',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_176_shift_north_pixels_103',
        "command": 'shift_north_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_face_southwest_104',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_105',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_bpl_26_27_28_106',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_176_face_northeast_107',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_176_pause_108',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_face_northwest_109',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_176_pause_110',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_face_southwest_111',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_176_pause_112',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_face_southeast_113',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_176_pause_114',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_jmp_115',
        "command": 'jmp',
        "args": ['ACTION_176_face_northeast_107']
    },
    {
        "identifier": 'ACTION_176_shift_south_pixels_116',
        "command": 'shift_south_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_117',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_118',
        "command": 'shift_z_down_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_176_jmp_119',
        "command": 'jmp',
        "args": ['ACTION_176_bpl_26_27_28_93']
    },
    {
        "identifier": 'ACTION_176_jmp_if_bit_set_120',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 0, 'ACTION_176_fixed_f_coord_off_140']
    },
    {
        "identifier": 'ACTION_176_shift_south_pixels_121',
        "command": 'shift_south_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_122',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_123',
        "command": 'shift_z_down_steps',
        "args": [13]
    },
    {
        "identifier": 'ACTION_176_pause_124',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_bpl_26_27_28_125',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_176_shadow_off_126',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_176_object_memory_clear_bit_127',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_176_set_solidity_bits_128',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_176_pause_129',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_176_shift_southwest_steps_130',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_176_shift_northeast_steps_131',
        "command": 'shift_northeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_176_pause_132',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_face_southeast_133',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_176_pause_134',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_shift_southwest_steps_135',
        "command": 'shift_southwest_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_176_pause_136',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_face_northwest_137',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_176_pause_138',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_176_jmp_139',
        "command": 'jmp',
        "args": ['ACTION_176_shift_northeast_steps_131']
    },
    {
        "identifier": 'ACTION_176_fixed_f_coord_off_140',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_176_shift_z_down_steps_141',
        "command": 'shift_z_down_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_176_jmp_142',
        "command": 'jmp',
        "args": ['ACTION_176_pause_124']
    }
]
