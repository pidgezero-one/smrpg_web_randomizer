from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2441_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2441_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [1542],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2441_set_action_script_async_2',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 355],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2441_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._233_FOREST_MAZE_AREA_03_UNDERGROUND, RadialDirections.SOUTH, 3, 38, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2441_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
