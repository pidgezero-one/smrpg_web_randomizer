from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1836_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7095, 4]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_1',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_4',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_5',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS]
    },
    {
        "identifier": 'EVENT_1836_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1836_action_queue_async_7_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1836_action_queue_async_7_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1836_run_background_event_8',
        "command": 'run_background_event',
        "args": [1854, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1836_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [1829]
    }
]
