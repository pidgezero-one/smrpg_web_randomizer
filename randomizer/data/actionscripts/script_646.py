from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_646_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_646_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_646_pause_5',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_646_pause_7',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_end_loop_8',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_646_object_memory_modify_bits_11',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_east_12',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_646_pause_13',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_646_shift_east_steps_14',
        "command": 'shift_east_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_set_priority_15',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_east_16',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_646_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_face_southwest_18',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_pause_19',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_646_face_southeast_20',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_pause_21',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_646_end_loop_22',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_646_fixed_f_coord_on_23',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_646_shift_south_steps_24',
        "command": 'shift_south_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_fixed_f_coord_off_25',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_646_walk_1_step_southeast_26',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_646_face_northeast_27',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_646_pause_28',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_shift_z_up_steps_30',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_northeast_32',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_646_pause_33',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_face_southeast_34',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_pause_35',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_face_northeast_37',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_646_add_z_coord_1_step_38',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_shift_northeast_steps_40',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_face_southeast_41',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_42',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_646_pause_43',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_start_loop_n_times_44',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_face_southwest_45',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_pause_46',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_face_southeast_47',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_pause_48',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_646_end_loop_49',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_646_pause_50',
        "command": 'pause',
        "args": [17]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_51',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_set_bit_52',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_53',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_54',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_object_memory_modify_bits_55',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_east_56',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_57',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_58',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_59',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_60',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_646_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_646_pause_62',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_63',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_southwest_64',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_646_walk_1_step_southeast_65',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_646_set_priority_66',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_shift_northeast_steps_67',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_646_pause_68',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_69',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_646_pause_70',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_71',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_72',
        "command": 'jump_to_height',
        "args": [104]
    },
    {
        "identifier": 'ACTION_646_shift_northeast_steps_73',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_74',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_75',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_646_shift_northeast_steps_76',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_77',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_646_set_bit_78',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_646_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_646_pause_80',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_81',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_start_loop_n_times_82',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_shift_z_up_pixels_83',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_shift_z_down_pixels_84',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_end_loop_85',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_86',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_87',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_88',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_fixed_f_coord_on_89',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_646_walk_1_step_east_90',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_646_fixed_f_coord_off_91',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_646_face_southwest_92',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_pause_93',
        "command": 'pause',
        "args": [72]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_94',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_95',
        "command": 'jump_to_height',
        "args": [54]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_96',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_646_pause_97',
        "command": 'pause',
        "args": [36]
    },
    {
        "identifier": 'ACTION_646_face_southeast_98',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_pause_99',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_100',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_101',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_102',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_646_walk_1_step_east_103',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_646_set_bit_104',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_646_clear_bit_105',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_106',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_pause_107',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_646_face_southeast_108',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_109',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_start_loop_n_times_110',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_shift_z_up_pixels_111',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_shift_z_down_pixels_112',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_646_end_loop_113',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_114',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jump_to_height_115',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_646_shift_southeast_steps_116',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_646_face_southwest_117',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_118',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_119',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_pause_120',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_646_jmp_if_bit_clear_121',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_646_pause_120']
    },
    {
        "identifier": 'ACTION_646_reset_properties_122',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_646_pause_123',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_646_set_sprite_sequence_124',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_646_pause_125',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_646_set_animation_speed_126',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_646_jmp_if_bit_set_127',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 4, 'ACTION_646_face_southwest_130']
    },
    {
        "identifier": 'ACTION_646_face_southeast_128',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_646_ret_129',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_646_face_southwest_130',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_646_ret_131',
        "command": 'ret'
    }
]
