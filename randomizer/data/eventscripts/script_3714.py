from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_0',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3714_jmp_if_object_not_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_1',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3714_jmp_if_object_not_in_level_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_run_background_event_2',
        "command": 'run_background_event',
        "args": [3713, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_run_background_event_3',
        "command": 'run_background_event',
        "args": [3716, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3585_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_7',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3714_set_action_script_sync_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_run_background_event_8',
        "command": 'run_background_event',
        "args": [3716, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 257],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_12',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3714_jmp_if_object_not_in_level_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_run_background_event_13',
        "command": 'run_background_event',
        "args": [3716, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_jmp_if_object_not_in_level_14',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3714_fade_in_from_black_async_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 881],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3714_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
