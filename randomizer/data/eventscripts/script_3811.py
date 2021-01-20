from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3811_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3811_action_queue_sync_0_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3811_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3811_action_queue_sync_1_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 2, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_3811_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3811_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
