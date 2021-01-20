from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3174_set_short_0',
        "command": 'set_short',
        "args": [0x7016, 0x0008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3174_set_short_1',
        "command": 'set_short',
        "args": [0x7018, 0x0076],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3174_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [66],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3174_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS, RadialDirections.SOUTH, 2, 112, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3174_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3174_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
