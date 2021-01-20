from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3816_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT, RadialDirections.SOUTHWEST, 6, 90, 2, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3816_ret_1',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3816_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'EVENT_3817_enter_area_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3816_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3816_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 3, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3816_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7098, 7, 'EVENT_3584_ret_0'],
        "subscript": []
    }
]
