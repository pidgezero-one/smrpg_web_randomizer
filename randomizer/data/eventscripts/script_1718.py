from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1718_fade_in_from_black_sync_0',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1718_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1718_action_queue_async_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 32, 22, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1718_action_queue_async_1_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1718_action_queue_async_1_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1718_action_queue_async_1_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
        ]
    },
    {
        "identifier": 'EVENT_1718_run_event_at_return_2',
        "command": 'run_event_at_return',
        "args": [1719],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1718_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
