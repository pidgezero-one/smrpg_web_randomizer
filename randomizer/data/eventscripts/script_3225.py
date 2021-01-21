from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3225_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3225_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3225_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7032, 0x7000]
    },
    {
        "identifier": 'EVENT_3225_mem_7000_shift_left_3',
        "command": 'mem_7000_shift_left',
        "args": [0x7032, 248]
    },
    {
        "identifier": 'EVENT_3225_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3225_add_short_mem_5',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7032]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3378, 'EVENT_3225_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3636, 'EVENT_3225_jmp_if_bit_set_33']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3894, 'EVENT_3225_jmp_if_bit_set_51']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4148, 'EVENT_3225_jmp_if_bit_set_69']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3890, 'EVENT_3225_jmp_if_bit_set_87']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3632, 'EVENT_3225_jmp_if_bit_set_105']
    },
    {
        "identifier": 'EVENT_3225_close_dialog_12',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3225_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_3225_run_dialog_23']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 1, 'EVENT_3225_run_dialog_25']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 2, 'EVENT_3225_run_dialog_27']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 3, 'EVENT_3225_run_dialog_29']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 4, 'EVENT_3225_run_dialog_31']
    },
    {
        "identifier": 'EVENT_3225_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_23',
        "command": 'run_dialog',
        "args": [1696, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_25',
        "command": 'run_dialog',
        "args": [1697, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_27',
        "command": 'run_dialog',
        "args": [1698, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_29',
        "command": 'run_dialog',
        "args": [1699, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_31',
        "command": 'run_dialog',
        "args": [1700, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_35',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 0, 'EVENT_3225_run_dialog_41']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_36',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 1, 'EVENT_3225_run_dialog_43']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 2, 'EVENT_3225_run_dialog_45']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_38',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 3, 'EVENT_3225_run_dialog_47']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_39',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 4, 'EVENT_3225_run_dialog_49']
    },
    {
        "identifier": 'EVENT_3225_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_41',
        "command": 'run_dialog',
        "args": [1708, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_43',
        "command": 'run_dialog',
        "args": [1709, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_45',
        "command": 'run_dialog',
        "args": [1710, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_47',
        "command": 'run_dialog',
        "args": [1711, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_49',
        "command": 'run_dialog',
        "args": [1712, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_52',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_53',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 0, 'EVENT_3225_run_dialog_59']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_54',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 1, 'EVENT_3225_run_dialog_61']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_55',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 2, 'EVENT_3225_run_dialog_63']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_56',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 3, 'EVENT_3225_run_dialog_65']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_57',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7028, 4, 'EVENT_3225_run_dialog_67']
    },
    {
        "identifier": 'EVENT_3225_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_59',
        "command": 'run_dialog',
        "args": [1720, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_61',
        "command": 'run_dialog',
        "args": [1721, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_63',
        "command": 'run_dialog',
        "args": [1722, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_65',
        "command": 'run_dialog',
        "args": [1723, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_67',
        "command": 'run_dialog',
        "args": [1724, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_68',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_69',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_70',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_71',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 0, 'EVENT_3225_run_dialog_77']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_72',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 1, 'EVENT_3225_run_dialog_79']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_73',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 2, 'EVENT_3225_run_dialog_81']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 3, 'EVENT_3225_run_dialog_83']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_75',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702a, 4, 'EVENT_3225_run_dialog_85']
    },
    {
        "identifier": 'EVENT_3225_jmp_76',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_77',
        "command": 'run_dialog',
        "args": [1732, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_79',
        "command": 'run_dialog',
        "args": [1733, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_80',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_81',
        "command": 'run_dialog',
        "args": [1734, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_82',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_83',
        "command": 'run_dialog',
        "args": [1735, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_84',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_85',
        "command": 'run_dialog',
        "args": [1736, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_86',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_87',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_88',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_89',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 0, 'EVENT_3225_run_dialog_95']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_90',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 1, 'EVENT_3225_run_dialog_97']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_91',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 2, 'EVENT_3225_run_dialog_99']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_92',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 3, 'EVENT_3225_run_dialog_101']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_93',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702c, 4, 'EVENT_3225_run_dialog_103']
    },
    {
        "identifier": 'EVENT_3225_jmp_94',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_95',
        "command": 'run_dialog',
        "args": [1744, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_96',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_97',
        "command": 'run_dialog',
        "args": [1745, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_99',
        "command": 'run_dialog',
        "args": [1746, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_100',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_101',
        "command": 'run_dialog',
        "args": [1747, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_102',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_103',
        "command": 'run_dialog',
        "args": [1748, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_104',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_bit_set_105',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_106',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_107',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 0, 'EVENT_3225_run_dialog_113']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_108',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 1, 'EVENT_3225_run_dialog_115']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_109',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 2, 'EVENT_3225_run_dialog_117']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_110',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 3, 'EVENT_3225_run_dialog_119']
    },
    {
        "identifier": 'EVENT_3225_jmp_if_var_equals_short_111',
        "command": 'jmp_if_var_equals_short',
        "args": [0x702e, 4, 'EVENT_3225_run_dialog_121']
    },
    {
        "identifier": 'EVENT_3225_jmp_112',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_113',
        "command": 'run_dialog',
        "args": [1756, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_114',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_115',
        "command": 'run_dialog',
        "args": [1757, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_116',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_117',
        "command": 'run_dialog',
        "args": [1758, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_118',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_119',
        "command": 'run_dialog',
        "args": [1759, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_120',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_run_dialog_121',
        "command": 'run_dialog',
        "args": [1760, AreaObjects.NPC_12, []]
    },
    {
        "identifier": 'EVENT_3225_jmp_122',
        "command": 'jmp',
        "args": ['EVENT_3225_pause_0']
    },
    {
        "identifier": 'EVENT_3225_set_bit_123',
        "command": 'set_bit',
        "args": [0x7042, 7]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_124',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._161_SUNKEN_SHIP_AREA_03_GREAPERS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_125',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._161_SUNKEN_SHIP_AREA_03_GREAPERS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_126',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._161_SUNKEN_SHIP_AREA_03_GREAPERS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_127',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_128',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_129',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_130',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_131',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_132',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_133',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_134',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_135',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_136',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_137',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_138',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_139',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_140',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_141',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_142',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_143',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_144',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_145',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_8, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_146',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_147',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_148',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_149',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_150',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_151',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_152',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_153',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_154',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_155',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_156',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_157',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_158',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_159',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_160',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES]
    },
    {
        "identifier": 'EVENT_3225_enable_trigger_in_level_161',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_162',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_163',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_164',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_165',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_166',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_167',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_168',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_169',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_170',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_171',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_172',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_173',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_174',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    },
    {
        "identifier": 'EVENT_3225_summon_to_level_175',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    },
    {
        "identifier": 'EVENT_3225_ret_176',
        "command": 'ret'
    }
]
