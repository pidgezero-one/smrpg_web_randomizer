from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_930_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_930_set_short_1',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_930_set_short_2',
        "command": 'set_short',
        "args": [0x7028, 0x0000]
    },
    {
        "identifier": 'EVENT_930_run_dialog_3',
        "command": 'run_dialog',
        "args": [2341, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_if_dialog_option_b_or_c_4',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_930_set_short_mem_54', 'EVENT_930_run_dialog_172']
    },
    {
        "identifier": 'EVENT_930_set_bit_5',
        "command": 'set_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 200, 'EVENT_930_run_dialog_52']
    },
    {
        "identifier": 'EVENT_930_store_item_amount_7000_8',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_930_run_dialog_168']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_930_run_dialog_30']
    },
    {
        "identifier": 'EVENT_930_run_dialog_14',
        "command": 'run_dialog',
        "args": [2369, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_to_subroutine_15',
        "command": 'jmp_to_subroutine',
        "args": [0xa958]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_930_run_dialog_174']
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_930_run_dialog_174']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_add_short_mem_19',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_mem_compare_20',
        "command": 'mem_compare',
        "args": [0x7000, 201]
    },
    {
        "identifier": 'EVENT_930_jmp_if_comparison_result_is_greater_or_equal_21',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_930_set_short_mem_40']
    },
    {
        "identifier": 'EVENT_930_set_object_memory_to_22',
        "command": 'set_object_memory_to',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_930_remove_one_from_inventory_23',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_end_loop_24',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_930_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_add_short_mem_26',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_run_dialog_27',
        "command": 'run_dialog',
        "args": [2346, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x70d8, 0x7000]
    },
    {
        "identifier": 'EVENT_930_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_30',
        "command": 'run_dialog',
        "args": [2349, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_store_item_amount_7000_31',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_mem_compare_32',
        "command": 'mem_compare',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_930_jmp_if_comparison_result_is_lesser_33',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_930_run_dialog_38']
    },
    {
        "identifier": 'EVENT_930_run_dialog_34',
        "command": 'run_dialog',
        "args": [2371, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_set_bit_35',
        "command": 'set_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_930_jmp_to_subroutine_36',
        "command": 'jmp_to_subroutine',
        "args": [0xa958]
    },
    {
        "identifier": 'EVENT_930_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_930_jmp_if_bit_set_16']
    },
    {
        "identifier": 'EVENT_930_run_dialog_38',
        "command": 'run_dialog',
        "args": [2370, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_41',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000]
    },
    {
        "identifier": 'EVENT_930_set_42',
        "command": 'set',
        "args": [0x7000, 200]
    },
    {
        "identifier": 'EVENT_930_dec_short_mem_43',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000]
    },
    {
        "identifier": 'EVENT_930_set_object_memory_to_45',
        "command": 'set_object_memory_to',
        "args": [0x7028]
    },
    {
        "identifier": 'EVENT_930_remove_one_from_inventory_46',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_end_loop_47',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_930_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7024]
    },
    {
        "identifier": 'EVENT_930_run_dialog_49',
        "command": 'run_dialog',
        "args": [2350, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_set_50',
        "command": 'set',
        "args": [0x70d8, 200]
    },
    {
        "identifier": 'EVENT_930_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_52',
        "command": 'run_dialog',
        "args": [2355, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_54',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_55',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_930_run_dialog_170']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_930_store_empty_inventory_slot_count_7000_57',
        "command": 'store_empty_inventory_slot_count_7000'
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_58',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_930_run_dialog_83']
    },
    {
        "identifier": 'EVENT_930_run_dialog_59',
        "command": 'run_dialog',
        "args": [2342, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_dec_short_mem_60',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_jmp_if_loaded_memory_is_below_0_61',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_930_set_short_mem_65']
    },
    {
        "identifier": 'EVENT_930_store_empty_inventory_slot_count_7000_62',
        "command": 'store_empty_inventory_slot_count_7000'
    },
    {
        "identifier": 'EVENT_930_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_930_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_930_jmp_to_subroutine_66']
    },
    {
        "identifier": 'EVENT_930_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7026]
    },
    {
        "identifier": 'EVENT_930_jmp_to_subroutine_66',
        "command": 'jmp_to_subroutine',
        "args": [0xa958]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_930_run_dialog_174']
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_68',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_930_run_dialog_174']
    },
    {
        "identifier": 'EVENT_930_set_object_memory_to_69',
        "command": 'set_object_memory_to',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_930_put_inventory_70',
        "command": 'put_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_end_loop_71',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_930_set_short_mem_72',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_930_dec_short_mem_73',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_930_set_79']
    },
    {
        "identifier": 'EVENT_930_play_sound_75',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_930_run_dialog_76',
        "command": 'run_dialog',
        "args": [2348, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_77',
        "command": 'set_short_mem',
        "args": [0x70d8, 0x7000]
    },
    {
        "identifier": 'EVENT_930_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_set_79',
        "command": 'set',
        "args": [0x70d8, 0]
    },
    {
        "identifier": 'EVENT_930_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_930_run_dialog_81',
        "command": 'run_dialog',
        "args": [2353, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_82',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_83',
        "command": 'run_dialog',
        "args": [2354, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_84',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_enable_controls_until_return_85',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_86',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_930_jmp_if_bit_set_90']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_87',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 0, 'EVENT_930_set_short_93']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_88',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_930_set_short_93']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_89',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_930_set_short_93']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_90',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_930_set_short_100']
    },
    {
        "identifier": 'EVENT_930_set_short_91',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_930_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_930_set_bit_103']
    },
    {
        "identifier": 'EVENT_930_set_short_93',
        "command": 'set_short',
        "args": [0x7024, 0x0001]
    },
    {
        "identifier": 'EVENT_930_store_item_amount_7000_94',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_95',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_930_set_bit_151']
    },
    {
        "identifier": 'EVENT_930_set_bit_96',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_97',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_930_run_dialog_104']
    },
    {
        "identifier": 'EVENT_930_run_dialog_98',
        "command": 'run_dialog',
        "args": [2343, AreaObjects.BOWSER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_jmp_99',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_set_short_100',
        "command": 'set_short',
        "args": [0x7024, 0x0005]
    },
    {
        "identifier": 'EVENT_930_store_item_amount_7000_101',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_102',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_930_set_bit_151']
    },
    {
        "identifier": 'EVENT_930_set_bit_103',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_930_run_dialog_104',
        "command": 'run_dialog',
        "args": [2343, AreaObjects.MARIO, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_set_7000_to_pressed_button_105',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_930_pause_106',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_930_jmp_if_7000_any_bits_set_107',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_930_clear_bit_112']
    },
    {
        "identifier": 'EVENT_930_jmp_if_7000_any_bits_set_108',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_930_clear_bit_131']
    },
    {
        "identifier": 'EVENT_930_jmp_if_7000_any_bits_set_109',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_930_play_sound_165']
    },
    {
        "identifier": 'EVENT_930_jmp_if_7000_any_bits_set_110',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_930_jmp_if_bit_set_160']
    },
    {
        "identifier": 'EVENT_930_jmp_111',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_clear_bit_112',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_113',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_930_play_sound_157']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_114',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_930_play_sound_157']
    },
    {
        "identifier": 'EVENT_930_play_sound_115',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_930_add_short_116',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_117',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_930_run_dialog_120']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_118',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 0, 'EVENT_930_run_dialog_125']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_119',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_930_run_dialog_125']
    },
    {
        "identifier": 'EVENT_930_run_dialog_120',
        "command": 'run_dialog',
        "args": [2344, AreaObjects.MARIO, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_121',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_930_mem_compare_122',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_jmp_if_loaded_memory_is_0_123',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_930_set_bit_149']
    },
    {
        "identifier": 'EVENT_930_jmp_124',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_run_dialog_125',
        "command": 'run_dialog',
        "args": [2344, AreaObjects.BOWSER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_set_short_mem_126',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_930_mem_compare_127',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_930_jmp_if_loaded_memory_is_0_128',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_930_set_bit_149']
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_129',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 10, 'EVENT_930_set_bit_149']
    },
    {
        "identifier": 'EVENT_930_jmp_130',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_clear_bit_131',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_132',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_930_play_sound_157']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_133',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_930_play_sound_157']
    },
    {
        "identifier": 'EVENT_930_play_sound_134',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_930_dec_short_135',
        "command": 'dec_short',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_136',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_930_run_dialog_139']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_137',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 0, 'EVENT_930_run_dialog_144']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_138',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_930_run_dialog_144']
    },
    {
        "identifier": 'EVENT_930_run_dialog_139',
        "command": 'run_dialog',
        "args": [2344, AreaObjects.MARIO, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_140',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_930_jmp_if_var_equals_short_145']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_141',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 1, 'EVENT_930_jmp_if_var_equals_short_147']
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_142',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_930_set_bit_155']
    },
    {
        "identifier": 'EVENT_930_jmp_143',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_run_dialog_144',
        "command": 'run_dialog',
        "args": [2344, AreaObjects.BOWSER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_145',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 1, 'EVENT_930_set_bit_155']
    },
    {
        "identifier": 'EVENT_930_jmp_146',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_jmp_if_var_equals_short_147',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 5, 'EVENT_930_set_bit_155']
    },
    {
        "identifier": 'EVENT_930_jmp_148',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_set_bit_149',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_930_jmp_150',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_set_bit_151',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_152',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 0, 'EVENT_930_run_dialog_98']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_153',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_930_run_dialog_98']
    },
    {
        "identifier": 'EVENT_930_jmp_154',
        "command": 'jmp',
        "args": ['EVENT_930_run_dialog_104']
    },
    {
        "identifier": 'EVENT_930_set_bit_155',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_930_jmp_156',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_play_sound_157',
        "command": 'play_sound',
        "args": [Sounds._003_MENU_SCROLL, 6]
    },
    {
        "identifier": 'EVENT_930_pause_158',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_930_jmp_159',
        "command": 'jmp',
        "args": ['EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_jmp_if_bit_set_160',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_930_set_7000_to_pressed_button_105']
    },
    {
        "identifier": 'EVENT_930_play_sound_161',
        "command": 'play_sound',
        "args": [Sounds._002_MENU_CANCEL, 6]
    },
    {
        "identifier": 'EVENT_930_close_dialog_162',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_930_set_bit_163',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_930_ret_164',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_930_play_sound_165',
        "command": 'play_sound',
        "args": [Sounds._001_MENU_SELECT, 6]
    },
    {
        "identifier": 'EVENT_930_close_dialog_166',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_930_ret_167',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_930_run_dialog_168',
        "command": 'run_dialog',
        "args": [2351, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_169',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_170',
        "command": 'run_dialog',
        "args": [2352, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_171',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_172',
        "command": 'run_dialog',
        "args": [2345, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_173',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_174',
        "command": 'run_dialog',
        "args": [2347, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_175',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_run_dialog_176',
        "command": 'run_dialog',
        "args": [2348, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_930_jmp_177',
        "command": 'jmp',
        "args": ['EVENT_930_clear_bit_178']
    },
    {
        "identifier": 'EVENT_930_clear_bit_178',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_930_clear_bit_179',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_930_clear_bit_180',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_930_clear_bit_181',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_930_clear_bit_182',
        "command": 'clear_bit',
        "args": [0x7042, 1]
    },
    {
        "identifier": 'EVENT_930_clear_bit_183',
        "command": 'clear_bit',
        "args": [0x7042, 2]
    },
    {
        "identifier": 'EVENT_930_set_short_184',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_930_set_short_185',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_930_set_short_186',
        "command": 'set_short',
        "args": [0x7028, 0x0000]
    },
    {
        "identifier": 'EVENT_930_run_background_event_187',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_930_ret_188',
        "command": 'ret'
    }
]
