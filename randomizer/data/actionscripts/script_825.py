from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_825_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_825_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 474, 'ACTION_825_set_700C_to_pressed_button_30']
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_825_visibility_off_3',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_825_floating_off_4',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_825_transfer_to_xyzf_5',
        "command": 'transfer_to_xyzf',
        "args": [22, 54, 18, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_825_sequence_playback_off_6',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_825_pause_7',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_8',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_825_pause_9',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_825_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_825_visibility_on_11',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_825_floating_on_12',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_825_object_memory_clear_bit_13',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_825_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_db_15',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x14, 0xaf, 0x9f]
    },
    {
        "identifier": 'ACTION_825_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_825_sequence_playback_on_17',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_825_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_825_pause_19',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_20',
        "command": 'jump_to_height',
        "args": [160]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_21',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_southeast_steps_22',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_825_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_db_24',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x14, 0xc6, 0x9f]
    },
    {
        "identifier": 'ACTION_825_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_26',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_825_clear_solidity_bits_27',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_825_shift_southeast_steps_28',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_825_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_825_set_animation_speed_2']
    },
    {
        "identifier": 'ACTION_825_set_700C_to_pressed_button_30',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_825_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 24, 'ACTION_825_visibility_off_69']
    },
    {
        "identifier": 'ACTION_825_mem_compare_32',
        "command": 'mem_compare',
        "args": [0x700c, 21]
    },
    {
        "identifier": 'ACTION_825_jmp_if_comparison_result_is_greater_or_equal_33',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_825_set_700C_to_pressed_button_53']
    },
    {
        "identifier": 'ACTION_825_pause_34',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_jmp_if_bit_clear_35',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_825_pause_34']
    },
    {
        "identifier": 'ACTION_825_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_db_37',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x18, 0xec, 0x9f]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_38',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_down_pixels_39',
        "command": 'shift_z_down_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_down_pixels_41',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_42',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_down_pixels_43',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_44',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_down_pixels_45',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_825_pause_46',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_47',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_down_pixels_48',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_pause_49',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_50',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_z_up_pixels_51',
        "command": 'shift_z_up_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_825_jmp_52',
        "command": 'jmp',
        "args": ['ACTION_825_pause_34']
    },
    {
        "identifier": 'ACTION_825_set_700C_to_pressed_button_53',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_825_add_54',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_825_load_mem_55',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_825_pause_56',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_825_end_loop_57',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_825_set_priority_58',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_59',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_825_turn_clockwise_45_degrees_60',
        "command": 'turn_clockwise_45_degrees'
    },
    {
        "identifier": 'ACTION_825_shift_f_direction_steps_61',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_825_start_loop_n_times_62',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_825_turn_clockwise_45_degrees_n_times_63',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_825_pause_64',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_825_end_loop_65',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_825_turn_random_direction_66',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_825_walk_1_step_f_direction_67',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_825_jmp_68',
        "command": 'jmp',
        "args": ['ACTION_825_turn_clockwise_45_degrees_60']
    },
    {
        "identifier": 'ACTION_825_visibility_off_69',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_825_floating_off_70',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_825_transfer_to_xyzf_71',
        "command": 'transfer_to_xyzf',
        "args": [20, 31, 2, RadialDirections.SOUTHEAST]
    },
    {
        "identifier": 'ACTION_825_set_sprite_sequence_72',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_825_sequence_playback_off_73',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_825_set_solidity_bits_74',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_825_set_solidity_bits_75',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_825_jmp_if_bit_clear_76',
        "command": 'jmp_if_bit_clear',
        "args": [0x7096, 3, 'ACTION_825_jump_to_height_78']
    },
    {
        "identifier": 'ACTION_825_pause_77',
        "command": 'pause',
        "args": [130]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_78',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_825_pause_79',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_825_visibility_on_80',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_825_floating_on_81',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_825_object_memory_clear_bit_82',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_825_set_bit_83',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_825_pause_84',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_db_85',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x18, 0x50, 0xa0]
    },
    {
        "identifier": 'ACTION_825_clear_bit_86',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_825_jmp_if_bit_set_87',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 3, 'ACTION_825_visibility_off_69']
    },
    {
        "identifier": 'ACTION_825_play_sound_88',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_825_sequence_playback_on_89',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_825_set_sprite_sequence_90',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_825_pause_91',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_825_object_memory_set_bit_92',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_825_play_sound_93',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 4]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_94',
        "command": 'jump_to_height',
        "args": [160]
    },
    {
        "identifier": 'ACTION_825_clear_solidity_bits_95',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_825_set_animation_speed_96',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_825_shift_southeast_steps_97',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_825_pause_98',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_825_db_99',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x18, 0x74, 0xa0]
    },
    {
        "identifier": 'ACTION_825_play_sound_100',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_825_jump_to_height_101',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_825_clear_solidity_bits_102',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_825_shift_southeast_steps_103',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_825_jmp_104',
        "command": 'jmp',
        "args": ['ACTION_825_visibility_off_69']
    }
]
