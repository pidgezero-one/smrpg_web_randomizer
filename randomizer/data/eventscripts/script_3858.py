from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3858_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, RadialDirections.NORTHEAST, 13, 62, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3858_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3858_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 0, 'EVENT_3858_enter_area_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3858_enter_area_3',
        "command": 'enter_area',
        "args": [Rooms._304_SEASIDE_TOWN_OUTSIDE, RadialDirections.NORTHEAST, 13, 62, 1, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3858_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
