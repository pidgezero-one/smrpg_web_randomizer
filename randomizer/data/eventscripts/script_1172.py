from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1172_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7087, 2, 'EVENT_1172_run_dialog_3']
    },
    {
        "identifier": 'EVENT_1172_run_dialog_1',
        "command": 'run_dialog',
        "args": [2928, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_set_bit_2',
        "command": 'set_bit',
        "args": [0x7087, 2]
    },
    {
        "identifier": 'EVENT_1172_run_dialog_3',
        "command": 'run_dialog',
        "args": [2929, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_jmp_if_dialog_option_b_4',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1172_run_dialog_35']
    },
    {
        "identifier": 'EVENT_1172_store_item_amount_7000_5',
        "command": 'store_item_amount_7000',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1172_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1172_run_dialog_34']
    },
    {
        "identifier": 'EVENT_1172_run_dialog_7',
        "command": 'run_dialog',
        "args": [2930, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_remove_one_from_inventory_8',
        "command": 'remove_one_from_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_1172_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1172_action_queue_async_9_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1172_action_queue_async_9_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [85]
            },
            {
                "identifier": 'EVENT_1172_action_queue_async_9_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1172_set_random_10',
        "command": 'set_random',
        "args": [0x7000, 10000]
    },
    {
        "identifier": 'EVENT_1172_mem_compare_11',
        "command": 'mem_compare',
        "args": [0x7000, 400]
    },
    {
        "identifier": 'EVENT_1172_jmp_if_comparison_result_is_lesser_12',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1172_run_dialog_19']
    },
    {
        "identifier": 'EVENT_1172_mem_compare_13',
        "command": 'mem_compare',
        "args": [0x7000, 1000]
    },
    {
        "identifier": 'EVENT_1172_jmp_if_comparison_result_is_lesser_14',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1172_run_dialog_24']
    },
    {
        "identifier": 'EVENT_1172_mem_compare_15',
        "command": 'mem_compare',
        "args": [0x7000, 2400]
    },
    {
        "identifier": 'EVENT_1172_jmp_if_comparison_result_is_lesser_16',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1172_run_dialog_29']
    },
    {
        "identifier": 'EVENT_1172_run_dialog_17',
        "command": 'run_dialog',
        "args": [2931, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1172_run_dialog_19',
        "command": 'run_dialog',
        "args": [2934, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1172_run_dialog_21',
        "command": 'run_dialog',
        "args": [2939, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1172_put_inventory_22',
        "command": 'put_inventory',
        "args": [items.FlowerTab]
    },
    {
        "identifier": 'EVENT_1172_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1172_run_dialog_24',
        "command": 'run_dialog',
        "args": [2933, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1172_run_dialog_26',
        "command": 'run_dialog',
        "args": [2938, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1172_put_inventory_27',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_1172_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1172_run_dialog_29',
        "command": 'run_dialog',
        "args": [2932, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1172_run_dialog_31',
        "command": 'run_dialog',
        "args": [2937, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1172_put_inventory_32',
        "command": 'put_inventory',
        "args": [items.MapleSyrup]
    },
    {
        "identifier": 'EVENT_1172_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1172_run_dialog_34',
        "command": 'run_dialog',
        "args": [2936, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_run_dialog_35',
        "command": 'run_dialog',
        "args": [2935, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1172_ret_36',
        "command": 'ret'
    }
]
