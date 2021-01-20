from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_406_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 'EVENT_406_pause_action_script_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_start_embedded_action_script_async_2',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_2_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_2_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_406_pause_3',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_jmp_if_object_in_air_4',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_0, 'EVENT_406_pause_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_run_dialog_5',
        "command": 'run_dialog',
        "args": [693, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_406_action_queue_async_6_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_406_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_start_embedded_action_script_async_10',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_10_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_406_start_embedded_action_script_async_10_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
        ]
    },
    {
        "identifier": 'EVENT_406_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_jmp_if_object_in_air_12',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.NPC_0, 'EVENT_406_pause_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_run_dialog_13',
        "command": 'run_dialog',
        "args": [694, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_406_action_queue_async_14_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_406_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_406_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
