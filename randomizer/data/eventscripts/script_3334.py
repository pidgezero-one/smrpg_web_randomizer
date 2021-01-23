from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3334_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7055, 7, 'EVENT_3334_run_dialog_4']
    },
    {
        "identifier": 'EVENT_3334_run_dialog_1',
        "command": 'run_dialog',
        "args": [1792, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3334_set_bit_2',
        "command": 'set_bit',
        "args": [0x7055, 7]
    },
    {
        "identifier": 'EVENT_3334_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_3334_action_queue_sync_5']
    },
    {
        "identifier": 'EVENT_3334_run_dialog_4',
        "command": 'run_dialog',
        "args": [1793, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3334_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3334_action_queue_sync_5_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, [0]]
            },
            {
                "identifier": 'EVENT_3334_action_queue_sync_5_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3334_action_queue_sync_5_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3334_set_7000_to_current_level_6',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3334_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [387, 'EVENT_3334_action_queue_async_11']
    },
    {
        "identifier": 'EVENT_3334_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3334_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [14, 102]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_8_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_8_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3334_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._353_VOLCANO_AREA_18_HINO_MART, RadialDirections.NORTHEAST, 1, 61, 0, [_0x68Flags.SHOW_MESSAGE, _0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3334_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3334_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3334_action_queue_async_11_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_11_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [3, 17]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_11_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3334_action_queue_async_11_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3334_enter_area_12',
        "command": 'enter_area',
        "args": [Rooms._353_VOLCANO_AREA_18_HINO_MART, RadialDirections.NORTHEAST, 6, 71, 0, [_0x68Flags.SHOW_MESSAGE, _0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3334_ret_13',
        "command": 'ret'
    }
]
