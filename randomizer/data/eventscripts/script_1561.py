from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1561_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1561_action_queue_sync_7_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1561_action_queue_sync_7_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1561_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_run_background_event_9',
        "command": 'run_background_event',
        "args": [1612, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1561_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
