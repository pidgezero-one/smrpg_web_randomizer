
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2576_action_queue_sync_0',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2576_action_queue_sync_0_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2576_action_queue_sync_1',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_2, True],
        "subscript": [
            {
                "identifier": 'EVENT_2576_action_queue_sync_1_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2576_action_queue_sync_2',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_2576_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2576_action_queue_async_3',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": 'EVENT_2576_action_queue_async_3_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2576_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2576_ret_5',
        "command": 'ret'
    }
]
