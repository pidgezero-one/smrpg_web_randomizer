from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3490_pause_0',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_3490_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3490_mem_7000_and_const_2',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1792, 'EVENT_3490_jmp_if_bit_set_9']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5120, 'EVENT_3490_jmp_if_bit_set_37']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8704, 'EVENT_3490_jmp_if_bit_set_65']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 12288, 'EVENT_3490_jmp_if_bit_set_93']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 15616, 'EVENT_3490_set_bit_140']
    },
    {
        "identifier": 'EVENT_3490_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3490_set_11',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_3490_set_short_12',
        "command": 'set_short',
        "args": [0x7016, 0x0f08]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_14',
        "command": 'set_short',
        "args": [0x7016, 0x1109]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_16',
        "command": 'set_short',
        "args": [0x7016, 0x100b]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 4, 'EVENT_3490_set_short_24']
    },
    {
        "identifier": 'EVENT_3490_set_19',
        "command": 'set',
        "args": [0x70ab, 22]
    },
    {
        "identifier": 'EVENT_3490_set_short_20',
        "command": 'set_short',
        "args": [0x7016, 0x120c]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_21',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_22',
        "command": 'set',
        "args": [0x70ab, 27]
    },
    {
        "identifier": 'EVENT_3490_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3490_set_short_26']
    },
    {
        "identifier": 'EVENT_3490_set_short_24',
        "command": 'set_short',
        "args": [0x7016, 0x120c]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_26',
        "command": 'set_short',
        "args": [0x7016, 0x100e]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_27',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_28',
        "command": 'set_short',
        "args": [0x7016, 0x1010]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_30',
        "command": 'set_short',
        "args": [0x7016, 0x1211]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_31',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_32',
        "command": 'set_short',
        "args": [0x7016, 0x0f12]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_33',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_34',
        "command": 'set_short',
        "args": [0x7016, 0x1213]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_35',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_37',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_set_bit_38',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3490_set_39',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_3490_set_short_40',
        "command": 'set_short',
        "args": [0x7016, 0x0f15]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_41',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_42',
        "command": 'set_short',
        "args": [0x7016, 0x1217]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_43',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_44',
        "command": 'set_short',
        "args": [0x7016, 0x0d18]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 5, 'EVENT_3490_set_short_52']
    },
    {
        "identifier": 'EVENT_3490_set_47',
        "command": 'set',
        "args": [0x70ab, 22]
    },
    {
        "identifier": 'EVENT_3490_set_short_48',
        "command": 'set_short',
        "args": [0x7016, 0x0c1a]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_49',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_50',
        "command": 'set',
        "args": [0x70ab, 27]
    },
    {
        "identifier": 'EVENT_3490_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_3490_set_short_54']
    },
    {
        "identifier": 'EVENT_3490_set_short_52',
        "command": 'set_short',
        "args": [0x7016, 0x0c1a]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_53',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_54',
        "command": 'set_short',
        "args": [0x7016, 0x1319]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_55',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_56',
        "command": 'set_short',
        "args": [0x7016, 0x0d1c]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_57',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_58',
        "command": 'set_short',
        "args": [0x7016, 0x0b1e]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_59',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_60',
        "command": 'set_short',
        "args": [0x7016, 0x0d1f]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_61',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_62',
        "command": 'set_short',
        "args": [0x7016, 0x0a21]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_63',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_65',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_set_bit_66',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3490_set_67',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_3490_set_short_68',
        "command": 'set_short',
        "args": [0x7016, 0x0d22]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_69',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_70',
        "command": 'set_short',
        "args": [0x7016, 0x0823]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_71',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_72',
        "command": 'set_short',
        "args": [0x7016, 0x0a24]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_73',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_74',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 6, 'EVENT_3490_set_short_80']
    },
    {
        "identifier": 'EVENT_3490_set_75',
        "command": 'set',
        "args": [0x70ab, 22]
    },
    {
        "identifier": 'EVENT_3490_set_short_76',
        "command": 'set_short',
        "args": [0x7016, 0x0826]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_77',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_78',
        "command": 'set',
        "args": [0x70ab, 27]
    },
    {
        "identifier": 'EVENT_3490_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_3490_set_short_82']
    },
    {
        "identifier": 'EVENT_3490_set_short_80',
        "command": 'set_short',
        "args": [0x7016, 0x0826]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_81',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_82',
        "command": 'set_short',
        "args": [0x7016, 0x0928]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_83',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_84',
        "command": 'set_short',
        "args": [0x7016, 0x082a]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_85',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_86',
        "command": 'set_short',
        "args": [0x7016, 0x092d]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_87',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_88',
        "command": 'set_short',
        "args": [0x7016, 0x072e]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_89',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_90',
        "command": 'set_short',
        "args": [0x7016, 0x052f]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_91',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_93',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_set_bit_94',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_3490_set_95',
        "command": 'set',
        "args": [0x70ab, 23]
    },
    {
        "identifier": 'EVENT_3490_set_short_96',
        "command": 'set_short',
        "args": [0x7016, 0x0531]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_97',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_98',
        "command": 'set_short',
        "args": [0x7016, 0x0432]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_99',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_100',
        "command": 'set_short',
        "args": [0x7016, 0x0c32]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_101',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_bit_set_102',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 7, 'EVENT_3490_set_short_108']
    },
    {
        "identifier": 'EVENT_3490_set_103',
        "command": 'set',
        "args": [0x70ab, 22]
    },
    {
        "identifier": 'EVENT_3490_set_short_104',
        "command": 'set_short',
        "args": [0x7016, 0x0c35]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_105',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_106',
        "command": 'set',
        "args": [0x70ab, 27]
    },
    {
        "identifier": 'EVENT_3490_jmp_107',
        "command": 'jmp',
        "args": ['EVENT_3490_set_short_110']
    },
    {
        "identifier": 'EVENT_3490_set_short_108',
        "command": 'set_short',
        "args": [0x7016, 0x0c35]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_109',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_110',
        "command": 'set_short',
        "args": [0x7016, 0x1036]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_111',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_112',
        "command": 'set_short',
        "args": [0x7016, 0x0d37]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_113',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_114',
        "command": 'set_short',
        "args": [0x7016, 0x0c38]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_115',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_116',
        "command": 'set_short',
        "args": [0x7016, 0x0b39]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_117',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_set_short_118',
        "command": 'set_short',
        "args": [0x7016, 0x143c]
    },
    {
        "identifier": 'EVENT_3490_jmp_to_subroutine_119',
        "command": 'jmp_to_subroutine',
        "args": [0x66b5]
    },
    {
        "identifier": 'EVENT_3490_jmp_120',
        "command": 'jmp',
        "args": ['EVENT_3490_pause_0']
    },
    {
        "identifier": 'EVENT_3490_set_short_mem_121',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7018]
    },
    {
        "identifier": 'EVENT_3490_set_short_mem_122',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_3490_mem_7000_and_const_123',
        "command": 'mem_7000_and_const',
        "args": [0xff00]
    },
    {
        "identifier": 'EVENT_3490_mem_7000_or_const_124',
        "command": 'mem_7000_or_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_3490_set_short_mem_125',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7000]
    },
    {
        "identifier": 'EVENT_3490_mem_7000_shift_left_126',
        "command": 'mem_7000_shift_left',
        "args": [0x7018, 248]
    },
    {
        "identifier": 'EVENT_3490_set_short_mem_127',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_3490_mem_7000_or_const_128',
        "command": 'mem_7000_or_const',
        "args": [0x00e0]
    },
    {
        "identifier": 'EVENT_3490_set_short_mem_129',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000]
    },
    {
        "identifier": 'EVENT_3490_set_short_130',
        "command": 'set_short',
        "args": [0x701a, 0x0000]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_object_not_in_level_131',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70AB, Rooms._069_MIDAS_RIVER_WATERFALL, 'EVENT_3490_pause_133']
    },
    {
        "identifier": 'EVENT_3490_action_queue_async_132',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3490_action_queue_async_132_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3490_pause_133',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3490_jmp_if_objects_action_script_running_134',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.MEM_70AB, 'EVENT_3490_pause_133']
    },
    {
        "identifier": 'EVENT_3490_set_action_script_sync_135',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 173]
    },
    {
        "identifier": 'EVENT_3490_summon_to_level_136',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70AB, Rooms._069_MIDAS_RIVER_WATERFALL]
    },
    {
        "identifier": 'EVENT_3490_add_137',
        "command": 'add',
        "args": [0x70ab, 0x01]
    },
    {
        "identifier": 'EVENT_3490_pause_138',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3490_ret_139',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3490_set_bit_140',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3490_ret_141',
        "command": 'ret'
    }
]
