from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_633_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_633_enter_area_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_633_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7063, 2, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_633_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, RadialDirections.SOUTHWEST, 18, 64, 6, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_633_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_633_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._064_MARRYMORE_OUTSIDE, RadialDirections.SOUTHWEST, 18, 64, 6, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_633_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]