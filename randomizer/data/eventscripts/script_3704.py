from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3704_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_9, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 'EVENT_3704_jmp_if_object_in_level_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3704_action_queue_async_2_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 250, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3704_action_queue_async_2_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_3704_jmp_if_object_in_level_3',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 'EVENT_3704_jmp_if_object_in_level_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 'EVENT_3704_jmp_if_object_in_level_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_unsync_action_script_5',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 245],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_jmp_if_object_in_level_7',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_2, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 'EVENT_3704_fade_in_from_black_async_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_jmp_if_object_not_in_level_8',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 'EVENT_3704_fade_in_from_black_async_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_unsync_action_script_9',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 245],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3704_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
