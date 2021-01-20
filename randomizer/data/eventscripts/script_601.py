from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_601_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 7, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_601_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._156_MARRYMORE_CHAPEL_KITCHEN_NO_SPRITESEXITS_UNUSED, RadialDirections.SOUTHWEST, 5, 89, 2, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_601_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
