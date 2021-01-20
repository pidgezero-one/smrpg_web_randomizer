from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_391_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 'EVENT_391_jmp_if_object_not_in_level_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_391_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [25, 28, 0, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_391_jmp_if_object_in_level_6',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_0, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_391_fade_in_from_black_async_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_jmp_if_object_in_level_7',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_391_fade_in_from_black_async_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_ret_9',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_391_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
