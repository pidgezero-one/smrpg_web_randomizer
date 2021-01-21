from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_604_store_item_amount_7000_0',
        "command": 'store_item_amount_7000',
        "args": [items.BrightCard]
    },
    {
        "identifier": 'EVENT_604_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_604_run_dialog_5']
    },
    {
        "identifier": 'EVENT_604_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 4, 'EVENT_604_run_dialog_39']
    },
    {
        "identifier": 'EVENT_604_run_dialog_3',
        "command": 'run_dialog',
        "args": [2057, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_604_run_dialog_5',
        "command": 'run_dialog',
        "args": [2054, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_604_set_action_script_async_17']
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_604_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_604_add_coins_10',
        "command": 'add_coins',
        "args": [100]
    },
    {
        "identifier": 'EVENT_604_remove_one_from_inventory_11',
        "command": 'remove_one_from_inventory',
        "args": [items.BrightCard]
    },
    {
        "identifier": 'EVENT_604_set_bit_12',
        "command": 'set_bit',
        "args": [0x709c, 4]
    },
    {
        "identifier": 'EVENT_604_run_dialog_13',
        "command": 'run_dialog',
        "args": [2077, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_604_run_dialog_14',
        "command": 'run_dialog',
        "args": [2468, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_604_run_dialog_15',
        "command": 'run_dialog',
        "args": [2469, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_604_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_604_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_run_dialog_19',
        "command": 'run_dialog',
        "args": [2108, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_jmp_if_dialog_option_b_20',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_604_set_action_script_async_26']
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_604_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_604_add_frog_coins_24',
        "command": 'add_frog_coins',
        "args": [5]
    },
    {
        "identifier": 'EVENT_604_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_604_remove_one_from_inventory_11']
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_26',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_604_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_run_dialog_28',
        "command": 'run_dialog',
        "args": [2307, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_jmp_if_dialog_option_b_29',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_604_set_action_script_async_35']
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_30',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_604_pause_31',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_604_add_frog_coins_33',
        "command": 'add_frog_coins',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_604_remove_one_from_inventory_11']
    },
    {
        "identifier": 'EVENT_604_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_604_pause_36',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_604_run_dialog_37',
        "command": 'run_dialog',
        "args": [2308, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_ret_38',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_604_run_dialog_39',
        "command": 'run_dialog',
        "args": [2329, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_jmp_if_dialog_option_b_40',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_604_run_dialog_53']
    },
    {
        "identifier": 'EVENT_604_store_frog_coin_amount_7000_41',
        "command": 'store_frog_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_604_mem_compare_42',
        "command": 'mem_compare',
        "args": [0x7000, 15]
    },
    {
        "identifier": 'EVENT_604_jmp_if_comparison_result_is_lesser_43',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_604_run_dialog_51']
    },
    {
        "identifier": 'EVENT_604_run_dialog_44',
        "command": 'run_dialog',
        "args": [2334, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_set_45',
        "command": 'set',
        "args": [0x7000, 15]
    },
    {
        "identifier": 'EVENT_604_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_604_dec_frog_coins_7000_47',
        "command": 'dec_frog_coins_7000'
    },
    {
        "identifier": 'EVENT_604_put_inventory_48',
        "command": 'put_inventory',
        "args": [items.BrightCard]
    },
    {
        "identifier": 'EVENT_604_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x709c, 4]
    },
    {
        "identifier": 'EVENT_604_ret_50',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_604_run_dialog_51',
        "command": 'run_dialog',
        "args": [2380, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_ret_52',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_604_run_dialog_53',
        "command": 'run_dialog',
        "args": [2335, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_604_ret_54',
        "command": 'ret'
    }
]
