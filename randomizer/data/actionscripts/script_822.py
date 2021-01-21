from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_822_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_822_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 21, 'ACTION_822_pause_119']
    },
    {
        "identifier": 'ACTION_822_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_822_pause_63']
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_on_7',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_822_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_9',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_southeast_10',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_822_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_off_12',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_822_face_southwest_13',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_822_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_pause_16',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_pause_17',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_20',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_21',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_22',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_24',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x17, 0xd3, 0x9c]
    },
    {
        "identifier": 'ACTION_822_set_bit_25',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_27',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_southeast_29',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_30',
        "command": 'shift_northeast_steps',
        "args": [16]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_31',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_34',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_35',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_36',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_pause_37',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_38',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x17, 0xf4, 0x9c]
    },
    {
        "identifier": 'ACTION_822_set_bit_39',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_41',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_43',
        "command": 'shift_northwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_44',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_45',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_46',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_47',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_48',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_49',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_50',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_51',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_52',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_53',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_54',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_55',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x17, 0x1c, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_56',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_57',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_58',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_59',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_60',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_visibility_off_61',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_822_ret_62',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_822_pause_63',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_64',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_on_65',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_66',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_67',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_68',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_69',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_pause_70',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_off_71',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_822_face_southwest_72',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_73',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_74',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_pause_75',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_76',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_77',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_78',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_79',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_80',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_81',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_82',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_83',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x16, 0x58, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_84',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_85',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_86',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_87',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_88',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_89',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_90',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_91',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_92',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_93',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_94',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_95',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x16, 0x76, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_96',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_97',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_98',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_99',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_100',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_101',
        "command": 'shift_northeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_102',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_southeast_103',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_822_shift_southwest_steps_104',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_105',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_106',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_107',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_108',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_109',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_110',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_111',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x16, 0x9b, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_112',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_113',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_114',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_115',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_116',
        "command": 'shift_northeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_822_visibility_off_117',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_822_ret_118',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_822_pause_119',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_pause_120',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_121',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_on_122',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_822_play_sound_123',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_124',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_northeast_125',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_822_pause_126',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_822_fixed_f_coord_off_127',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_822_face_southwest_128',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_822_play_sound_129',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_130',
        "command": 'shift_northeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_131',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_132',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_133',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_134',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_135',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_136',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_137',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x15, 0xd2, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_138',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_139',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_140',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_141',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_southeast_142',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_143',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_northwest_144',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_822_shift_northwest_steps_145',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_146',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_147',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_148',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_149',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_150',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_151',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_152',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_153',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x15, 0xf6, 0x9d]
    },
    {
        "identifier": 'ACTION_822_set_bit_154',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_155',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_156',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_157',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_walk_1_step_northeast_158',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_822_walk_1_step_southeast_159',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_822_shift_southeast_steps_160',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_161',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_162',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_play_sound_163',
        "command": 'play_sound',
        "args": [Sounds._030_SURPRISED_MONSTER, 4]
    },
    {
        "identifier": 'ACTION_822_jump_to_height_164',
        "command": 'jump_to_height',
        "args": [105]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_165',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_822_set_solidity_bits_166',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_pause_167',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_822_db_168',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x15, 0x18, 0x9e]
    },
    {
        "identifier": 'ACTION_822_set_bit_169',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_822_play_sound_170',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_822_clear_solidity_bits_171',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_822_set_animation_speed_172',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_822_shift_northeast_steps_173',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_822_visibility_off_174',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_822_ret_175',
        "command": 'ret'
    }
]
