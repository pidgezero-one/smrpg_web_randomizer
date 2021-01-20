from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1640_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 7, 'EVENT_1640_run_dialog_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 4, 'EVENT_1640_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_4',
        "command": 'run_dialog',
        "args": [1125, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_5',
        "command": 'set_bit',
        "args": [0x704d, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_6',
        "command": 'run_dialog',
        "args": [1126, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_store_coin_amount_7000_7',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_mem_compare_8',
        "command": 'mem_compare',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_comparison_result_is_greater_or_equal_9',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1640_store_coin_amount_7000_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_10',
        "command": 'run_dialog_duration',
        "args": [1129, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_11',
        "command": 'run_dialog_duration',
        "args": [1128, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_store_coin_amount_7000_13',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_mem_compare_14',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_comparison_result_is_lesser_15',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1640_store_7000_minecart_timer_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 2, 'EVENT_1640_store_7000_minecart_timer_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_store_7000_minecart_timer_17',
        "command": 'store_7000_minecart_timer',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_18',
        "command": 'run_dialog_duration',
        "args": [1101, DialogDurations.FOREVER, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_19',
        "command": 'run_dialog_duration',
        "args": [1173, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_dialog_option_b_or_c_20',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_1640_set_37', 'EVENT_1640_run_dialog_49'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_1640_set_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_store_7000_minecart_timer_22',
        "command": 'store_7000_minecart_timer',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_23',
        "command": 'run_dialog_duration',
        "args": [1127, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_dialog_option_b_24',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1640_pause_47'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_pause_25',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_action_script_async_26',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_27',
        "command": 'set_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_store_coin_amount_7000_28',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_mem_compare_29',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_comparison_result_is_lesser_30',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1640_set_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_31',
        "command": 'run_dialog',
        "args": [1130, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_duration_32',
        "command": 'run_dialog_duration',
        "args": [1131, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_if_dialog_option_b_or_c_33',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_1640_set_37', 'EVENT_1640_run_dialog_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_34',
        "command": 'set',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x707b, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1640_run_dialog_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_37',
        "command": 'set',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_38',
        "command": 'set_bit',
        "args": [0x707b, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_39',
        "command": 'run_dialog',
        "args": [1132, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_dec_coins_41',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_42',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_43',
        "command": 'set_bit',
        "args": [0x707a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_ret_44',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_45',
        "command": 'run_dialog',
        "args": [1133, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_1640_run_dialog_duration_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_pause_47',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_action_script_async_48',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_49',
        "command": 'run_dialog',
        "args": [1128, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_ret_50',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_run_dialog_51',
        "command": 'run_dialog',
        "args": [1134, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_set_bit_52',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1640_ret_53',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
