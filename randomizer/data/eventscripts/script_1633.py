from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1633_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 1, 'EVENT_1633_set_short_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 4, 'EVENT_1633_set_short_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_run_dialog_2',
        "command": 'run_dialog',
        "args": [1091, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_bit_3',
        "command": 'set_bit',
        "args": [0x707b, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_short_4',
        "command": 'set_short',
        "args": [0x7024, 0x000a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_5',
        "command": 'set',
        "args": [0x7000, 1088],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_6',
        "command": 'set',
        "args": [0x70ae, 20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_to_subroutine_7',
        "command": 'jmp_to_subroutine',
        "args": [0x20fe],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1633_set_bit_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_bit_10',
        "command": 'set_bit',
        "args": [0x705e, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_to_event_11',
        "command": 'jmp_to_event',
        "args": [280],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_run_dialog_13',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_swap_short_mem_14',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_store_coin_amount_7000_15',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_mem_compare_16',
        "command": 'mem_compare',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_if_comparison_result_is_greater_or_equal_17',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1633_swap_short_mem_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_swap_short_mem_18',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_add_19',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_add_20',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_append_to_dialog_at_7000_21',
        "command": 'append_to_dialog_at_7000',
        "args": [[_0x63Flags.CLOSABLE, _0x63Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_swap_short_mem_23',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_add_24',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_append_to_dialog_at_7000_25',
        "command": 'append_to_dialog_at_7000',
        "args": [[_0x63Flags.CLOSABLE, _0x63Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_jmp_if_dialog_option_b_26',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1633_pause_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_dec_coins_28',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_pause_29',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_action_script_async_30',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_bit_31',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_pause_33',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_set_action_script_async_34',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1633_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
