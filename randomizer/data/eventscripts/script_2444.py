from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2444_set_bit_0',
        "command": 'set_bit',
        "args": [0x7047, 1]
    },
    {
        "identifier": 'EVENT_2444_set_short_1',
        "command": 'set_short',
        "args": [0x7016, 0x0006]
    },
    {
        "identifier": 'EVENT_2444_set_short_2',
        "command": 'set_short',
        "args": [0x7018, 0x0028]
    },
    {
        "identifier": 'EVENT_2444_run_event_as_subroutine_3',
        "command": 'run_event_as_subroutine',
        "args": [66]
    },
    {
        "identifier": 'EVENT_2444_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._235_FOREST_MAZE_AREA_08_UNDERGROUND, RadialDirections.SOUTH, 28, 110, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2444_ret_5',
        "command": 'ret'
    }
]
