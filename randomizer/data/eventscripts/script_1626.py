from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1626_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_1626_store_item_amount_7000_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_dialog_3',
        "command": 'run_dialog',
        "args": [1156, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_store_item_amount_7000_5',
        "command": 'store_item_amount_7000',
        "args": [items.CarboCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_jmp_if_var_not_equals_short_6',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_1626_run_dialog_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_store_item_amount_7000_7',
        "command": 'store_item_amount_7000',
        "args": [items.ShinyStone],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_jmp_if_var_not_equals_short_8',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_1626_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_dialog_9',
        "command": 'run_dialog',
        "args": [1158, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_dialog_11',
        "command": 'run_dialog',
        "args": [1159, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_jmp_if_dialog_option_b_12',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1626_pause_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_pause_13',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_set_action_script_async_14',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.ShinyStone],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_dialog_16',
        "command": 'run_dialog',
        "args": [1160, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_set_17',
        "command": 'set',
        "args": [0x70a7, 137],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_set_18',
        "command": 'set',
        "args": [0x7000, 1161],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [3827],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_pause_21',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_set_action_script_async_22',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_run_dialog_23',
        "command": 'run_dialog',
        "args": [1148, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1626_ret_24',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
