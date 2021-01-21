from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1872_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1872_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1872_store_item_amount_7000_2',
        "command": 'store_item_amount_7000',
        "args": [0xac]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1872_jmp_if_bit_set_6']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_4',
        "command": 'run_dialog',
        "args": [1297, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1872_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 2, 'EVENT_1872_run_dialog_8']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_7',
        "command": 'run_dialog',
        "args": [1288, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_run_dialog_8',
        "command": 'run_dialog',
        "args": [1289, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_dialog_option_b_9',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1872_pause_38']
    },
    {
        "identifier": 'EVENT_1872_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1872_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1872_store_coin_amount_7000_12',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1872_mem_compare_13',
        "command": 'mem_compare',
        "args": [0x7000, 500]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_comparison_result_is_greater_or_equal_14',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1872_play_sound_17']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_15',
        "command": 'run_dialog',
        "args": [1293, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1872_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1872_set_18',
        "command": 'set',
        "args": [0x7000, 500]
    },
    {
        "identifier": 'EVENT_1872_dec_coins_19',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1872_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ea]
    },
    {
        "identifier": 'EVENT_1872_mem_compare_21',
        "command": 'mem_compare',
        "args": [0x7000, 2]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_comparison_result_is_lesser_22',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1872_run_dialog_30']
    },
    {
        "identifier": 'EVENT_1872_mem_compare_23',
        "command": 'mem_compare',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_comparison_result_is_lesser_24',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1872_run_dialog_27']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_25',
        "command": 'run_dialog',
        "args": [1292, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_1872_jmp_if_var_equals_byte_32']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_27',
        "command": 'run_dialog',
        "args": [1291, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_run_dialog_duration_28',
        "command": 'run_dialog_duration',
        "args": [1287, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1872_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1872_jmp_if_var_equals_byte_32']
    },
    {
        "identifier": 'EVENT_1872_run_dialog_30',
        "command": 'run_dialog',
        "args": [1290, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1872_run_dialog_duration_31',
        "command": 'run_dialog_duration',
        "args": [1287, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1872_jmp_if_var_equals_byte_32',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ea, 5, 'EVENT_1872_play_sound_34']
    },
    {
        "identifier": 'EVENT_1872_add_33',
        "command": 'add',
        "args": [0x70ea, 0x01]
    },
    {
        "identifier": 'EVENT_1872_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1872_run_dialog_35',
        "command": 'run_dialog',
        "args": [1294, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1872_put_inventory_36',
        "command": 'put_inventory',
        "args": [0xac]
    },
    {
        "identifier": 'EVENT_1872_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1872_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1872_set_action_script_async_39',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1872_ret_40',
        "command": 'ret'
    }
]
