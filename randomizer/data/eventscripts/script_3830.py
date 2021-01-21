from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3830_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 6, 'EVENT_3830_run_dialog_12']
    },
    {
        "identifier": 'EVENT_3830_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3830_run_dialog_14']
    },
    {
        "identifier": 'EVENT_3830_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_3830_run_dialog_6']
    },
    {
        "identifier": 'EVENT_3830_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3830_action_queue_async_5']
    },
    {
        "identifier": 'EVENT_3830_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3830_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [16, 42]
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_4_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_4_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3830_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [15, 43]
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_jmp_if_bit_clear_2',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3830_action_queue_async_5_SUBSCRIPT_face_northwest_5']
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_jmp_4',
                "command": 'jmp',
                "args": ['EVENT_3830_run_dialog_6']
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_5_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3830_run_dialog_6',
        "command": 'run_dialog',
        "args": [3745, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3830_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3830_action_queue_async_7_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3830_action_queue_async_7_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3830_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3830_set_bit_9',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3830_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3830_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3830_run_dialog_12',
        "command": 'run_dialog',
        "args": [3748, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_3830_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3830_run_dialog_14',
        "command": 'run_dialog',
        "args": [3746, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3830_ret_15',
        "command": 'ret'
    }
]
