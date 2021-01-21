from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3599_set_short_0',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3599_set_short_1',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_3599_set_short_2',
        "command": 'set_short',
        "args": [0x701c, 0x0000]
    },
    {
        "identifier": 'EVENT_3599_store_empty_inventory_slot_count_7000_3',
        "command": 'store_empty_inventory_slot_count_7000'
    },
    {
        "identifier": 'EVENT_3599_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3599_set_short_mem_33']
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_3599_mem_compare_7',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3599_jmp_if_comparison_result_is_lesser_8',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3599_set_short_mem_13']
    },
    {
        "identifier": 'EVENT_3599_jmp_if_loaded_memory_is_0_9',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_3599_set_short_mem_13']
    },
    {
        "identifier": 'EVENT_3599_dec_short_mem_10',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_3599_set_short_mem_15']
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3599_set_object_memory_to_16',
        "command": 'set_object_memory_to',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_3599_put_inventory_17',
        "command": 'put_inventory',
        "args": [items.YoshiCookie]
    },
    {
        "identifier": 'EVENT_3599_end_loop_18',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3599_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7026, 0, 'EVENT_3599_set_48']
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_3599_add_short_mem_21',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_mem_compare_23',
        "command": 'mem_compare',
        "args": [0x7000, 201]
    },
    {
        "identifier": 'EVENT_3599_jmp_if_comparison_result_is_greater_or_equal_24',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3599_set_short_36']
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_3599_jmp_if_var_equals_short_26',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3599_run_dialog_31']
    },
    {
        "identifier": 'EVENT_3599_run_dialog_27',
        "command": 'run_dialog',
        "args": [950, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x70d8, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_3599_set_48']
    },
    {
        "identifier": 'EVENT_3599_run_dialog_31',
        "command": 'run_dialog',
        "args": [2362, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3599_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_3599_set_short_mem_28']
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_3599_set_short_mem_20']
    },
    {
        "identifier": 'EVENT_3599_set_short_36',
        "command": 'set_short',
        "args": [0x7024, 0x00c8]
    },
    {
        "identifier": 'EVENT_3599_dec_short_mem_37',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d8]
    },
    {
        "identifier": 'EVENT_3599_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_3599_set_41',
        "command": 'set',
        "args": [0x7000, 200]
    },
    {
        "identifier": 'EVENT_3599_dec_short_mem_42',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_3599_run_dialog_43',
        "command": 'run_dialog',
        "args": [2510, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3599_play_sound_44',
        "command": 'play_sound',
        "args": [Sounds._061_DEEP_UHOH, 6]
    },
    {
        "identifier": 'EVENT_3599_pause_45',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3599_run_dialog_46',
        "command": 'run_dialog',
        "args": [952, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3599_set_47',
        "command": 'set',
        "args": [0x70d8, 200]
    },
    {
        "identifier": 'EVENT_3599_set_48',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_3599_set_49',
        "command": 'set',
        "args": [0x70b8, 0]
    },
    {
        "identifier": 'EVENT_3599_set_short_50',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3599_set_short_51',
        "command": 'set_short',
        "args": [0x7026, 0x0000]
    },
    {
        "identifier": 'EVENT_3599_ret_52',
        "command": 'ret'
    }
]
