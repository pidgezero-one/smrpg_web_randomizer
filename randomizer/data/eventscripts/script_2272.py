from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7087, 1, 'EVENT_2272_run_dialog_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_1',
        "command": 'run_dialog',
        "args": [2902, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_2',
        "command": 'set_bit',
        "args": [0x7087, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_4',
        "command": 'run_dialog',
        "args": [2905, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 7, 'EVENT_2272_jmp_if_bit_clear_62'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_2272_jmp_if_bit_clear_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_clear_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 1, 'EVENT_2272_jmp_if_bit_set_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_10',
        "command": 'run_dialog',
        "args": [2913, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 1, 'EVENT_2272_jmp_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_13',
        "command": 'run_dialog',
        "args": [2911, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_14',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_jmp_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_15',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_16',
        "command": 'mem_compare',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_17',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_18',
        "command": 'set',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_19',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_20',
        "command": 'set_bit',
        "args": [0x7088, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_22',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_23',
        "command": 'put_inventory',
        "args": [items.LuckyJewel],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_25',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_28',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 1, 'EVENT_2272_jmp_if_bit_set_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_29',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 0, 'EVENT_2272_jmp_if_bit_set_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_30',
        "command": 'run_dialog',
        "args": [2913, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_32',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 1, 'EVENT_2272_jmp_if_bit_set_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_33',
        "command": 'run_dialog',
        "args": [2911, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_34',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_jmp_if_bit_set_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_35',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_36',
        "command": 'mem_compare',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_37',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_38',
        "command": 'set',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_39',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_40',
        "command": 'set_bit',
        "args": [0x7088, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_41',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_42',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_43',
        "command": 'put_inventory',
        "args": [items.LuckyJewel],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_45',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 0, 'EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_48',
        "command": 'run_dialog',
        "args": [2908, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_49',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_50',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_51',
        "command": 'mem_compare',
        "args": [0x7000, 200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_52',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_53',
        "command": 'set',
        "args": [0x7000, 200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_54',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_55',
        "command": 'set_bit',
        "args": [0x7088, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_56',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_57',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_58',
        "command": 'put_inventory',
        "args": [items.MysteryEgg],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_60',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_61',
        "command": 'jmp',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_62',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 1, 'EVENT_2272_jmp_if_bit_set_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_63',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 0, 'EVENT_2272_jmp_if_bit_set_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_clear_64',
        "command": 'jmp_if_bit_clear',
        "args": [0x7088, 2, 'EVENT_2272_jmp_if_bit_set_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_65',
        "command": 'run_dialog',
        "args": [2913, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_ret_66',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_67',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 1, 'EVENT_2272_jmp_if_bit_set_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_68',
        "command": 'run_dialog',
        "args": [2911, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_69',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_jmp_if_bit_set_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_70',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_71',
        "command": 'mem_compare',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_72',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_80'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_73',
        "command": 'set',
        "args": [0x7000, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_74',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_75',
        "command": 'set_bit',
        "args": [0x7088, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_77',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_78',
        "command": 'put_inventory',
        "args": [items.LuckyJewel],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_80',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_82',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 0, 'EVENT_2272_jmp_if_bit_set_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_83',
        "command": 'run_dialog',
        "args": [2908, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_84',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_jmp_if_bit_set_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_85',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_86',
        "command": 'mem_compare',
        "args": [0x7000, 200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_87',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_95'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_88',
        "command": 'set',
        "args": [0x7000, 200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_89',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_90',
        "command": 'set_bit',
        "args": [0x7088, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_91',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_92',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_93',
        "command": 'put_inventory',
        "args": [items.MysteryEgg],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_94',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_95',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_96',
        "command": 'jmp',
        "args": ['EVENT_2272_jmp_if_bit_set_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_bit_set_97',
        "command": 'jmp_if_bit_set',
        "args": [0x7088, 2, 'EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_98',
        "command": 'run_dialog',
        "args": [2914, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_dialog_option_b_99',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_store_coin_amount_7000_100',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_mem_compare_101',
        "command": 'mem_compare',
        "args": [0x7000, 300],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_if_comparison_result_is_lesser_102',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2272_run_dialog_110'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_103',
        "command": 'set',
        "args": [0x7000, 300],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_dec_coins_104',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_set_bit_105',
        "command": 'set_bit',
        "args": [0x7088, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_play_sound_106',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_107',
        "command": 'run_dialog',
        "args": [2912, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_put_inventory_108',
        "command": 'put_inventory',
        "args": [items.FryingPan],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_109',
        "command": 'jmp',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_110',
        "command": 'run_dialog',
        "args": [2910, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_jmp_111',
        "command": 'jmp',
        "args": ['EVENT_2272_run_dialog_112'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_run_dialog_112',
        "command": 'run_dialog',
        "args": [2909, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2272_ret_113',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
