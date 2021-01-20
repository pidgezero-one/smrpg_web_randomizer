from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2648_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7046, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2648_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7046, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2648_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2648_set_bit_3',
        "command": 'set_bit',
        "args": [0x7059, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2648_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2648_action_queue_sync_4_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2648_action_queue_sync_4_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2648_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2648_action_queue_async_5_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2648_action_queue_async_5_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2648_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2648_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
