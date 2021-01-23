from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3306_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_3306_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [25, 'EVENT_3306_enter_area_4']
    },
    {
        "identifier": 'EVENT_3306_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER, RadialDirections.SOUTHWEST, 30, 71, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3306_ret_3',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3306_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, RadialDirections.SOUTHWEST, 10, 112, 6, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_3306_ret_5',
        "command": 'ret'
    }
]
