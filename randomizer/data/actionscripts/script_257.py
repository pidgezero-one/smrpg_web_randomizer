from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_257_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_700C_to_current_level_2',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_257_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 117, 'ACTION_257_set_bit_55']
    },
    {
        "identifier": 'ACTION_257_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_257_set_bit_8']
    },
    {
        "identifier": 'ACTION_257_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_257_set_bit_8']
    },
    {
        "identifier": 'ACTION_257_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_257_pause_5']
    },
    {
        "identifier": 'ACTION_257_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_257_pause_9',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_add_z_coord_1_step_11',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_pause_14',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_17',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_walk_1_step_southwest_19',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_steps_21',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_22',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_steps_23',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_steps_25',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_26',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_walk_1_step_southwest_27',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_28',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_29',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_30',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_walk_1_step_northeast_32',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_steps_34',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_steps_36',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_37',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_steps_38',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_walk_1_step_northeast_40',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_41',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_42',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_257_set_sprite_sequence_45']
    },
    {
        "identifier": 'ACTION_257_jmp_44',
        "command": 'jmp',
        "args": ['ACTION_257_shift_southwest_pixels_17']
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_45',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_pause_46',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_47',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_48',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_dec_z_coord_1_step_49',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_257_set_bit_50',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_257_jmp_51',
        "command": 'jmp',
        "args": ['ACTION_257_pause_5']
    },
    {
        "identifier": 'ACTION_257_pause_52',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_257_jmp_if_bit_clear_53',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_257_set_bit_55']
    },
    {
        "identifier": 'ACTION_257_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_257_pause_52']
    },
    {
        "identifier": 'ACTION_257_set_bit_55',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_257_pause_56',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_57',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_z_up_pixels_58',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_59',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_60',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_pause_61',
        "command": 'pause',
        "args": [14]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_62',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_63',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_south_pixels_64',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_65',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_south_pixels_66',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_67',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_68',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_69',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_steps_70',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_71',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_72',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_73',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_74',
        "command": 'shift_southwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_75',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_76',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_77',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_78',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_79',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_80',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_81',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_82',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_steps_83',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_84',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_85',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_86',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_87',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_88',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_89',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_jmp_if_bit_set_90',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_257_shift_northeast_pixels_105']
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_91',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_92',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_93',
        "command": 'shift_southwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_94',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_95',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_96',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_steps_97',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_98',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_99',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_100',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_101',
        "command": 'shift_southwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_102',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_257_shift_southwest_pixels_103',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_257_jmp_104',
        "command": 'jmp',
        "args": ['ACTION_257_shift_northeast_pixels_77']
    },
    {
        "identifier": 'ACTION_257_shift_northeast_pixels_105',
        "command": 'shift_northeast_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_257_walk_1_step_north_106',
        "command": 'walk_1_step_north'
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_107',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_pause_108',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_257_set_sprite_sequence_109',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_set_animation_speed_110',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_257_shift_z_down_pixels_111',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_257_set_bit_112',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_257_jmp_113',
        "command": 'jmp',
        "args": ['ACTION_257_pause_52']
    }
]
