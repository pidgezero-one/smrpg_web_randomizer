from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_395_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 7, 'EVENT_395_run_dialog_37']
    },
    {
        "identifier": 'EVENT_395_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 3, 'EVENT_395_run_event_as_subroutine_27']
    },
    {
        "identifier": 'EVENT_395_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 2, 'EVENT_395_run_dialog_32']
    },
    {
        "identifier": 'EVENT_395_store_item_amount_7000_3',
        "command": 'store_item_amount_7000',
        "args": [items.Wallet]
    },
    {
        "identifier": 'EVENT_395_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_293_run_dialog_8']
    },
    {
        "identifier": 'EVENT_395_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_395_run_dialog_6',
        "command": 'run_dialog',
        "args": [669, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_395_set_action_script_async_21']
    },
    {
        "identifier": 'EVENT_395_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_395_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_395_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_395_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_395_run_dialog_12',
        "command": 'run_dialog',
        "args": [671, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_set_13',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_395_set_14',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_395_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_395_remove_one_from_inventory_16',
        "command": 'remove_one_from_inventory',
        "args": [items.Wallet]
    },
    {
        "identifier": 'EVENT_395_set_bit_17',
        "command": 'set_bit',
        "args": [0x7083, 2]
    },
    {
        "identifier": 'EVENT_395_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7083, 3]
    },
    {
        "identifier": 'EVENT_395_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 978]
    },
    {
        "identifier": 'EVENT_395_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_395_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_395_remember_last_object_22',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_395_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_395_run_dialog_24',
        "command": 'run_dialog',
        "args": [670, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_set_bit_25',
        "command": 'set_bit',
        "args": [0x7083, 3]
    },
    {
        "identifier": 'EVENT_395_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_395_run_event_as_subroutine_27',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_395_run_dialog_28',
        "command": 'run_dialog',
        "args": [672, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_store_item_amount_7000_29',
        "command": 'store_item_amount_7000',
        "args": [items.Wallet]
    },
    {
        "identifier": 'EVENT_395_jmp_if_var_equals_short_30',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_395_run_dialog_36']
    },
    {
        "identifier": 'EVENT_395_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_395_jmp_if_dialog_option_b_7']
    },
    {
        "identifier": 'EVENT_395_run_dialog_32',
        "command": 'run_dialog',
        "args": [668, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_ret_33',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_395_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_395_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_293_run_dialog_8']
    },
    {
        "identifier": 'EVENT_395_run_dialog_36',
        "command": 'run_dialog',
        "args": [889, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_run_dialog_37',
        "command": 'run_dialog',
        "args": [890, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_395_set_bit_38',
        "command": 'set_bit',
        "args": [0x709c, 7]
    },
    {
        "identifier": 'EVENT_395_ret_39',
        "command": 'ret'
    }
]
