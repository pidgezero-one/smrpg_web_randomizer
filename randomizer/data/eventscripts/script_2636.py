from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2636_set_0',
        "command": 'set',
        "args": [0x70a7, 174],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2636_jmp_if_bit_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 1, 'EVENT_2636_run_dialog_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_run_dialog_4',
        "command": 'run_dialog',
        "args": [3300, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2636_ret_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._104_GRATE_GUYS_CASINO_FRONT_DOOR, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2636_action_queue_sync_8_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2636_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2636_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
        ]
    },
    {
        "identifier": 'EVENT_2636_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_run_dialog_11',
        "command": 'run_dialog',
        "args": [3301, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 6, 'EVENT_2636_run_dialog_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_run_dialog_14',
        "command": 'run_dialog',
        "args": [3298, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_run_dialog_16',
        "command": 'run_dialog',
        "args": [3299, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2636_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
