from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_376_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_run_background_event_1',
        "command": 'run_background_event',
        "args": [392, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_jmp_if_object_in_level_2',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_5, Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 'EVENT_376_jmp_if_object_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_376_action_queue_async_4_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_376_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 118, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_376_action_queue_async_4_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_376_action_queue_async_4_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_376_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 98],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_jmp_if_object_in_level_6',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_6, Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 'EVENT_376_jmp_if_object_in_level_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_376_action_queue_async_8_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_376_action_queue_async_8_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_376_action_queue_async_8_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
        ]
    },
    {
        "identifier": 'EVENT_376_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 128],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_jmp_if_object_in_level_10',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_4, Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 'EVENT_376_action_queue_sync_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_376_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_376_action_queue_async_11_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_376_action_queue_async_11_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_376_action_queue_async_11_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_376_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_376_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_376_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_376_action_queue_async_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_376_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_262_fade_out_music_to_volume_2'],
        "subscript": []
    },
]
