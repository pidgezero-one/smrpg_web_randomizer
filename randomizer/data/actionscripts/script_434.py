from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_434_jump_to_subroutine_0',
        "command": 'jump_to_subroutine',
        "args": [0x4fa4]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_434_shadow_off_30']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [22, 'ACTION_434_shadow_off_84']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [23, 'ACTION_434_shadow_off_140']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [24, 'ACTION_434_shadow_on_214']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [25, 'ACTION_434_shadow_off_253']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [26, 'ACTION_434_shadow_off_281']
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_8',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_all_bits_clear_9',
        "command": 'jmp_if_700C_all_bits_clear',
        "args": [[0], 'ACTION_434_shadow_on_13']
    },
    {
        "identifier": 'ACTION_434_shadow_off_10',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_11',
        "command": 'shirt_to_xy_coords',
        "args": [7, 48]
    },
    {
        "identifier": 'ACTION_434_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_22']
    },
    {
        "identifier": 'ACTION_434_shadow_on_13',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_14',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_15',
        "command": 'walk_to_xy_coords',
        "args": [6, 49]
    },
    {
        "identifier": 'ACTION_434_shadow_off_16',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_17',
        "command": 'walk_to_xy_coords',
        "args": [7, 48]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_18',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_19',
        "command": 'mem_700C_and_const',
        "args": [0xfffe]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_20',
        "command": 'mem_700C_or_const',
        "args": [0x0001]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_21',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_22',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_23',
        "command": 'walk_to_xy_coords',
        "args": [6, 49]
    },
    {
        "identifier": 'ACTION_434_shadow_on_24',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_25',
        "command": 'walk_to_xy_coords',
        "args": [4, 53]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_26',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_27',
        "command": 'mem_700C_and_const',
        "args": [0xfffe]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_28',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_14']
    },
    {
        "identifier": 'ACTION_434_shadow_off_30',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_31',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_32',
        "command": 'mem_700C_and_const',
        "args": [0x0006]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_33',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [2, 'ACTION_434_jmp_if_700C_not_equals_short_36']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_34',
        "command": 'shirt_to_xy_coords',
        "args": [10, 39]
    },
    {
        "identifier": 'ACTION_434_jmp_35',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_52']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_36',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [4, 'ACTION_434_jmp_if_700C_not_equals_short_39']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_37',
        "command": 'shirt_to_xy_coords',
        "args": [15, 37]
    },
    {
        "identifier": 'ACTION_434_jmp_38',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_63']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_39',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [6, 'ACTION_434_jump_to_subroutine_42']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_40',
        "command": 'shirt_to_xy_coords',
        "args": [10, 39]
    },
    {
        "identifier": 'ACTION_434_jmp_41',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_74']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_42',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_43',
        "command": 'walk_to_xy_coords',
        "args": [8, 44]
    },
    {
        "identifier": 'ACTION_434_shadow_on_44',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_45',
        "command": 'walk_to_xy_coords',
        "args": [10, 40]
    },
    {
        "identifier": 'ACTION_434_shadow_off_46',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_47',
        "command": 'walk_to_xy_coords',
        "args": [10, 39]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_48',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_49',
        "command": 'mem_700C_and_const',
        "args": [0xfff9]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_50',
        "command": 'mem_700C_or_const',
        "args": [0x0002]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_51',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_52',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_53',
        "command": 'walk_to_xy_coords',
        "args": [11, 37]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_54',
        "command": 'walk_to_xy_coords',
        "args": [12, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_on_55',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_56',
        "command": 'walk_to_xy_coords',
        "args": [14, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_off_57',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_58',
        "command": 'walk_to_xy_coords',
        "args": [15, 37]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_59',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_60',
        "command": 'mem_700C_and_const',
        "args": [0xfff9]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_61',
        "command": 'mem_700C_or_const',
        "args": [0x0004]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_62',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_63',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_64',
        "command": 'walk_to_xy_coords',
        "args": [14, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_on_65',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_66',
        "command": 'walk_to_xy_coords',
        "args": [12, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_off_67',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_68',
        "command": 'walk_to_xy_coords',
        "args": [11, 37]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_69',
        "command": 'walk_to_xy_coords',
        "args": [10, 39]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_70',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_71',
        "command": 'mem_700C_and_const',
        "args": [0xfff9]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_72',
        "command": 'mem_700C_or_const',
        "args": [0x0006]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_73',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_74',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_75',
        "command": 'walk_to_xy_coords',
        "args": [10, 40]
    },
    {
        "identifier": 'ACTION_434_shadow_on_76',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_77',
        "command": 'walk_to_xy_coords',
        "args": [8, 44]
    },
    {
        "identifier": 'ACTION_434_shadow_off_78',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_79',
        "command": 'walk_to_xy_coords',
        "args": [7, 46]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_80',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_81',
        "command": 'mem_700C_and_const',
        "args": [0xfff9]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_82',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_83',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_42']
    },
    {
        "identifier": 'ACTION_434_shadow_off_84',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_85',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_86',
        "command": 'mem_700C_and_const',
        "args": [0x0018]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_87',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [8, 'ACTION_434_jmp_if_700C_not_equals_short_90']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_88',
        "command": 'shirt_to_xy_coords',
        "args": [11, 26]
    },
    {
        "identifier": 'ACTION_434_jmp_89',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_106']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_90',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [16, 'ACTION_434_jmp_if_700C_not_equals_short_93']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_91',
        "command": 'shirt_to_xy_coords',
        "args": [6, 38]
    },
    {
        "identifier": 'ACTION_434_jmp_92',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_118']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_93',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [24, 'ACTION_434_jump_to_subroutine_96']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_94',
        "command": 'shirt_to_xy_coords',
        "args": [11, 26]
    },
    {
        "identifier": 'ACTION_434_jmp_95',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_130']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_96',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_97',
        "command": 'walk_to_xy_coords',
        "args": [15, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_on_98',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_99',
        "command": 'walk_to_xy_coords',
        "args": [11, 27]
    },
    {
        "identifier": 'ACTION_434_shadow_off_100',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_101',
        "command": 'walk_to_xy_coords',
        "args": [11, 26]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_102',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_103',
        "command": 'mem_700C_and_const',
        "args": [0xffe7]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_104',
        "command": 'mem_700C_or_const',
        "args": [0x0008]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_105',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_106',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_107',
        "command": 'walk_to_xy_coords',
        "args": [10, 27]
    },
    {
        "identifier": 'ACTION_434_shadow_on_108',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_109',
        "command": 'walk_to_xy_coords',
        "args": [8, 32]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_110',
        "command": 'walk_to_xy_coords',
        "args": [8, 34]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_111',
        "command": 'walk_to_xy_coords',
        "args": [6, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_off_112',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_113',
        "command": 'walk_to_xy_coords',
        "args": [6, 38]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_114',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_115',
        "command": 'mem_700C_and_const',
        "args": [0xffe7]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_116',
        "command": 'mem_700C_or_const',
        "args": [0x0010]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_117',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_118',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_119',
        "command": 'walk_to_xy_coords',
        "args": [6, 37]
    },
    {
        "identifier": 'ACTION_434_shadow_on_120',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_121',
        "command": 'walk_to_xy_coords',
        "args": [8, 34]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_122',
        "command": 'walk_to_xy_coords',
        "args": [8, 32]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_123',
        "command": 'walk_to_xy_coords',
        "args": [10, 27]
    },
    {
        "identifier": 'ACTION_434_shadow_off_124',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_125',
        "command": 'walk_to_xy_coords',
        "args": [11, 26]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_126',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_127',
        "command": 'mem_700C_and_const',
        "args": [0xffe7]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_128',
        "command": 'mem_700C_or_const',
        "args": [0x0018]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_129',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_130',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_131',
        "command": 'walk_to_xy_coords',
        "args": [11, 27]
    },
    {
        "identifier": 'ACTION_434_shadow_on_132',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_133',
        "command": 'walk_to_xy_coords',
        "args": [15, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_off_134',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_135',
        "command": 'walk_to_xy_coords',
        "args": [16, 36]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_136',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_137',
        "command": 'mem_700C_and_const',
        "args": [0xffe7]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_138',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_139',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_96']
    },
    {
        "identifier": 'ACTION_434_shadow_off_140',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_141',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_142',
        "command": 'mem_700C_and_const',
        "args": [0x00e0]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_143',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [32, 'ACTION_434_jmp_if_700C_not_equals_short_147']
    },
    {
        "identifier": 'ACTION_434_shadow_on_144',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_145',
        "command": 'shirt_to_xy_coords',
        "args": [8, 19]
    },
    {
        "identifier": 'ACTION_434_jmp_146',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_168']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_147',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [64, 'ACTION_434_jmp_if_700C_not_equals_short_150']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_148',
        "command": 'shirt_to_xy_coords',
        "args": [11, 24]
    },
    {
        "identifier": 'ACTION_434_jmp_149',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_176']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_150',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [96, 'ACTION_434_jmp_if_700C_not_equals_short_153']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_151',
        "command": 'shirt_to_xy_coords',
        "args": [15, 24]
    },
    {
        "identifier": 'ACTION_434_jmp_152',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_186']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_153',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [128, 'ACTION_434_jmp_if_700C_not_equals_short_157']
    },
    {
        "identifier": 'ACTION_434_shadow_on_154',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_155',
        "command": 'shirt_to_xy_coords',
        "args": [18, 14]
    },
    {
        "identifier": 'ACTION_434_jmp_156',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_195']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_157',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [160, 'ACTION_434_jump_to_subroutine_160']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_158',
        "command": 'shirt_to_xy_coords',
        "args": [15, 24]
    },
    {
        "identifier": 'ACTION_434_jmp_159',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_204']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_160',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_161',
        "command": 'walk_to_xy_coords',
        "args": [10, 22]
    },
    {
        "identifier": 'ACTION_434_shadow_on_162',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_163',
        "command": 'walk_to_xy_coords',
        "args": [8, 19]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_164',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_165',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_166',
        "command": 'mem_700C_or_const',
        "args": [0x0020]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_167',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_168',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_169',
        "command": 'walk_to_xy_coords',
        "args": [10, 22]
    },
    {
        "identifier": 'ACTION_434_shadow_off_170',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_171',
        "command": 'walk_to_xy_coords',
        "args": [11, 24]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_172',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_173',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_174',
        "command": 'mem_700C_or_const',
        "args": [0x0040]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_175',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_176',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_177',
        "command": 'walk_to_xy_coords',
        "args": [12, 24]
    },
    {
        "identifier": 'ACTION_434_shadow_on_178',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_179',
        "command": 'walk_to_xy_coords',
        "args": [14, 24]
    },
    {
        "identifier": 'ACTION_434_shadow_off_180',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_181',
        "command": 'walk_to_xy_coords',
        "args": [15, 24]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_182',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_183',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_184',
        "command": 'mem_700C_or_const',
        "args": [0x0060]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_185',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_186',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_187',
        "command": 'walk_to_xy_coords',
        "args": [16, 21]
    },
    {
        "identifier": 'ACTION_434_shadow_on_188',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_189',
        "command": 'walk_to_xy_coords',
        "args": [18, 18]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_190',
        "command": 'walk_to_xy_coords',
        "args": [18, 14]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_191',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_192',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_193',
        "command": 'mem_700C_or_const',
        "args": [0x0080]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_194',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_195',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_196',
        "command": 'walk_to_xy_coords',
        "args": [18, 18]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_197',
        "command": 'walk_to_xy_coords',
        "args": [16, 21]
    },
    {
        "identifier": 'ACTION_434_shadow_off_198',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_199',
        "command": 'walk_to_xy_coords',
        "args": [15, 24]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_200',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_201',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_202',
        "command": 'mem_700C_or_const',
        "args": [0x00a0]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_203',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_204',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_205',
        "command": 'walk_to_xy_coords',
        "args": [14, 24]
    },
    {
        "identifier": 'ACTION_434_shadow_on_206',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_207',
        "command": 'walk_to_xy_coords',
        "args": [12, 24]
    },
    {
        "identifier": 'ACTION_434_shadow_off_208',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_209',
        "command": 'walk_to_xy_coords',
        "args": [11, 24]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_210',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_211',
        "command": 'mem_700C_and_const',
        "args": [0xff1f]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_212',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_213',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_160']
    },
    {
        "identifier": 'ACTION_434_shadow_on_214',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_215',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_216',
        "command": 'mem_700C_and_const',
        "args": [0x0300]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_217',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [256, 'ACTION_434_jmp_if_700C_not_equals_short_221']
    },
    {
        "identifier": 'ACTION_434_shadow_off_218',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_219',
        "command": 'shirt_to_xy_coords',
        "args": [26, 32]
    },
    {
        "identifier": 'ACTION_434_jmp_220',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_234']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_221',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [512, 'ACTION_434_jump_to_subroutine_225']
    },
    {
        "identifier": 'ACTION_434_shadow_off_222',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_223',
        "command": 'shirt_to_xy_coords',
        "args": [22, 32]
    },
    {
        "identifier": 'ACTION_434_jmp_224',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_244']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_225',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_226',
        "command": 'walk_to_xy_coords',
        "args": [26, 24]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_227',
        "command": 'walk_to_xy_coords',
        "args": [26, 28]
    },
    {
        "identifier": 'ACTION_434_shadow_off_228',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_229',
        "command": 'walk_to_xy_coords',
        "args": [26, 32]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_230',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_231',
        "command": 'mem_700C_and_const',
        "args": [0xfcff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_232',
        "command": 'mem_700C_or_const',
        "args": [0x0100]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_233',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_234',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_235',
        "command": 'walk_to_xy_coords',
        "args": [25, 32]
    },
    {
        "identifier": 'ACTION_434_shadow_on_236',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_237',
        "command": 'walk_to_xy_coords',
        "args": [23, 32]
    },
    {
        "identifier": 'ACTION_434_shadow_off_238',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_239',
        "command": 'walk_to_xy_coords',
        "args": [22, 32]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_240',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_241',
        "command": 'mem_700C_and_const',
        "args": [0xfcff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_242',
        "command": 'mem_700C_or_const',
        "args": [0x0200]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_243',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_244',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_245',
        "command": 'walk_to_xy_coords',
        "args": [23, 30]
    },
    {
        "identifier": 'ACTION_434_shadow_on_246',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_247',
        "command": 'walk_to_xy_coords',
        "args": [26, 24]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_248',
        "command": 'walk_to_xy_coords',
        "args": [26, 20]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_249',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_250',
        "command": 'mem_700C_and_const',
        "args": [0xfcff]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_251',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_252',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_225']
    },
    {
        "identifier": 'ACTION_434_shadow_off_253',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_254',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_255',
        "command": 'mem_700C_and_const',
        "args": [0x0400]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_256',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [1024, 'ACTION_434_jump_to_subroutine_259']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_257',
        "command": 'shirt_to_xy_coords',
        "args": [16, 37]
    },
    {
        "identifier": 'ACTION_434_jmp_258',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_270']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_259',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_260',
        "command": 'walk_to_xy_coords',
        "args": [21, 34]
    },
    {
        "identifier": 'ACTION_434_shadow_on_261',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_262',
        "command": 'walk_to_xy_coords',
        "args": [20, 35]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_263',
        "command": 'walk_to_xy_coords',
        "args": [17, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_off_264',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_265',
        "command": 'walk_to_xy_coords',
        "args": [16, 37]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_266',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_267',
        "command": 'mem_700C_and_const',
        "args": [0xfbff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_268',
        "command": 'mem_700C_or_const',
        "args": [0x0400]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_269',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_270',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_271',
        "command": 'walk_to_xy_coords',
        "args": [17, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_on_272',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_273',
        "command": 'walk_to_xy_coords',
        "args": [20, 35]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_274',
        "command": 'walk_to_xy_coords',
        "args": [21, 34]
    },
    {
        "identifier": 'ACTION_434_shadow_off_275',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_276',
        "command": 'walk_to_xy_coords',
        "args": [21, 33]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_277',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_278',
        "command": 'mem_700C_and_const',
        "args": [0xfbff]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_279',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_280',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_259']
    },
    {
        "identifier": 'ACTION_434_shadow_off_281',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_282',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_283',
        "command": 'mem_700C_and_const',
        "args": [0x1800]
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_284',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [2048, 'ACTION_434_jmp_if_700C_not_equals_short_287']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_285',
        "command": 'shirt_to_xy_coords',
        "args": [18, 47]
    },
    {
        "identifier": 'ACTION_434_jmp_286',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_304']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_287',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [4096, 'ACTION_434_jmp_if_700C_not_equals_short_291']
    },
    {
        "identifier": 'ACTION_434_shadow_on_288',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_289',
        "command": 'shirt_to_xy_coords',
        "args": [20, 55]
    },
    {
        "identifier": 'ACTION_434_jmp_290',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_313']
    },
    {
        "identifier": 'ACTION_434_jmp_if_700C_not_equals_short_291',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [6144, 'ACTION_434_jump_to_subroutine_294']
    },
    {
        "identifier": 'ACTION_434_shirt_to_xy_coords_292',
        "command": 'shirt_to_xy_coords',
        "args": [18, 47]
    },
    {
        "identifier": 'ACTION_434_jmp_293',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_322']
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_294',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_295',
        "command": 'walk_to_xy_coords',
        "args": [25, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_on_296',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_297',
        "command": 'walk_to_xy_coords',
        "args": [19, 45]
    },
    {
        "identifier": 'ACTION_434_shadow_off_298',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_299',
        "command": 'walk_to_xy_coords',
        "args": [18, 47]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_300',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_301',
        "command": 'mem_700C_and_const',
        "args": [0xe7ff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_302',
        "command": 'mem_700C_or_const',
        "args": [0x0800]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_303',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_304',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_305',
        "command": 'walk_to_xy_coords',
        "args": [18, 49]
    },
    {
        "identifier": 'ACTION_434_shadow_on_306',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_307',
        "command": 'walk_to_xy_coords',
        "args": [18, 51]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_308',
        "command": 'walk_to_xy_coords',
        "args": [20, 55]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_309',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_310',
        "command": 'mem_700C_and_const',
        "args": [0xe7ff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_311',
        "command": 'mem_700C_or_const',
        "args": [0x1000]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_312',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_313',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_314',
        "command": 'walk_to_xy_coords',
        "args": [18, 51]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_315',
        "command": 'walk_to_xy_coords',
        "args": [18, 49]
    },
    {
        "identifier": 'ACTION_434_shadow_off_316',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_317',
        "command": 'walk_to_xy_coords',
        "args": [18, 47]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_318',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_319',
        "command": 'mem_700C_and_const',
        "args": [0xe7ff]
    },
    {
        "identifier": 'ACTION_434_mem_700C_or_const_320',
        "command": 'mem_700C_or_const',
        "args": [0x1800]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_321',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jump_to_subroutine_322',
        "command": 'jump_to_subroutine',
        "args": [0x4fb1]
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_323',
        "command": 'walk_to_xy_coords',
        "args": [19, 45]
    },
    {
        "identifier": 'ACTION_434_shadow_on_324',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_325',
        "command": 'walk_to_xy_coords',
        "args": [25, 35]
    },
    {
        "identifier": 'ACTION_434_shadow_off_326',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_434_walk_to_xy_coords_327',
        "command": 'walk_to_xy_coords',
        "args": [26, 34]
    },
    {
        "identifier": 'ACTION_434_set_700C_to_7000_short_mem_328',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_mem_700C_and_const_329',
        "command": 'mem_700C_and_const',
        "args": [0xe7ff]
    },
    {
        "identifier": 'ACTION_434_set_7000_short_mem_to_700C_330',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7036]
    },
    {
        "identifier": 'ACTION_434_jmp_331',
        "command": 'jmp',
        "args": ['ACTION_434_jump_to_subroutine_294']
    }
]
