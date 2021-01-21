from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1409_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1409_action_queue_async_0_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 34, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1409_action_queue_async_0_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1409_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [1537]
    },
    {
        "identifier": 'EVENT_1409_ret_2',
        "command": 'ret'
    }
]
