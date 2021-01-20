from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2453_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2453_set_1',
        "command": 'set',
        "args": [0x70ac, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2453_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [1542],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2453_set_action_script_async_3',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 360],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2453_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, RadialDirections.SOUTH, 10, 84, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2453_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
