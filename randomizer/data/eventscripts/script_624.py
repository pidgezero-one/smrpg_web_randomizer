from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_624_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_624_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_624_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._006_MARRYMORE_INN_2F, RadialDirections.NORTHEAST, 15, 52, 1, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_624_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
