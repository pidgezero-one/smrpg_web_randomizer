from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3122_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_3122_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, RadialDirections.SOUTH, 12, 108, 11, []]
    },
    {
        "identifier": 'EVENT_3122_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [14]
    },
    {
        "identifier": 'EVENT_3122_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3122_action_queue_async_3_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [144]
            }
        ]
    },
    {
        "identifier": 'EVENT_3122_ret_4',
        "command": 'ret'
    }
]
