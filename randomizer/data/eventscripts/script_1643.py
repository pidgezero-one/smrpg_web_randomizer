from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1643_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_2',
        "command": 'run_dialog',
        "args": [1124, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_jmp_if_dialog_option_b_3',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1643_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_pause_4',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_store_item_amount_7000_6',
        "command": 'store_item_amount_7000',
        "args": [items.ShinyStone],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_jmp_if_var_not_equals_short_7',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 0, 'EVENT_1643_run_dialog_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_store_item_amount_7000_8',
        "command": 'store_item_amount_7000',
        "args": [0xac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1643_run_dialog_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_10',
        "command": 'run_dialog',
        "args": [1295, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_jmp_if_dialog_option_b_11',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1643_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_pause_12',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_remove_one_from_inventory_14',
        "command": 'remove_one_from_inventory',
        "args": [0xac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_15',
        "command": 'run_dialog',
        "args": [1154, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_16',
        "command": 'set',
        "args": [0x70a7, 138],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_17',
        "command": 'set',
        "args": [0x7000, 1155],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_event_as_subroutine_18',
        "command": 'run_event_as_subroutine',
        "args": [3827],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_20',
        "command": 'run_dialog',
        "args": [1153, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_duration_21',
        "command": 'run_dialog_duration',
        "args": [1154, DialogDurations.SHORT, [_0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_pause_23',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_25',
        "command": 'run_dialog',
        "args": [1154, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_run_dialog_27',
        "command": 'run_dialog',
        "args": [1296, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1643_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
