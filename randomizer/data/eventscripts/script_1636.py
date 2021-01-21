from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1636_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 4, 'EVENT_1636_run_dialog_7']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_3',
        "command": 'run_dialog',
        "args": [1123, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_duration_4',
        "command": 'run_dialog_duration',
        "args": [1208, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_set_bit_5',
        "command": 'set_bit',
        "args": [0x704e, 4]
    },
    {
        "identifier": 'EVENT_1636_set_6',
        "command": 'set',
        "args": [0x70b0, 0]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_7',
        "command": 'run_dialog',
        "args": [1209, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": [0x23a2]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1636_jmp_if_bit_set_14']
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b0]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_duration_11',
        "command": 'run_dialog_duration',
        "args": [1211, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_12',
        "command": 'run_dialog',
        "args": [1220, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_1636_set_bit_16']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_duration_15',
        "command": 'run_dialog_duration',
        "args": [1210, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_set_bit_16',
        "command": 'set_bit',
        "args": [0x7042, 3]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b0]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_duration_18',
        "command": 'run_dialog_duration',
        "args": [1211, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_jmp_to_subroutine_19',
        "command": 'jmp_to_subroutine',
        "args": [0x23a2]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_1636_run_dialog_12']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_21',
        "command": 'run_dialog',
        "args": [1212, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_dialog_option_b_22',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1636_pause_190']
    },
    {
        "identifier": 'EVENT_1636_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1636_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1636_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": [0x23a2]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_clear_26',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_1636_run_dialog_12']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 4, 'EVENT_1636_set_29']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_28',
        "command": 'run_dialog',
        "args": [1213, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_set_29',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_1636_store_7000_item_quantity_to_70A7_30',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_equals_short_31',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1636_add_59']
    },
    {
        "identifier": 'EVENT_1636_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_33',
        "command": 'run_dialog',
        "args": [1048, AreaObjects.NPC_14, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_1636_mem_7000_and_const_35',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_1636_add_36',
        "command": 'add',
        "args": [0x7000, 1328]
    },
    {
        "identifier": 'EVENT_1636_append_to_dialog_at_7000_37',
        "command": 'append_to_dialog_at_7000',
        "args": [[_0x63Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_set_7000_to_tapped_button_38',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_39',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_1636_set_bit_70']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_40',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1636_play_sound_45']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_41',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_1636_dec_48']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_42',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_1636_add_59']
    },
    {
        "identifier": 'EVENT_1636_pause_43',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1636_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_1636_set_7000_to_tapped_button_38']
    },
    {
        "identifier": 'EVENT_1636_play_sound_45',
        "command": 'play_sound',
        "args": [Sounds._002_MENU_CANCEL, 6]
    },
    {
        "identifier": 'EVENT_1636_close_dialog_46',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1636_run_dialog_21']
    },
    {
        "identifier": 'EVENT_1636_dec_48',
        "command": 'dec',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_1636_mem_7000_and_const_50',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_1636_mem_7000_or_const_51',
        "command": 'mem_7000_or_const',
        "args": [0x0060]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_52',
        "command": 'set_short_mem',
        "args": [0x70a7, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_byte_53',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70a7, 109, 'EVENT_1636_store_7000_item_quantity_to_70A7_55']
    },
    {
        "identifier": 'EVENT_1636_dec_54',
        "command": 'dec',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1636_store_7000_item_quantity_to_70A7_55',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_equals_short_56',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1636_dec_48']
    },
    {
        "identifier": 'EVENT_1636_play_sound_57',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_1636_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_1636_run_dialog_33']
    },
    {
        "identifier": 'EVENT_1636_add_59',
        "command": 'add',
        "args": [0x70a7, 0x01]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_60',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_1636_mem_7000_and_const_61',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_1636_mem_7000_or_const_62',
        "command": 'mem_7000_or_const',
        "args": [0x0060]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x70a7, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_byte_64',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70a7, 109, 'EVENT_1636_store_7000_item_quantity_to_70A7_66']
    },
    {
        "identifier": 'EVENT_1636_add_65',
        "command": 'add',
        "args": [0x70a7, 0x01]
    },
    {
        "identifier": 'EVENT_1636_store_7000_item_quantity_to_70A7_66',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_equals_short_67',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1636_add_59']
    },
    {
        "identifier": 'EVENT_1636_play_sound_68',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_1636_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_1636_run_dialog_33']
    },
    {
        "identifier": 'EVENT_1636_set_bit_70',
        "command": 'set_bit',
        "args": [0x7042, 4]
    },
    {
        "identifier": 'EVENT_1636_play_sound_71',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_1636_close_dialog_72',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_run_dialog_73',
        "command": 'run_dialog',
        "args": [1214, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_bit_set_74',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_1636_close_dialog_76']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_duration_75',
        "command": 'run_dialog_duration',
        "args": [1218, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_close_dialog_76',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_set_short_77',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_1636_store_7000_item_quantity_to_70A7_78',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_79',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_81',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_82',
        "command": 'run_dialog',
        "args": [1047, AreaObjects.NPC_14, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_set_7000_to_tapped_button_83',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_84',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_1636_set_bit_109']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_85',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1636_play_sound_90']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_86',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_1636_set_short_mem_93']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_7000_any_bits_set_87',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_1636_jmp_if_var_not_equals_short_102']
    },
    {
        "identifier": 'EVENT_1636_pause_88',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1636_jmp_89',
        "command": 'jmp',
        "args": ['EVENT_1636_set_7000_to_tapped_button_83']
    },
    {
        "identifier": 'EVENT_1636_play_sound_90',
        "command": 'play_sound',
        "args": [Sounds._002_MENU_CANCEL, 6]
    },
    {
        "identifier": 'EVENT_1636_close_dialog_91',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_1636_run_dialog_21']
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_93',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1636_mem_compare_94',
        "command": 'mem_compare',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_loaded_memory_is_not_0_95',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_1636_add_short_99']
    },
    {
        "identifier": 'EVENT_1636_play_sound_96',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1636_pause_97',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1636_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_1636_set_7000_to_tapped_button_83']
    },
    {
        "identifier": 'EVENT_1636_add_short_99',
        "command": 'add_short',
        "args": [0x7026, 0x01]
    },
    {
        "identifier": 'EVENT_1636_play_sound_100',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_1636_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_81']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_102',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 1, 'EVENT_1636_dec_short_106']
    },
    {
        "identifier": 'EVENT_1636_play_sound_103',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1636_pause_104',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1636_jmp_105',
        "command": 'jmp',
        "args": ['EVENT_1636_set_7000_to_tapped_button_83']
    },
    {
        "identifier": 'EVENT_1636_dec_short_106',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_1636_play_sound_107',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_1636_jmp_108',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_81']
    },
    {
        "identifier": 'EVENT_1636_set_bit_109',
        "command": 'set_bit',
        "args": [0x7042, 5]
    },
    {
        "identifier": 'EVENT_1636_play_sound_110',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_1636_close_dialog_111',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_112',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_113',
        "command": 'run_dialog',
        "args": [1215, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_114',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a7]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_115',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 96, 'EVENT_1636_jmp_if_var_not_equals_short_118']
    },
    {
        "identifier": 'EVENT_1636_set_short_116',
        "command": 'set_short',
        "args": [0x7010, 0x0002]
    },
    {
        "identifier": 'EVENT_1636_jmp_117',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_118',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 97, 'EVENT_1636_jmp_if_var_not_equals_short_121']
    },
    {
        "identifier": 'EVENT_1636_set_short_119',
        "command": 'set_short',
        "args": [0x7010, 0x000a]
    },
    {
        "identifier": 'EVENT_1636_jmp_120',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_121',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 98, 'EVENT_1636_jmp_if_var_not_equals_short_124']
    },
    {
        "identifier": 'EVENT_1636_set_short_122',
        "command": 'set_short',
        "args": [0x7010, 0x001e]
    },
    {
        "identifier": 'EVENT_1636_jmp_123',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_124',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 99, 'EVENT_1636_jmp_if_var_not_equals_short_127']
    },
    {
        "identifier": 'EVENT_1636_set_short_125',
        "command": 'set_short',
        "args": [0x7010, 0x0004]
    },
    {
        "identifier": 'EVENT_1636_jmp_126',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_127',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 100, 'EVENT_1636_jmp_if_var_not_equals_short_130']
    },
    {
        "identifier": 'EVENT_1636_set_short_128',
        "command": 'set_short',
        "args": [0x7010, 0x000c]
    },
    {
        "identifier": 'EVENT_1636_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_130',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 101, 'EVENT_1636_jmp_if_var_not_equals_short_133']
    },
    {
        "identifier": 'EVENT_1636_set_short_131',
        "command": 'set_short',
        "args": [0x7010, 0x001e]
    },
    {
        "identifier": 'EVENT_1636_jmp_132',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_133',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 102, 'EVENT_1636_jmp_if_var_not_equals_short_136']
    },
    {
        "identifier": 'EVENT_1636_set_short_134',
        "command": 'set_short',
        "args": [0x7010, 0x0002]
    },
    {
        "identifier": 'EVENT_1636_jmp_135',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_136',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 103, 'EVENT_1636_jmp_if_var_not_equals_short_139']
    },
    {
        "identifier": 'EVENT_1636_set_short_137',
        "command": 'set_short',
        "args": [0x7010, 0x0002]
    },
    {
        "identifier": 'EVENT_1636_jmp_138',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_139',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 104, 'EVENT_1636_jmp_if_var_not_equals_short_142']
    },
    {
        "identifier": 'EVENT_1636_set_short_140',
        "command": 'set_short',
        "args": [0x7010, 0x000f]
    },
    {
        "identifier": 'EVENT_1636_jmp_141',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_142',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 105, 'EVENT_1636_jmp_if_var_not_equals_short_145']
    },
    {
        "identifier": 'EVENT_1636_set_short_143',
        "command": 'set_short',
        "args": [0x7010, 0x0014]
    },
    {
        "identifier": 'EVENT_1636_jmp_144',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_145',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 106, 'EVENT_1636_jmp_if_var_not_equals_short_148']
    },
    {
        "identifier": 'EVENT_1636_set_short_146',
        "command": 'set_short',
        "args": [0x7010, 0x0028]
    },
    {
        "identifier": 'EVENT_1636_jmp_147',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_148',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 107, 'EVENT_1636_jmp_if_var_not_equals_short_151']
    },
    {
        "identifier": 'EVENT_1636_set_short_149',
        "command": 'set_short',
        "args": [0x7010, 0x0032]
    },
    {
        "identifier": 'EVENT_1636_jmp_150',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_151',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 108, 'EVENT_1636_jmp_if_var_not_equals_short_154']
    },
    {
        "identifier": 'EVENT_1636_set_short_152',
        "command": 'set_short',
        "args": [0x7010, 0x0028]
    },
    {
        "identifier": 'EVENT_1636_jmp_153',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_154',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 110, 'EVENT_1636_jmp_if_var_not_equals_short_157']
    },
    {
        "identifier": 'EVENT_1636_set_short_155',
        "command": 'set_short',
        "args": [0x7010, 0x0019]
    },
    {
        "identifier": 'EVENT_1636_jmp_156',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_157',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 111, 'EVENT_1636_start_loop_n_times_160']
    },
    {
        "identifier": 'EVENT_1636_set_short_158',
        "command": 'set_short',
        "args": [0x7010, 0x0009]
    },
    {
        "identifier": 'EVENT_1636_jmp_159',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_166']
    },
    {
        "identifier": 'EVENT_1636_start_loop_n_times_160',
        "command": 'start_loop_n_times',
        "args": [249]
    },
    {
        "identifier": 'EVENT_1636_play_sound_161',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_1636_pause_162',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1636_end_loop_163',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1636_close_dialog_164',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1636_ret_165',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_166',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b0]
    },
    {
        "identifier": 'EVENT_1636_set_object_memory_to_167',
        "command": 'set_object_memory_to',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_1636_add_short_mem_168',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7010]
    },
    {
        "identifier": 'EVENT_1636_put_70A7_equips_inventory_169',
        "command": 'put_70A7_equips_inventory'
    },
    {
        "identifier": 'EVENT_1636_end_loop_170',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_171',
        "command": 'set_short_mem',
        "args": [0x702a, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_mem_compare_172',
        "command": 'mem_compare',
        "args": [0x7000, 100]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_comparison_result_is_greater_or_equal_173',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1636_run_dialog_177']
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_174',
        "command": 'set_short_mem',
        "args": [0x70b0, 0x7000]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_175',
        "command": 'run_dialog',
        "args": [1216, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_jmp_176',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_17']
    },
    {
        "identifier": 'EVENT_1636_run_dialog_177',
        "command": 'run_dialog',
        "args": [1217, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_dialog_option_b_or_c_178',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_1636_set_181', 'EVENT_1636_set_183']
    },
    {
        "identifier": 'EVENT_1636_set_179',
        "command": 'set',
        "args": [0x70a7, 144]
    },
    {
        "identifier": 'EVENT_1636_jmp_180',
        "command": 'jmp',
        "args": ['EVENT_1636_play_sound_184']
    },
    {
        "identifier": 'EVENT_1636_set_181',
        "command": 'set',
        "args": [0x70a7, 113]
    },
    {
        "identifier": 'EVENT_1636_jmp_182',
        "command": 'jmp',
        "args": ['EVENT_1636_play_sound_184']
    },
    {
        "identifier": 'EVENT_1636_set_183',
        "command": 'set',
        "args": [0x70a7, 114]
    },
    {
        "identifier": 'EVENT_1636_play_sound_184',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_1636_run_dialog_185',
        "command": 'run_dialog',
        "args": [1219, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1636_put_inventory_186',
        "command": 'put_inventory',
        "args": [0x70a7]
    },
    {
        "identifier": 'EVENT_1636_set_short_mem_187',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1636_add_188',
        "command": 'add',
        "args": [0x7000, 65436]
    },
    {
        "identifier": 'EVENT_1636_jmp_189',
        "command": 'jmp',
        "args": ['EVENT_1636_set_short_mem_171']
    },
    {
        "identifier": 'EVENT_1636_pause_190',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1636_set_action_script_async_191',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1636_ret_192',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1636_store_empty_inventory_slot_count_7000_193',
        "command": 'store_empty_inventory_slot_count_7000'
    },
    {
        "identifier": 'EVENT_1636_mem_compare_194',
        "command": 'mem_compare',
        "args": [0x7000, 29]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_comparison_result_is_greater_or_equal_195',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1636_clear_bit_206']
    },
    {
        "identifier": 'EVENT_1636_set_short_196',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_1636_set_197',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_1636_start_loop_n_times_198',
        "command": 'start_loop_n_times',
        "args": [14]
    },
    {
        "identifier": 'EVENT_1636_store_7000_item_quantity_to_70A7_199',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_equals_short_200',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1636_add_202']
    },
    {
        "identifier": 'EVENT_1636_add_short_201',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_1636_add_202',
        "command": 'add',
        "args": [0x70a7, 0x01]
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_equals_byte_203',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a7, 109, 'EVENT_1636_add_202']
    },
    {
        "identifier": 'EVENT_1636_end_loop_204',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1636_jmp_if_var_not_equals_short_205',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 0, 'EVENT_1636_set_bit_208']
    },
    {
        "identifier": 'EVENT_1636_clear_bit_206',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1636_ret_207',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1636_set_bit_208',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1636_ret_209',
        "command": 'ret'
    }
]
