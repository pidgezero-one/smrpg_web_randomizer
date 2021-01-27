from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_824_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_shadow_on_1',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_824_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [25, 107, 0, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_824_jmp_if_var_equals_byte_5',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 27, 'ACTION_824_set_sprite_sequence_70']
    },
    {
        "identifier": 'ACTION_824_jmp_if_random_above_66_6',
        "command": 'jmp_if_random_above_66',
        "args": [0x9e71, 'ACTION_824_shift_southwest_pixels_12']
    },
    {
        "identifier": 'ACTION_824_pause_7',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_824_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_824_set_animation_speed_13']
    },
    {
        "identifier": 'ACTION_824_shift_southwest_pixels_9',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_824_pause_10',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_824_set_animation_speed_13']
    },
    {
        "identifier": 'ACTION_824_shift_southwest_pixels_12',
        "command": 'shift_southwest_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_824_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_824_visibility_on_15',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_824_shift_southeast_steps_16',
        "command": 'shift_southeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_824_start_loop_n_times_17',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_824_walk_1_step_southwest_19',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_20',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_floating_on_21',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_824_walk_1_step_southwest_22',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_824_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_24',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x8d, 0x9e]
    },
    {
        "identifier": 'ACTION_824_floating_off_25',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_26',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_824_jump_to_height_28',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_824_shift_northwest_steps_29',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_shift_northwest_pixels_30',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_824_set_priority_31',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_shift_northwest_pixels_32',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_33',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_pause_34',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_35',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xa9, 0x9e]
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_36',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_jmp_if_bit_set_37',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_824_walk_1_step_northwest_39']
    },
    {
        "identifier": 'ACTION_824_play_sound_38',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_walk_1_step_northwest_39',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_824_set_priority_40',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_shift_northwest_steps_41',
        "command": 'shift_northwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_42',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_824_walk_1_step_southwest_43',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_44',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_floating_on_45',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_824_walk_1_step_southwest_46',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_824_pause_47',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_48',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xc8, 0x9e]
    },
    {
        "identifier": 'ACTION_824_floating_off_49',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_50',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_51',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_824_jump_to_height_52',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_824_shift_southeast_steps_53',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_54',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_pause_55',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_56',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xdd, 0x9e]
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_57',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_jmp_if_bit_set_58',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_824_shift_southeast_steps_60']
    },
    {
        "identifier": 'ACTION_824_play_sound_59',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_shift_southeast_steps_60',
        "command": 'shift_southeast_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_824_end_loop_61',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_824_start_loop_n_times_62',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_visibility_on_63',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_824_pause_64',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_visibility_off_65',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_824_pause_66',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_end_loop_67',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_824_db_68',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_824_ret_69',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_824_set_sprite_sequence_70',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_824_pause_71',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_824_visibility_on_72',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_824_jmp_if_bit_set_73',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_824_jump_to_height_78']
    },
    {
        "identifier": 'ACTION_824_jump_to_height_74',
        "command": 'jump_to_height',
        "args": [32]
    },
    {
        "identifier": 'ACTION_824_set_priority_75',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_walk_to_xy_coords_76',
        "command": 'walk_to_xy_coords',
        "args": [24, 108]
    },
    {
        "identifier": 'ACTION_824_jmp_77',
        "command": 'jmp',
        "args": ['ACTION_824_set_solidity_bits_82']
    },
    {
        "identifier": 'ACTION_824_jump_to_height_78',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_824_set_priority_79',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_walk_to_xy_coords_80',
        "command": 'walk_to_xy_coords',
        "args": [27, 114]
    },
    {
        "identifier": 'ACTION_824_set_priority_81',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_82',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_pause_83',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_84',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x20, 0x9f]
    },
    {
        "identifier": 'ACTION_824_play_sound_85',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_floating_off_86',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_87',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_jump_to_height_88',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_824_shift_southwest_steps_89',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_set_priority_90',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_91',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_floating_on_92',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_824_pause_93',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_94',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x3a, 0x9f]
    },
    {
        "identifier": 'ACTION_824_floating_off_95',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_96',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_play_sound_97',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_jump_to_height_98',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_824_shift_southwest_steps_99',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_100',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_floating_on_101',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_824_jmp_if_bit_clear_102',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_824_pause_105']
    },
    {
        "identifier": 'ACTION_824_pause_103',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_824_set_priority_104',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_pause_105',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_106',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x5a, 0x9f]
    },
    {
        "identifier": 'ACTION_824_floating_off_107',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_108',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_play_sound_109',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_jump_to_height_110',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_824_shift_southwest_steps_111',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_824_set_priority_112',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_set_solidity_bits_113',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_floating_on_114',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_824_pause_115',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_db_116',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x74, 0x9f]
    },
    {
        "identifier": 'ACTION_824_floating_off_117',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_824_clear_solidity_bits_118',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_824_play_sound_119',
        "command": 'play_sound',
        "args": [Sounds._109_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_824_walk_1_step_southwest_120',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_824_start_loop_n_times_121',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_824_visibility_on_122',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_824_pause_123',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_visibility_off_124',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_824_pause_125',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_824_end_loop_126',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_824_db_127',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_824_clear_bit_128',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_824_ret_129',
        "command": 'ret'
    }
]
