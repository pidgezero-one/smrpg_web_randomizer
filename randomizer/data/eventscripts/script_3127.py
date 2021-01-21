from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3127_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3127_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._333_KERO_SEWERS_ENTRANCE, RadialDirections.SOUTH, 5, 20, 1, []]
    },
    {
        "identifier": 'EVENT_3127_fade_in_from_black_sync_2',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3127_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3127_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [144]
            }
        ]
    },
    {
        "identifier": 'EVENT_3127_ret_4',
        "command": 'ret'
    }
]
