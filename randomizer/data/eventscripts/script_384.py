from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_384_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 'EVENT_384_jmp_if_object_not_in_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_fade_in_from_black_async_1',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_384_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 97, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_384_action_queue_async_3_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_384_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_jmp_if_object_in_level_5',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 'EVENT_384_fade_in_from_black_async_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_apply_solidity_mod_8',
        "command": 'apply_solidity_mod',
        "args": [Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_jmp_if_object_not_in_level_11',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_384_action_queue_async_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_384_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [257],
        "subscript": []
    },
]
