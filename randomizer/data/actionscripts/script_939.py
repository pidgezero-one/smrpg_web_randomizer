from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_939_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 0, 'ACTION_939_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 1, 'ACTION_939_set_sprite_sequence_44']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 2, 'ACTION_939_set_sprite_sequence_57']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_byte_4',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 3, 'ACTION_939_inc_palette_row_by_70']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_byte_5',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 4, 'ACTION_939_inc_palette_row_by_86']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'ACTION_939_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 1, 'ACTION_939_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 2, 'ACTION_939_set_sprite_sequence_14']
    },
    {
        "identifier": 'ACTION_939_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_939_pause_7']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_939_pause_7']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 4]
    },
    {
        "identifier": 'ACTION_939_jump_to_height_16',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_939_pause_17',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_939_floating_off_18',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_939_set_animation_speed_19',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_939_shift_south_pixels_20',
        "command": 'shift_south_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_939_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 4]
    },
    {
        "identifier": 'ACTION_939_set_700C_to_pressed_button_22',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_939_add_23',
        "command": 'add',
        "args": [0x700c, 65515]
    },
    {
        "identifier": 'ACTION_939_jmp_if_700C_equals_short_24',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_939_set_object_memory_bits_29']
    },
    {
        "identifier": 'ACTION_939_jmp_if_700C_equals_short_25',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_939_set_object_memory_bits_31']
    },
    {
        "identifier": 'ACTION_939_jmp_if_700C_equals_short_26',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_939_set_object_memory_bits_33']
    },
    {
        "identifier": 'ACTION_939_jmp_if_700C_equals_short_27',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_939_set_object_memory_bits_35']
    },
    {
        "identifier": 'ACTION_939_jmp_if_700C_equals_short_28',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_939_set_object_memory_bits_37']
    },
    {
        "identifier": 'ACTION_939_set_object_memory_bits_29',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0]]
    },
    {
        "identifier": 'ACTION_939_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_set_object_memory_bits_31',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [1]]
    },
    {
        "identifier": 'ACTION_939_jmp_32',
        "command": 'jmp',
        "args": ['ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_set_object_memory_bits_33',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0, 1]]
    },
    {
        "identifier": 'ACTION_939_jmp_34',
        "command": 'jmp',
        "args": ['ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_set_object_memory_bits_35',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [2]]
    },
    {
        "identifier": 'ACTION_939_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_set_object_memory_bits_37',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0, 2]]
    },
    {
        "identifier": 'ACTION_939_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_pause_39',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_40',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 2, 'ACTION_939_pause_39']
    },
    {
        "identifier": 'ACTION_939_visibility_off_41',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_939_pause_42',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_939_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_44',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_shift_xy_pixels_45',
        "command": 'shift_xy_pixels',
        "args": [244, 3]
    },
    {
        "identifier": 'ACTION_939_pause_46',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_47',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 0, 'ACTION_939_set_sprite_sequence_51']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_48',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'ACTION_939_set_sprite_sequence_53']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_49',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'ACTION_939_set_sprite_sequence_55']
    },
    {
        "identifier": 'ACTION_939_jmp_50',
        "command": 'jmp',
        "args": ['ACTION_939_pause_46']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_51',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_52',
        "command": 'jmp',
        "args": ['ACTION_939_pause_46']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_53',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_939_pause_46']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_55',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_56',
        "command": 'jmp',
        "args": ['ACTION_939_play_sound_15']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_57',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_shift_xy_pixels_58',
        "command": 'shift_xy_pixels',
        "args": [232, 8]
    },
    {
        "identifier": 'ACTION_939_pause_59',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_60',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 0, 'ACTION_939_set_sprite_sequence_64']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_61',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 1, 'ACTION_939_set_sprite_sequence_66']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_62',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 2, 'ACTION_939_set_sprite_sequence_68']
    },
    {
        "identifier": 'ACTION_939_jmp_63',
        "command": 'jmp',
        "args": ['ACTION_939_pause_59']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_64',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_65',
        "command": 'jmp',
        "args": ['ACTION_939_pause_59']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_66',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_67',
        "command": 'jmp',
        "args": ['ACTION_939_pause_59']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_68',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_69',
        "command": 'jmp',
        "args": ['ACTION_939_play_sound_15']
    },
    {
        "identifier": 'ACTION_939_inc_palette_row_by_70',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_71',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_shift_xy_pixels_72',
        "command": 'shift_xy_pixels',
        "args": [12, 3]
    },
    {
        "identifier": 'ACTION_939_pause_73',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 0, 'ACTION_939_set_sprite_sequence_78']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_75',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 1, 'ACTION_939_set_sprite_sequence_80']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_76',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 2, 'ACTION_939_set_sprite_sequence_82']
    },
    {
        "identifier": 'ACTION_939_jmp_77',
        "command": 'jmp',
        "args": ['ACTION_939_pause_73']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_78',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_79',
        "command": 'jmp',
        "args": ['ACTION_939_pause_73']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_80',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_81',
        "command": 'jmp',
        "args": ['ACTION_939_pause_73']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_82',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jump_to_subroutine_83',
        "command": 'jump_to_subroutine',
        "args": [0xaf0f]
    },
    {
        "identifier": 'ACTION_939_inc_palette_row_by_84',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_939_ret_85',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_939_inc_palette_row_by_86',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_87',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_shift_xy_pixels_88',
        "command": 'shift_xy_pixels',
        "args": [24, 8]
    },
    {
        "identifier": 'ACTION_939_pause_89',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_90',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 0, 'ACTION_939_set_sprite_sequence_94']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_91',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 1, 'ACTION_939_set_sprite_sequence_96']
    },
    {
        "identifier": 'ACTION_939_jmp_if_var_equals_short_92',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 2, 'ACTION_939_set_sprite_sequence_98']
    },
    {
        "identifier": 'ACTION_939_jmp_93',
        "command": 'jmp',
        "args": ['ACTION_939_pause_89']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_94',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_95',
        "command": 'jmp',
        "args": ['ACTION_939_pause_89']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_96',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jmp_97',
        "command": 'jmp',
        "args": ['ACTION_939_pause_89']
    },
    {
        "identifier": 'ACTION_939_set_sprite_sequence_98',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_939_jump_to_subroutine_99',
        "command": 'jump_to_subroutine',
        "args": [0xaf0f]
    },
    {
        "identifier": 'ACTION_939_inc_palette_row_by_100',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_939_ret_101',
        "command": 'ret'
    }
]
